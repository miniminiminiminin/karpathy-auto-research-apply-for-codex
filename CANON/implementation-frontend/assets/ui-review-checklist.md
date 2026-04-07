# UI Review Checklist

```text
SEAM := {
  route_or_component,
  interaction_goal,
  states_covered,
  responsive_surfaces
}

PASS IF
  hierarchy_is_clear
  AND primary_action_or_primary_task_is_clear
  AND next_step_or_completion_outcome_is_clear
  AND empty_loading_and_error_states_are_covered
  AND interactive_affordance_is_explicit_across(pointer, keyboard, touch_when_relevant)
  AND hover_and_focus_feedback_are_consistent_and_bounded
  AND contrast_target_is_named_from(wcag_target_or_local_accessibility_bar)_and_checked_by_policy
  AND accessibility_impact_is_reviewed
  AND comparable_experience_is_reviewed
  AND state_meaning_is_not_color_only
  AND user_control_for_zoom_motion_and_input_path_is_reviewed_when_relevant
  AND reduced_motion_fallback_is_defined_when_motion_exists
  AND keyboard_and_focus_path_is_reviewed
  AND component_responsibility_stayed_narrow
  AND state_stays_close_to_the_interaction_seam
  AND performance_sensitive_surface_is_reviewed_when_applicable
  AND visual_language_is_preserved

FAIL IF
  hierarchy_is_unclear
  OR primary_action_is_competing_with_secondary_noise
  OR next_step_after_primary_action_is_ambiguous
  OR critical_states_are_missing
  OR interactive_affordance_is_implicit_for_non_native_clickable_ui
  OR hover_or_motion_is_the_only_state_signal
  OR contrast_target_is_implicit
  OR accessibility_review_is_missing
  OR comparable_experience_review_is_missing
  OR fixed_breakpoint_set_is_forced_without_seam_reason
  OR not_applicable_claim_lacks_risk_reason
  OR component_responsibility_widened

EVIDENCE := {
  verification_command,
  screenshots_when_visual_claims_matter,
  interaction_or_test_proof,
  zoom_or_reduced_motion_proof_when_relevant,
  bounded_performance_note,
  verification_owner
}

DECISION := { approved, required_fixes, follow_up }
```
