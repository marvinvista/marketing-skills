# content repurposing map

- Category: Content / Creator / Social
- Product mechanic: map one source asset into ads, social posts, emails, landing copy, and sales enablement
- Output: content repurposing map
- Evidence surfaces: social-content-automation, seo-content-briefing, ad-creative-generation

## When To Use

Repurpose long-form or campaign assets across channels.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `social-content-automation` | channel rules, cadence, hooks, captions, media, voice, approvals, and response loops | Which content repeats as a system versus a one-off post; Which approvals or response rules block scheduling |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |

## Required Inputs

- Audience, channel, creator type, content format, and cadence
- Message pillars, proof, brand voice, and claim boundaries
- Source asset or campaign moment to repurpose
- Distribution path, usage rights, and review cadence
- Social content automation: Channels, cadence, voice rules, message pillars, and campaign moment
- Social content automation: Asset inventory, approval owner, comment handling rule, and distribution path
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- Specific constraints, examples, and existing assets for content repurposing map

## Decision Rules

- Make the content mechanic explicit before writing posts or scripts.
- Preserve the claim and proof when adapting across channels or languages.
- Separate creator sourcing, asset intake, approval, and reuse rights.
- Social content automation: Which content repeats as a system versus a one-off post
- Social content automation: Which approvals or response rules block scheduling
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `map one source asset into ads, social posts, emails, landing copy, and sales enablement` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Social content automation, SEO content briefing, Ad creative generation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return content repurposing map with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for content repurposing map
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: content repurposing map.
- Organizing mechanic: map one source asset into ads, social posts, emails, landing copy, and sales enablement.
- Core fields or sections: original asset, extractable claim, channel adaptation, format, CTA, proof preserved, owner, reuse rights.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Social content automation: channel, post type, hook, proof, caption, CTA, asset state, owner
- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action
- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state

## Decision Gates

- Social content automation: do not mark the artifact ready until hooks, examples, ctas, and review notes are channel-specific.
- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.
- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.

## QA Checks

- The asset can be produced without hidden context.
- Hooks, examples, captions, CTAs, and review notes are channel-specific.
- Reuse rights, attribution needs, and approval checkpoints are visible.
- Social content automation: Hooks, examples, CTAs, and review notes are channel-specific.
- Social content automation: The content can be produced without hidden context.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.

## Failure Modes

- Writing a calendar before defining the repeatable content loop.
- Treating creator fit as follower count alone.
- Repurposing content without adapting the proof or CTA to the channel.
- Social content automation: Creating a calendar before defining the repeatable content loop.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.
- Ad creative generation: Generating asset volume without a hypothesis and review state.

## Proof Metrics

- Qualified engagement
- Reusable asset volume
- Creator acceptance and renewal signal
- Downstream lead or sales-assist signal
- Social content automation: publishing reliability
- Social content automation: qualified engagement and reusable asset volume
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time

## Example Prompt

Use $content-repurposing-map to create content repurposing map for a marketing task in Content / Creator / Social. Apply the Social content automation, SEO content briefing, Ad creative generation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
