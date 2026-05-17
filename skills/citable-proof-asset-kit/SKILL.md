---
name: citable-proof-asset-kit
description: Use when you need proof kit and publishing checklist to package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite.
---

# citable proof asset kit

## Quick Start

- Produce proof kit and publishing checklist.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: claim, proof asset, format, audience question.
- Use the artifact to decide: Which proof, page, listing, or data fix ships first.
- Do not mark ready until: Every remediation item ties to a specific answer gap.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return proof kit and publishing checklist. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not proof kit and publishing checklist, the main decision is outside answer-source-remediation, brand-governance-review, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
