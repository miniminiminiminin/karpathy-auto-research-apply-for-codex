---
name: intake-and-routing
description: Use when a new request, mixed request, or ambiguous request must be restated, bounded, and routed to the single best next repo-local skill before planning or implementation begins.
---

# Intake And Routing

## Overview

Turn an incoming request into a clear next move, then stop.

**Core principle:** if the objective, success condition, or next operating track is still fuzzy, do not pretend planning has started and do not let execution start by accident.

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance the request still needs intake, boundary-setting, or skill selection, you ABSOLUTELY MUST do intake first.

IF INTAKE APPLIES TO THE REQUEST, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

<HARD-GATE>
Before any planning, architecture, implementation, or review move, you MUST name the outcome, success condition, current boundary, and next owner.

Do not route work forward until the request has a named outcome, boundary, and owner for the next decision.
Do not ask exploratory multi-question bundles.
Do not start coding, planning, or architecture exploration "just to get context."
Do not treat creative work as "too simple" to need design.
</HARD-GATE>

<NON-NEGOTIABLE>
Choose the minimum viable next route. If one direct skill fits cleanly, do not escalate to orchestration. If ambiguity remains material, ask one focused clarification question instead of guessing.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
If the user explicitly asks for subagents, delegation, parallel evaluation, or orchestration, you MUST make the orchestration decision explicit. Route to `multi-agent-orchestration` unless you can record a concrete no-fan-out reason that keeps one direct owner clearly superior.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before routing, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<OWNER-BOUNDARY>
Do not let intake quietly become planning, architecture, implementation, or repo-wide skill editing.
If the request is to revise CANON itself, absorb external principle libraries, or repackage the skill system across owners, route to `skillsmith` after restating the seam.
</OWNER-BOUNDARY>

## Red Flags

These thoughts mean STOP: you're rationalizing.

| Thought | Reality |
|---------|---------|
| "The user already said enough, I can just start" | Named work is not the same as a bounded request. |
| "I'll explore the repo first and route after" | Intake decides how exploration should happen. |
| "I can code one slice while the rest is unclear" | Partial execution is still execution. Route first. |
| "The ambiguity is minor" | If it can change the next skill, it is material. |
| "I already know the owner because it's probably me" | Self-assigning the next owner is not evidence. Name it explicitly. |
| "I can ask a few quick questions and then decide" | Ask one focused question, not a bundle. |
| "Implementation is the minimum viable next route" | Only after intake proves product, planning, architecture, and review do not own the next move. |
| "This feels like harmless context gathering" | Undisciplined context gathering turns into accidental planning. |
| "This is too simple to need design" | Simple projects still need design before implementation. |

## Required Reads

- You MUST start from `assets/intake-record.md` before routing. Switch to `assets/routing-decision.md` only when multiple next skills need explicit comparison.
- You MUST read `references/signal-driven-routing.md` before routing research, feedback, redesign, competitive-direction, or cross-team packaging signals.
- Read `references/intake-clarification-patterns.md` when the request is still fuzzy after restatement or when you are tempted to ask more than one question.
- Read `references/severity-and-escalation.md` when runtime impact, support severity, or escalation posture may change the route.

## Routing

```text
IF outcome IS unclear OR boundary IS unclear OR owner IS unclear:
  ROUTE -> intake-and-routing
ELSE IF user_explicitly_requests_subagents OR delegation OR parallel_evaluation OR orchestration:
  ROUTE -> multi-agent-orchestration
ELSE IF multiple_owned_outcomes_can_progress_in_parallel OR multiple_independent_tracks_are_present:
  ROUTE -> multi-agent-orchestration
ELSE IF request_implies_new_behavior OR new_feature_direction:
  ROUTE -> product-and-ux BEFORE planning_or_architecture_or_implementation
ELSE IF creative_work_or_behavior_change_is_present_even_if_small:
  ROUTE -> product-and-ux BEFORE implementation
ELSE IF runtime_impact OR incident_coordination dominates:
  ROUTE -> release-and-operations
ELSE IF evidence_is_incomplete OR acceptance_risk dominates:
  ROUTE -> quality-and-review
ELSE IF request_is_repo_wide_canon_revision OR skill_system_absorption OR multi_owner_skill_maintenance:
  ROUTE -> skillsmith
ELSE:
  ROUTE -> the_single_best_direct_skill
```

## Procedure

```text
1. DECLARE(support_files := exact assets/ + references/ set OR none)
2. READ(required_assets_and_references_before_routing)
3. RECORD(why_each_declared_file_was_loaded)
4. RESTATE(request := target_outcome + success_condition + constraints + explicit_non_goals)
5. CHECK(current_context, existing_constraints, approval_state, evidence_state)
6. IDENTIFY(dominant_track := product-and-ux OR visual-design OR planning-and-scoping OR architecture-and-design OR implementation OR autonomous-app-loop OR quality-and-review OR release-and-operations OR multi-agent-orchestration OR skillsmith)
7. RECORD(missing_inputs := approval OR boundary OR proof_expectation OR design_decision OR stakeholder_owner OR severity)
7A. CLASSIFY(request_scale := single_owner_single_batch OR single_owner_multi_batch OR mixed_owner_multi_batch)
7B. RECORD(active_batch_now, parked_follow_ups, decomposition_seam) IF request_spans_multiple_owners_or_is_oversized
7C. RECORD(orchestration_trigger, no_fan_out_reason) IF user_explicitly_requests_subagents OR delegation OR parallel_evaluation OR orchestration OR multiple_independent_tracks_are_present
8. ROUTE -> multi-agent-orchestration IF user_explicitly_requests_subagents OR delegation OR parallel_evaluation OR orchestration
8A. ROUTE -> multi-agent-orchestration IF multiple_owned_outcomes_can_progress_in_parallel OR multiple_independent_tracks_are_present
8B. ROUTE -> product-and-ux IF request_implies_new_behavior OR new_feature_direction AND direction_or_approval_is_not_explicit AND orchestration_is_not_the_active_question
8C. ROUTE -> skillsmith IF request_is_repo_wide_canon_revision OR skill_system_absorption OR owner_split_is_the_real_work AND orchestration_is_not_the_active_question
9. ASK(one_focused_question) IF material_ambiguity_remains = TRUE
10. CHOOSE(one_next_skill)
11. RECORD(why_alternatives_lost_now IN assets/intake-record.md OR assets/routing-decision.md)
12. STOP("intake complete") WHEN the next owner can proceed without guessing
```

## Asset Routing

```text
IF default_delivery_intake:
  START -> assets/intake-record.md
ELSE IF multiple_next_skills_need_explicit_comparison:
  START -> assets/routing-decision.md
ELSE IF approval_owner_or_communication_path_is_ambiguous:
  START -> assets/stakeholder-alignment-note.md
ELSE IF request_is_a_hypothesis_or_test_idea:
  START -> assets/experiment-intake.md
```

## Output Contract

Return an intake record with:

- support files declared before execution
- files read before routing
- why each file was loaded
- request restatement
- target outcome and success condition
- current constraints and explicit non-goals
- request scale and decomposition seam
- orchestration trigger and no-fan-out reason when orchestration was materially considered
- missing boundary or evidence
- active batch now and parked follow-ups when the request is oversized
- considered next skills
- chosen next skill
- why nearby alternatives lost
- next owner or next action
- one focused clarification question, if needed
- support files actually used
