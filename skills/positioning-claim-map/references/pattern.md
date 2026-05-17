# positioning claim map

- Category: Research / Audience Simulation
- Product mechanic: map competitors, alternatives, claims, proof, objections, and whitespace
- Output: positioning claim map
- Evidence surfaces: customer-research-synthesis

## When To Use

Clarify positioning against alternatives using claims and proof.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for positioning claim map

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `map competitors, alternatives, claims, proof, objections, and whitespace` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return positioning claim map with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for positioning claim map
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: positioning claim map.
- Organizing mechanic: map competitors, alternatives, claims, proof, objections, and whitespace.
- Core fields or sections: alternative, claim, proof, objection, whitespace, segment, risk, decision.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $positioning-claim-map to create positioning claim map for a marketing task in Research / Audience Simulation. Apply the Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
