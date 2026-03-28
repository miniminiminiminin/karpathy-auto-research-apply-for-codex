# Hierarchy And Composition

```text
AUTHORITY := {
  type := mixed_external_principles_and_house_rule,
  sources := [screen_layout_visual_and_mobile_patterns, visual_principles_sources],
  note := "Hierarchy is a comprehension system before it is a style choice."
}

PASS IF
  the_screen_has_one_clear_primary_focus
  AND each_surface_has_one_primary_action_or_primary_focus
  AND reading_order_is_obvious_without_relying_on_color_or_decoration
  AND visual_order_does_not_break_source_or_focus_order
  AND size_position_density_background_and_repetition_point_toward_the_same_priority
  AND secondary_context_is_softened_before_new_labels_borders_or_icons_are_added
  AND comparison_layouts_keep_alignment_strong_enough_for_scanning
  AND layouts_for_reading_preserve_measure_rhythm_and_paragraph_composure
  AND narrow_widths_keep_the_same_core_decision_structure
  AND breakpoints_are_triggered_by_content_failure_not_device_assumption

FAIL IF
  multiple_regions_compete_as_primary
  OR two_actions_compete_as_primary_on_one_surface
  OR hierarchy_only_exists_in_the_happy_path_mockup
  OR decorative_motion_or_visual_novelty_hides_navigation_or_actions
  OR visual_reordering_breaks_reading_or_focus_order
  OR the_layout_depends_on_extra_explanation_to_be_understood

SIGNAL_TO_ACTION := {
  "multiple_regions_compete_as_primary" -> "remove_or_soften_secondary_emphasis_before_enlarging_the_primary",
  "layout_only_works_on_wide_canvas" -> "linearize_or_restack_before_shrinking_type",
  "source_order_breaks_under_reordering" -> "restore_semantic_order_or_document_and_test_the_exception",
  "user_must_read_labels_to_find_primary_action" -> "rework_position_contrast_and_spacing_before_adding_badges_or_helper_copy"
}

REQUIRED_EVIDENCE := {
  named_primary_focus,
  named_secondary_context,
  narrow_width_priority_behavior,
  one_before_and_after_explanation_for_a_hierarchy_fix
}
```
