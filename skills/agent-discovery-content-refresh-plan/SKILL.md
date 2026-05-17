---
name: agent-discovery-content-refresh-plan
description: Use when you need refresh plan and CMS handoff to refresh stale pages, FAQs, comparison copy, and proof assets based on answer-surface gaps.
---

# agent discovery content refresh plan

## Quick Start

- Produce refresh plan and CMS handoff.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: stale page, target question, missing proof, refresh angle.
- Use the artifact to decide: Which page, section, or proof asset should be created or refreshed.
- Do not mark ready until: Each brief includes the answer, proof, schema need, and indexability check.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return refresh plan and CMS handoff. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not refresh plan and CMS handoff, the main decision is outside seo-content-briefing, ai-search-visibility-monitoring, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
