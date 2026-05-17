---
name: lead-list-prioritization-scorecard
description: Use when a marketer or go-to-market operator needs lead scoring table and routing notes for Lead Intelligence / Conversion work involving Lead list building, Lead enrichment and research, especially when the task must score leads by fit, trigger, intent, evidence strength, urgency, and route.
---

# lead list prioritization scorecard

## Quick Start

- Produce lead scoring table and routing notes.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.
- Run `scripts/score_leads.py` when the user provides structured inputs for the repeatable table, scorecard, or checklist.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return lead scoring table and routing notes. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
