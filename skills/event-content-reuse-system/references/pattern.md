# event content reuse system

- Category: Content / Creator / Social
- Product mechanic: turn event, webinar, or field moments into social, email, ads, and sales follow-up assets
- Output: event content reuse system
- Evidence surfaces: social-content-automation, lead-list-building, outbound-cadence-automation

## When To Use

Repurpose event content into campaign assets and follow-up.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `lead-list-building` | segment rules, account criteria, exclusions, dedupe logic, and owner routing | Which records qualify for action now; Which gaps block enrichment, routing, or outreach |
| `outbound-cadence-automation` | trigger, channel sequence, wait states, personalization, stop rules, replies, and owner handoff | Which step runs, stops, or escalates based on signal; Which personalization is strong enough to use |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Lead list building: ICP or segment definition, triggers, disqualifiers, and territory or market limits
- Lead list building: Required list fields, evidence standard, dedupe rule, and owner route
- Outbound cadence automation: Target segment, trigger, proof point, channel mix, and reply route
- Outbound cadence automation: Suppression rules, step timing, stop conditions, owner, and fallback copy
- Specific constraints, examples, and existing assets for event content reuse system

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Lead list building: Which records qualify for action now
- Lead list building: Which gaps block enrichment, routing, or outreach
- Outbound cadence automation: Which step runs, stops, or escalates based on signal
- Outbound cadence automation: Which personalization is strong enough to use
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `turn event, webinar, or field moments into social, email, ads, and sales follow-up assets` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation, Lead list building, Outbound cadence automation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return event content reuse system with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for event content reuse system
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: event content reuse system.
- Organizing mechanic: turn event, webinar, or field moments into social, email, ads, and sales follow-up assets.
- Core fields or sections: event moment, captured asset, lead signal, follow-up segment, social cut, email angle, owner.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Lead list building: account or lead, segment, fit reason, trigger, evidence, disqualifier, route
- Outbound cadence automation: step, channel, trigger, message angle, wait, stop rule, route

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Lead list building: do not mark the artifact ready until every accepted record has fit, trigger, evidence, and a route.
- Outbound cadence automation: do not mark the artifact ready until every step has a trigger, wait rule, stop rule, and reply route.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Lead list building: Every accepted record has fit, trigger, evidence, and a route.
- Lead list building: Disqualified records state the rule that removed them.
- Outbound cadence automation: Every step has a trigger, wait rule, stop rule, and reply route.
- Outbound cadence automation: Suppression and unsubscribe paths are handled before sending.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Lead list building: Building a large list before defining exclusions and evidence standards.
- Outbound cadence automation: Automating follow-up before reply handling and stop rules are defined.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Lead list building: qualified record count
- Lead list building: owner acceptance rate
- Outbound cadence automation: positive reply rate
- Outbound cadence automation: booking rate and unsubscribe rate

## Example Prompt

Use $event-content-reuse-system to create event content reuse system for a marketing task in Content / Creator / Social. Apply the Social content automation, Lead list building, Outbound cadence automation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
