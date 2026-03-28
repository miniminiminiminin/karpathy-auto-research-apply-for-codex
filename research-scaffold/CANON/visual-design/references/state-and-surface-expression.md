# State And Surface Expression

```text
AUTHORITY := {
  type := house_rule_with_external_grounding,
  sources := [inclusive_visual_review, implementation_frontend_state_coverage, visual_principles_sources],
  note := "Loading, empty, error, and blocked states are part of the visual system, not fallback leftovers."
}

PASS IF
  default_loading_empty_error_and_blocked_states_follow_the_same_visual_language
  AND status_is_obvious_without_using_color_as_the_only_signal
  AND low_risk_status_signals_use_low_interruption_patterns_before_escalation
  AND empty_states_reduce_inactive_scaffolding_before_adding_illustration
  AND empty_states_teach_the_next_action_or_context
  AND loading_states_preserve_orientation_and_expected_structure
  AND error_states_preserve_trust_and_show_recovery_paths
  AND each_relevant_state_has_a_next_step_or_human_fallback_when_needed
  AND decision_points_include_instruction_and_reassurance_when_relevant
  AND blocked_states_do_not_tease_actions_that_have_no_effect
  AND user_controls_for_motion_or_interruption_intensity_are_preserved_when_relevant
  AND surface_treatments_help_users_distinguish_priority_without_texture_noise

FAIL IF
  the_primary_state_is_designed_but_other_states_drop_to_library_defaults
  OR status_is_communicated_only_through_badge_color
  OR status_feedback_is_interruptive_without_severity_reason
  OR supportive_illustration_overpowers_the_recovery_action
  OR a_relevant_state_has_no_next_step_or_recovery_visibility
  OR surfaces_gain_depth_or_border_treatment_without_helping_grouping

STATE_SEVERITY := {
  missing_default_or_error_state := critical,
  missing_loading_or_blocked_state_when_relevant := high,
  missing_empty_or_success_state_when_relevant := medium
}

SIGNAL_TO_ACTION := {
  "error_state_loses_trust" -> "simplify_surface_and_prioritize_recovery_action_and_message",
  "loading_state_disorients" -> "preserve_structure_and_expected_measure_while_signaling_progress",
  "empty_state_feels_like_marketing" -> "remove_ornament_and_raise_explanation_plus_next_action",
  "user_is_left_hanging_after_a_decision" -> "add_instruction_reassurance_and_what_happens_next",
  "blocked_state_teases_unavailable_actions" -> "remove_or_demote_inactive_controls_and_show_the_unlock_condition"
}

REQUIRED_EVIDENCE := {
  per_state_visual_intent,
  per_state_primary_action_or_recovery_path,
  per_state_non_color_signal,
  narrow_width_behavior_for_relevant_states
}
```
