# Promotion Decision

```text
PROMOTION := {
  status,
  keep_reason,
  discard_reason,
  escalate_reason,
  next_owner,
  next_slice_candidate
}

ALLOWED status := keep | discard | escalate | ship_candidate

PASS IF
  status
  AND next_owner

FAIL IF
  status = keep AND keep_reason IS missing
  OR status = discard AND discard_reason IS missing
  OR status = escalate AND escalate_reason IS missing
```
