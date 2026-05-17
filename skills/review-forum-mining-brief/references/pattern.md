# review forum mining brief

- Category: Research / Audience Simulation
- Product mechanic: mine reviews, forums, communities, calls, and comments for pain, language, triggers, and objections
- Output: review mining brief
- Evidence surfaces: customer-research-synthesis, message-testing

## When To Use

Extract customer language from public or owned feedback.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- Specific constraints, examples, and existing assets for review forum mining brief

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `mine reviews, forums, communities, calls, and comments for pain, language, triggers, and objections` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Customer research synthesis, Message testing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return review mining brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for review forum mining brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: review mining brief.
- Organizing mechanic: mine reviews, forums, communities, calls, and comments for pain, language, triggers, and objections.
- Core fields or sections: review or comment, evidence type, pain, language, trigger, objection, segment, message implication.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence
- Message testing: message, audience, claim, proof, score, risk, objection, next test

## Decision Gates

- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence
- Message testing: message score movement
- Message testing: conversion or reply lift

## Example Prompt

Use $review-forum-mining-brief to create review mining brief for a marketing task in Research / Audience Simulation. Apply the Customer research synthesis, Message testing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
