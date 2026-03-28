# Loop Record

```text
LOOP_RECORD := {
  iteration_id,
  purpose_link,
  active_slice,
  changed_surface,
  proof_summary,
  score_delta,
  promotion_status,
  memory_note,
  next_action
}

PASS IF
  iteration_id
  AND active_slice
  AND proof_summary
  AND promotion_status
  AND next_action
```
