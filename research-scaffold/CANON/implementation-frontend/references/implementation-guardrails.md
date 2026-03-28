# Frontend Implementation Guardrails

```text
PASS IF
  composition_and_seam_local_state_are_preferred_over_multi_responsibility_components
  AND loading_error_empty_disabled_and_recovery_states_are_explicit_before_polish
  AND async_and_data_wiring_stay_at_the_nearest_useful_boundary

FAIL IF
  new_dependency_materially_changes_the_seam
  OR caching_layer_materially_changes_the_seam
  OR rendering_strategy_materially_changes_the_seam

IF FAIL THEN ROUTE -> planning-and-scoping
```
