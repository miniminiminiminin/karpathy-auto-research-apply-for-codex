# Color, Type, And Density

```text
AUTHORITY := {
  type := mixed_external_principles_and_house_rule,
  sources := [design_system_methodology, inclusive_design_principles, visual_principles_sources],
  note := "Typography, color, and density must make the task easier before they signal personality."
}

PASS IF
  typography_roles_are_small_repeatable_and_scannable
  AND weight_size_and_spacing_do_more_hierarchy_work_than_extra_chrome
  AND color_roles_are_semantic_and_consistent
  AND accent_usage_is_sparse_deliberate_and_teaches_one_meaning_at_a_time
  AND content_is_preserved_before_chrome_is_added
  AND density_matches_the_real_task_not_aesthetic_fear_of_empty_space
  AND generous_spacing_is_the_default_until_compactness_is_earned
  AND contrast_and_legibility_survive_real_states_and_real_copy_lengths
  AND sensitive_or_high_stakes_slices_keep_a_dignified_non_judgmental_tone

FAIL IF
  the_screen_uses_many_visual_accents_without_priority_gain
  OR multiple_font_sizes_or_weights_exist_without_named_roles
  OR chrome_is_preserved_by_sacrificing_readability
  OR density_is_reduced_by_shrinking_type_before_removing_noise
  OR palette_or_type_choices_feel_generic_because_no_rules_were_named

SIGNAL_TO_ACTION := {
  "too_many_accents" -> "reduce_accent_roles_to_semantic_or_primary_emphasis_only",
  "type_scale_feels_random" -> "name_each_role_and_remove_one_off_sizes_or_weights",
  "surface_feels_punitive_or_alarm_heavy" -> "reduce_alarm_styling_unless_risk_is_real_and_actionable",
  "screen_feels_crowded" -> "remove_low_value_chrome_or_secondary_copy_before_tightening_spacing",
  "screen_feels_generic" -> "define_specific_type_color_and_surface_rules_instead_of_mood_adjectives"
}

REQUIRED_EVIDENCE := {
  named_type_roles,
  named_color_roles,
  one_density_tradeoff_note,
  one_do_and_dont_example
}
```
