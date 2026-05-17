# AI referral ROI readout

- Category: AI Search / Agent Discovery
- Product mechanic: read AI referrals, bot traffic, assisted conversion, and revenue signal without over-claiming attribution
- Output: AI referral readout and dashboard spec
- Evidence surfaces: ai-search-visibility-monitoring, campaign-analytics-qa

## When To Use

Measure AI-search and answer-surface traffic value with attribution caveats.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `campaign-analytics-qa` | UTMs, events, conversion paths, dashboards, attribution fields, expected values, and readout decisions | Which metrics are trustworthy enough for a decision; Which tracking gaps block launch or interpretation |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Campaign analytics QA: Campaign plan, channels, events, conversion definition, dashboard, and owner
- Campaign analytics QA: Expected values, test records, attribution rules, data freshness, and decision cadence
- Specific constraints, examples, and existing assets for AI referral ROI readout

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Campaign analytics QA: Which metrics are trustworthy enough for a decision
- Campaign analytics QA: Which tracking gaps block launch or interpretation
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `read AI referrals, bot traffic, assisted conversion, and revenue signal without over-claiming attribution` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI search visibility monitoring, Campaign analytics QA; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return AI referral readout and dashboard spec with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for AI referral ROI readout
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: AI referral readout and dashboard spec.
- Organizing mechanic: read AI referrals, bot traffic, assisted conversion, and revenue signal without over-claiming attribution.
- Core fields or sections: referral surface, traffic type, session path, assisted event, revenue caveat, bot signal, dashboard field.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Campaign analytics QA: event, parameter, expected value, observed value, owner, status, decision impact

## Decision Gates

- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Campaign analytics QA: do not mark the artifact ready until tracking is tested before performance interpretation.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Campaign analytics QA: Tracking is tested before performance interpretation.
- Campaign analytics QA: Each metric states the decision it can change.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Campaign analytics QA: Reading campaign performance before verifying event and attribution integrity.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Campaign analytics QA: QA pass rate
- Campaign analytics QA: attribution coverage and data freshness

## Example Prompt

Use $ai-referral-roi-readout to create AI referral readout and dashboard spec for a marketing task in AI Search / Agent Discovery. Apply the AI search visibility monitoring, Campaign analytics QA mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
