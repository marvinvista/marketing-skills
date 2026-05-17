# answer-led list hypothesis panel

- Category: Lead Intelligence / Conversion
- Product mechanic: use answer proof gaps and synthetic audience checks to refine list hypotheses, disqualifiers, and follow-up routes
- Output: answer-led list hypothesis panel
- Evidence surfaces: lead-list-building, answer-source-remediation, synthetic-audience-simulation

## When To Use

Use answer gaps to sharpen list hypotheses before outreach.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |
| `synthetic-audience-simulation` | persona assumptions, prompt framing, scenarios, synthetic responses, validation needs, and confidence limits | Which hypotheses are worth testing with real evidence; Which simulated output must not be treated as proof |

## Required Inputs

- Target account or lead segment, trigger, and disqualifiers
- Available lists, enrichment fields, intent signals, and consent limits
- Sales handoff owner, CRM fields, and next-step rules
- Message library, proof, and routing or booking path
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Synthetic audience simulation: Audience definition, assumptions, scenario, question set, and intended decision
- Synthetic audience simulation: Validation plan, confidence threshold, known evidence, and excluded claims
- Specific constraints, examples, and existing assets for answer-led list hypothesis panel

## Decision Rules

- Do not enrich or sequence leads until the qualification rule is explicit.
- Tie personalization to a real trigger, pain, role, or account event.
- Route every reply, visit, or chat outcome to a named next action.
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- Synthetic audience simulation: Which hypotheses are worth testing with real evidence
- Synthetic audience simulation: Which simulated output must not be treated as proof
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `use answer proof gaps and synthetic audience checks to refine list hypotheses, disqualifiers, and follow-up routes` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Lead list building, Answer source remediation, Synthetic audience simulation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return answer-led list hypothesis panel with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for answer-led list hypothesis panel
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: answer-led list hypothesis panel.
- Organizing mechanic: use answer proof gaps and synthetic audience checks to refine list hypotheses, disqualifiers, and follow-up routes.
- Core fields or sections: answer gap, proof gap, list hypothesis, target segment, synthetic check, disqualifier, confidence, follow-up route.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status
- Synthetic audience simulation: persona, assumption, scenario, prompt, response, confidence, validation need

## Decision Gates

- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.
- Synthetic audience simulation: do not mark the artifact ready until synthetic output is labeled separately from observed evidence.

## QA Checks

- Every record has fit, intent, evidence, and next-step fields or a clear gap.
- Outreach respects suppression, consent, and channel-specific risk.
- The handoff is auditable from signal to owner to next step.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.
- Synthetic audience simulation: Synthetic output is labeled separately from observed evidence.
- Synthetic audience simulation: The artifact includes a validation step before launch use.

## Failure Modes

- Building large lists with no disqualification logic.
- Using enrichment fields that do not change the message or route.
- Automating follow-up before reply handling is defined.
- Lead list building: Building a large list before defining exclusions and evidence standards.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.
- Synthetic audience simulation: Treating simulated reactions as proof instead of hypothesis generation.

## Proof Metrics

- Qualified records created
- Positive reply or booking rate
- Signal-to-action latency
- Handoff completion and CRM accuracy
- Lead list building: qualified record count
- Lead list building: owner acceptance rate
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy
- Synthetic audience simulation: assumption shortlist quality
- Synthetic audience simulation: validation hit rate

## Example Prompt

Use $answer-led-list-hypothesis-panel to create answer-led list hypothesis panel for a marketing task in Lead Intelligence / Conversion. Apply the Lead list building, Answer source remediation, Synthetic audience simulation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
