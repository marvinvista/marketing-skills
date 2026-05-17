#!/usr/bin/env python3
"""Run Plugin Eval against every marketing skill and write aggregate reports."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DATA_FILE = REPO_ROOT / "data" / "marketing_skills.json"
SUMMARY_JSON = REPO_ROOT / "evals" / "plugin_eval_all_skills.json"
SUMMARY_MD = REPO_ROOT / "evals" / "plugin_eval_all_skills.md"
MIN_SCORE = 93
PLUGIN_EVAL_CLI_LABEL = "resolved locally via PLUGIN_EVAL_CLI or Codex plugin cache"


def fail(message: str) -> None:
    raise SystemExit(f"plugin-eval all-skills failed: {message}")


def read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_plugin_eval_cli() -> Path:
    env_path = os.environ.get("PLUGIN_EVAL_CLI")
    if env_path:
        cli = Path(env_path).expanduser()
        if cli.exists():
            return cli
        fail(f"PLUGIN_EVAL_CLI does not exist: {cli}")

    candidates = sorted(
        Path.home().glob(".codex/plugins/cache/openai-curated/plugin-eval/*/scripts/plugin-eval.js"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    if candidates:
        return candidates[0]
    fail("could not find plugin-eval CLI; set PLUGIN_EVAL_CLI")


def metric_value(result: dict, metric_id: str) -> int | float | None:
    for metric in result.get("metrics", []):
        if metric.get("id") == metric_id:
            return metric.get("value")
    return None


def run_plugin_eval(cli: Path, skill_name: str) -> dict:
    skill_path = SKILLS_DIR / skill_name
    command = ["node", str(cli), "analyze", str(skill_path), "--format", "json"]
    result = subprocess.run(command, cwd=REPO_ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        output = "\n".join(part for part in [result.stdout, result.stderr] if part)
        fail(f"plugin-eval failed for {skill_name}\n{output}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        fail(f"plugin-eval returned invalid JSON for {skill_name}: {exc}")


def summarize_result(skill: dict, result: dict) -> dict:
    summary = result["summary"]
    check_counts = summary["checkCounts"]
    active_budget = (
        result["budgets"]["trigger_cost_tokens"]["value"]
        + result["budgets"]["invoke_cost_tokens"]["value"]
    )
    return {
        "skill": skill["name"],
        "category": skill["category"],
        "score": summary["score"],
        "grade": summary["grade"],
        "risk": summary["riskLevel"],
        "fail_checks": check_counts.get("fail", 0) + check_counts.get("error", 0),
        "warn_checks": check_counts.get("warn", 0) + check_counts.get("warning", 0),
        "info_checks": check_counts.get("info", 0),
        "active_budget_tokens": active_budget,
        "trigger_cost_tokens": result["budgets"]["trigger_cost_tokens"]["value"],
        "invoke_cost_tokens": result["budgets"]["invoke_cost_tokens"]["value"],
        "deferred_cost_tokens": result["budgets"]["deferred_cost_tokens"]["value"],
        "total_tokens": result["budgets"]["total_tokens"]["value"],
        "description_length_chars": metric_value(result, "description_length_chars"),
        "fix_first": [item["id"] for item in summary.get("fixFirst", [])],
        "top_recommendations": summary.get("topRecommendations", []),
    }


def write_json_report(cli: Path, rows: list[dict]) -> None:
    failed_gate = [
        row
        for row in rows
        if row["score"] < MIN_SCORE or row["fail_checks"] or row["warn_checks"]
    ]
    payload = {
        "run_date": date.today().isoformat(),
        "plugin_eval_cli": PLUGIN_EVAL_CLI_LABEL,
        "skills_tested": len(rows),
        "minimum_score": min(row["score"] for row in rows),
        "maximum_active_budget_tokens": max(row["active_budget_tokens"] for row in rows),
        "maximum_trigger_cost_tokens": max(row["trigger_cost_tokens"] for row in rows),
        "failed_gate_count": len(failed_gate),
        "gate": {
            "minimum_score": MIN_SCORE,
            "fail_checks_allowed": 0,
            "warn_checks_allowed": 0,
            "info_checks_allowed": True,
        },
        "results": rows,
    }
    SUMMARY_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_markdown_report(cli: Path, rows: list[dict]) -> None:
    failed_gate = [
        row
        for row in rows
        if row["score"] < MIN_SCORE or row["fail_checks"] or row["warn_checks"]
    ]
    low_risk = sum(1 for row in rows if row["risk"] == "low")
    lines = [
        "# Plugin Eval All Skills",
        "",
        f"Run date: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Skills evaluated individually: {len(rows)}",
        f"- Gate: score >= {MIN_SCORE}, zero fail/error checks, zero warn/warning checks",
        f"- Gate failures: {len(failed_gate)}",
        f"- Low-risk skills: {low_risk}",
        f"- Minimum score: {min(row['score'] for row in rows)}",
        f"- Maximum active budget: {max(row['active_budget_tokens'] for row in rows)} tokens",
        f"- Maximum trigger cost: {max(row['trigger_cost_tokens'] for row in rows)} tokens",
        f"- Plugin Eval CLI: {PLUGIN_EVAL_CLI_LABEL}",
        "",
        "## Method",
        "",
        "- Ran Plugin Eval `analyze` against every `skills/*/SKILL.md` target listed in `data/marketing_skills.json`.",
        "- Treated informational coverage-artifact notes as non-blocking because these skills are mostly instruction artifacts; helper-backed scripts are covered by the repo test suite.",
        "- Preserved per-skill score, risk, warning/failure counts, and token budget data in `evals/plugin_eval_all_skills.json`.",
        "",
        "## Results",
        "",
        "| Skill | Category | Score | Risk | Fail | Warn | Active Tokens | Trigger Tokens |",
        "| --- | --- | ---: | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in sorted(rows, key=lambda item: (item["category"], item["skill"])):
        lines.append(
            f"| `{row['skill']}` | {row['category']} | {row['score']} | {row['risk']} | "
            f"{row['fail_checks']} | {row['warn_checks']} | {row['active_budget_tokens']} | "
            f"{row['trigger_cost_tokens']} |"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    data = read_json(DATA_FILE)
    skills = data.get("skills", [])
    if not isinstance(skills, list) or not skills:
        fail("data/marketing_skills.json has no skills")

    cli = resolve_plugin_eval_cli()
    rows = [summarize_result(skill, run_plugin_eval(cli, skill["name"])) for skill in skills]
    write_json_report(cli, rows)
    write_markdown_report(cli, rows)

    failed_gate = [
        row
        for row in rows
        if row["score"] < MIN_SCORE or row["fail_checks"] or row["warn_checks"]
    ]
    if failed_gate:
        sample = ", ".join(row["skill"] for row in failed_gate[:10])
        fail(f"{len(failed_gate)} skills failed Plugin Eval gate: {sample}")

    print(f"Plugin Eval analyzed {len(rows)} skills: all passed the score/warning gate.")
    print(f"Wrote {SUMMARY_JSON.relative_to(REPO_ROOT)}")
    print(f"Wrote {SUMMARY_MD.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
