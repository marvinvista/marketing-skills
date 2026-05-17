---
name: campaign-preflight-qa-checklist
description: Use when a marketer or go-to-market operator needs campaign preflight checklist for Lifecycle / Ops / Analytics work involving Campaign analytics QA, Marketing ops orchestration, especially when the task must check assets, audiences, approvals, tracking, consent, owner routing, and rollback before launch.
---

# campaign preflight QA checklist

## Quick Start

- Produce campaign preflight checklist.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.
- Run `scripts/build_campaign_qa.py` when the user provides structured inputs for the repeatable table, scorecard, or checklist.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return campaign preflight checklist. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
