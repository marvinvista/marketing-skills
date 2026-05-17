# experiment readout

- Category: Lifecycle / Ops / Analytics
- Product mechanic: summarize experiment result, confidence, tradeoffs, decision, and next test
- Output: experiment readout
- Evidence surfaces: campaign-analytics-qa, message-testing

## When To Use

Turn campaign or message tests into decisions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |

## Required Inputs

- Campaign, lifecycle, or data workflow boundary
- Events, properties, audiences, consent rules, and owners
- Tools, destinations, templates, and rollback constraints
- Measurement question and decision cadence
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- Specific constraints, examples, and existing assets for experiment readout

## Decision Rules

- Define the data contract before evaluating performance.
- QA audiences, assets, tracking, and rollback before launch.
- Separate plumbing failures from campaign-performance interpretation.
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `summarize experiment result, confidence, tradeoffs, decision, and next test` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Campaign analytics QA, Message testing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return experiment readout with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for experiment readout
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: experiment readout.
- Organizing mechanic: summarize experiment result, confidence, tradeoffs, decision, and next test.
- Core fields or sections: hypothesis, variant, result, confidence, tradeoff, decision, next test, metric caveat.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact
- Message testing: message, audience, claim, proof, score, risk, objection, next test

## Decision Gates

- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.

## QA Checks

- Every field, audience, event, and destination has an owner and check.
- Consent, suppression, and rollback are visible in the artifact.
- The readout says what decision the metric will change.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.

## Failure Modes

- Reading performance before verifying event and audience integrity.
- Launching without suppression or rollback coverage.
- Building dashboards that do not map to an operating decision.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.

## Proof Metrics

- QA pass rate
- Audience sync accuracy
- Decision latency
- Lifecycle movement or reactivation lift
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness
- Message testing: message score movement
- Message testing: conversion or reply lift

## Example Prompt

Use $experiment-readout to create experiment readout for a marketing task in Lifecycle / Ops / Analytics. Apply the Campaign analytics QA, Message testing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
