---
name: enrichment-field-contract
description: Use when you need enrichment field contract to define enrichment fields, source priority, freshness, usage, and fallback behavior.
---

# enrichment field contract

## Quick Start

- Produce enrichment field contract.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: field, source priority, freshness, confidence.
- Use the artifact to decide: Which fields change score, route, or message.
- Do not mark ready until: Every enrichment field has a usage rule and freshness standard.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return enrichment field contract. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not enrichment field contract, the main decision is outside lead-enrichment-and-research, audience-data-sync, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
