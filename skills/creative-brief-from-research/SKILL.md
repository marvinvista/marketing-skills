---
name: creative-brief-from-research
description: Use when you need creative brief with claims, proof, and constraints to convert audience insight, proof, and objections into a production-ready creative brief.
---

# creative brief from research

## Quick Start

- Produce creative brief with claims, proof, and constraints.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: insight, audience, claim, proof.
- Use the artifact to decide: Which variable changes in the next creative test.
- Do not mark ready until: Each creative variant changes one declared variable or is marked exploratory.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return creative brief with claims, proof, and constraints. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not creative brief with claims, proof, and constraints, the main decision is outside ad-creative-generation, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
