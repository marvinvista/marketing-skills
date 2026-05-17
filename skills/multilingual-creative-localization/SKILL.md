---
name: multilingual-creative-localization
description: Use when you need localized creative plan to localize campaign copy, video, voice, and proof while preserving intent and claim boundaries.
---

# multilingual creative localization

## Quick Start

- Produce localized creative plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: locale, original intent, claim, proof.
- Use the artifact to decide: Which content repeats as a system versus a one-off post.
- Do not mark ready until: Hooks, examples, CTAs, and review notes are channel-specific.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return localized creative plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not localized creative plan, the main decision is outside social-content-automation, brand-governance-review, video-ad-production, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
