---
name: consent-suppression-rollback-plan
description: Use when you need consent and rollback plan to define consent checks, suppression rules, privacy review, rollback path, and incident owner.
---

# consent suppression rollback plan

## Quick Start

- Produce consent and rollback plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: consent rule, suppression list, risky action, rollback trigger.
- Use the artifact to decide: Which work can launch, wait, or roll back.
- Do not mark ready until: Every dependency has an owner and failure fallback.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return consent and rollback plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not consent and rollback plan, the main decision is outside marketing-ops-orchestration, brand-governance-review, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
