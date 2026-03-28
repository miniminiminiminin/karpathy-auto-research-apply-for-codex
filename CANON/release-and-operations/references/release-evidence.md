# Release Evidence

```text
PASS IF
  shipping_scope IS explicit
  AND fresh_verification IS present
  AND security_automation_is_fresh_or_explicitly_waived
  AND rollback_owner IS explicit
  AND monitoring_owner IS explicit
  AND open_risk_profile IS explicit
  AND evidence_source IS explicit
  AND uncertainty_label IS explicit
  AND threshold_trigger IS explicit_when_monitoring_or_follow_up_matters
  AND threshold_action IS explicit_when_monitoring_or_follow_up_matters
  AND next_signal_review_time IS explicit_when_monitoring_or_follow_up_matters
  AND signal_threshold_matrix_is_explicit_when_monitoring_or_follow_up_matters
  AND sustainability_materiality IS explicit
  AND sustainability_decision_matrix_is_explicit_when_operational_sustainability_is_plausibly_material
  AND sustainability_decision_class_is_explicit_when_material
  AND material_sustainability_risk_has_a_named_decision_or_mitigation

FAIL IF
  verification_is_stale
  OR security_automation_is_stale_without_waiver
  OR rollback_owner IS missing
  OR monitoring_owner IS missing
  OR open_risk_profile IS implicit
  OR evidence_source IS missing
  OR uncertainty_label IS implicit
  OR threshold_trigger IS missing_when_monitoring_or_follow_up_matters
  OR threshold_action IS missing_when_monitoring_or_follow_up_matters
  OR next_signal_review_time IS missing_when_monitoring_or_follow_up_matters
  OR signal_threshold_matrix IS missing_when_monitoring_or_follow_up_matters
  OR sustainability_materiality IS implicit
  OR sustainability_decision_matrix IS missing_when_operational_sustainability_is_plausibly_material
  OR sustainability_decision_class IS missing_when_material
  OR sustainability_note_when_operationally_material IS present_without_decision_or_mitigation

IF shipping_scope IS vague THEN FAIL

AND record(change_type, risk_level, evidence_timeframe, verification_time, rollback_method, recovery_verifier, before_after_state_when_risky, monitoring_owner, cheapest_safe_path_chosen, chosen_rollout_shape, rollback_trigger, next_signal_review_time, threshold_trigger, threshold_action, signal_threshold_matrix, sustainability_materiality, sustainability_decision_matrix, sustainability_decision_class, sustainability_note_when_operationally_material, sustainability_decision_or_mitigation)
AND record(security_scan_jobs, security_artifacts, security_owner)

IF endpoint_or_method_matters THEN
  record(endpoint, method, observed_response)

IF environment_is_resource_constrained THEN
  record(build_strategy, recovery_path)

IF ship_decision_depends_on_runtime_monitoring THEN
  record(observability_coverage, alert_coverage)

keep_branch_as_is_is_allowed_without_forced_cleanup
discard_requires_explicit_confirmation

IF security_findings_exist THEN ROUTE -> security-review

NOT(can_deploy = safe_to_operate)
AND prefer(fresh_runtime_checks_over_inherited_confidence)
```
