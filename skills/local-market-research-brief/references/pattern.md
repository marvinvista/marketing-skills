# local market research brief

- Category: Research / Audience Simulation
- Product mechanic: turn local reviews, storefront signals, route context, and customer language into market insight
- Output: local market research brief
- Evidence surfaces: customer-research-synthesis, local-storefront-growth, lead-list-building

## When To Use

Synthesize local market signals into campaign and route decisions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |
| `local-storefront-growth` | locations, radius, local offer, route plan, reviews, community proof, and owner follow-up | Which local targets get field action versus digital follow-up; Which local proof or listing gap blocks trust |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Local storefront growth: Target location set, radius, category, offer, local proof, and field owner
- Local storefront growth: Route constraints, review signals, storefront data, and follow-up channel
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Specific constraints, examples, and existing assets for local market research brief

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- Local storefront growth: Which local targets get field action versus digital follow-up
- Local storefront growth: Which local proof or listing gap blocks trust
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn local reviews, storefront signals, route context, and customer language into market insight` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Customer research synthesis, Local storefront growth, Lead list building; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return local market research brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for local market research brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: local market research brief.
- Organizing mechanic: turn local reviews, storefront signals, route context, and customer language into market insight.
- Core fields or sections: location, review signal, storefront gap, local language, route context, segment, offer implication, next action.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence
- Local storefront growth: location, radius, offer, local proof, route, owner, follow-up
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route

## Decision Gates

- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.
- Local storefront growth: do not mark the artifact ready until routes are prioritized by fit, proximity, and actionability.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.
- Local storefront growth: Routes are prioritized by fit, proximity, and actionability.
- Local storefront growth: Local proof is tied to the offer and outreach path.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.
- Local storefront growth: Treating local prospecting as a generic list without route and proof context.
- Lead list building: Building a large list before defining exclusions and evidence standards.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence
- Local storefront growth: route completion
- Local storefront growth: local response or conversion rate
- Lead list building: qualified record count
- Lead list building: owner acceptance rate

## Example Prompt

Use $local-market-research-brief to create local market research brief for a marketing task in Research / Audience Simulation. Apply the Customer research synthesis, Local storefront growth, Lead list building mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
