# landing page message match

- Category: Creative / Ads / Assets
- Product mechanic: align ad angle, page headline, proof, objections, CTA, and tracking for a conversion path
- Output: message-match landing page spec
- Evidence surfaces: ad-creative-generation, message-testing, seo-content-briefing

## When To Use

Design landing-page variants matched to ad angles.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `message-testing` | audience, claim, proof, clarity, differentiation, objection handling, risk, and next action | Which message advances, changes, or gets rejected; Which weakness requires research, proof, or creative iteration |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Message testing: Messages to compare, target audience, channel, decision criteria, and scoring scale
- Message testing: Proof points, objections, alternatives, risk constraints, and intended next action
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Specific constraints, examples, and existing assets for landing page message match

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Message testing: Which message advances, changes, or gets rejected
- Message testing: Which weakness requires research, proof, or creative iteration
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `align ad angle, page headline, proof, objections, CTA, and tracking for a conversion path` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Message testing, SEO content briefing; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return message-match landing page spec with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for landing page message match
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: message-match landing page spec.
- Organizing mechanic: align ad angle, page headline, proof, objections, CTA, and tracking for a conversion path.
- Core fields or sections: ad angle, page headline, proof block, objection block, CTA, tracking parameter, conversion path.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Message testing: message, audience, claim, proof, score, risk, objection, next test
- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Message testing: do not mark the artifact ready until scores use explicit criteria instead of preference alone.
- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Message testing: Scores use explicit criteria instead of preference alone.
- Message testing: The winning message includes a next test or launch boundary.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Message testing: Choosing a message without separating clarity, proof, differentiation, and risk.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Message testing: message score movement
- Message testing: conversion or reply lift
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality

## Example Prompt

Use $landing-page-message-match to create message-match landing page spec for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Message testing, SEO content briefing mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
