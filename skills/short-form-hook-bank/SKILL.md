---
name: short-form-hook-bank
description: Use when you need hook bank and test notes to generate platform-specific hooks for short-form video while preserving proof and CTA.
---

# short-form hook bank

## Quick Start

- Produce hook bank and test notes.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: platform, hook type, opening line, proof cue.
- Use the artifact to decide: Which moments belong in the first seconds versus proof body.
- Do not mark ready until: The storyboard names timing, visual, line, caption, and CTA.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return hook bank and test notes. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not hook bank and test notes, the main decision is outside video-ad-production, social-content-automation, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
