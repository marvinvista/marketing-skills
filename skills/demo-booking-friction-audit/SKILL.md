---
name: demo-booking-friction-audit
description: Use when you need booking friction audit to inspect the path from ad, page, chat, form, or outreach to booked meeting.
---

# demo booking friction audit

## Quick Start

- Produce booking friction audit.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: entry point, friction point, required field, routing delay.
- Use the artifact to decide: Which visitors book, route to a human, nurture, or exit.
- Do not mark ready until: Each question changes routing or qualification.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return booking friction audit. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not booking friction audit, the main decision is outside inbound-chat-qualification, website-visitor-identification, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
