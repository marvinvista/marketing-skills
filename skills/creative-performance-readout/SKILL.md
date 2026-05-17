---
name: creative-performance-readout
description: Use when a marketer or go-to-market operator needs creative readout and next-test backlog for Creative / Ads / Assets work involving Ad creative generation, Campaign analytics QA, especially when the task must separate creative signal from tracking, spend, audience, and conversion-path noise.
---

# creative performance readout

## Quick Start

- Produce creative readout and next-test backlog.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return creative readout and next-test backlog. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
