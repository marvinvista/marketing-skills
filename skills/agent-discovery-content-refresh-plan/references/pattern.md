# agent discovery content refresh plan

- Category: AI Search / Agent Discovery
- Product mechanic: refresh stale pages, FAQs, comparison copy, and proof assets based on answer-surface gaps
- Output: refresh plan and CMS handoff
- Evidence surfaces: seo-content-briefing, ai-search-visibility-monitoring

## When To Use

Plan content refreshes that improve AI discovery.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |
| `ai-search-visibility-monitoring` | priority prompts, answer text, rank, entity mention, citations, and next-action paths | Which prompts need monitoring, remediation, or new proof; Which answer gaps matter enough to ship work this cycle |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- AI search visibility monitoring: Prompt set with persona, intent, market, and answer surface
- AI search visibility monitoring: Observed answers, ranks, citations, alternatives, and target next action
- Specific constraints, examples, and existing assets for agent discovery content refresh plan

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- AI search visibility monitoring: Which prompts need monitoring, remediation, or new proof
- AI search visibility monitoring: Which answer gaps matter enough to ship work this cycle
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `refresh stale pages, FAQs, comparison copy, and proof assets based on answer-surface gaps` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for SEO content briefing, AI search visibility monitoring; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return refresh plan and CMS handoff with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for agent discovery content refresh plan
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: refresh plan and CMS handoff.
- Organizing mechanic: refresh stale pages, FAQs, comparison copy, and proof assets based on answer-surface gaps.
- Core fields or sections: stale page, target question, missing proof, refresh angle, schema or index need, CMS owner, expected answer change.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action
- AI search visibility monitoring: prompt, surface, rank or inclusion, answer summary, citation status, gap, action

## Decision Gates

- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.
- AI search visibility monitoring: do not mark the artifact ready until observed answer text is separated from interpretation.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.
- AI search visibility monitoring: Observed answer text is separated from interpretation.
- AI search visibility monitoring: Every visibility gap has a matching proof or content action.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.
- AI search visibility monitoring: Counting mentions without checking answer accuracy and next-action usefulness.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality
- AI search visibility monitoring: share of answer
- AI search visibility monitoring: citation inclusion and quality

## Example Prompt

Use $agent-discovery-content-refresh-plan to create refresh plan and CMS handoff for a marketing task in AI Search / Agent Discovery. Apply the SEO content briefing, AI search visibility monitoring mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
