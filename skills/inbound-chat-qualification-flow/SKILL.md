---
name: inbound-chat-qualification-flow
description: Use when you need chat qualification flow to design chat questions, qualification logic, handoff moments, and fallback messages.
---

# inbound chat qualification flow

## Quick Start

- Produce chat qualification flow.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: question, branch, qualification rule, score.
- Use the artifact to decide: Which visitors book, route to a human, nurture, or exit.
- Do not mark ready until: Each question changes routing or qualification.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return chat qualification flow. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not chat qualification flow, the main decision is outside inbound-chat-qualification, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
