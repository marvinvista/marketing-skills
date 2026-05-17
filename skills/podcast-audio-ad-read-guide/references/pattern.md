# podcast audio ad read guide

- Category: Creative / Ads / Assets
- Product mechanic: write host-read or produced audio ads with pronunciation, timing, claim, and CTA control
- Output: audio ad script and read guide
- Evidence surfaces: social-content-automation, ad-creative-generation

## When To Use

Create podcast or audio ad copy and read guidance.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for podcast audio ad read guide

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `write host-read or produced audio ads with pronunciation, timing, claim, and CTA control` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return audio ad script and read guide with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for podcast audio ad read guide
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: audio ad script and read guide.
- Organizing mechanic: write host-read or produced audio ads with pronunciation, timing, claim, and CTA control.
- Core fields or sections: host line, timing, pronunciation, claim, proof, CTA, read style, compliance note.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $podcast-audio-ad-read-guide to create audio ad script and read guide for a marketing task in Creative / Ads / Assets. Apply the Social content automation, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
