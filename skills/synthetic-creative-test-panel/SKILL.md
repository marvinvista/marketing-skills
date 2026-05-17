---
name: synthetic-creative-test-panel
description: Use when you need synthetic creative test panel to use synthetic audience scenarios to pressure-test creative angles, reactions, confidence, and validation needs.
---

# synthetic creative test panel

## Quick Start

- Produce synthetic creative test panel.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: audience assumption, scenario, creative angle, simulated reaction.
- Use the artifact to decide: Which hypotheses are worth testing with real evidence.
- Do not mark ready until: Synthetic output is labeled separately from observed evidence.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return synthetic creative test panel. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not synthetic creative test panel, the main decision is outside synthetic-audience-simulation, ad-creative-generation, message-testing, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
