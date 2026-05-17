---
name: synthetic-enrichment-panel
description: Use when you need synthetic enrichment panel to test enrichment assumptions, personalization cues, confidence limits, and validation needs with synthetic panels.
---

# synthetic enrichment panel

## Quick Start

- Produce synthetic enrichment panel.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: enrichment assumption, persona, scenario, personalization cue.
- Use the artifact to decide: Which hypotheses are worth testing with real evidence.
- Do not mark ready until: Synthetic output is labeled separately from observed evidence.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return synthetic enrichment panel. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not synthetic enrichment panel, the main decision is outside synthetic-audience-simulation, lead-enrichment-and-research, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
