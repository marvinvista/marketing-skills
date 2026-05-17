# creative enrichment personalization plan

- Category: Creative / Ads / Assets
- Product mechanic: turn enrichment fields into personalization claims, creative variants, confidence checks, and fallback copy
- Output: creative personalization plan
- Evidence surfaces: ad-creative-generation, lead-enrichment-and-research

## When To Use

Use enrichment fields to personalize creative without overreaching.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `lead-enrichment-and-research` | fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior | Which fields change score, route, or message; Which missing fields require manual research or conservative fallback |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Lead enrichment and research: Target records, required enrichment fields, freshness rule, and source priority
- Lead enrichment and research: Usage rule for routing, personalization, scoring, and fallback when a field is missing
- Specific constraints, examples, and existing assets for creative enrichment personalization plan

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Lead enrichment and research: Which fields change score, route, or message
- Lead enrichment and research: Which missing fields require manual research or conservative fallback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn enrichment fields into personalization claims, creative variants, confidence checks, and fallback copy` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Lead enrichment and research; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creative personalization plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for creative enrichment personalization plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creative personalization plan.
- Organizing mechanic: turn enrichment fields into personalization claims, creative variants, confidence checks, and fallback copy.
- Core fields or sections: enrichment field, audience cue, personalization claim, creative variant, confidence, fallback copy, review flag.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Lead enrichment and research: record, field, value, confidence, freshness, message use, fallback

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Lead enrichment and research: do not mark the artifact ready until every enrichment field has a usage rule and freshness standard.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Lead enrichment and research: Every enrichment field has a usage rule and freshness standard.
- Lead enrichment and research: Low-confidence values are not used for strong personalization.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Lead enrichment and research: Collecting enrichment data that does not change routing or messaging.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Lead enrichment and research: field completion rate
- Lead enrichment and research: freshness and confidence coverage

## Example Prompt

Use $creative-enrichment-personalization-plan to create creative personalization plan for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Lead enrichment and research mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
