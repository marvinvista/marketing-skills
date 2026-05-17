---
name: multichannel-prospecting-orchestration
description: Use when you need multichannel prospecting map to coordinate email, LinkedIn, phone, retargeting, chat, and sales owner handoff.
---

# multichannel prospecting orchestration

## Quick Start

- Produce multichannel prospecting map.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: channel, step, trigger, owner.
- Use the artifact to decide: Which step runs, stops, or escalates based on signal.
- Do not mark ready until: Every step has a trigger, wait rule, stop rule, and reply route.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return multichannel prospecting map. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not multichannel prospecting map, the main decision is outside outbound-cadence-automation, marketing-ops-orchestration, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
