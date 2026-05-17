---
name: claims-hallucination-review
description: Use when you need claims review checklist to review AI-generated marketing for unsupported claims, factual drift, missing caveats, and legal risk.
---

# claims hallucination review

## Quick Start

- Produce claims review checklist.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: generated claim, evidence status, drift risk, caveat.
- Use the artifact to decide: What can publish, what needs edits, and what needs explicit approval.
- Do not mark ready until: Unsupported claims are blocked or rewritten before launch.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return claims review checklist. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not claims review checklist, the main decision is outside brand-governance-review, answer-source-remediation, ai-marketing-agent-workflow, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
