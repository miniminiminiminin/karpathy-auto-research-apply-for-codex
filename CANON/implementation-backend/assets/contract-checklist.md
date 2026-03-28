# Contract Checklist

```text
CONTRACT := {
  seam,
  irreducible_core,
  existing_capability_reused_or_rejected_with_reason,
  consumer_list,
  producer_list,
  failing_or_blocked_case_recorded_before_fix,
  watched_test_fail_before_implementation,
  failure_reason_confirmed,
  minimal_code_written_to_pass,
  versioning_impact,
  compatibility_risk,
  validation_path,
  edge_handling,
  responsibility_split,
  file_or_class_split_trigger,
  large_file_exception_rationale,
  verification_after_fix
}

PASS IF
  public_contract_is_named
  AND irreducible_core_is_named
  AND existing_capability_reused_or_rejected_with_reason_is_named
  AND hidden_dependency_is_avoided
  AND contract_is_parseable_or_inspectable
  AND watched_test_fail_before_implementation
  AND failure_reason_confirmed
  AND minimal_code_written_to_pass
  AND validation_path_is_covered
  AND failure_path_is_covered
  AND actionable_error_behavior_is_defined
  AND side_effect_boundary_is_isolated
  AND responsibility_split_is_recorded
  AND file_or_class_split_trigger_is_recorded
  AND consumer_impact_is_recorded
  AND idempotency_expectation_is_recorded
  AND bounded_runtime_behavior_is_recorded
  AND runtime_proof_is_present
  AND edge_cases_are_covered
  AND additive_evolution_is_preferred_or_breaking_change_is_explicitly_approved
  AND performance_note_is_added_when_relevant

FAIL IF
  public_contract_is_implicit
  OR irreducible_core_is_missing
  OR existing_capability_reused_or_rejected_with_reason_is_missing
  OR watched_test_fail_before_implementation IS missing
  OR validation_path_is_missing
  OR failure_path_is_missing
  OR responsibility_split_is_missing
  OR file_or_class_split_trigger_is_missing
  OR consumer_impact_is_missing
  OR runtime_proof_is_required_but_missing

DECISION := { approved, blockers, follow_up }
```
