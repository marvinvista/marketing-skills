---
name: stakeholder-simulation-scenario-plan
description: Use when a marketer or go-to-market operator needs simulation scenario plan for Research / Audience Simulation work involving Synthetic audience simulation, Message testing, especially when the task must simulate stakeholder reactions to launches, messages, pricing, policy, or market events.
---

# stakeholder simulation scenario plan

## Quick Start

- Produce simulation scenario plan.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return simulation scenario plan. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
