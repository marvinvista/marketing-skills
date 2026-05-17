---
name: referral-partner-lead-loop
description: Use when you need referral lead loop plan to design partner, affiliate, referral, or ambassador lead flow with tracking and ownership.
---

# referral partner lead loop

## Quick Start

- Produce referral lead loop plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: partner type, referral trigger, lead handoff, tracking field.
- Use the artifact to decide: Which records qualify for action now.
- Do not mark ready until: Every accepted record has fit, trigger, evidence, and a route.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return referral lead loop plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not referral lead loop plan, the main decision is outside lead-list-building, outbound-cadence-automation, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
