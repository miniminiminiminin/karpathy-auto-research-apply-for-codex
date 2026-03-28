# Backend Architecture Review

```text
ARCHITECTURE_REVIEW := PASS IF
  public_seam_is_named
  AND dependency_boundary_is_explicit
  AND validation_happens_at_the_boundary
  AND side_effects_are_isolated_from_decision_logic_where_practical
  AND compatibility_story_exists_for_changed_callers_or_consumers
  AND error_behavior_is_actionable
  AND caching_indexing_or_queue_behavior_is_acknowledged_when_relevant
  AND rollback_sensitivity_is_called_out

FAIL IF
  contract_widens_implicitly
  OR convenience_imports_couple_modules
  OR database_or_queue_changes_have_no_consumer_impact_note
  OR generic_errors_hide_failing_boundary
  OR performance_sensitive_seams_change_without_query_payload_batching_or_retry_note
```
