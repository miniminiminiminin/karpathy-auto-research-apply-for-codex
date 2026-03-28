---
name: product-and-ux
description: Use when user problems, flows, messaging, or experience trade-offs need current evidence and a clear direction before implementation.
---

# Product And UX

## Overview

Shape the experience before the interface calcifies.

**Core principle:** if the user problem, evidence quality, or decision criteria are weak, design talk will collapse into taste.

Help turn ideas into fully formed designs and specs through natural collaborative dialogue.

Start by understanding the current project context, then ask questions one at a time to refine the idea. Once you understand what you're building, present the design and get user approval.

<HARD-GATE>
Do not jump from a vague request to screens, feature lists, or implementation advice. First make the user, job, success condition, and evidence path explicit.
Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it. This applies to EVERY project regardless of perceived simplicity.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before shaping direction, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<APPROVAL-GATE>
Do not route implementation guidance forward until the direction package has been reviewed and explicitly approved.
</APPROVAL-GATE>

<NON-NEGOTIABLE>
Questions come before methods. State the question, segment scope, evidence strength, and limitations before turning research, feedback, or content direction into product guidance.
</NON-NEGOTIABLE>

<ANTI-PATTERN>
Do not confuse trend narration, user quotes, brand adjectives, or "good UX instincts" with a usable product decision.
</ANTI-PATTERN>

## Anti-Pattern: "This Is Too Simple To Need A Design"

Every project goes through this process. A todo list, a single-function utility, a config change all of them. "Simple" projects are where unexamined assumptions cause the most wasted work. The design can be short (a few sentences for truly simple projects), but you MUST present it and get approval.

## When to Use

- a request is still a user-problem, flow, messaging, or direction question
- research, feedback, support, trend, or brand signals exist but have not become product guidance
- frontend implementation is close but the experience direction is still unstable
- the next move is bounded direction, not coding or release review

## Do Not Use

- low-level implementation after the experience is already approved
- detailed visual art direction after the UX direction is already approved
- backend-only contract work
- release or runtime approval

## Required Reads

- You MUST read `references/signal-translation-rules.md` before reducing research, feedback, competitive, design-direction, or cross-team packaging signals into product direction.
- You MUST read `references/service-outcome-principles.md` when service clarity, expectation-setting, assistance-path design, no-dead-end handling, or comparable task completion is part of the question.
- You MUST start from `assets/product-brief.md` before shaping direction. Switch to a narrower asset only when the evidence mode is already clear.
- Read `assets/ux-review.md` when the next move is section-by-section design approval, changes requested, or measurable approval criteria.

## Checklist

You MUST create a task for each of these items and complete them in order:

1. **Explore project context** check files, docs, recent commits
2. **Ask clarifying questions** one at a time, understand purpose/constraints/success criteria
3. **Propose 2-3 approaches** with trade-offs and your recommendation
4. **Present design** in sections scaled to their complexity, get user approval after each section
5. **Write design direction record** save the validated direction in local assets and route it forward only after approval
6. **User or named approval owner reviews written direction** ask for approval before planning begins
7. **Transition to implementation planning** route to `planning-and-scoping`

## Procedure

```text
STEP_1 := declare(support_files := exact assets/ + references/ set OR none)
STEP_2 := read(required_assets_and_references_before_direction)
STEP_3 := record(why_each_declared_file_was_loaded)
STEP_4 := restate(user, job, desired_outcome)
STEP_5 := assess(scope := single_project OR multi_subproject)
STEP_6 := decompose_into_subprojects IF project_is_too_large_for_one_direction_package
STEP_7 := ask(one_question_at_a_time)
STEP_8 := name(decision_question, evidence_mode)
STEP_9 := define(segment_scope, evidence_strength, limitations, contradictory_signals)
STEP_10 := compare(2_to_3_approaches, recommended_direction, avoid_list)
STEP_11 := present(design_sections_scaled_to_complexity)
STEP_12 := get_user_or_named_approval_owner_review_after_each_section
STEP_13 := translate(signals -> tradeoffs, service_outcome_rules, recommended_direction, avoid_list, remaining_uncertainty)
STEP_14 := record(service_purpose, expectation_setting, assistance_path, no_dead_end_handling, comparable_experience_risk, decision_explanation_rules)
STEP_15 := record(direction_approval_status, approval_owner, approval_notes)
STEP_16 := package(minimum_guidance)

IF direction_approval_status = approved AND any_of(named_hierarchy_model, named_typography_roles, named_color_roles, named_state_visual_rules, named_breakpoint_behavior, visual_approval_evidence) IS missing THEN ROUTE -> visual-design
ELSE IF direction_approval_status = approved THEN ROUTE -> planning-and-scoping
ELSE STOP("product direction is still incomplete")
```

## Key Principles

- **One question at a time** Don't overwhelm with multiple questions
- **Multiple choice preferred** Easier to answer than open-ended when possible
- **YAGNI ruthlessly** Remove unnecessary features from all designs
- **Explore alternatives** Always propose 2-3 approaches before settling
- **Incremental validation** Present design, get user or named approval-owner review before moving on
- **Be flexible** Go back and clarify when something doesn't make sense

## Choose Roles

- use `agents/po-pm.md` when the main job is product framing, scope, and trade-off selection
- use `agents/ux-researcher.md` when evidence gathering or interpretation is the weak point
- use `agents/content-strategist.md` when messaging, comprehension, or launch language is the seam
- use `agents/ui-ux-designer.md` when the direction must become concrete interaction guidance or low-to-mid fidelity hierarchy guidance

## Choose Assets

```text
IF default_direction_package THEN START -> assets/product-brief.md
ELSE IF missing_input = research_design THEN SWITCH -> assets/ux-research-plan.md
ELSE IF evidence_mode = feedback OR evidence_mode = support THEN SWITCH -> assets/feedback-coding-sheet.md OR assets/support-insight-brief.md
ELSE IF evidence_mode = market OR evidence_mode = competitive THEN SWITCH -> assets/trend-brief.md
ELSE IF seam = positioning OR seam = message_architecture THEN SWITCH -> assets/brand-foundation-worksheet.md OR assets/message-house.md
ELSE IF seam = launch_messaging THEN SWITCH -> assets/launch-content-brief.md
ELSE IF direction_exists AND review_needed THEN SWITCH -> assets/ux-review.md
ELSE STOP("choose the asset that matches the actual evidence mode")
```

## Choose References

```text
IF evidence_mode = research THEN READ -> references/ux-research-methods.md
ELSE IF evidence_mode = feedback OR evidence_mode = support THEN READ -> references/feedback-synthesis-framework.md OR references/support-signal-synthesis.md
ELSE IF evidence_mode = trend OR evidence_mode = competitive THEN READ -> references/trend-research-rubric.md
ELSE IF service_clarity_or_flow_continuity_is_the_main_risk THEN READ -> references/service-outcome-principles.md
ELSE IF direction_must_resolve_into_ui_rules THEN READ -> references/design-system-methodology.md OR references/mobile-first-experience-principles.md OR references/interaction-accessibility-principles.md OR references/ui-ideation-prompt-patterns.md
ELSE IF direction_is_still_low_fidelity_or_flow_shaping OR hierarchy_or_state_clarity_is_unproven THEN READ -> references/wireframe-discipline.md
ELSE IF visual_inputs_must_be_distilled_into_reusable_rules THEN READ -> references/design-system-extraction.md
ELSE READ -> references/signal-translation-rules.md
```

## Output Contract

Return a product and UX brief with:

- declared support files
- files read before direction
- why each file was loaded
- user and job
- question answered
- evidence path and limitations
- trade-offs
- recommended direction
- service purpose and promise
- expectation-setting notes
- no-dead-end handling
- assistance path
- decision explanation rules
- comparable experience risk
- what to avoid
- remaining uncertainty
- design sections reviewed and approval status
- next skill
- files actually used
