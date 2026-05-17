---
name: citation-source-gap-map
description: Use when you need citation gap map and proof backlog to identify cited and uncited proof assets, pages, listings, and third-party references.
---

# citation source gap map

## Quick Start

- Produce citation gap map and proof backlog.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: answer claim, cited asset, missing proof, stale proof.
- Use the artifact to decide: Which proof, page, listing, or data fix ships first.
- Do not mark ready until: Every remediation item ties to a specific answer gap.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return citation gap map and proof backlog. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not citation gap map and proof backlog, the main decision is outside answer-source-remediation, seo-content-briefing, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
