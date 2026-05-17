# brand compliance creative review

- Category: Creative / Ads / Assets
- Product mechanic: review ads and assets for claim support, brand fit, legal risk, and platform constraints
- Output: creative compliance review
- Evidence surfaces: brand-governance-review, ad-creative-generation

## When To Use

Review creative before launch, reuse, or paid amplification.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for brand compliance creative review

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `review ads and assets for claim support, brand fit, legal risk, and platform constraints` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Brand governance review, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creative compliance review with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for brand compliance creative review
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creative compliance review.
- Organizing mechanic: review ads and assets for claim support, brand fit, legal risk, and platform constraints.
- Core fields or sections: asset, claim, proof, voice fit, platform risk, required edit, reviewer, approval state.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Brand governance review: review issue count
- Brand governance review: approval turnaround time
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $brand-compliance-creative-review to create creative compliance review for a marketing task in Creative / Ads / Assets. Apply the Brand governance review, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
