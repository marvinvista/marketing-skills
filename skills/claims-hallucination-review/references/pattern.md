# claims hallucination review

- Category: Marketing Agents / Governance
- Product mechanic: review AI-generated marketing for unsupported claims, factual drift, missing caveats, and legal risk
- Output: claims review checklist
- Evidence surfaces: brand-governance-review, answer-source-remediation, ai-marketing-agent-workflow

## When To Use

Review AI marketing for unsupported claims and hallucinations.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |

## Required Inputs

- Bounded marketing job, allowed tools, and final artifact
- Human judgment points, review owners, and escalation rules
- Brand memory, prompt library, evidence base, and eval criteria
- Telemetry needs, rollout stage, and risk tolerance
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Specific constraints, examples, and existing assets for claims hallucination review

## Decision Rules

- Scope the agent by job, artifact, allowed actions, and failure mode.
- Put review gates where factuality, claim risk, brand fit, or spend can fail.
- Use evals before expanding autonomy or tool access.
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `review AI-generated marketing for unsupported claims, factual drift, missing caveats, and legal risk` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Brand governance review, Answer source remediation, AI marketing agent workflow; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return claims review checklist with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for claims hallucination review
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: claims review checklist.
- Organizing mechanic: review AI-generated marketing for unsupported claims, factual drift, missing caveats, and legal risk.
- Core fields or sections: generated claim, evidence status, drift risk, caveat, correction, reviewer, blocked use.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status
- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry

## Decision Gates

- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.
- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.

## QA Checks

- The workflow states what the agent can decide, draft, route, or never do.
- Each tool call has an input, output, owner, and failure fallback.
- Telemetry captures quality, acceptance, rework, and business impact.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.

## Failure Modes

- Designing an agent around a vague role instead of a bounded job.
- Skipping approval because the first demos look plausible.
- Measuring volume without quality, acceptance, or risk metrics.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.

## Proof Metrics

- Acceptance rate
- Review burden and rework rate
- Eval pass rate
- Time saved with quality preserved
- Brand governance review: review issue count
- Brand governance review: approval turnaround time
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate

## Example Prompt

Use $claims-hallucination-review to create claims review checklist for a marketing task in Marketing Agents / Governance. Apply the Brand governance review, Answer source remediation, AI marketing agent workflow mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
