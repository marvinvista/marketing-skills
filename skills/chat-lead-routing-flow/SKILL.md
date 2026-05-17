---
name: chat-lead-routing-flow
description: Use when you need chat lead routing flow to turn chat qualification answers into list membership, owner routing, follow-up timing, and suppression-aware actions.
---

# chat lead routing flow

## Quick Start

- Produce chat lead routing flow.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: chat answer, qualification score, list membership, fit rule.
- Use the artifact to decide: Which visitors book, route to a human, nurture, or exit.
- Do not mark ready until: Each question changes routing or qualification.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return chat lead routing flow. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not chat lead routing flow, the main decision is outside inbound-chat-qualification, lead-list-building, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
