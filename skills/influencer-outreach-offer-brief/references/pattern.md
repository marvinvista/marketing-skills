# influencer outreach offer brief

- Category: Content / Creator / Social
- Product mechanic: draft creator outreach, offer, deliverables, approvals, usage rights, and renewal terms
- Output: creator outreach brief
- Evidence surfaces: ugc-creator-workflow, social-content-automation, outbound-cadence-automation

## When To Use

Brief creator outreach and partnership offers with usage terms.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ugc-creator-workflow` | creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse | Which creators or assets are approved, revised, renewed, or reused; Which rights or approvals block paid amplification |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `outbound-cadence-automation` | trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff | Which step runs, stops, or escalates based on signal; Which personalization is strong enough to use |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- UGC creator workflow: Creator criteria, offer, deliverables, asset examples, and usage rights
- UGC creator workflow: Approval path, revision rule, tagging taxonomy, and paid reuse constraints
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Outbound cadence automation: Target segment, trigger, proof point, channel mix, and reply route
- Outbound cadence automation: Suppression rules, step timing, stop conditions, owner, and fallback copy
- Specific constraints, examples, and existing assets for influencer outreach offer brief

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- UGC creator workflow: Which creators or assets are approved, revised, renewed, or reused
- UGC creator workflow: Which rights or approvals block paid amplification
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Outbound cadence automation: Which step runs, stops, or escalates based on signal
- Outbound cadence automation: Which personalization is strong enough to use
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `draft creator outreach, offer, deliverables, approvals, usage rights, and renewal terms` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for UGC creator workflow, Social content automation, Outbound cadence automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creator outreach brief with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for influencer outreach offer brief
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creator outreach brief.
- Organizing mechanic: draft creator outreach, offer, deliverables, approvals, usage rights, and renewal terms.
- Core fields or sections: creator segment, offer, deliverables, usage rights, approval path, outreach hook, renewal option.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- UGC creator workflow: creator, deliverable, hook, proof, rights, revision, approval, reuse state
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Outbound cadence automation: step, channel, trigger, message angle, wait, stop rule, route

## Decision Gates

- UGC creator workflow: do not mark the artifact ready until rights, usage windows, and edit permissions are explicit.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Outbound cadence automation: do not mark the artifact ready until every step has a trigger, wait rule, stop rule, and reply route.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- UGC creator workflow: Rights, usage windows, and edit permissions are explicit.
- UGC creator workflow: Creator fit is scored beyond follower count.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Outbound cadence automation: Every step has a trigger, wait rule, stop rule, and reply route.
- Outbound cadence automation: Suppression and unsubscribe paths are handled before sending.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- UGC creator workflow: Collecting creator assets without rights, tagging, and reuse rules.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Outbound cadence automation: Automating follow-up before reply handling and stop rules are defined.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- UGC creator workflow: approved asset rate
- UGC creator workflow: creator renewal or reuse rate
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Outbound cadence automation: positive reply rate
- Outbound cadence automation: booking rate and unsubscribe rate

## Example Prompt

Use $influencer-outreach-offer-brief to create creator outreach brief for a marketing task in Content / Creator / Social. Apply the UGC creator workflow, Social content automation, Outbound cadence automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
