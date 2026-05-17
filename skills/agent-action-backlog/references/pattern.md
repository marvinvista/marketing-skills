# agent action backlog

- Category: AI Search / Agent Discovery
- Product mechanic: convert visibility gaps into the smallest on-page, off-page, data, and workflow actions to ship
- Output: ranked agent-discovery action backlog
- Evidence surfaces: ai-search-visibility-monitoring, answer-source-remediation, marketing-ops-orchestration

## When To Use

Prioritize actions that improve agent discovery and answer inclusion.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |
| `marketing-ops-orchestration` | owners, dependencies, systems, approvals, launch states, fallback paths, and rollback | Which work can launch, wait, or roll back; Which owner or dependency blocks the next action |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Marketing ops orchestration: Workflow boundary, systems involved, owner map, launch date, and dependency list
- Marketing ops orchestration: Approval needs, fallback path, rollback trigger, and status reporting cadence
- Specific constraints, examples, and existing assets for agent action backlog

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- Marketing ops orchestration: Which work can launch, wait, or roll back
- Marketing ops orchestration: Which owner or dependency blocks the next action
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `convert visibility gaps into the smallest on-page, off-page, data, and workflow actions to ship` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI search visibility monitoring, Answer source remediation, Marketing ops orchestration; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return ranked agent-discovery action backlog with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agent action backlog
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: ranked agent-discovery action backlog.
- Organizing mechanic: convert visibility gaps into the smallest on-page, off-page, data, and workflow actions to ship.
- Core fields or sections: visibility gap, surface, smallest action, asset or system touched, owner, effort, impact, cycle.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status
- Marketing ops orchestration: workstream, owner, dependency, system, approval, fallback, rollback, status

## Decision Gates

- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.
- Marketing ops orchestration: do not mark the artifact ready until every dependency has an owner and failure fallback.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.
- Marketing ops orchestration: Every dependency has an owner and failure fallback.
- Marketing ops orchestration: Launch and rollback criteria are visible before execution.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.
- Marketing ops orchestration: Shipping a workflow with unclear ownership or rollback responsibility.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy
- Marketing ops orchestration: cycle time
- Marketing ops orchestration: handoff completion and rollback readiness

## Example Prompt

Use $agent-action-backlog to create ranked agent-discovery action backlog for a marketing task in AI Search / Agent Discovery. Apply the AI search visibility monitoring, Answer source remediation, Marketing ops orchestration mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
