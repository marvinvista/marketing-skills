---
name: message-test-scorecard
description: Use when you need message test scorecard to score messages by clarity, relevance, proof, differentiation, risk, and next-action strength.
---

# message test scorecard

## Quick Start

- Produce message test scorecard.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: message, audience, clarity, relevance.
- Use the artifact to decide: Which message advances, changes, or gets rejected.
- Do not mark ready until: Scores use explicit criteria instead of preference alone.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return message test scorecard. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not message test scorecard, the main decision is outside message-testing, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
