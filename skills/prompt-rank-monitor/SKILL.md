---
name: prompt-rank-monitor
description: Use when a marketer or go-to-market operator needs prompt-rank table and monitoring cadence for AI Search / Agent Discovery work involving AI search visibility monitoring, especially when the task must build a reusable prompt-rank table for answer engines and competitor comparisons.
---

# prompt rank monitor

## Quick Start

- Produce prompt-rank table and monitoring cadence.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.
- Run `scripts/build_prompt_rank_table.py` when the user provides structured inputs for the repeatable table, scorecard, or checklist.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return prompt-rank table and monitoring cadence. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
