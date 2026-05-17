---
name: catalog-ad-feed-plan
description: Use when you need catalog creative feed plan to turn product attributes, audience segments, and creative rules into a catalog ad feed plan.
---

# catalog ad feed plan

## Quick Start

- Produce catalog creative feed plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: product field, audience segment, creative rule, image rule.
- Use the artifact to decide: Which variable changes in the next creative test.
- Do not mark ready until: Each creative variant changes one declared variable or is marked exploratory.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return catalog creative feed plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not catalog creative feed plan, the main decision is outside ad-creative-generation, product-image-generation, audience-data-sync, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
