# page schema indexability audit

- Category: AI Search / Agent Discovery
- Product mechanic: check whether pages, structured data, feeds, and crawl paths expose the proof agents need
- Output: indexability audit and implementation tickets
- Evidence surfaces: seo-content-briefing, answer-source-remediation

## When To Use

Audit indexability and structured proof for AI discovery.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `seo-content-briefing` | questions, search intent, answer gaps, proof, page type, schema, and crawl paths | Which page, section, or proof asset should be created or refreshed; Which structured data or crawl fix must ship with content |
| `answer-source-remediation` | cited assets, missing proof, stale claims, crawl exposure, correction paths, and owner actions | Which proof, page, listing, or data fix ships first; Which answer risk needs correction before optimization work |

## Required Inputs

- Brand, product, category, and buyer question set
- Answer engines or agent surfaces to inspect
- Known competitors, preferred proof, and exclusion rules
- Current crawlable pages, docs, feeds, listings, and media assets
- SEO content briefing: Target queries or questions, page inventory, audience intent, and desired answer
- SEO content briefing: Proof assets, comparison gaps, schema needs, internal links, and crawl constraints
- Answer source remediation: Observed answer gaps, cited assets, missing proof, stale pages, and desired correction
- Answer source remediation: Publishing owner, content or data action, review need, and expected answer change
- Specific constraints, examples, and existing assets for page schema indexability audit

## Decision Rules

- Separate visibility, answer accuracy, citation quality, and downstream intent.
- Treat a missing citation as an evidence problem before calling it a ranking problem.
- Prioritize changes that improve the answer, the cited proof, and the next user action together.
- SEO content briefing: Which page, section, or proof asset should be created or refreshed
- SEO content briefing: Which structured data or crawl fix must ship with content
- Answer source remediation: Which proof, page, listing, or data fix ships first
- Answer source remediation: Which answer risk needs correction before optimization work
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `check whether pages, structured data, feeds, and crawl paths expose the proof agents need` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for SEO content briefing, Answer source remediation; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return indexability audit and implementation tickets with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for page schema indexability audit
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: indexability audit and implementation tickets.
- Organizing mechanic: check whether pages, structured data, feeds, and crawl paths expose the proof agents need.
- Core fields or sections: page, crawl path, structured data, proof exposure, indexability issue, fix owner, test method, priority.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- SEO content briefing: query or question, intent, page type, answer block, proof, schema, link action
- Answer source remediation: answer gap, claim, current proof, missing proof, fix, owner, status

## Decision Gates

- SEO content briefing: do not mark the artifact ready until each brief includes the answer, proof, schema need, and indexability check.
- Answer source remediation: do not mark the artifact ready until every remediation item ties to a specific answer gap.

## QA Checks

- Every recommendation names the answer surface, query class, expected user, and proof asset.
- The artifact distinguishes observed answer text from inferred optimization work.
- No private evidence identities or unpublished links appear in output.
- SEO content briefing: Each brief includes the answer, proof, schema need, and indexability check.
- SEO content briefing: The content gap is tied to a specific question or intent.
- Answer source remediation: Every remediation item ties to a specific answer gap.
- Answer source remediation: The fix improves evidence quality, not just keyword coverage.

## Failure Modes

- Optimizing pages without first defining the answer questions.
- Counting mentions while ignoring whether the answer is accurate or useful.
- Publishing generic content that does not add citable proof.
- SEO content briefing: Writing generic content that does not create citable proof or answer structure.
- Answer source remediation: Calling a ranking problem before checking whether answer evidence is missing or stale.

## Proof Metrics

- Share of answer for priority questions
- Citation inclusion and citation quality
- Referral or assisted-conversion signal
- Remediation shipped per cycle
- SEO content briefing: indexed proof coverage
- SEO content briefing: answer inclusion and citation quality
- Answer source remediation: remediation shipped
- Answer source remediation: citation coverage and accuracy

## Example Prompt

Use $page-schema-indexability-audit to create indexability audit and implementation tickets for a marketing task in AI Search / Agent Discovery. Apply the SEO content briefing, Answer source remediation mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
