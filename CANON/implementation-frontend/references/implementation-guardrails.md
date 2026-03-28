# Frontend Implementation Guardrails

```text
AUTHORITY := {
  type := house_rule,
  note := "This file defines routing and scope discipline, not external standards."
}

PASS IF
  composition_and_seam_local_state_are_preferred_over_multi_responsibility_components
  AND loading_error_empty_disabled_and_recovery_states_are_explicit_before_polish
  AND async_and_data_wiring_stay_at_the_nearest_useful_boundary
  AND state_meaning_does_not_depend_on_color_only
  AND browser_or_platform_controls_are_not_suppressed_without_approved_exception
  AND comparable_experience_is_treated_as_behavioral_not_decorative_quality

FAIL IF
  new_dependency_materially_changes_the_seam
  OR caching_layer_materially_changes_the_seam
  OR rendering_strategy_materially_changes_the_seam

IF FAIL THEN ROUTE -> planning-and-scoping
```
