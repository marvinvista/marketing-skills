---
name: experiment-readout
description: Use when you need experiment readout to summarize experiment result, confidence, tradeoffs, decision, and next test.
---

# experiment readout

## Quick Start

- Produce experiment readout.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: hypothesis, variant, result, confidence.
- Use the artifact to decide: Which metrics are trustworthy enough for a decision.
- Do not mark ready until: Tracking is tested before performance interpretation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return experiment readout. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not experiment readout, the main decision is outside campaign-analytics-qa, message-testing, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
