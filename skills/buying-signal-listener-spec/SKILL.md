---
name: buying-signal-listener-spec
description: Use when you need signal listener spec to specify web, product, social, hiring, funding, content, and CRM signals that trigger action.
---

# buying signal listener spec

## Quick Start

- Produce signal listener spec.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: signal type, event, threshold, source.
- Use the artifact to decide: Which visits trigger sales, nurture, retargeting, or no action.
- Do not mark ready until: Confidence level and evidence are visible before routing.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return signal listener spec. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not signal listener spec, the main decision is outside website-visitor-identification, lead-enrichment-and-research, audience-data-sync, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
