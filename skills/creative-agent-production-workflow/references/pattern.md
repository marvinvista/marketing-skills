# creative agent production workflow

- Category: Creative / Ads / Assets
- Product mechanic: scope an AI workflow for generating creative variants, applying review gates, and handing off approved assets
- Output: creative agent production workflow
- Evidence surfaces: ad-creative-generation, ai-marketing-agent-workflow

## When To Use

Specify agent-assisted creative production with review and handoff gates.

## Product Mechanics

| Surface | Inspect | Decision It Changes |
| --- | --- | --- |
| `ad-creative-generation` | hooks, angles, proof, formats, offers, CTAs, and channel limits | Which variable changes in the next creative test; Which claim or proof needs review before production |
| `ai-marketing-agent-workflow` | bounded job, inputs, tools, allowed actions, review gates, fallbacks, and telemetry | What the agent may draft, route, decide, or escalate; Which gate must pass before expanding autonomy |

## Required Inputs

- Audience, offer, channel, format, and conversion event
- Allowed claims, proof points, brand rules, and risk constraints
- Existing winners, losers, competitor examples, and performance readouts
- Production limits for copy, image, video, voice, landing page, or catalog assets
- Ad creative generation: Audience belief, offer, channel, format, and conversion event
- Ad creative generation: Approved proof points, claim limits, brand rules, and prior creative results
- AI marketing agent workflow: Job boundary, final artifact, allowed tools, and unavailable actions
- AI marketing agent workflow: Review owner, escalation rule, eval criteria, telemetry need, and rollout stage
- Specific constraints, examples, and existing assets for creative agent production workflow

## Decision Rules

- Change one primary variable at a time unless the task is exploratory ideation.
- Tie every creative angle to a buyer belief, proof point, and next action.
- Separate creative quality from media budget, targeting, and tracking effects.
- Ad creative generation: Which variable changes in the next creative test
- Ad creative generation: Which claim or proof needs review before production
- AI marketing agent workflow: What the agent may draft, route, decide, or escalate
- AI marketing agent workflow: Which gate must pass before expanding autonomy
- If the user asks for strategy only, still return the smallest artifact this mechanic can produce.
- If launch risk is present, mark the item as review-required rather than pretending it is ready.

## Procedure

- Confirm the user needs the `scope an AI workflow for generating creative variants, applying review gates, and handing off approved assets` mechanic and identify the audience, artifact, and review owner.
- Collect only the inputs needed for Ad creative generation, AI marketing agent workflow; infer low-risk defaults and mark missing high-risk fields.
- Map each surface to the artifact fields before drafting recommendations.
- Apply the decision rules in `references/pattern.md` before drafting the artifact.
- Return creative agent production workflow with QA checks, failure modes, metric, and next action.

## Artifact Template

- Context and decision the artifact supports
- Input table with owner, freshness, and gaps
- Mechanic-specific work product for creative agent production workflow
- Decision rules applied and tradeoffs
- QA checklist, failure modes, metric, and next action

## Skill-Specific Work Product

- Final artifact: creative agent production workflow.
- Organizing mechanic: scope an AI workflow for generating creative variants, applying review gates, and handing off approved assets.
- Core fields or sections: agent job, input brief, variant rule, generation step, review gate, tool boundary, output handoff.
- Keep the artifact narrow enough that the owner can execute or review the next action today.

## Artifact Fields

- Ad creative generation: angle, hook, proof point, format, CTA, hypothesis, review state
- AI marketing agent workflow: job, input, tool, action right, review gate, fallback, telemetry

## Decision Gates

- Ad creative generation: do not mark the artifact ready until each creative variant changes one declared variable or is marked exploratory.
- AI marketing agent workflow: do not mark the artifact ready until every tool action has an input, output, owner, and fallback.

## QA Checks

- Every variant has a hypothesis, audience, claim, proof, CTA, and review owner.
- Unsupported claims are flagged before assets are promoted to production.
- The output is ready for a designer, editor, media buyer, or reviewer to use.
- Ad creative generation: Each creative variant changes one declared variable or is marked exploratory.
- Ad creative generation: Each claim connects to an approved proof point.
- AI marketing agent workflow: Every tool action has an input, output, owner, and fallback.
- AI marketing agent workflow: Risky actions are blocked by review or eval gates.

## Failure Modes

- Generating many variants without a testable hypothesis matrix.
- Letting style changes masquerade as positioning tests.
- Ignoring platform, legal, or brand constraints until final review.
- Ad creative generation: Generating asset volume without a hypothesis and review state.
- AI marketing agent workflow: Defining an agent role without a bounded job and final artifact.

## Proof Metrics

- Creative holdout or lift signal
- Hook, thumb-stop, click, and conversion movement
- Approval cycle time
- Reusable winning assets created
- Ad creative generation: hook rate, click rate, conversion rate, and winning-asset reuse
- Ad creative generation: approval cycle time
- AI marketing agent workflow: eval pass rate
- AI marketing agent workflow: acceptance rate and rework rate

## Example Prompt

Use $creative-agent-production-workflow to create creative agent production workflow for a marketing task in Creative / Ads / Assets. Apply the Ad creative generation, AI marketing agent workflow mechanics and return the QA checks, failure modes, proof metric, and next action.

## Optional Helper

No helper script is bundled for this skill.

## Evidence Boundary

The evidence behind this skill is maintained outside this repository. Keep this file focused on reusable behavior, not private identities.
