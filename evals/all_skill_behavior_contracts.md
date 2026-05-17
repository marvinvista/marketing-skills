# All Skill Behavior Contracts

Run date: 2026-05-17

## Summary

- Skills with prompt-to-artifact contracts: 116
- Deep edge-case fixtures: 10
- Contract checks: skill invocation, expected artifact fields, QA checks, failure modes, proof metrics, and next action.

## Deep Fixture Skills

- `marketing-output-eval-harness`: meta-evaluation quality
- `marketing-agent-workflow-spec`: agent scope and autonomy
- `claims-hallucination-review`: unsupported marketing claims
- `brand-voice-memory`: style drift and reusable memory quality
- `ai-answer-visibility-scorecard`: answer-surface scoring consistency
- `share-of-answer-benchmark`: competitor comparison and aggregation
- `brand-compliance-creative-review`: pre-launch creative approval
- `website-visitor-to-account-workflow`: visitor routing and handoff quality
- `audience-sync-contract`: field mapping and activation readiness
- `consent-suppression-rollback-plan`: unsafe launch prevention

## Per-Skill Contracts

| Skill | Category | Output | Expected Fields |
| --- | --- | --- | --- |
| `agent-action-backlog` | AI Search / Agent Discovery | ranked agent-discovery action backlog | visibility gap, surface, smallest action, asset or system touched |
| `agent-discovery-content-refresh-plan` | AI Search / Agent Discovery | refresh plan and CMS handoff | stale page, target question, missing proof, refresh angle |
| `agent-discovery-question-map` | AI Search / Agent Discovery | question map, prompt set, and proof inventory | buyer question, persona, intent stage, answer surface |
| `agentic-answer-ops-workflow` | AI Search / Agent Discovery | agentic answer ops workflow | monitored prompt, agent job, allowed action, evidence lookup |
| `ai-answer-brand-risk-map` | AI Search / Agent Discovery | AI answer brand risk map | priority prompt, observed answer, brand risk, claim status |
| `ai-answer-visibility-scorecard` | AI Search / Agent Discovery | visibility scorecard with remediation backlog | prompt, surface, mention status, rank |
| `ai-referral-roi-readout` | AI Search / Agent Discovery | AI referral readout and dashboard spec | referral surface, traffic type, session path, assisted event |
| `ai-shopping-feed-optimizer` | AI Search / Agent Discovery | shopping feed optimization plan | product, feed field, PDP proof, image signal |
| `answer-claim-risk-review` | AI Search / Agent Discovery | answer risk review and correction plan | answer text, unsupported claim, stale phrase, missing caveat |
| `answer-ready-content-brief` | AI Search / Agent Discovery | answer-ready content brief | target question, intent, answer block, proof |
| `citable-proof-asset-kit` | AI Search / Agent Discovery | proof kit and publishing checklist | claim, proof asset, format, audience question |
| `citation-source-gap-map` | AI Search / Agent Discovery | citation gap map and proof backlog | answer claim, cited asset, missing proof, stale proof |
| `generative-search-weekly-ops-report` | AI Search / Agent Discovery | weekly ops report with actions | prompt movement, citation gap, shipped fix, traffic signal |
| `page-schema-indexability-audit` | AI Search / Agent Discovery | indexability audit and implementation tickets | page, crawl path, structured data, proof exposure |
| `prompt-rank-monitor` | AI Search / Agent Discovery | prompt-rank table and monitoring cadence | prompt, surface, run date, mention status |
| `search-creative-message-bridge` | AI Search / Agent Discovery | search-to-creative message bridge | answer insight, buyer belief, creative angle, proof to reuse |
| `seo-brand-proof-governance` | AI Search / Agent Discovery | SEO proof governance brief | target query, claim, approved proof, schema need |
| `share-of-answer-benchmark` | AI Search / Agent Discovery | share-of-answer report | prompt cluster, entity mention, competitor alternative, answer framing |
| `community-ambassador-loop-design` | Content / Creator / Social | ambassador loop plan | member segment, referral trigger, proof asset, reward |
| `community-response-playbook` | Content / Creator / Social | community response playbook | question type, response pattern, proof, escalation trigger |
| `content-repurposing-map` | Content / Creator / Social | content repurposing map | original asset, extractable claim, channel adaptation, format |
| `creator-discovery-scorecard` | Content / Creator / Social | creator scorecard | creator, audience fit, trust signal, content quality |
| `creator-performance-reuse-readout` | Content / Creator / Social | creator performance readout | creator asset, spend or organic context, performance signal, learning |
| `event-content-reuse-system` | Content / Creator / Social | event content reuse system | event moment, captured asset, lead signal, follow-up segment |
| `influencer-outreach-offer-brief` | Content / Creator / Social | creator outreach brief | creator segment, offer, deliverables, usage rights |
| `seo-social-content-brief` | Content / Creator / Social | SEO/social content brief | search question, social hook, proof, content angle |
| `social-content-calendar-system` | Content / Creator / Social | social calendar and posting system | pillar, channel, format, hook |
| `social-listening-insight-brief` | Content / Creator / Social | social listening brief | channel, post or comment, pain, language |
| `ugc-intake-rights-workflow` | Content / Creator / Social | UGC intake and rights workflow | asset, creator, rights window, edit permission |
| `voiceover-localization-workflow` | Content / Creator / Social | voiceover localization workflow | source script, locale, timing, tone |
| `ad-variant-matrix-builder` | Creative / Ads / Assets | creative variant matrix | hook, angle, proof, format |
| `agentic-video-production-workflow` | Creative / Ads / Assets | agentic video production workflow | video job, script input, scene generation, voice or caption rule |
| `brand-compliance-creative-review` | Creative / Ads / Assets | creative compliance review | asset, claim, proof, voice fit |
| `catalog-ad-feed-plan` | Creative / Ads / Assets | catalog creative feed plan | product field, audience segment, creative rule, image rule |
| `chat-creative-conversion-plan` | Creative / Ads / Assets | chat creative conversion plan | ad angle, landing promise, chat question, qualification rule |
| `competitor-ad-teardown` | Creative / Ads / Assets | competitor ad teardown | competitor angle, format, claim, proof |
| `creative-agent-production-workflow` | Creative / Ads / Assets | creative agent production workflow | agent job, input brief, variant rule, generation step |
| `creative-brief-from-research` | Creative / Ads / Assets | creative brief with claims, proof, and constraints | insight, audience, claim, proof |
| `creative-enrichment-personalization-plan` | Creative / Ads / Assets | creative personalization plan | enrichment field, audience cue, personalization claim, creative variant |
| `creative-fatigue-refresh-plan` | Creative / Ads / Assets | creative refresh plan | fatigued asset, symptom, retained learning, variable to refresh |
| `creative-lead-capture-loop` | Creative / Ads / Assets | creative lead-capture loop | creative angle, audience, lead signal, capture field |
| `creative-outbound-message-bridge` | Creative / Ads / Assets | creative-to-outbound message bridge | creative angle, trigger, lead segment, email hook |
| `creative-performance-readout` | Creative / Ads / Assets | creative readout and next-test backlog | asset, audience, spend context, tracking confidence |
| `landing-page-message-match` | Creative / Ads / Assets | message-match landing page spec | ad angle, page headline, proof block, objection block |
| `multilingual-creative-localization` | Creative / Ads / Assets | localized creative plan | locale, original intent, claim, proof |
| `multimodal-asset-assembly-brief` | Creative / Ads / Assets | multimodal assembly brief | format, image, video, voice |
| `offer-angle-mining` | Creative / Ads / Assets | offer angle map | audience segment, pain, desire, objection |
| `paid-launch-checklist` | Creative / Ads / Assets | paid launch checklist | asset, audience, budget, conversion event |
| `podcast-audio-ad-read-guide` | Creative / Ads / Assets | audio ad script and read guide | host line, timing, pronunciation, claim |
| `product-image-qa-brief` | Creative / Ads / Assets | product image brief and QA checklist | product attribute, shot type, context, fidelity risk |
| `short-form-hook-bank` | Creative / Ads / Assets | hook bank and test notes | platform, hook type, opening line, proof cue |
| `synthetic-creative-test-panel` | Creative / Ads / Assets | synthetic creative test panel | audience assumption, scenario, creative angle, simulated reaction |
| `ugc-ad-script-pack` | Creative / Ads / Assets | UGC script pack | creator persona, hook, story beat, product use |
| `video-ad-storyboard` | Creative / Ads / Assets | video storyboard and shot list | scene, hook, product moment, proof line |
| `video-seo-content-reuse-plan` | Creative / Ads / Assets | video SEO reuse plan | video asset, transcript moment, target query, answer block |
| `visual-asset-prompt-brief` | Creative / Ads / Assets | visual prompt brief and production notes | asset goal, scene, product detail, style constraint |
| `account-list-sourcing-brief` | Lead Intelligence / Conversion | account list sourcing brief | segment rule, list source, inclusion criterion, exclusion |
| `account-research-snapshot` | Lead Intelligence / Conversion | account research snapshot | account context, role pain, trigger, proof match |
| `agentic-list-building-workflow` | Lead Intelligence / Conversion | agentic list building workflow | agent job, target segment, list criteria, evidence lookup |
| `answer-led-list-hypothesis-panel` | Lead Intelligence / Conversion | answer-led list hypothesis panel | answer gap, proof gap, list hypothesis, target segment |
| `audience-list-sync-readiness` | Lead Intelligence / Conversion | audience list sync readiness check | audience segment, list criterion, join key, consent status |
| `buying-signal-listener-spec` | Lead Intelligence / Conversion | signal listener spec | signal type, event, threshold, source |
| `chat-lead-routing-flow` | Lead Intelligence / Conversion | chat lead routing flow | chat answer, qualification score, list membership, fit rule |
| `crm-handoff-qa` | Lead Intelligence / Conversion | CRM handoff QA checklist | record, owner, route, next step |
| `demo-booking-friction-audit` | Lead Intelligence / Conversion | booking friction audit | entry point, friction point, required field, routing delay |
| `enrichment-field-contract` | Lead Intelligence / Conversion | enrichment field contract | field, source priority, freshness, confidence |
| `event-lead-capture-followup` | Lead Intelligence / Conversion | event follow-up plan | event note, lead segment, booth context, meeting signal |
| `icp-segment-trigger-map` | Lead Intelligence / Conversion | ICP trigger map | segment, fit rule, trigger, disqualifier |
| `inbound-chat-qualification-flow` | Lead Intelligence / Conversion | chat qualification flow | question, branch, qualification rule, score |
| `intent-led-outbound-sequence` | Lead Intelligence / Conversion | intent-led email sequence | trigger, pain, proof, opening line |
| `lead-list-prioritization-scorecard` | Lead Intelligence / Conversion | lead scoring table and routing notes | record, fit score, intent score, evidence strength |
| `linkedin-prospecting-cadence` | Lead Intelligence / Conversion | LinkedIn cadence | connection reason, first note, follow-up step, proof |
| `local-business-prospecting-route` | Lead Intelligence / Conversion | local prospecting route | location, category, fit, local proof |
| `multichannel-prospecting-orchestration` | Lead Intelligence / Conversion | multichannel prospecting map | channel, step, trigger, owner |
| `referral-partner-lead-loop` | Lead Intelligence / Conversion | referral lead loop plan | partner type, referral trigger, lead handoff, tracking field |
| `reply-intent-triage-rules` | Lead Intelligence / Conversion | reply triage rules | reply text, intent class, urgency, objection |
| `sales-marketing-feedback-loop` | Lead Intelligence / Conversion | sales feedback loop | reply or objection, segment, message gap, list update |
| `visitor-list-routing-plan` | Lead Intelligence / Conversion | visitor list routing plan | visit signal, matched account, list membership, intent threshold |
| `website-visitor-to-account-workflow` | Lead Intelligence / Conversion | visitor-to-account workflow | visit path, matched account, intent score, confidence |
| `attribution-diagnostic` | Lifecycle / Ops / Analytics | attribution diagnostic | touchpoint, source capture, identity link, conversion event |
| `audience-sync-contract` | Lifecycle / Ops / Analytics | audience sync contract | audience, field, join key, refresh cadence |
| `campaign-preflight-qa-checklist` | Lifecycle / Ops / Analytics | campaign preflight checklist | asset, audience, tracking, approval |
| `campaign-tracking-plan` | Lifecycle / Ops / Analytics | campaign tracking plan | channel, UTM, event, property |
| `consent-suppression-rollback-plan` | Lifecycle / Ops / Analytics | consent and rollback plan | consent rule, suppression list, risky action, rollback trigger |
| `email-template-system` | Lifecycle / Ops / Analytics | email template system | template, dynamic field, segment, proof block |
| `experiment-readout` | Lifecycle / Ops / Analytics | experiment readout | hypothesis, variant, result, confidence |
| `lifecycle-segmentation-map` | Lifecycle / Ops / Analytics | lifecycle segmentation map | state, transition, trigger, suppression |
| `marketing-dashboard-spec` | Lifecycle / Ops / Analytics | dashboard spec | metric, dimension, threshold, data check |
| `retention-reactivation-loop` | Lifecycle / Ops / Analytics | retention or reactivation loop | lifecycle state, trigger, message, suppression |
| `warehouse-audience-activation-plan` | Lifecycle / Ops / Analytics | warehouse activation plan | table, join key, segment rule, consent |
| `whatsapp-sms-conversation-flow` | Lifecycle / Ops / Analytics | messaging conversation flow | channel, consent state, message step, branch |
| `agentic-seo-briefing-workflow` | Marketing Agents / Governance | agentic SEO briefing workflow | agent job, target query, brief input, proof lookup |
| `ai-workflow-telemetry-plan` | Marketing Agents / Governance | AI workflow telemetry plan | workflow step, quality metric, acceptance signal, rework reason |
| `automation-risk-register` | Marketing Agents / Governance | automation risk register | risk, trigger, affected workflow, mitigation |
| `brand-voice-memory` | Marketing Agents / Governance | brand voice memory | approved phrase, banned pattern, claim, proof |
| `claims-hallucination-review` | Marketing Agents / Governance | claims review checklist | generated claim, evidence status, drift risk, caveat |
| `human-approval-ladder` | Marketing Agents / Governance | approval ladder | risk level, action right, review owner, escalation trigger |
| `internal-knowledge-activation` | Marketing Agents / Governance | knowledge activation plan | approved doc, insight, access boundary, allowed use |
| `marketing-agent-workflow-spec` | Marketing Agents / Governance | agent workflow spec | job, input, tool, allowed action |
| `marketing-output-eval-harness` | Marketing Agents / Governance | marketing eval harness | criterion, test case, expected behavior, failure mode |
| `prompt-library-maintenance` | Marketing Agents / Governance | prompt library maintenance plan | prompt pattern, example, variant, failure |
| `tool-orchestration-map` | Marketing Agents / Governance | tool orchestration map | model call, tool, input, output |
| `audience-intelligence-brief` | Research / Audience Simulation | audience intelligence brief | segment, motivation, channel, trigger |
| `customer-journey-evidence-map` | Research / Audience Simulation | journey evidence map | stage, question, objection, proof need |
| `interview-guide-builder` | Research / Audience Simulation | interview guide | buyer question, objection, alternative, decision criterion |
| `interview-synthesis-matrix` | Research / Audience Simulation | interview synthesis matrix | theme, quote, segment, objection |
| `local-market-research-brief` | Research / Audience Simulation | local market research brief | location, review signal, storefront gap, local language |
| `market-segmentation-memo` | Research / Audience Simulation | segmentation memo | segment, job, trigger, channel |
| `message-test-scorecard` | Research / Audience Simulation | message test scorecard | message, audience, clarity, relevance |
| `positioning-claim-map` | Research / Audience Simulation | positioning claim map | alternative, claim, proof, objection |
| `research-decision-memo` | Research / Audience Simulation | research decision memo | decision, evidence, finding, confidence |
| `review-forum-mining-brief` | Research / Audience Simulation | review mining brief | review or comment, evidence type, pain, language |
| `stakeholder-simulation-scenario-plan` | Research / Audience Simulation | simulation scenario plan | stakeholder type, scenario, expected reaction, objection |
| `survey-instrument-builder` | Research / Audience Simulation | survey instrument and analysis plan | decision, respondent criteria, screener, question |
| `synthetic-audience-panel-builder` | Research / Audience Simulation | synthetic panel spec | persona, assumption, scenario, prompt |
| `synthetic-enrichment-panel` | Research / Audience Simulation | synthetic enrichment panel | enrichment assumption, persona, scenario, personalization cue |
