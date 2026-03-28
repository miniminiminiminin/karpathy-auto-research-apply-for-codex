# Visual Rule Matrix

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_direction,
  why_each_file_was_loaded,
  files_actually_used
}

SLICE := {
  route_or_component,
  user_goal,
  visual_goal,
  approval_owner
}

TOKENS := {
  typography_roles,
  color_roles,
  spacing_rhythm,
  variation_budget,
  surface_or_elevation_roles,
  imagery_policy
}

SURFACES := {
  primary_surface,
  secondary_surface,
  navigation_or_shell_surface,
  data_or_form_surface
}

STATE_MATRIX := {
  default,
  loading_with_rule_or_not_applicable_reason,
  empty_with_rule_or_not_applicable_reason,
  error_with_rule_or_not_applicable_reason,
  blocked_with_rule_or_not_applicable_reason,
  success_or_confirmation_with_rule_or_not_applicable_reason
}

STATE_BEHAVIOR := {
  primary_action_per_state,
  next_step_or_recovery_visibility_per_state,
  status_accuracy_proof,
  decision_rationale_visibility_when_system_decides,
  human_help_entrypoint_when_relevant
}

BREAKPOINT_MATRIX := {
  narrow_width_behavior,
  narrow_width_failure_signal,
  medium_width_behavior_or_not_applicable_reason,
  wide_width_behavior_or_not_applicable_reason,
  source_order_and_focus_order_lock,
  elements_that_must_not_change_priority,
  elements_that_may_collapse_or_linearize
}

IMPLEMENTATION := {
  token_mapping_or_variant_hooks,
  component_or_surface_rules,
  progressive_enhancement_or_fallback,
  user_controls_preserved := zoom_motion_scaling_notification_controls,
  do_examples,
  dont_examples,
  unresolved_risks
}

PASS IF
  SUPPORT.files_actually_used IS named
  AND TOKENS.typography_roles
  AND TOKENS.color_roles
  AND STATE_MATRIX.default
  AND STATE_BEHAVIOR.primary_action_per_state
  AND STATE_BEHAVIOR.next_step_or_recovery_visibility_per_state
  AND BREAKPOINT_MATRIX.narrow_width_behavior
  AND BREAKPOINT_MATRIX.source_order_and_focus_order_lock
  AND IMPLEMENTATION.token_mapping_or_variant_hooks
  AND IMPLEMENTATION.token_mapping_or_variant_hooks_are_specific_not_generic
  AND every_not_applicable_state_or_breakpoint_has_a_reason

FAIL IF
  any_relevant_state_is_missing_without_not_applicable_marking
  OR primary_action_per_state_is_missing_or_competing
  OR next_step_or_recovery_visibility_is_missing_for_relevant_states
  OR breakpoint_behavior_is_generic_or_implicit
  OR implementation_hooks_are_missing
  OR token_mapping_or_variant_hooks_use_adjective_only_language
```
