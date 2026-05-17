---
name: brand-voice-memory
description: Use when you need brand voice memory to distill approved voice, claims, examples, banned patterns, and review notes into reusable memory.
---

# brand voice memory

## Quick Start

- Produce brand voice memory.
- Read `references/pattern.md` before drafting; it contains product mechanics, required inputs, decision rules, artifact fields, QA checks, failure modes, proof metrics, and an example prompt.

## Skill-Specific Checklist

- Anchor the artifact around these fields: approved phrase, banned pattern, claim, proof.
- Use the artifact to decide: What can publish, what needs edits, and what needs explicit approval.
- Do not mark ready until: Unsupported claims are blocked or rewritten before launch.

## Workflow

1. Confirm the requested artifact, target audience, and review owner.
2. Gather only the missing high-risk inputs; infer low-risk defaults and label assumptions.
3. Apply the relevant decision rules and artifact template from `references/pattern.md`.
4. Return the artifact with QA checks, failure modes, proof metric, and next action.

## Output Contract

Return brand voice memory. Include the decision supported, required inputs, generated artifact, QA checks, failure modes, proof metric, and next action.

## Boundary

Use another skill if the final artifact is not brand voice memory, the main decision is outside brand-governance-review, social-content-automation, or the user only needs broad strategy.

## Guardrails

- Keep private evidence identities and unpublished links out of repo-facing output.
- Separate observed evidence, inference, and recommended action.
- Ask for missing high-risk inputs before producing launch-ready work.
- Keep the artifact narrow enough to execute or review today.
