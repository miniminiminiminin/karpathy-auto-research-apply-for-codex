---
name: implementation-frontend
description: Use when an approved route, component, or client interaction seam needs implementation with explicit state, accessibility, and responsive proof.
---

# Implementation Frontend

## Overview

Ship the frontend seam without leaking into unrelated layers.

**Core principle:** if the user-facing behavior, accessibility impact, and verification path are not explicit, the frontend change is not ready.

Write the test first. Watch it fail. Write minimal code to pass.

**Violating the letter of the rules is violating the spirit of the rules.**

<HARD-GATE>
Do not start implementation from vibes. Name the route or component seam, the states that matter, the data contract, and the proof that will verify the change.
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before coding, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Keep state as close to usage as possible, preserve semantic structure, and avoid performance work that is not backed by a user-facing bottleneck or measurable interaction risk.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Do not let one component, hook, or page absorb unrelated layout policy, data wiring, effect control, and visual state just because it is convenient. Split responsibilities before the seam becomes hard to reason about.
</NON-NEGOTIABLE>

<CHANGE-RADIUS-GATE>
If the implementation expands beyond one primary route or component seam, adds a new owner, or starts changing adjacent surfaces not named in the plan, stop and route back to planning-and-scoping.
</CHANGE-RADIUS-GATE>

<DISCIPLINE-GATE>
root_cause_or_failure_mode_is_named_before_fix.
red_green_proof_is_required_when_behavior_changes.
NO_PRODUCTION_CODE_WITHOUT_A_FAILING_TEST_FIRST.
</DISCIPLINE-GATE>

<ANTI-PATTERN>
Do not treat a pretty happy path as frontend completeness.
</ANTI-PATTERN>

<OWNER-BOUNDARY>
Do not decide product policy, service eligibility, or outcome framing from inside frontend implementation.
If the main uncertainty is the product rule rather than the seam translation, route back to `product-and-ux`.
</OWNER-BOUNDARY>

## Required Reads

- You MUST read `references/implementation-guardrails.md` before coding when this skill triggers.
- You MUST start from `assets/frontend-implementation-brief.md` before implementation.
- IF state_coverage_is_the_main_risk THEN START -> `assets/component-state-checklist.md`

## When to Use

- IF approved_route_component_or_interaction_seam_needs_building THEN USE
- IF remaining_risk_is_state_coverage_accessibility_responsiveness_or_ui_wiring THEN USE
- IF design_exists_but_exact_state_and_proof_handling_are_still_missing THEN USE
- IF new_feature OR bug_fix OR refactor OR behavior_change THEN USE

## Do Not Use

- IF request_is_open_ended_product_discovery THEN ROUTE -> product-and-ux
- IF approved_ux_exists_but_any_of(named_hierarchy_model, named_typography_roles, named_color_roles, relevant_state_visual_rules, named_breakpoint_behavior, visual_rule_matrix, visual_approval_evidence) IS missing THEN ROUTE -> visual-design
- IF backend_contract_is_not_stable THEN ROUTE -> architecture-and-design OR implementation-backend
- IF work_is_review_or_release_gate THEN ROUTE -> quality-and-review

## The Iron Law

```text
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over.

**No exceptions:**
- Don't keep it as "reference"
- Don't "adapt" it while writing tests
- Don't look at it
- Delete means delete

Implement fresh from tests. Period.

## Procedure

```text
STEP_0 := DECLARE(support_files := exact assets/ + references/ set OR none)
STEP_0A := READ(required_assets_and_references_before_coding)
STEP_0B := RECORD(why_each_declared_file_was_loaded)
INPUT := { seam, user_facing_behavior, data_contract, required_states, token_handoff, proof_plan }

IF user_facing_behavior_is_implicit OR state_coverage_is_missing THEN STOP("define the frontend seam first")
IF behavior_change_or_bug_fix AND root_cause_or_failure_mode_is_implicit THEN STOP("name the failure mode before fixing")
IF change_radius_exceeds_one_primary_seam OR adjacent_surface_changes_are_unplanned THEN ROUTE -> planning-and-scoping

STATE_SET := NAME(loading, empty, success, error, blocked_interaction)
IF behavior_change_or_bug_fix THEN
  RECORD(expected_failure_or_missing_state_before_fix)
  WRITE(minimal_failing_test_showing_one_behavior_or_state)
  VERIFY_RED(test_fails_for_expected_reason_not_typo_or_harness_error)

IMPLEMENT minimum_change_that_satisfies(approved_behavior)

GUARDRAILS := KEEP(
  state_local_to_usage,
  semantic_structure_intact,
  component_or_hook_responsibility_is_single_and_named,
  large_component_or_file_split_when_it_crosses_responsibility_or_about_200_lines_without_irreducible_reason,
  sensitive_data_out_of_client_storage,
  readable_measure_and_asset_size_expectations_named,
  primary_emphasis_beats_decorative_treatment,
  comparable_experience_preserved_across_input_and_context,
  user_control_not_suppressed_for_zoom_motion_or_alternate_path
)

IF new_dependency OR caching_layer OR rendering_strategy materially_changes_the_seam THEN ROUTE -> planning-and-scoping

VERIFY FROM user_facing_seam USING(
  targeted_tests,
  interaction_proof,
  accessibility_checks,
  pre_delivery_checklist_when_hover_focus_motion_affordance_or_contrast_risk_exists,
  responsive_checks,
  token_handoff_checks,
  media_contrast_checks
)
VERIFY(red_green_proof) IF behavior_change_or_bug_fix
REFACTOR_ONLY_AFTER_GREEN()

HANDOFF := RECORD(exact_behavior, exact_files, exact_proof)

STOP("frontend delivery note is ready")
```

## Choose Roles

- `IF default_frontend_build THEN use agents/software-engineer-frontend.md`
- `IF state_flow_or_low_level_visual_intent_needs_implementation_alignment AFTER visual direction is approved THEN use agents/ui-ux-designer.md`
- `IF interaction_proof_accessibility_or_regression_is_weak THEN use agents/qa.md`

## Choose Assets

- `IF default_delivery_note THEN START -> assets/frontend-handoff.md`
- `IF behavior_or_visual_acceptance_is_the_gate OR hover_focus_motion_affordance_or_contrast_risk_exists THEN START -> assets/ui-review-checklist.md`
- `IF state_coverage_is_the_highest_risk THEN START -> assets/component-state-checklist.md`
- `IF seam_is_known_but_behavior_and_proof_need_a_build_brief THEN START -> assets/frontend-implementation-brief.md`

## Choose References

- `IF coding_guardrail_needed THEN READ -> references/implementation-guardrails.md`
- `IF seam_should_inherit_shared_tokens_effects_or_variants THEN READ -> references/design-system-foundations.md`
- `IF translating_approved_ux_into_props_variants_and_stateful_behavior OR emphasis_rules_need_translation THEN READ -> references/component-implementation-playbook.md`
- `IF layout_navigation_media_or_breakpoint_behavior_matters OR readable_measure_asset_size_risk_is_high THEN READ -> references/responsive-layout-patterns.md`
- `IF custom_interaction_focus_or_announcements_are_part_of_the_seam THEN READ -> references/aria-and-keyboard-baseline.md`
- `IF missing_states_or_blocked_interactions_are_likely THEN READ -> references/ui-state-coverage.md`
- `IF animation_rendering_cost_or_bundle_behavior_could_regress_the_ux THEN READ -> references/frontend-performance-guardrails.md`

## Output Contract

Return a frontend delivery note with:

- declared support files
- files read before coding
- why each file was loaded
- seam implemented
- component responsibility and split decision
- states and accessibility coverage
- comparable experience and user-control coverage
- proof run
- watched failing test before implementation
- wrote minimal code to pass
- responsive or performance notes
- change radius and any reroute trigger
- next owner or next skill
- files actually used

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple UI behavior breaks. Test takes little time. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Manual checks are not systematic and are hard to re-run. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "TDD will slow me down" | TDD is faster than debugging broken state coverage later. |

## Red Flags - STOP and Start Over

- Code before test
- Test after implementation
- Test passes immediately
- Can't explain why test failed
- Tests added later
- Rationalizing just this once
- Keep as reference or adapt existing code
- Already spent X hours, deleting is wasteful

All of these mean: Delete code. Start over with TDD.
