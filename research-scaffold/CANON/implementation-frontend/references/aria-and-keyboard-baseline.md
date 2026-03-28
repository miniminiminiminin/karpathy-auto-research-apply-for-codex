# ARIA And Keyboard Baseline

```text
AUTHORITY := {
  type := external_summary_plus_house_rule,
  primary_sources := [WCAG, WAI_APG, MDN],
  warning := "Prefer semantic HTML first. No ARIA is better than bad ARIA."
}

INPUT := { component_type, framework_or_runtime, wcag_target_or_local_bar, support_matrix_if_needed }

MINIMUM_CHECKS := PASS IF
  semantic_html_is_used_first
  AND interactive_elements_are_keyboard_reachable_and_operable
  AND labels_and_descriptions_are_defined
  AND state_attributes_exist_when_behavior_changes
  AND focus_is_visible_and_predictable_after(open, close, submit, error)
  AND dynamic_status_changes_are_announced
  AND live_regions_exist_when_async_or_validation_updates_would_be_silent
  AND visual_state_maps_to(accessible_name, role, state)
  AND high_contrast_and_reduced_motion_are_checked_when_relevant
  AND navigation_instructions_exist_when_keyboard_model_is_not_obvious

COMMON_COMPONENT_RULES := {
  dialogs := initial_focus AND escape_handling AND return_focus_on_close,
  menus_and_listboxes := arrow_key_movement AND expanded_state,
  tabs := selected_state AND tab_order AND panel_labeling,
  forms := labels AND descriptions AND errors AND invalid_state
}

PROOF := PASS IF
  keyboard_path_for_main_task_exists
  AND tab_and_shift_tab_path_exists
  AND arrow_key_behavior_is_checked_when_composite_widget_exists
  AND esc_behavior_is_checked_when_dismissible_ui_exists
  AND screen_reader_visible_labels_and_state_changes_are_checked
  AND representative_assistive_tech_and_browser_checks_exist_for_complex_widgets
  AND mobile_touch_and_screen_reader_checks_exist_when_mobile_is_in_scope
  AND no_trap_dead_end_or_invisible_focus_transition_exists

SUPPORT_MATRIX_RULE := PASS IF
  native_controls_or_low_risk_static_content_use_lightweight_checks
  AND custom_widgets_or_complex_async_announcements_use_named_browser_and_assistive_tech_pairs
  AND chosen_pairs_match_the_actual_support_policy_instead_of_a_generic_fixed_combo
```
