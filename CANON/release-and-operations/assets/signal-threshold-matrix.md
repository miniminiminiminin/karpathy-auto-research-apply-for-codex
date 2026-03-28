# Signal Threshold Matrix

```text
USE_THIS_ASSET IF
  ship_decision_depends_on_post_launch_monitoring
  OR mitigate_and_monitor_is_a_candidate
  OR rollback_depends_on_runtime_thresholds
  OR follow_up_priority_depends_on_measured_signals

SIGNAL := {
  name,
  source,
  environment,
  baseline_window,
  comparison_window,
  threshold_shape,
  threshold_value,
  trigger_condition,
  action_when_triggered,
  action_owner,
  review_time,
  stop_condition
}

PASS IF
  every_material_signal_has_a_named_source
  AND every_material_signal_has_a_baseline_window
  AND every_material_signal_has_a_comparison_window
  AND every_material_signal_has_a_threshold_shape
  AND every_material_signal_has_a_threshold_value_or_explicit_binary_trigger
  AND every_material_signal_has_a_trigger_bound_action
  AND every_material_signal_has_a_named_action_owner
  AND every_material_signal_has_a_review_time
  AND every_material_signal_has_a_stop_condition

FAIL IF
  monitoring_language_is_generic
  OR threshold_shape_is_missing
  OR threshold_value_is_missing_without_binary_trigger
  OR action_when_triggered_is_missing
  OR action_owner_is_missing
  OR baseline_window_is_missing
  OR comparison_window_is_missing
  OR review_time_is_missing
  OR stop_condition_is_missing
```
