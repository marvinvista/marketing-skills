---
name: campaign-preflight-qa-checklist
description: Use when you need campaign preflight checklist to check assets, audiences, approvals, tracking, consent, owner routing, and rollback before launch.
---

# campaign preflight QA checklist

## Quick Start

- Produce campaign preflight checklist.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.
- Run `scripts/build_campaign_qa.py` when the user provides structured inputs for the repeatable table, scorecard, or checklist.

## Skill-Specific Checklist

- Anchor the artifact around these fields: asset, audience, tracking, approval.
- Use the artifact to decide: Which metrics are trustworthy enough for a decision.
- Do not mark ready until: Tracking is tested before performance interpretation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return campaign preflight checklist. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not campaign preflight checklist, the main decision is outside campaign-analytics-qa, marketing-ops-orchestration, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
