#!/usr/bin/env python3
"""Build and verify prompt-to-artifact behavior contracts for every skill."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DATA_FILE = REPO_ROOT / "data" / "marketing_skills.json"
CONTRACT_JSON = REPO_ROOT / "evals" / "all_skill_behavior_contracts.json"
CONTRACT_MD = REPO_ROOT / "evals" / "all_skill_behavior_contracts.md"

BASE_MUST_INCLUDE = [
    "decision supported",
    "required inputs",
    "generated artifact",
    "QA checks",
    "failure modes",
    "proof metric",
    "next action",
]

CATEGORY_SCENARIOS = {
    "AI Search / Agent Discovery": "B2B analytics platform improving answer-engine discovery",
    "Creative / Ads / Assets": "workflow automation product launching paid creative tests",
    "Content / Creator / Social": "education brand turning one campaign moment into reusable content",
    "Lead Intelligence / Conversion": "data product routing account signals into outbound follow-up",
    "Research / Audience Simulation": "research team deciding which buyer segment and message to test",
    "Lifecycle / Ops / Analytics": "marketing ops team preparing a lifecycle campaign for launch",
    "Marketing Agents / Governance": "growth team evaluating an AI-assisted marketing workflow",
}

DEEP_FIXTURES = {
    "marketing-output-eval-harness": {
        "risk_surface": "meta-evaluation quality",
        "scenario": "An AI workflow drafts landing-page copy from approved product notes, but one sample output invents a benchmark claim and skips the proof link.",
        "expected_decisions": [
            "block unsupported claims until evidence is supplied",
            "score factuality, claim support, brand fit, usefulness, and operational reliability separately",
            "set pass thresholds and review owners before the workflow expands",
        ],
        "must_include": ["criterion", "test case", "expected behavior", "threshold", "owner", "failure mode"],
    },
    "marketing-agent-workflow-spec": {
        "risk_surface": "agent scope and autonomy",
        "scenario": "A campaign-brief agent may read approved inputs and draft briefs, but it must not publish, change budgets, or message leads.",
        "expected_decisions": [
            "define the bounded job and final artifact",
            "list allowed tools and blocked actions",
            "place human approval gates before spend, claims, or outreach",
        ],
        "must_include": ["bounded job", "allowed tools", "non-actions", "review gate", "fallback", "telemetry"],
    },
    "claims-hallucination-review": {
        "risk_surface": "unsupported marketing claims",
        "scenario": "A draft says the product is fastest in market, reduces cost by 70 percent, and is certified for a regulated use case without attached proof.",
        "expected_decisions": [
            "separate supported, unsupported, stale, and risky claims",
            "rewrite or block unsupported claims",
            "name the proof or reviewer needed before launch use",
        ],
        "must_include": ["claim", "proof", "risk level", "required edit", "approval state", "next action"],
    },
    "brand-voice-memory": {
        "risk_surface": "style drift and reusable memory quality",
        "scenario": "A team wants durable voice guidance from approved emails, product pages, and rejected phrases without turning style into vague adjectives.",
        "expected_decisions": [
            "separate approved patterns from banned patterns",
            "preserve claim boundaries while capturing tone",
            "include examples that can be reused by future workflows",
        ],
        "must_include": ["voice rule", "approved example", "banned pattern", "claim boundary", "review note"],
    },
    "ai-answer-visibility-scorecard": {
        "risk_surface": "answer-surface scoring consistency",
        "scenario": "Three answer engines mention the product differently: one omits it, one cites stale proof, and one recommends a competitor first.",
        "expected_decisions": [
            "score visibility separately from answer accuracy and citation quality",
            "prioritize remediation by buyer question and downstream action",
            "mark observed answer text separately from interpretation",
        ],
        "must_include": ["prompt", "surface", "answer summary", "citation status", "gap", "action"],
    },
    "share-of-answer-benchmark": {
        "risk_surface": "competitor comparison and aggregation",
        "scenario": "A prompt set compares four alternatives across category, problem, and comparison queries with mixed rank and citation quality.",
        "expected_decisions": [
            "calculate share by priority prompt set",
            "separate mention count from quality and next-action usefulness",
            "identify proof gaps that explain displacement",
        ],
        "must_include": ["prompt", "rank or inclusion", "competitor rank", "citation status", "trend note"],
    },
    "brand-compliance-creative-review": {
        "risk_surface": "pre-launch creative approval",
        "scenario": "A paid social asset includes a strong performance claim, a risky comparison, a platform-sensitive image, and no named reviewer.",
        "expected_decisions": [
            "block or rewrite unsupported claims before launch",
            "assign approval state and owner for each risk",
            "preserve the creative intent while reducing claim and platform risk",
        ],
        "must_include": ["claim", "proof", "risk level", "required edit", "owner", "approval state"],
    },
    "website-visitor-to-account-workflow": {
        "risk_surface": "visitor routing and handoff quality",
        "scenario": "Three visitor sessions include a high-intent known account, an uncertain account match, and a low-intent anonymous visit.",
        "expected_decisions": [
            "route only high-confidence signals to sales action",
            "send uncertain matches to conservative fallback",
            "show evidence, confidence, owner, and follow-up timing",
        ],
        "must_include": ["visit", "matched account", "intent level", "evidence", "confidence", "owner", "follow-up"],
    },
    "audience-sync-contract": {
        "risk_surface": "field mapping and activation readiness",
        "scenario": "A lifecycle audience must sync from warehouse to email and ad destinations with consent, join keys, freshness, and expected counts.",
        "expected_decisions": [
            "define required fields, joins, exclusions, and owner checks",
            "block activation when counts or consent checks fail",
            "include rollback criteria and destination status",
        ],
        "must_include": ["audience", "field", "join key", "destination", "exclusion", "owner", "check"],
    },
    "consent-suppression-rollback-plan": {
        "risk_surface": "unsafe launch prevention",
        "scenario": "A campaign is ready to launch, but suppression status is stale, consent records are mixed, and rollback ownership is unclear.",
        "expected_decisions": [
            "mark the launch review-required until consent and suppression checks pass",
            "define rollback trigger, owner, and status reporting",
            "separate privacy risk from general campaign QA",
        ],
        "must_include": ["consent", "suppression", "rollback", "owner", "approval", "status"],
    },
}


def fail(message: str) -> None:
    raise SystemExit(f"behavior contract test failed: {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_json(path: Path) -> object:
    return json.loads(read(path))


def section(text: str, heading: str) -> str:
    start = text.find(heading)
    if start == -1:
        return ""
    next_heading = text.find("\n## ", start + len(heading))
    return text[start:] if next_heading == -1 else text[start:next_heading]


def bullet_items(text: str) -> list[str]:
    return [line[2:].strip() for line in text.splitlines() if line.startswith("- ")]


def core_fields(pattern_md: str) -> list[str]:
    match = re.search(r"^- Core fields or sections: (.+?)\.$", pattern_md, re.MULTILINE)
    if not match:
        return []
    return [part.strip() for part in match.group(1).split(",") if part.strip()]


def clean_terms(values: list[str], limit: int) -> list[str]:
    terms: list[str] = []
    for value in values:
        term = re.sub(r"^[^:]+:\s*", "", value).strip()
        if term and term not in terms:
            terms.append(term)
        if len(terms) >= limit:
            break
    return terms


def build_contract(skill: dict) -> dict:
    name = skill["name"]
    pattern_md = read(SKILLS_DIR / name / "references" / "pattern.md")
    fields = core_fields(pattern_md)
    artifact_fields = clean_terms(bullet_items(section(pattern_md, "## Artifact Fields")), 4)
    qa_checks = clean_terms(bullet_items(section(pattern_md, "## QA Checks")), 4)
    failures = clean_terms(bullet_items(section(pattern_md, "## Failure Modes")), 4)
    metrics = clean_terms(bullet_items(section(pattern_md, "## Proof Metrics")), 4)

    if len(fields) < 4:
        fail(f"{name} has fewer than four core fields")
    if len(qa_checks) < 4:
        fail(f"{name} has fewer than four QA checks")
    if len(failures) < 4:
        fail(f"{name} has fewer than four failure modes")
    if len(metrics) < 4:
        fail(f"{name} has fewer than four proof metrics")

    scenario = CATEGORY_SCENARIOS.get(skill["category"], "marketing team producing a reviewable artifact")
    prompt = (
        f"Use ${name} for a fictional {scenario}. Produce {skill['output']} using the "
        f"{', '.join(skill['surfaces'])} surface mechanics. Include decision supported, "
        "required inputs, generated artifact, QA checks, failure modes, proof metric, and next action. "
        "Label assumptions and ask only for missing high-risk inputs before making launch-ready claims."
    )

    return {
        "skill": name,
        "category": skill["category"],
        "output": skill["output"],
        "surfaces": skill["surfaces"],
        "prompt": prompt,
        "must_include": BASE_MUST_INCLUDE + fields[:4],
        "expected_artifact_fields": fields,
        "surface_artifact_fields": artifact_fields,
        "qa_checks": qa_checks,
        "failure_modes": failures,
        "proof_metrics": metrics,
        "clarification_rule": "Ask for missing high-risk inputs before producing launch-ready work; label low-risk assumptions.",
    }


def build_deep_fixture(skill_name: str, skills_by_name: dict[str, dict]) -> dict:
    if skill_name not in skills_by_name:
        fail(f"deep fixture references missing skill: {skill_name}")
    skill = skills_by_name[skill_name]
    fixture = DEEP_FIXTURES[skill_name]
    prompt = (
        f"Use ${skill_name} for this edge-case fixture: {fixture['scenario']} "
        f"Return {skill['output']} with QA checks, failure modes, proof metric, and next action."
    )
    return {
        "skill": skill_name,
        "category": skill["category"],
        "risk_surface": fixture["risk_surface"],
        "prompt": prompt,
        "expected_decisions": fixture["expected_decisions"],
        "must_include": fixture["must_include"] + ["QA checks", "failure modes", "proof metric", "next action"],
    }


def build_payload() -> dict:
    data = read_json(DATA_FILE)
    skills = data.get("skills", [])
    if not isinstance(skills, list) or not skills:
        fail("data/marketing_skills.json has no skills")
    skills_by_name = {skill["name"]: skill for skill in skills}
    contracts = [build_contract(skill) for skill in skills]
    deep_fixtures = [build_deep_fixture(name, skills_by_name) for name in DEEP_FIXTURES]
    return {
        "run_date": date.today().isoformat(),
        "skills_tested": len(contracts),
        "contract_type": "prompt-to-artifact behavior contract",
        "coverage": {
            "per_skill_contracts": len(contracts),
            "deep_edge_case_fixtures": len(deep_fixtures),
            "deep_fixture_skills": list(DEEP_FIXTURES),
        },
        "contracts": contracts,
        "deep_fixtures": deep_fixtures,
    }


def validate_payload(payload: dict) -> None:
    skills = read_json(DATA_FILE)["skills"]
    expected_names = {skill["name"] for skill in skills}
    contract_names = {contract["skill"] for contract in payload.get("contracts", [])}
    if contract_names != expected_names:
        missing = sorted(expected_names - contract_names)[:5]
        extra = sorted(contract_names - expected_names)[:5]
        fail(f"contract skill mismatch missing={missing} extra={extra}")
    if payload["coverage"]["deep_edge_case_fixtures"] != len(DEEP_FIXTURES):
        fail("deep fixture count mismatch")

    for contract in payload["contracts"]:
        name = contract["skill"]
        prompt = contract["prompt"]
        if f"${name}" not in prompt:
            fail(f"{name} prompt does not invoke skill")
        for term in BASE_MUST_INCLUDE:
            if term not in contract["must_include"] and term not in prompt:
                fail(f"{name} contract missing required behavior term: {term}")
        for key in ["expected_artifact_fields", "qa_checks", "failure_modes", "proof_metrics"]:
            if len(contract[key]) < 4:
                fail(f"{name} contract has too few {key}")
        if len(contract["must_include"]) < 11:
            fail(f"{name} contract must_include is too thin")

    deep_names = {fixture["skill"] for fixture in payload["deep_fixtures"]}
    if deep_names != set(DEEP_FIXTURES):
        fail("deep fixture skills mismatch")
    for fixture in payload["deep_fixtures"]:
        if len(fixture["expected_decisions"]) < 3:
            fail(f"{fixture['skill']} deep fixture has too few decisions")
        if len(fixture["must_include"]) < 8:
            fail(f"{fixture['skill']} deep fixture must_include is too thin")


def write_reports(payload: dict) -> None:
    CONTRACT_JSON.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# All Skill Behavior Contracts",
        "",
        f"Run date: {payload['run_date']}",
        "",
        "## Summary",
        "",
        f"- Skills with prompt-to-artifact contracts: {payload['coverage']['per_skill_contracts']}",
        f"- Deep edge-case fixtures: {payload['coverage']['deep_edge_case_fixtures']}",
        "- Contract checks: skill invocation, expected artifact fields, QA checks, failure modes, proof metrics, and next action.",
        "",
        "## Deep Fixture Skills",
        "",
    ]
    for fixture in payload["deep_fixtures"]:
        lines.append(f"- `{fixture['skill']}`: {fixture['risk_surface']}")
    lines.extend(
        [
            "",
            "## Per-Skill Contracts",
            "",
            "| Skill | Category | Output | Expected Fields |",
            "| --- | --- | --- | --- |",
        ]
    )
    for contract in sorted(payload["contracts"], key=lambda item: (item["category"], item["skill"])):
        fields = ", ".join(contract["expected_artifact_fields"][:4])
        lines.append(f"| `{contract['skill']}` | {contract['category']} | {contract['output']} | {fields} |")
    CONTRACT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify prompt-to-artifact behavior contracts for all skills")
    parser.add_argument("--write-report", action="store_true", help="write eval contract JSON and Markdown")
    args = parser.parse_args()

    payload = build_payload()
    validate_payload(payload)
    if args.write_report:
        write_reports(payload)
    elif CONTRACT_JSON.exists():
        existing = read_json(CONTRACT_JSON)
        validate_payload(existing)
        if existing != payload:
            fail("evals/all_skill_behavior_contracts.json is stale; rerun with --write-report")

    print(
        f"Behavior contracts verified for {payload['coverage']['per_skill_contracts']} skills "
        f"with {payload['coverage']['deep_edge_case_fixtures']} deep fixtures."
    )
    if args.write_report:
        print(f"Wrote {CONTRACT_JSON.relative_to(REPO_ROOT)}")
        print(f"Wrote {CONTRACT_MD.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
