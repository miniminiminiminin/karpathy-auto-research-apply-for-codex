# Frontend Implementation Brief

```text
EVIDENCE_POLICY := {
  use_minimum_fields_needed_for_the_actual_risk,
  mark_non_applicable_items_explicitly,
  do_not_invent_browser_or_assistive_tech_matrices_for_low_risk_static_seams,
  raise_evidence_depth_when_custom_widgets_async_updates_or_cross_breakpoint_behavior_exist
}

RELEVANCE_RULES := {
  comparable_experience_check_is_required_when_the_seam_is_user_facing,
  zoom_or_reduced_motion_check_is_required_when_layout_motion_media_or_custom_controls_can_hide_or_block_use,
  screen_reader_or_browser_matrix_is_required_when_custom_widgets_async_announcements_or_browser_specific_behavior_exist,
  not_applicable_claims_must_name_why_the_risk_is_absent
}

SEAM := {
  route_or_component,
  component_purpose,
  framework_or_runtime,
  user_facing_behavior,
  primary_task,
  primary_action,
  next_step_after_primary_action,
  props_or_input_contract,
  typing_strategy,
  styling_approach,
  data_contract_assumption,
  component_responsibility,
  extracted_or_planned_subseams,
  file_or_component_split_trigger,
  large_file_exception_rationale,
  state_location,
  variant_or_token_strategy,
  readable_measure_expectation,
  asset_size_expectations,
  emphasis_hierarchy,
  expected_failure_or_missing_state_before_fix,
  error_boundary_or_parent_fallback
}

STATES := {
  required_states,
  states_marked_not_applicable,
  comparable_experience_notes,
  user_control_preservation,
  accessibility_notes,
  wcag_target_or_local_accessibility_bar,
  screen_reader_or_browser_matrix_when_risk_requires_it,
  focus_flow,
  aria_notes,
  recovery_behavior,
  inactive_control_policy,
  overlay_or_contrast_strategy,
  navigation_or_media_behavior,
  responsive_notes,
  breakpoint_contract,
  browser_support_policy_or_baseline
}

PROOF := {
  verification_command,
  verification_after_fix,
  manual_checks,
  automated_checks,
  comparable_experience_check,
  zoom_or_reduced_motion_check_when_relevant,
  next_step_continuity_check,
  readable_measure_check,
  asset_size_check,
  performance_baseline_and_after_note,
  usage_examples_required,
  test_seam,
  handoff_target
}
```
