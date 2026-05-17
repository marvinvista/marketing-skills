---
name: ugc-intake-rights-workflow
description: Use when a marketer or go-to-market operator needs UGC intake and rights workflow for Content / Creator / Social work involving UGC creator workflow, Ad creative generation, especially when the task must manage creator asset intake, rights, tagging, approvals, edits, and paid reuse.
---

# UGC intake rights workflow

## Quick Start

- Produce UGC intake and rights workflow.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return UGC intake and rights workflow. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
