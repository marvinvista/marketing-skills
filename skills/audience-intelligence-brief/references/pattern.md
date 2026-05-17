# audience intelligence brief

- Category: Research / Audience Simulation
- Product mechanic: turn audience data into motivations, segments, channels, triggers, and risks
- Output: audience intelligence brief
- Evidence surfaces: customer-research-synthesis, audience-data-sync

## When To Use

Convert audience data into campaign decisions and channel choices.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |
| `audience-data-sync` | fields, joins, freshness, destinations, exclusions, consent, owner checks, and sync failures | Which audience is eligible for activation; Which sync gap blocks launch or needs rollback |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Audience data sync: Audience definition, field mapping, refresh cadence, destination, and owner
- Audience data sync: Consent, suppression, join keys, exclusion rules, and expected row counts
- Specific constraints, examples, and existing assets for audience intelligence brief

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- Audience data sync: Which audience is eligible for activation
- Audience data sync: Which sync gap blocks launch or needs rollback
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn audience data into motivations, segments, channels, triggers, and risks` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Customer research synthesis, Audience data sync; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return audience intelligence brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for audience intelligence brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: audience intelligence brief.
- Organizing mechanic: turn audience data into motivations, segments, channels, triggers, and risks.
- Core fields or sections: segment, motivation, channel, trigger, risk, data signal, message implication, next test.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence
- Audience data sync: audience, field, join key, destination, refresh, exclusion, owner, check

## Decision Gates

- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.
- Audience data sync: do not mark the artifact ready until expected and actual counts are checked before activation.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.
- Audience data sync: Expected and actual counts are checked before activation.
- Audience data sync: Consent and suppression rules are visible in the contract.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.
- Audience data sync: Activating an audience before validating fields, counts, and exclusions.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence
- Audience data sync: match rate
- Audience data sync: sync latency and error rate

## Example Prompt

Use $audience-intelligence-brief to create audience intelligence brief for a marketing task in Research / Audience Simulation. Apply the Customer research synthesis, Audience data sync mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
