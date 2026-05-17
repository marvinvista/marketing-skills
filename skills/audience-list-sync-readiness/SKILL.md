---
name: audience-list-sync-readiness
description: Use when you need audience list sync readiness check to align audience segments, list criteria, join keys, consent status, exclusions, destinations, and count checks.
---

# audience list sync readiness

## Quick Start

- Produce audience list sync readiness check.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: audience segment, list criterion, join key, consent status.
- Use the artifact to decide: Which audience is eligible for activation.
- Do not mark ready until: Expected and actual counts are checked before activation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return audience list sync readiness check. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not audience list sync readiness check, the main decision is outside audience-data-sync, lead-list-building, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
