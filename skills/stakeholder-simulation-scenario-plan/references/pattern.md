# stakeholder simulation scenario plan

- Category: Research / Audience Simulation
- Product mechanic: simulate stakeholder reactions to launches, messages, pricing, policy, or market events
- Output: simulation scenario plan
- Evidence surfaces: synthetic-audience-simulation, message-testing

## When To Use

Plan stakeholder reaction simulations for launch or message decisions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `synthetic-audience-simulation` | persona assumptions, prompt framing, scenarios, synthetic responses, validation needs, and confidence limits | Which hypotheses are worth testing with real evidence; Which simulated output must not be treated as proof |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Synthetic audience simulation: Audience definition, assumptions, scenario, question set, and intended decision
- Synthetic audience simulation: Validation plan, confidence threshold, known evidence, and excluded claims
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- Specific constraints, examples, and existing assets for stakeholder simulation scenario plan

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Synthetic audience simulation: Which hypotheses are worth testing with real evidence
- Synthetic audience simulation: Which simulated output must not be treated as proof
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `simulate stakeholder reactions to launches, messages, pricing, policy, or market events` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Synthetic audience simulation, Message testing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return simulation scenario plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for stakeholder simulation scenario plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: simulation scenario plan.
- Organizing mechanic: simulate stakeholder reactions to launches, messages, pricing, policy, or market events.
- Core fields or sections: stakeholder type, scenario, expected reaction, objection, risk, decision, validation step.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Synthetic audience simulation: persona, assumption, scenario, prompt, response, confidence, validation need
- Message testing: message, audience, claim, proof, score, risk, objection, next test

## Decision Gates

- Synthetic audience simulation: do not mark the artifact ready until synthetic output is labeled separately from observed evidence.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Synthetic audience simulation: Synthetic output is labeled separately from observed evidence.
- Synthetic audience simulation: The artifact includes a validation step before launch use.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Synthetic audience simulation: Treating simulated reactions as proof instead of hypothesis generation.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Synthetic audience simulation: assumption shortlist quality
- Synthetic audience simulation: validation hit rate
- Message testing: message score movement
- Message testing: conversion or reply lift

## Example Prompt

Use $stakeholder-simulation-scenario-plan to create simulation scenario plan for a marketing task in Research / Audience Simulation. Apply the Synthetic audience simulation, Message testing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
