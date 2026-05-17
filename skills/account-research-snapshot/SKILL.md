---
name: account-research-snapshot
description: Use when you need account research snapshot to summarize account context, role pain, trigger, proof match, objection, and first message angle.
---

# account research snapshot

## Quick Start

- Produce account research snapshot.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: account context, role pain, trigger, proof match.
- Use the artifact to decide: Which fields change score, route, or message.
- Do not mark ready until: Every enrichment field has a usage rule and freshness standard.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return account research snapshot. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not account research snapshot, the main decision is outside lead-enrichment-and-research, customer-research-synthesis, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
