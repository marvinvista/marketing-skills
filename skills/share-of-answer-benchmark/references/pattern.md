# share of answer benchmark

- Category: AI Search / Agent Discovery
- Product mechanic: compare answer share, entity mentions, claim framing, and competitor displacement opportunities
- Output: share-of-answer report
- Evidence surfaces: ai-search-visibility-monitoring, customer-research-synthesis

## When To Use

Benchmark answer share against competitors and alternatives.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `customer-research-synthesis` | interviews, reviews, calls, surveys, comments, objections, and segment language | Which message, segment, or channel assumption changes; Which evidence gap must be resolved before launch |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Customer research synthesis: Research question, target segment, decision to support, and confidence threshold
- Customer research synthesis: Raw notes, transcripts, reviews, survey rows, or social snippets with evidence labels
- Specific constraints, examples, and existing assets for share of answer benchmark

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Customer research synthesis: Which message, segment, or channel assumption changes
- Customer research synthesis: Which evidence gap must be resolved before launch
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `compare answer share, entity mentions, claim framing, and competitor displacement opportunities` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI search visibility monitoring, Customer research synthesis; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return share-of-answer report with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for share of answer benchmark
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: share-of-answer report.
- Organizing mechanic: compare answer share, entity mentions, claim framing, and competitor displacement opportunities.
- Core fields or sections: prompt cluster, entity mention, competitor alternative, answer framing, rank, proof gap, opportunity, benchmark date.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Customer research synthesis: theme, evidence, segment, confidence, objection, implication, next evidence

## Decision Gates

- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Customer research synthesis: do not mark the artifact ready until observed evidence, synthesis, and recommendation are labeled separately.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Customer research synthesis: Observed evidence, synthesis, and recommendation are labeled separately.
- Customer research synthesis: Findings state confidence limits and the next evidence to collect.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Customer research synthesis: Turning research into themes without a decision or confidence boundary.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Customer research synthesis: assumptions validated or rejected
- Customer research synthesis: decision confidence

## Example Prompt

Use $share-of-answer-benchmark to create share-of-answer report for a marketing task in AI Search / Agent Discovery. Apply the AI search visibility monitoring, Customer research synthesis mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
