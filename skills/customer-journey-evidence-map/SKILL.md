---
name: customer-journey-evidence-map
description: Use when you need journey evidence map to map stages, questions, objections, proof needs, channels, and conversion gaps.
---

# customer journey evidence map

## Quick Start

- Produce journey evidence map.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: stage, question, objection, proof need.
- Use the artifact to decide: Which message, segment, or channel assumption changes.
- Do not mark ready until: Observed evidence, synthesis, and recommendation are labeled separately.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return journey evidence map. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not journey evidence map, the main decision is outside customer-research-synthesis, inbound-chat-qualification, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
