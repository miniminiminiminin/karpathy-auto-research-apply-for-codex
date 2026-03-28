# Project State

```text
PROJECT_STATE := {
  purpose_summary,
  rubric_status,
  current_stage,
  active_iteration,
  active_plan_reference,
  project_surface,
  open_risks,
  next_owner
}

PASS IF
  purpose_summary
  AND rubric_status = locked
  AND current_stage
  AND active_iteration
  AND project_surface

FAIL IF
  rubric_status IS missing
  OR active_iteration IS missing
  OR next_owner IS missing
```
