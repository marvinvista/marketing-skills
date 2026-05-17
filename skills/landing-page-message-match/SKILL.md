---
name: landing-page-message-match
description: Use when a marketer or go-to-market operator needs message-match landing page spec for Creative / Ads / Assets work involving Ad creative generation, Message testing, SEO content briefing, especially when the task must align ad angle, page headline, proof, objections, CTA, and tracking for a conversion path.
---

# landing page message match

## Quick Start

- Produce message-match landing page spec.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return message-match landing page spec. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
