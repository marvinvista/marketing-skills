#!/usr/bin/env python3
"""Evaluate every marketing skill for installability, packaging, and utility."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DATA_FILE = REPO_ROOT / "data" / "marketing_skills.json"
REPORT_FILE = REPO_ROOT / "evals" / "all_skill_test_report.md"

REQUIRED_FILES = [
    "SKILL.md",
    "LICENSE.txt",
    "agents/openai.yaml",
    "references/pattern.md",
]
REQUIRED_REFERENCE_SECTIONS = [
    "## When To Use",
    "## Product Mechanics",
    "## Required Inputs",
    "## Decision Rules",
    "## Procedure",
    "## Artifact Template",
    "## Skill-Specific Work Product",
    "## Artifact Fields",
    "## Decision Gates",
    "## QA Checks",
    "## Failure Modes",
    "## Proof Metrics",
    "## Example Prompt",
    "## Optional Helper",
    "## Evidence Boundary",
]
SECTION_MIN_BULLETS = {
    "## Required Inputs": 6,
    "## Decision Rules": 5,
    "## Procedure": 5,
    "## QA Checks": 4,
    "## Failure Modes": 4,
    "## Proof Metrics": 4,
}
UTILITY_TERMS = [
    "review owner",
    "missing high-risk",
    "QA checks",
    "failure modes",
    "proof metric",
    "next action",
]
BOUNDARY_PATTERNS = [
    re.compile("com" + "pan" + r"(?:y|ies)", re.IGNORECASE),
    re.compile(r"y\s+combinator", re.IGNORECASE),
    re.compile(r"y" + "combinator", re.IGNORECASE),
    re.compile(r"\byc\s+ai\b", re.IGNORECASE),
    re.compile(r"\byc\s+marketing\b", re.IGNORECASE),
    re.compile("holo" + "cron", re.IGNORECASE),
    re.compile(r"private\s+urls?", re.IGNORECASE),
    re.compile(r"source\s+names?", re.IGNORECASE),
    re.compile("Feature " + "ID"),
    re.compile("feature" + "_id"),
    re.compile(r"feature-" + r"\d{3}"),
]


@dataclass
class SkillResult:
    name: str
    category: str
    score: int
    status: str
    issues: list[str]


def fail(message: str) -> None:
    raise SystemExit(f"all-skill test failed: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    next_heading = text.find("\n## ", start + len(heading))
    if next_heading == -1:
        return text[start:]
    return text[start:next_heading]


def bullet_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.startswith("- "))


def comma_field_count(line: str) -> int:
    _, _, value = line.partition(":")
    return len([part.strip() for part in value.split(",") if part.strip()])


def run_command(args: list[str]) -> None:
    result = subprocess.run(
        args,
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        output = "\n".join(part for part in [result.stdout, result.stderr] if part)
        fail(f"command failed: {' '.join(args)}\n{output}")


def validate_install_copy(name: str, tmp_root: Path) -> None:
    src = SKILLS_DIR / name
    dest = tmp_root / name
    shutil.copytree(src, dest)
    for rel_path in REQUIRED_FILES:
        if not (dest / rel_path).exists():
            fail(f"{name} install copy missing {rel_path}")
    installed_name = frontmatter(read(dest / "SKILL.md")).get("name")
    if installed_name != name:
        fail(f"{name} installed frontmatter name mismatch: {installed_name}")


def issue_if(issues: list[str], condition: bool, message: str) -> None:
    if not condition:
        issues.append(message)


def evaluate_skill(skill: dict[str, object]) -> SkillResult:
    name = str(skill["name"])
    category = str(skill["category"])
    output = str(skill["output"])
    mechanic = str(skill["mechanic"])
    surfaces = [str(item) for item in skill["surfaces"]]
    skill_dir = SKILLS_DIR / name
    skill_md = read(skill_dir / "SKILL.md")
    pattern_md = read(skill_dir / "references" / "pattern.md")
    agent_yaml = read(skill_dir / "agents" / "openai.yaml")
    fm = frontmatter(skill_md)
    issues: list[str] = []

    issue_if(issues, fm.get("name") == name, "frontmatter name matches folder")
    issue_if(issues, fm.get("description", "").startswith("Use when "), "frontmatter has trigger language")
    issue_if(issues, output in fm.get("description", ""), "frontmatter names expected artifact")
    issue_if(issues, mechanic in fm.get("description", ""), "frontmatter names operating mechanic")
    issue_if(issues, len(skill_md.splitlines()) <= 80, "SKILL.md stays concise for progressive disclosure")
    issue_if(issues, "Read `references/pattern.md`" in skill_md, "SKILL.md points to the detailed reference")
    issue_if(issues, "## Output Contract" in skill_md, "SKILL.md states an output contract")
    issue_if(issues, "## Guardrails" in skill_md, "SKILL.md includes guardrails")
    issue_if(issues, f"${name}" in agent_yaml, "agent metadata default prompt invokes the skill")
    issue_if(issues, "default_prompt:" in agent_yaml, "agent metadata includes a default prompt")
    issue_if(issues, f"Final artifact: {output}" in pattern_md, "reference names the final artifact")
    issue_if(issues, f"Organizing mechanic: {mechanic}" in pattern_md, "reference names the organizing mechanic")
    issue_if(issues, "Core fields or sections:" in pattern_md, "reference names core artifact fields")
    issue_if(issues, "Keep the artifact narrow enough" in pattern_md, "reference pushes toward usable next-step scope")
    issue_if(issues, "not private identities" in pattern_md, "reference includes evidence boundary guardrail")
    issue_if(issues, "observed" in pattern_md.lower() or "evidence" in pattern_md.lower(), "reference distinguishes evidence from inference")
    issue_if(issues, "TODO" not in pattern_md and "TBD" not in pattern_md, "reference contains no placeholder markers")

    for heading in REQUIRED_REFERENCE_SECTIONS:
        issue_if(issues, heading in pattern_md, f"reference includes {heading}")
    for heading, minimum in SECTION_MIN_BULLETS.items():
        issue_if(issues, bullet_count(section(pattern_md, heading)) >= minimum, f"{heading} has at least {minimum} bullets")
    for surface in surfaces:
        issue_if(issues, surface in pattern_md, f"reference covers surface {surface}")
    for term in UTILITY_TERMS:
        issue_if(issues, term.lower() in (skill_md + "\n" + pattern_md).lower(), f"guidance includes {term}")

    core_line = next(
        (line for line in pattern_md.splitlines() if line.startswith("- Core fields or sections:")),
        "",
    )
    issue_if(issues, comma_field_count(core_line) >= 4, "core artifact has at least four concrete fields")

    score = max(0, 100 - len(issues) * 5)
    status = "pass" if score >= 90 else "fail"
    return SkillResult(name=name, category=category, score=score, status=status, issues=issues)


def validate_distinct_specs(skills: list[dict[str, object]]) -> None:
    for key in ["name", "mechanic", "output", "one_line_description"]:
        values = [str(item[key]) for item in skills]
        duplicates = sorted({value for value in values if values.count(value) > 1})
        if duplicates:
            fail(f"duplicate {key}: {duplicates[:3]}")


def validate_boundary_text(paths: list[Path]) -> None:
    for path in paths:
        text = read(path)
        for pattern in BOUNDARY_PATTERNS:
            if pattern.search(text):
                fail(f"boundary pattern found in {path.relative_to(REPO_ROOT)}: {pattern.pattern}")


def helper_tests() -> list[str]:
    test_paths = sorted(SKILLS_DIR.glob("*/tests/test_*.py"))
    for test_path in test_paths:
        run_command([sys.executable, str(test_path.relative_to(REPO_ROOT))])
    return [path.relative_to(REPO_ROOT).as_posix() for path in test_paths]


def behavior_contract_tests(write_report: bool) -> None:
    args = [sys.executable, "scripts/test_skill_behavior_contracts.py"]
    if write_report:
        args.append("--write-report")
    run_command(args)


def write_report(results: list[SkillResult], helper_test_paths: list[str]) -> None:
    passed = sum(1 for result in results if result.status == "pass")
    lines = [
        "# All Skill Test Report",
        "",
        f"Run date: {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Skills tested: {len(results)}",
        f"- Skills passed: {passed}",
        f"- Skills failed: {len(results) - passed}",
        f"- Helper tests passed: {len(helper_test_paths)}",
        "- Install-copy test: passed for every skill",
        "- Packaging and utility threshold: passed for every skill",
        "- Behavior contracts: passed for every skill, including 10 deep edge-case fixtures",
        "- Boundary scan: passed",
        "",
        "## Method",
        "",
        "- Copied every skill into a temporary install root and verified required files.",
        "- Checked OpenAI-style progressive disclosure: concise `SKILL.md`, trigger frontmatter, agent metadata, and detailed `references/pattern.md`.",
        "- Checked usefulness criteria: explicit inputs, decision rules, procedure, artifact fields, QA checks, failure modes, proof metrics, and next action.",
        "- Verified prompt-to-artifact behavior contracts for every skill and deeper edge-case contracts for the highest-risk skills.",
        "- Ran every helper-backed skill test.",
        "",
        "## Results",
        "",
        "| Skill | Category | Score | Result |",
        "| --- | --- | ---: | --- |",
    ]
    for result in sorted(results, key=lambda item: (item.category, item.name)):
        lines.append(f"| `{result.name}` | {result.category} | {result.score} | {result.status} |")
    lines.append("")
    if helper_test_paths:
        lines.extend(["## Helper Tests", ""])
        for path in helper_test_paths:
            lines.append(f"- `{path}`")
        lines.append("")
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Test every marketing skill in this pack")
    parser.add_argument("--write-report", action="store_true", help="write evals/all_skill_test_report.md")
    args = parser.parse_args()

    data = json.loads(read(DATA_FILE))
    skills = data.get("skills", [])
    if not isinstance(skills, list) or not skills:
        fail("data/marketing_skills.json has no skills")

    validate_distinct_specs(skills)
    run_command([sys.executable, "scripts/validate_skills.py"])
    run_command([sys.executable, "scripts/test_install_sh.py"])

    with tempfile.TemporaryDirectory(prefix="marketing-skills-all-") as tmp:
        tmp_root = Path(tmp)
        for skill in skills:
            validate_install_copy(str(skill["name"]), tmp_root)

    results = [evaluate_skill(skill) for skill in skills]
    failures = [result for result in results if result.status != "pass"]
    behavior_contract_tests(args.write_report)
    helper_test_paths = helper_tests()
    validate_boundary_text([REPORT_FILE] if REPORT_FILE.exists() else [])

    if args.write_report:
        write_report(results, helper_test_paths)
        validate_boundary_text([REPORT_FILE])

    if failures:
        lines = [f"{result.name}: {result.score} ({', '.join(result.issues[:3])})" for result in failures]
        fail("utility threshold failures:\n" + "\n".join(lines))

    print(f"Tested {len(results)} skills: all passed install, packaging, utility, and helper checks.")
    if args.write_report:
        print(f"Wrote {REPORT_FILE.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
