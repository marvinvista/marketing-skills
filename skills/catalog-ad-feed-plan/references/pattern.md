# catalog ad feed plan

- Category: Creative / Ads / Assets
- Product mechanic: turn product attributes, audience segments, and creative rules into a catalog ad feed plan
- Output: catalog creative feed plan
- Evidence surfaces: ad-creative-generation, product-image-generation, audience-data-sync

## When To Use

Build repeatable catalog creative from product data.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `product-image-generation` | shot type, product fidelity, merchandising context, prompts, negative constraints, and visual QA | Which image prompts are ready for generation or retouching; Which visual defects block commerce or ad use |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Product image generation: Product details, required shot types, usage context, dimensions, and brand rules
- Product image generation: Prompt constraints, unacceptable artifacts, approval owner, and retouching path
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Specific constraints, examples, and existing assets for catalog ad feed plan

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Product image generation: Which image prompts are ready for generation or retouching
- Product image generation: Which visual defects block commerce or ad use
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn product attributes, audience segments, and creative rules into a catalog ad feed plan` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Product image generation, Audience data sync; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return catalog creative feed plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for catalog ad feed plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: catalog creative feed plan.
- Organizing mechanic: turn product attributes, audience segments, and creative rules into a catalog ad feed plan.
- Core fields or sections: product field, audience segment, creative rule, image rule, feed mapping, exclusion, destination, QA check.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Product image generation: product, shot type, context, prompt, negative constraint, QA note, approval
- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Product image generation: do not mark the artifact ready until product details, scale, text, and prohibited artifacts are checked.
- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Product image generation: Product details, scale, text, and prohibited artifacts are checked.
- Product image generation: Each asset has a usage context and approval state.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Product image generation: Generating appealing images that fail product fidelity or merchandising needs.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Product image generation: asset acceptance rate
- Product image generation: visual defect rate
- Audience data sync: match rate
- Audience data sync: sync latency and error rate

## Example Prompt

Use $catalog-ad-feed-plan to create catalog creative feed plan for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Product image generation, Audience data sync mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
