# synthetic creative test panel

- Category: Creative / Ads / Assets
- Product mechanic: use synthetic audience scenarios to pressure-test creative angles, reactions, confidence, and validation needs
- Output: synthetic creative test panel
- Evidence surfaces: synthetic-audience-simulation, ad-creative-generation, message-testing

## When To Use

Stress-test creative concepts with synthetic audience assumptions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `synthetic-audience-simulation` | persona assumptions, prompt framing, scenarios, synthetic responses, validation needs, and confidence limits | Which hypotheses are worth testing with real evidence; Which simulated output must not be treated as proof |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Synthetic audience simulation: Audience definition, assumptions, scenario, question set, and intended decision
- Synthetic audience simulation: Validation plan, confidence threshold, known evidence, and excluded claims
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- Specific constraints, examples, and existing assets for synthetic creative test panel

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Synthetic audience simulation: Which hypotheses are worth testing with real evidence
- Synthetic audience simulation: Which simulated output must not be treated as proof
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `use synthetic audience scenarios to pressure-test creative angles, reactions, confidence, and validation needs` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Synthetic audience simulation, Ad creative generation, Message testing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return synthetic creative test panel with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for synthetic creative test panel
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: synthetic creative test panel.
- Organizing mechanic: use synthetic audience scenarios to pressure-test creative angles, reactions, confidence, and validation needs.
- Core fields or sections: audience assumption, scenario, creative angle, simulated reaction, validation need, confidence, next real test.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Synthetic audience simulation: persona, assumption, scenario, prompt, response, confidence, validation need
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Message testing: message, audience, claim, proof, score, risk, objection, next test

## Decision Gates

- Synthetic audience simulation: do not mark the artifact ready until synthetic output is labeled separately from observed evidence.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Synthetic audience simulation: Synthetic output is labeled separately from observed evidence.
- Synthetic audience simulation: The artifact includes a validation step before launch use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Synthetic audience simulation: Treating simulated reactions as proof instead of hypothesis generation.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Synthetic audience simulation: assumption shortlist quality
- Synthetic audience simulation: validation hit rate
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Message testing: message score movement
- Message testing: conversion or reply lift

## Example Prompt

Use $synthetic-creative-test-panel to create synthetic creative test panel for a marketing task in Creative / Ads / Assets. Apply the Synthetic audience simulation, Ad creative generation, Message testing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
