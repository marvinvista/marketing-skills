# agent discovery question map

- Category: AI Search / Agent Discovery
- Product mechanic: map buyer questions to the answer engines, agents, and proof assets that can influence discovery
- Output: question map, prompt set, and proof inventory
- Evidence surfaces: ai-search-visibility-monitoring, answer-source-remediation

## When To Use

Turn buyer questions into a prioritized answer-engine inspection map.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Specific constraints, examples, and existing assets for agent discovery question map

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `map buyer questions to the answer engines, agents, and proof assets that can influence discovery` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI search visibility monitoring, Answer source remediation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return question map, prompt set, and proof inventory with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agent discovery question map
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: question map, prompt set, and proof inventory.
- Organizing mechanic: map buyer questions to the answer engines, agents, and proof assets that can influence discovery.
- Core fields or sections: buyer question, persona, intent stage, answer surface, prompt wording, current answer, cited proof, action priority.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status

## Decision Gates

- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy

## Example Prompt

Use $agent-discovery-question-map to create question map, prompt set, and proof inventory for a marketing task in AI Search / Agent Discovery. Apply the AI search visibility monitoring, Answer source remediation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
