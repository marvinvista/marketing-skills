# chat creative conversion plan

- Category: Creative / Ads / Assets
- Product mechanic: align ad angles, landing promises, chat questions, qualification rules, and conversion handoff
- Output: chat creative conversion plan
- Evidence surfaces: ad-creative-generation, inbound-chat-qualification, message-testing

## When To Use

Connect creative promises to inbound chat conversion paths.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `inbound-chat-qualification` | questions, answer branches, qualification rules, fallback copy, handoff notes, and booking path | Which visitors book, route to a human, nurture, or exit; Which questions are necessary versus conversion friction |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Inbound chat qualification: Target visitor, qualification criteria, required fields, and disqualifiers
- Inbound chat qualification: Chat questions, routing rules, handoff owner, fallback message, and booking path
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- Specific constraints, examples, and existing assets for chat creative conversion plan

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Inbound chat qualification: Which visitors book, route to a human, nurture, or exit
- Inbound chat qualification: Which questions are necessary versus conversion friction
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `align ad angles, landing promises, chat questions, qualification rules, and conversion handoff` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Inbound chat qualification, Message testing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return chat creative conversion plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for chat creative conversion plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: chat creative conversion plan.
- Organizing mechanic: align ad angles, landing promises, chat questions, qualification rules, and conversion handoff.
- Core fields or sections: ad angle, landing promise, chat question, qualification rule, message match, handoff path, conversion event, fix.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Inbound chat qualification: question, answer branch, qualification rule, score, route, fallback, handoff note
- Message testing: message, audience, claim, proof, score, risk, objection, next test

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Inbound chat qualification: do not mark the artifact ready until each question changes routing or qualification.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Inbound chat qualification: Each question changes routing or qualification.
- Inbound chat qualification: Fallback and handoff messages preserve context for the next owner.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Inbound chat qualification: Asking chat questions that do not change route or handoff quality.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Inbound chat qualification: qualified handoff rate
- Inbound chat qualification: booking completion and fallback rate
- Message testing: message score movement
- Message testing: conversion or reply lift

## Example Prompt

Use $chat-creative-conversion-plan to create chat creative conversion plan for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Inbound chat qualification, Message testing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
