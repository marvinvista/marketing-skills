---
name: lifecycle-segmentation-map
description: Use when you need lifecycle segmentation map to define lifecycle states, transitions, triggers, suppressions, and owner actions.
---

# lifecycle segmentation map

## Quick Start

- Produce lifecycle segmentation map.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: state, transition, trigger, suppression.
- Use the artifact to decide: Which audience is eligible for activation.
- Do not mark ready until: Expected and actual counts are checked before activation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return lifecycle segmentation map. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not lifecycle segmentation map, the main decision is outside audience-data-sync, marketing-ops-orchestration, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
