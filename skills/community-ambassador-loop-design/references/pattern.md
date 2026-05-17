# community ambassador loop design

- Category: Content / Creator / Social
- Product mechanic: design member, customer, or local advocate loops that produce referrals, proof, and content
- Output: ambassador loop plan
- Evidence surfaces: ugc-creator-workflow, social-content-automation, local-storefront-growth

## When To Use

Build an ambassador or advocacy loop with proof generation.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ugc-creator-workflow` | creator fit, deliverables, asset intake, rights, approvals, revisions, tagging, and reuse | Which creators or assets are approved, revised, renewed, or reused; Which rights or approvals block paid amplification |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `local-storefront-growth` | locations, radius, local offer, route plan, reviews, community proof, and owner follow-up | Which local targets get field action versus digital follow-up; Which local proof or listing gap blocks trust |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- UGC creator workflow: Creator criteria, offer, deliverables, asset examples, and usage rights
- UGC creator workflow: Approval path, revision rule, tagging taxonomy, and paid reuse constraints
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- Local storefront growth: Target location set, radius, category, offer, local proof, and field owner
- Local storefront growth: Route constraints, review signals, storefront data, and follow-up channel
- Specific constraints, examples, and existing assets for community ambassador loop design

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- UGC creator workflow: Which creators or assets are approved, revised, renewed, or reused
- UGC creator workflow: Which rights or approvals block paid amplification
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- Local storefront growth: Which local targets get field action versus digital follow-up
- Local storefront growth: Which local proof or listing gap blocks trust
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `design member, customer, or local advocate loops that produce referrals, proof, and content` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for UGC creator workflow, Social content automation, Local storefront growth; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return ambassador loop plan with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for community ambassador loop design
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: ambassador loop plan.
- Organizing mechanic: design member, customer, or local advocate loops that produce referrals, proof, and content.
- Core fields or sections: member segment, referral trigger, proof asset, reward, content loop, owner, tracking, renewal.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- UGC creator workflow: creator, deliverable, hook, proof, rights, revision, approval, reuse state
- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- Local storefront growth: location, radius, offer, local proof, route, owner, follow-up

## Decision Gates

- UGC creator workflow: do not mark the artifact ready until rights, usage windows, and edit permissions are explicit.
- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- Local storefront growth: do not mark the artifact ready until routes are prioritized by fit, proximity, and actionability.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- UGC creator workflow: Rights, usage windows, and edit permissions are explicit.
- UGC creator workflow: Creator fit is scored beyond follower count.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- Local storefront growth: Routes are prioritized by fit, proximity, and actionability.
- Local storefront growth: Local proof is tied to the offer and outreach path.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- UGC creator workflow: Collecting creator assets without rights, tagging, and reuse rules.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- Local storefront growth: Treating local prospecting as a generic list without route and proof context.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- UGC creator workflow: approved asset rate
- UGC creator workflow: creator renewal or reuse rate
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- Local storefront growth: route completion
- Local storefront growth: local response or conversion rate

## Example Prompt

Use $community-ambassador-loop-design to create ambassador loop plan for a marketing task in Content / Creator / Social. Apply the UGC creator workflow, Social content automation, Local storefront growth mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
