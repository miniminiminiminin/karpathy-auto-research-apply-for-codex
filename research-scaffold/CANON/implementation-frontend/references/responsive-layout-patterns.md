# Responsive Layout Patterns

```text
AUTHORITY := {
  type := external_summary_plus_house_rule,
  primary_sources := [WCAG_reflow, WCAG_target_size, MDN, web.dev],
  note := "Treat numeric thresholds as explicit policy, not implied defaults."
}

INPUT := {
  mobile_content_priority,
  breakpoint_contract,
  navigation_behavior,
  image_or_media_behavior,
  css_method_or_framework,
  browser_support_policy_or_baseline,
  presentation_proof
}

WORKING_ORDER :=
  1 -> mobile_baseline
  2 -> tablet_and_desktop_expansion
  3 -> extreme_content_and_zoom_cases

CHECKS := PASS IF
  mobile_content_priority_is_named_before_breakpoint_expansion
  content_width_matches_readability_before_canvas_fill
  AND readable_measure_survives_breakpoint_expansion_without_turning_into_canvas_fill
  AND supporting_content_can_move_to_adjacent_columns_before_core_content_is_widened
  AND container_behavior_and_overflow_are_safe
  AND text_wrapping_and_truncation_are_safe
  AND touch_target_size_is_safe
  AND keyboard_and_screen_reader_compatibility_is_safe
  AND content_order_stays_logical_across_breakpoints
  AND primary_action_remains_visible_on_narrow_widths
  AND fixed_or_max_widths_follow_content_stability_before_grid_symmetry
  AND large_elements_shrink_faster_than_small_elements_when_needed
  AND screenshots_or_media_are_cropped_or_reframed_before_being_scaled_to_unreadability
  AND icons_logos_and_screenshots_render_near_intended_size_or_switch_to_a_simpler_representation
  AND asset_size_rules_prevent_icons_logos_and_screenshots_from_drifting_into_generic_fill_behavior
  AND target_size_policy_is_explicit_for_interactive_surfaces
  AND touch_primary_or_high_risk_surfaces_prefer_targets_at_or_above_44px
  AND baseline_accessibility_target_size_does_not_drop_below_24px_without_documented_exception
  AND zoom_to_200_percent_preserves_meaning_and_control_access
  AND the_same_core_task_can_be_completed_without_wide_screen_assumptions
  AND reflow_check_at_320_css_px_or_equivalent_zoom_is_named_when_required_by_policy

PROOF := {
  mobile_tablet_desktop_manual_check,
  zoom_check,
  reflow_or_320_css_px_check,
  image_sizing_and_aspect_ratio_check,
  screenshot_or_media_cropping_check,
  late_loading_media_overflow_check,
  cross_browser_spot_check
}
```
