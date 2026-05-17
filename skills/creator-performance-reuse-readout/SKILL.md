---
name: creator-performance-reuse-readout
description: Use when you need creator performance readout to evaluate creator assets for performance, learning, renewal, and paid reuse decisions.
---

# creator performance reuse readout

## Quick Start

- Produce creator performance readout.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: creator asset, spend or organic context, performance signal, learning.
- Use the artifact to decide: Which creators or assets are approved, revised, renewed, or reused.
- Do not mark ready until: Rights, usage windows, and edit permissions are explicit.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return creator performance readout. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not creator performance readout, the main decision is outside ugc-creator-workflow, social-content-automation, campaign-analytics-qa, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
