# UGC ad script pack

- Category: Creative / Ads / Assets
- Product mechanic: write creator-style ad scripts with believable hooks, proof moments, and usage constraints
- Output: UGC script pack
- Evidence surfaces: ugc-creator-workflow, ad-creative-generation

## When To Use

Create UGC-style ad scripts for paid or organic use.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ugc-creator-workflow` | creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse | Which creators or assets are approved, revised, renewed, or reused; Which rights or approvals block paid amplification |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- UGC creator workflow: Creator criteria, offer, deliverables, asset examples, and usage rights
- UGC creator workflow: Approval path, revision rule, tagging taxonomy, and paid reuse constraints
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for UGC ad script pack

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- UGC creator workflow: Which creators or assets are approved, revised, renewed, or reused
- UGC creator workflow: Which rights or approvals block paid amplification
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `write creator-style ad scripts with believable hooks, proof moments, and usage constraints` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for UGC creator workflow, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return UGC script pack with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for UGC ad script pack
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: UGC script pack.
- Organizing mechanic: write creator-style ad scripts with believable hooks, proof moments, and usage constraints.
- Core fields or sections: creator persona, hook, story beat, product use, proof moment, disclosure, usage limit, CTA.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- UGC creator workflow: creator, deliverable, hook, proof, rights, revision, approval, reuse state
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- UGC creator workflow: do not mark the artifact ready until rights, usage windows, and edit permissions are explicit.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- UGC creator workflow: Rights, usage windows, and edit permissions are explicit.
- UGC creator workflow: Creator fit is scored beyond follower count.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- UGC creator workflow: Collecting creator assets without rights, tagging, and reuse rules.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- UGC creator workflow: approved asset rate
- UGC creator workflow: creator renewal or reuse rate
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $ugc-ad-script-pack to create UGC script pack for a marketing task in Creative / Ads / Assets. Apply the UGC creator workflow, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
