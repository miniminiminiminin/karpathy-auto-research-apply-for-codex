# Architecture Review Checklist

```text
PASS IF
  support_files_are_declared_before_decision
  AND required_files_were_read_before_decision
  AND file_usage_reasoning_is_recorded
  AND target_seam_is_named
  AND at_least_one_alternative_was_considered
  AND losing_options_are_rejected_explicitly
  AND dependency_direction_is_explicit
  AND consumers_and_owners_are_explicit
  AND observability_baseline_is_specific
  AND rollback_trigger_and_owner_are_defined
  AND next_implementation_skill_is_named

FAIL IF
  support_files_are_only_declared_but_not_read
  OR target_seam_is_implicit
  OR dependency_direction_is_missing
  OR observability_baseline_is_generic
  OR rollback_trigger_and_owner_are_missing
  OR next_implementation_skill_is_missing
```
