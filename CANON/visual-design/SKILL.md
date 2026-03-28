---
name: visual-design
description: Use when a product slice needs explicit visual direction, hierarchy, typography, color, density, or art-direction decisions before frontend implementation or visual approval.
---

# Visual Design

## Overview

Turn approved UX intent into a visual language that can survive implementation.

**Core principle:** if hierarchy, density, tone, and state expression are still implicit, implementation will drift toward generic UI.

<HARD-GATE>
Do not treat visual quality as polish. Before implementation or approval, name the slice, visual goal, hierarchy model, type and color rules, state expression, and review bar.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before making visual direction, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<APPROVAL-GATE>
Do not route a slice into implementation until the visual direction or critique record has an explicit approval disposition.
</APPROVAL-GATE>

<ANTI-PATTERN>
Do not confuse surface novelty, moodboard adjectives, or brand-flavored decoration with a usable visual system.
</ANTI-PATTERN>

<OWNER-BOUNDARY>
Do not invent service logic inside `visual-design`.
You MAY define the visual expression of already-approved expectation-setting, trust cues, recovery visibility, and help paths, but you do not own the underlying service policy or flow contract.
If a principle cannot be translated into hierarchy, composition, typography, color, density, state expression, or responsive-surface behavior, route it back to `product-and-ux`.
</OWNER-BOUNDARY>

## When to Use

- visual direction is weak, generic, or contested
- hierarchy, density, typography, color, or state styling still need a decision
- UX direction exists but the screen would still be easy to implement blandly
- review feedback says the interface feels flat, inconsistent, or under-directed
- a design system or product slice needs stronger visual rules before implementation

## Do Not Use

- user-problem discovery before the experience direction exists
- backend, contract, or topology design
- code implementation after the visual direction is already explicit and approved

## Required Reads

- You MUST start from `assets/visual-direction-brief.md` before shaping a new slice.
- You MUST fill `assets/visual-rule-matrix.md` before claiming the direction is implementation-ready.
- You MUST read `references/visual-principles-sources.md` before finalizing reusable visual rules.
- IF review_or_revision_of_existing_ui THEN START -> `assets/design-critique-record.md`

## Objective Gates

- route to `visual-design` if any of the following are missing for the slice:
  - named hierarchy model
  - one clear primary action or primary focus per surface
  - named typography roles
  - named color roles
  - named state-expression rules for relevant states
  - named breakpoint or narrow-width behavior
  - named next step or recovery visibility for key states
  - user-need evidence and behavior hypothesis
  - preserved user control over zoom, motion, scaling, or interruption intensity
  - implementation-facing rule matrix
  - explicit visual approval evidence

## Procedure

```text
STEP_1 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_2 := READ(required_assets_and_references_before_direction)
STEP_3 := RECORD(why_each_declared_file_was_loaded)
STEP_4 := NAME(slice, user_goal, confidence_level, current_visual_failure)
STEP_5 := DEFINE(visual_goal, tone, avoid_list, approval_owner, user_need_evidence, behavior_hypothesis)
STEP_6 := CHOOSE(hierarchy_model, typography_model, color_strategy, spacing_and_density_strategy, state_expression_strategy, trust_and_reassurance_strategy)
STEP_7 := FILL(visual_rule_matrix := tokens, component_or_surface_rules, relevant_states, breakpoint_behavior, decision_points, do_and_dont_examples, implementation_hooks)
STEP_8 := TEST(direction_against := clarity, scanability, actionability, accessibility, responsive_survival, implementation_survival, status_accuracy)
STEP_9 := CHECK(owner_boundary := visual_rule OR route_back_to_product_and_ux)
STEP_10 := CRITIQUE(competing_visual_signals, generic_defaults, ornamental_noise, token_or_component_implications)
STEP_11 := PACKAGE(direction_record OR critique_record, explicit_rules, unresolved_risks, approval_status, evidence)

IF visual_goal_or_hierarchy_is_implicit THEN STOP("visual direction is not ready")
IF visual_rule_matrix_is_missing THEN STOP("implementation survival is not explicit")
IF service_or_flow_logic_is_carrying_the_main_decision THEN STOP("route this principle back to product-and-ux")
IF approval_evidence_is_missing OR approval_status != approved THEN STOP("visual design still needs approval")
IF approval_mode_is_self_review_only THEN STOP("visual approval needs independent review or explicit user approval")
ELSE ROUTE -> planning-and-scoping OR implementation-frontend
```

## Choose Roles

- `IF default_visual_direction_or_critique THEN use agents/ui-ux-designer.md`
- `IF the_main_gap_is_art_direction_or_visual_taste_control THEN use agents/art-director.md`
- `IF visual_acceptance_or_regression_bar_is_the_gate THEN use agents/visual-critic.md`

## Choose Assets

- `IF new_slice_or_new_direction THEN START -> assets/visual-direction-brief.md`
- `IF implementation_survival_must_be_explicit THEN START -> assets/visual-rule-matrix.md`
- `IF existing_screen_needs_hard_nosed_review THEN START -> assets/design-critique-record.md`
- `IF approval_gate_needs_checklist THEN START -> assets/visual-review-checklist.md`

## Choose References

- `IF hierarchy_composition_or_reading_order_is_the_main_risk THEN READ -> references/hierarchy-and-composition.md`
- `IF typography_color_or_density_direction_is_the_main_risk THEN READ -> references/color-type-and-density.md`
- `IF states_surfaces_or_empty_loading_error_expression_are_the_main_risk THEN READ -> references/state-and-surface-expression.md`
- `IF reusable_rules_or_principle_sources_need_grounding THEN READ -> references/visual-principles-sources.md`

## Output Contract

Return a visual direction note or critique record with:

- declared support files
- files read before direction
- why each file was loaded
- slice and visual goal
- hierarchy strategy
- typography, color, density, and state-expression rules
- implementation-ready visual rule matrix
- avoid list and generic-failure warnings
- approval status with evidence
- next owner or next skill
- files actually used
