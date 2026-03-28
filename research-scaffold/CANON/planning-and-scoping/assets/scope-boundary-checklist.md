# Scope Boundary Checklist

```text
PASS IF
  target_requirement_is_quoted
  AND minimum_useful_slice_is_named
  AND reuse_before_rebuild_is_decided
  AND owned_seam_is_named
  AND non_goals_are_explicit
  AND dependency_risks_or_blockers_are_explicit
  AND producer_or_consumer_blast_radius_is_explicit_when_relevant
  AND verification_owner_is_explicit
  AND proof_bearing_verification_command_or_evidence_is_explicit
  AND stop_condition_is_explicit
  AND receiving_owner_or_handoff_target_is_explicit
  AND the_slice_can_be_executed_without_guessing

FAIL IF
  scope_drift_is_hidden
  OR current_slice_is_bigger_than_the_irreducible_core
  OR proof_path_is_missing
  OR handoff_target_is_missing
```
