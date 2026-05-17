# social content calendar system

- Category: Content / Creator / Social
- Product mechanic: turn narrative pillars, campaign moments, and channel rules into a reusable content calendar
- Output: social calendar and posting system
- Evidence surfaces: social-content-automation

## When To Use

Plan social content around repeatable campaign mechanics.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Specific constraints, examples, and existing assets for social content calendar system

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn narrative pillars, campaign moments, and channel rules into a reusable content calendar` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return social calendar and posting system with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for social content calendar system
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: social calendar and posting system.
- Organizing mechanic: turn narrative pillars, campaign moments, and channel rules into a reusable content calendar.
- Core fields or sections: pillar, channel, format, hook, proof, asset, publish date, owner, response rule.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Social content automation: Creating a calendar before defining the repeatable content loop.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume

## Example Prompt

Use $social-content-calendar-system to create social calendar and posting system for a marketing task in Content / Creator / Social. Apply the Social content automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
