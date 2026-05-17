# product image QA brief

- Category: Creative / Ads / Assets
- Product mechanic: define product image generation constraints, shot types, merchandising context, and QA checks
- Output: product image brief and QA checklist
- Evidence surfaces: product-image-generation, ad-creative-generation

## When To Use

Create and QA product imagery for commerce or ads.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `product-image-generation` | shot type, product fidelity, merchandising context, prompts, negative constraints, and visual QA | Which image prompts are ready for generation or retouching; Which visual defects block commerce or ad use |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Product image generation: Product details, required shot types, usage context, dimensions, and brand rules
- Product image generation: Prompt constraints, unacceptable artifacts, approval owner, and retouching path
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for product image QA brief

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Product image generation: Which image prompts are ready for generation or retouching
- Product image generation: Which visual defects block commerce or ad use
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `define product image generation constraints, shot types, merchandising context, and QA checks` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Product image generation, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return product image brief and QA checklist with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for product image QA brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: product image brief and QA checklist.
- Organizing mechanic: define product image generation constraints, shot types, merchandising context, and QA checks.
- Core fields or sections: product attribute, shot type, context, fidelity risk, prompt constraint, unacceptable artifact, approval state.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Product image generation: product, shot type, context, prompt, negative constraint, QA note, approval
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- Product image generation: do not mark the artifact ready until product details, scale, text, and prohibited artifacts are checked.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Product image generation: Product details, scale, text, and prohibited artifacts are checked.
- Product image generation: Each asset has a usage context and approval state.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Product image generation: Generating appealing images that fail product fidelity or merchandising needs.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Product image generation: asset acceptance rate
- Product image generation: visual defect rate
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $product-image-qa-brief to create product image brief and QA checklist for a marketing task in Creative / Ads / Assets. Apply the Product image generation, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
