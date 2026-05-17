---
name: email-template-system
description: Use when you need email template system to create reusable templates, dynamic fields, QA states, and version rules.
---

# email template system

## Quick Start

- Produce email template system.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: template, dynamic field, segment, proof block.
- Use the artifact to decide: Which work can launch, wait, or roll back.
- Do not mark ready until: Every dependency has an owner and failure fallback.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return email template system. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not email template system, the main decision is outside marketing-ops-orchestration, outbound-cadence-automation, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
