# Bootstrap Record

```text
BOOTSTRAP := {
  purpose_path,
  purpose_confirmed,
  rubric_path,
  rubric_generation_source,
  rubric_generated_or_present,
  rubric_lock_status,
  baseline_proof_path,
  baseline_capture_status,
  initialization_files,
  next_owner,
  next_skill
}

PASS IF
  BOOTSTRAP.purpose_path
  AND BOOTSTRAP.purpose_confirmed
  AND BOOTSTRAP.rubric_generation_source
  AND BOOTSTRAP.rubric_generated_or_present
  AND BOOTSTRAP.rubric_lock_status
  AND BOOTSTRAP.baseline_proof_path
  AND BOOTSTRAP.next_owner
  AND BOOTSTRAP.next_skill

FAIL IF
  BOOTSTRAP.purpose_confirmed IS not_yes
  OR BOOTSTRAP.rubric_generated_or_present IS not_yes
  OR BOOTSTRAP.rubric_lock_status IS missing_or_not_locked
  OR BOOTSTRAP.baseline_capture_status IS missing_or_not_started
```
