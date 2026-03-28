# Iteration Brief

```text
ITERATION := {
  purpose_link,
  active_slice,
  expected_user_or_system_gain,
  non_goals,
  owned_files_or_surface,
  proof_path,
  expected_signal,
  planner_owner,
  executor_owner,
  evaluator_owner
}

PASS IF
  purpose_link
  AND active_slice
  AND non_goals
  AND proof_path
  AND planner_owner
  AND executor_owner
  AND evaluator_owner

FAIL IF
  active_slice IS vague
  OR proof_path IS implied
  OR non_goals IS missing
```
