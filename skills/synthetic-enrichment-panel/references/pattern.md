# synthetic enrichment panel

- Category: Research / Audience Simulation
- Product mechanic: test enrichment assumptions, personalization cues, confidence limits, and validation needs with synthetic panels
- Output: synthetic enrichment panel
- Evidence surfaces: synthetic-audience-simulation, lead-enrichment-and-research, customer-research-synthesis

## When To Use

Pressure-test enrichment assumptions before personalization reaches outreach or creative.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `synthetic-audience-simulation` | persona assumptions, prompt framing, scenarios, synthetic responses, validation needs, and confidence limits | Which hypotheses are worth testing with real evidence; Which simulated output must not be treated as proof |
| `lead-enrichment-and-research` | fields, evidence freshness, confidence, role pain, trigger, message use, and fallback behavior | Which fields change score, route, or message; Which missing fields require manual research or conservative fallback |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Decision to improve and audience segment under study
- Known assumptions, hypotheses, and prior evidence
- Research method, respondent criteria, and confidence threshold
- Synthesis format required for a campaign, product, or positioning decision
- Synthetic audience simulation: Audience definition, assumptions, scenario, question set, and intended decision
- Synthetic audience simulation: Validation plan, confidence threshold, known evidence, and excluded claims
- Lead enrichment and research: Target records, required enrichment fields, freshness rule, and source priority
- Lead enrichment and research: Usage rule for routing, personalization, scoring, and fallback when a field is missing
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for synthetic enrichment panel

## Decision Rules

- Frame the decision before collecting or simulating responses.
- Keep observed evidence, synthetic output, and inference separate.
- Translate findings into a decision, not just themes.
- Synthetic audience simulation: Which hypotheses are worth testing with real evidence
- Synthetic audience simulation: Which simulated output must not be treated as proof
- Lead enrichment and research: Which fields change score, route, or message
- Lead enrichment and research: Which missing fields require manual research or conservative fallback
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `test enrichment assumptions, personalization cues, confidence limits, and validation needs with synthetic panels` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Synthetic audience simulation, Lead enrichment and research, Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return synthetic enrichment panel with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for synthetic enrichment panel
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: synthetic enrichment panel.
- Organizing mechanic: test enrichment assumptions, personalization cues, confidence limits, and validation needs with synthetic panels.
- Core fields or sections: enrichment assumption, persona, scenario, personalization cue, simulated reaction, confidence, validation need, blocked use.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Synthetic audience simulation: persona, assumption, scenario, prompt, response, confidence, validation need
- Lead enrichment and research: record, field, value, confidence, freshness, message use, fallback
- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- Synthetic audience simulation: do not mark the artifact ready until synthetic output is labeled separately from observed evidence.
- Lead enrichment and research: do not mark the artifact ready until every enrichment field has a usage rule and freshness standard.
- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- The artifact states sample, segment, assumption, and confidence limits.
- Findings include implications, objections, and next evidence to collect.
- Quotes or examples are labeled by evidence type.
- Synthetic audience simulation: Synthetic output is labeled separately from observed evidence.
- Synthetic audience simulation: The artifact includes a validation step before launch use.
- Lead enrichment and research: Every enrichment field has a usage rule and freshness standard.
- Lead enrichment and research: Low-confidence values are not used for strong personalization.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Treating synthetic responses as proof without validation.
- Summarizing interviews without a decision framework.
- Averaging segments that need different messages or channels.
- Synthetic audience simulation: Treating simulated reactions as proof instead of hypothesis generation.
- Lead enrichment and research: Collecting enrichment data that does not change routing or messaging.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Decision confidence
- Assumptions validated or rejected
- Segment or message clarity
- Next evidence cost reduced
- Synthetic audience simulation: assumption shortlist quality
- Synthetic audience simulation: validation hit rate
- Lead enrichment and research: field completion rate
- Lead enrichment and research: freshness and confidence coverage
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $synthetic-enrichment-panel to create synthetic enrichment panel for a marketing task in Research / Audience Simulation. Apply the Synthetic audience simulation, Lead enrichment and research, Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
