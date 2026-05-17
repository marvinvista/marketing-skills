---
name: ai-referral-roi-readout
description: Use when you need AI referral readout and dashboard spec to read AI referrals, bot traffic, assisted conversion, and revenue signal without over-claiming attribution.
---

# AI referral ROI readout

## Quick Start

- Produce AI referral readout and dashboard spec.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: referral surface, traffic type, session path, assisted event.
- Use the artifact to decide: Which prompts need monitoring, remediation, or new proof.
- Do not mark ready until: Observed answer text is separated from interpretation.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return AI referral readout and dashboard spec. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not AI referral readout and dashboard spec, the main decision is outside ai-search-visibility-monitoring, campaign-analytics-qa, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
