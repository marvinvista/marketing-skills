# creative performance readout

- Category: Creative / Ads / Assets
- Product mechanic: separate creative signal from tracking, spend, audience, and conversion-path noise
- Output: creative readout and next-test backlog
- Evidence surfaces: ad-creative-generation, campaign-analytics-qa

## When To Use

Analyze creative results and choose next tests.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Specific constraints, examples, and existing assets for creative performance readout

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `separate creative signal from tracking, spend, audience, and conversion-path noise` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Campaign analytics QA; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creative readout and next-test backlog with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for creative performance readout
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creative readout and next-test backlog.
- Organizing mechanic: separate creative signal from tracking, spend, audience, and conversion-path noise.
- Core fields or sections: asset, audience, spend context, tracking confidence, creative signal, learning, next test, stop rule.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness

## Example Prompt

Use $creative-performance-readout to create creative readout and next-test backlog for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Campaign analytics QA mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
