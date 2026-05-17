# community response playbook

- Category: Content / Creator / Social
- Product mechanic: draft response patterns for comments, questions, objections, praise, and moderation risk
- Output: community response playbook
- Evidence surfaces: social-content-automation, brand-governance-review

## When To Use

Create social or community response guidance for repeat questions.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `brand-governance-review` | claims, proof, voice, compliance risk, platform limits, and approval state | What can publish, what needs edits, and what needs explicit approval; Which recurring issue should be added to voice or claim memory |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Brand governance review: Brand voice, approved claims, banned patterns, legal or policy constraints
- Brand governance review: Draft asset, channel, proof links or notes, reviewer, and required approval level
- Specific constraints, examples, and existing assets for community response playbook

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Brand governance review: What can publish, what needs edits, and what needs explicit approval
- Brand governance review: Which recurring issue should be added to voice or claim memory
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `draft response patterns for comments, questions, objections, praise, and moderation risk` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation, Brand governance review; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return community response playbook with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for community response playbook
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: community response playbook.
- Organizing mechanic: draft response patterns for comments, questions, objections, praise, and moderation risk.
- Core fields or sections: question type, response pattern, proof, escalation trigger, moderation risk, owner, update rule.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Brand governance review: claim, proof, risk level, voice issue, required edit, owner, approval state

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Brand governance review: do not mark the artifact ready until unsupported claims are blocked or rewritten before launch.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Brand governance review: Unsupported claims are blocked or rewritten before launch.
- Brand governance review: Edits preserve intent while removing risk.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Brand governance review: Treating brand review as tone cleanup while ignoring proof and risk.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Brand governance review: review issue count
- Brand governance review: approval turnaround time

## Example Prompt

Use $community-response-playbook to create community response playbook for a marketing task in Content / Creator / Social. Apply the Social content automation, Brand governance review mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
