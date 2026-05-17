---
name: account-list-sourcing-brief
description: Use when you need account list sourcing brief to turn segment rules into source selection, list criteria, exclusions, and evidence fields.
---

# account list sourcing brief

## Quick Start

- Produce account list sourcing brief.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: segment rule, list source, inclusion criterion, exclusion.
- Use the artifact to decide: Which records qualify for action now.
- Do not mark ready until: Every accepted record has fit, trigger, evidence, and a route.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return account list sourcing brief. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not account list sourcing brief, the main decision is outside lead-list-building, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
