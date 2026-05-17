---
name: citable-proof-asset-kit
description: Use when a marketer or go-to-market operator needs proof kit and publishing checklist for AI Search / Agent Discovery work involving Answer source remediation, Brand governance review, especially when the task must package claims, proof, press, docs, FAQs, and comparison assets so answers have better evidence to cite.
---

# citable proof asset kit

## Quick Start

- Produce proof kit and publishing checklist.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return proof kit and publishing checklist. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
