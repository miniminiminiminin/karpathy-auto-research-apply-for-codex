# Sustainability Decision Matrix

```text
USE_THIS_ASSET IF
  the_change_can_materially_shift_runtime_cost_capacity_or_resource_use
  OR the_rollout_shape_changes_compute_or_data_movement_behavior
  OR mitigation_or_hold_might_depend_on_operational_efficiency_or_load

SUSTAINABILITY := {
  materiality_class,
  impact_vector,
  impact_horizon,
  evidence_basis,
  user_or_operator_risk,
  decision_class,
  mitigation_or_measurement,
  decision_owner,
  review_time
}

materiality_class := material OR non_material
impact_vector := capacity OR latency OR energy_or_compute OR storage_or_transfer OR operator_burden OR mixed
impact_horizon := launch_window OR steady_state OR peak_load OR backlog_recovery OR long_lived
decision_class := accept_now OR mitigate_before_ship OR measure_before_ship OR hold

PASS IF
  materiality_class_is_explicit
  AND impact_vector_is_explicit_when_material
  AND impact_horizon_is_explicit_when_material
  AND evidence_basis_is_explicit_when_material
  AND decision_class_is_explicit_when_material
  AND decision_owner_is_named_when_material
  AND review_time_is_named_when_material
  AND mitigation_or_measurement_is_explicit_when_decision_class != accept_now

FAIL IF
  materiality_class_is_implicit
  OR impact_vector_is_missing_when_material
  OR impact_horizon_is_missing_when_material
  OR evidence_basis_is_missing_when_material
  OR decision_class_is_missing_when_material
  OR decision_owner_is_missing_when_material
  OR review_time_is_missing_when_material
  OR mitigation_or_measurement_is_generic_when_decision_class != accept_now
```
