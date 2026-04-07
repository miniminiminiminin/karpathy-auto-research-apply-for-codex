# Ops Reporting Rules

Operational reporting should reduce uncertainty quickly.

```text
REPORT_SHAPE := {
  larger_workstream,
  current_status,
  completed_this_session,
  user_impact,
  evidence_source,
  confidence_or_uncertainty,
  fallback_or_safe_mode_when_recommendation_quality_is_in_question,
  revalidation_trigger_when_rule_or_ranking_inputs_can_drift,
  next_action_or_next_seam,
  next_update_time IF unresolved
}

FAILURE_MODES := {
  vague_monitoring_claims,
  no_owner_for_next_action,
  speculation_mixed_with_confirmed_facts
}

PASS IF
  every_field_in(REPORT_SHAPE) IS present_when_relevant
  AND uncertainty_is_labeled_instead_of_hidden
  AND next_action_or_next_seam_has_a_named_owner
  AND recommendation_quality_regression_is_reported_as_current_fact_or_explicit_unknown_not_hand_waved
  AND completed_this_session_is_specific_when_work_was_done

FAIL IF
  report_matches_any(FAILURE_MODES)
```
