# Evaluation Report

```text
EVALUATION := {
  proof_run,
  baseline_reference,
  rubric_score_before,
  rubric_score_after,
  delta,
  regressions,
  unresolved_risks,
  evaluator_decision,
  rationale
}

PASS IF
  proof_run
  AND rubric_score_after
  AND evaluator_decision

FAIL IF
  proof_run IS stale
  OR evaluator_decision IS missing
  OR rationale IS missing
```
