# agentic answer ops workflow

- Category: AI Search / Agent Discovery
- Product mechanic: orchestrate AI answer monitoring, evidence lookup, remediation actions, review gates, and telemetry
- Output: agentic answer ops workflow
- Evidence surfaces: ai-marketing-agent-workflow, ai-search-visibility-monitoring, answer-source-remediation

## When To Use

Design agent-assisted operations for AI answer visibility and remediation.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Specific constraints, examples, and existing assets for agentic answer ops workflow

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `orchestrate AI answer monitoring, evidence lookup, remediation actions, review gates, and telemetry` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for AI marketing agent workflow, AI search visibility monitoring, Answer source remediation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return agentic answer ops workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agentic answer ops workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: agentic answer ops workflow.
- Organizing mechanic: orchestrate AI answer monitoring, evidence lookup, remediation actions, review gates, and telemetry.
- Core fields or sections: monitored prompt, agent job, allowed action, evidence lookup, remediation task, review gate, telemetry, fallback.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry
- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status

## Decision Gates

- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.
- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy

## Example Prompt

Use $agentic-answer-ops-workflow to create agentic answer ops workflow for a marketing task in AI Search / Agent Discovery. Apply the AI marketing agent workflow, AI search visibility monitoring, Answer source remediation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
