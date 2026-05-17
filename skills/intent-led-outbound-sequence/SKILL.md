---
name: intent-led-outbound-sequence
description: Use when a marketer or go-to-market operator needs intent-led email sequence for Lead Intelligence / Conversion work involving Outbound cadence automation, Lead enrichment and research, especially when the task must write outbound emails tied to a specific trigger, pain, proof, and reply route.
---

# intent-led outbound sequence

## Quick Start

- Produce intent-led email sequence.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return intent-led email sequence. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
