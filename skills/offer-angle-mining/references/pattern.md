# offer angle mining

- Category: Creative / Ads / Assets
- Product mechanic: mine research, reviews, competitor ads, and sales objections for offer angles worth testing
- Output: offer angle map
- Evidence surfaces: ad-creative-generation, customer-research-synthesis

## When To Use

Find the strongest campaign angles before writing creative.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for offer angle mining

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `mine research, reviews, competitor ads, and sales objections for offer angles worth testing` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return offer angle map with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for offer angle mining
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: offer angle map.
- Organizing mechanic: mine research, reviews, competitor ads, and sales objections for offer angles worth testing.
- Core fields or sections: audience segment, pain, desire, objection, competitor angle, proof point, offer angle, test rationale.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $offer-angle-mining to create offer angle map for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
