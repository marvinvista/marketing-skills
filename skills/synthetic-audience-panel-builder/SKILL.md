---
name: synthetic-audience-panel-builder
description: Use when you need synthetic panel spec to define synthetic panel composition, assumptions, prompts, validation checks, and confidence limits.
---

# synthetic audience panel builder

## Quick Start

- Produce synthetic panel spec.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: persona, assumption, scenario, prompt.
- Use the artifact to decide: Which hypotheses are worth testing with real evidence.
- Do not mark ready until: Synthetic output is labeled separately from observed evidence.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return synthetic panel spec. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not synthetic panel spec, the main decision is outside synthetic-audience-simulation, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
