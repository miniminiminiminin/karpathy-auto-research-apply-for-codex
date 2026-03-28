# Frontend Implementation Guardrails

```text
AUTHORITY := {
  type := house_rule,
  note := "This file defines routing and scope discipline, not external standards."
}

PASS IF
  composition_and_seam_local_state_are_preferred_over_multi_responsibility_components
  AND each_component_or_hook_has_one_primary_reason_to_change
  AND page_shell_data_fetching_and_presentational_subseams_are_separated_when_they_would_otherwise_compete
  AND file_growth_past_about_200_lines_requires_an_irreducible_seam_reason_or_a_split
  AND loading_error_empty_disabled_and_recovery_states_are_explicit_before_polish
  AND async_and_data_wiring_stay_at_the_nearest_useful_boundary
  AND state_meaning_does_not_depend_on_color_only
  AND browser_or_platform_controls_are_not_suppressed_without_approved_exception
  AND comparable_experience_is_treated_as_behavioral_not_decorative_quality

FAIL IF
  a_single_component_or_hook_became_a_god_object
  OR a_file_grew_past_about_200_lines_without_a_named_irreducible_reason
  OR new_dependency_materially_changes_the_seam
  OR caching_layer_materially_changes_the_seam
  OR rendering_strategy_materially_changes_the_seam

IF FAIL THEN ROUTE -> planning-and-scoping
```
