# QA Verdict

## Summary

- summary:
- next:

## Scope

- seam:
- qa owner:
- claimed behavior:
- regression surface:
- verification target chosen and why:
- reproduction status:
- confidence:

## Evidence

- verification command:
- full verification command:
- exact output:
- screenshots or artifacts:
- stale evidence:
- proof freshness or evidence gaps:
- independent rerun:
- behavior covered:
- comparable experience covered:
- context equivalence matrix covered:
- context equivalence not-applicable reason:
- responsive survival covered:
- user control covered:
- implementation-detail dependence:
- coverage blind spots:
- flaky evidence handling:
- performance regression evidence:
- docs reviewed:
- examples exercised or inspected:
- remaining operator or user-facing risk:
- impact:
- workaround:
- environment checked:
- static validation proof:
- runtime verification proof:
- migration or reprocessing proof:
- threshold trigger reviewed:
- threshold action reviewed:
- sustainability decision class reviewed when material:
- sustainability decision quality adequate:
- sustainability decision not-applicable reason:
- sustainability decision reviewed when material:

## Findings

- findings:
- risks:
- open questions:

## Verdict

- pass:
- fail:
- completion claim allowed:
- failure type:
- last known good:
- root cause:
- prevention:
- blockers:
- follow-up:
- regression handoff:
- regression prevention:

PASS IF
  pass = true IMPLIES completion_claim_allowed = true
  AND pass = true IMPLIES stale_evidence IS none_or_no
  AND pass = true IMPLIES comparable_experience_covered IS explicit_or_not_applicable
  AND pass = true IMPLIES context_equivalence_matrix_covered IS explicit_or_not_applicable_with_reason
  AND pass = true IMPLIES context_equivalence_not_applicable_reason IS explicit_or_not_applicable
  AND pass = true IMPLIES threshold_trigger_reviewed IS explicit_or_not_applicable
  AND pass = true IMPLIES threshold_action_reviewed IS explicit_or_not_applicable
  AND pass = true IMPLIES sustainability_decision_class_reviewed_when_material IS explicit_or_not_applicable_with_reason
  AND pass = true IMPLIES sustainability_decision_quality_adequate IS explicit
  AND pass = true IMPLIES sustainability_decision_not_applicable_reason IS explicit_or_not_applicable
  AND pass = true IMPLIES sustainability_decision_reviewed_when_material IS explicit_or_not_applicable_with_reason

FAIL IF
  pass = true AND proof_freshness_or_evidence_gaps IS unresolved
  OR pass = true AND comparable_experience_covered IS missing
  OR pass = true AND context_equivalence_matrix_covered IS missing
  OR pass = true AND context_equivalence_matrix_covered = not_applicable AND context_equivalence_not_applicable_reason IS missing
  OR pass = true AND threshold_trigger_reviewed IS missing
  OR pass = true AND threshold_action_reviewed IS missing
  OR pass = true AND sustainability_decision_class_reviewed_when_material IS missing
  OR pass = true AND sustainability_decision_class_reviewed_when_material = not_applicable AND sustainability_decision_not_applicable_reason IS missing
  OR pass = true AND sustainability_decision_quality_adequate IS missing
  OR pass = true AND sustainability_decision_reviewed_when_material IS missing
  OR pass = true AND sustainability_decision_reviewed_when_material = not_applicable AND sustainability_decision_not_applicable_reason IS missing

DecisionQuality := {
  decision_class_fits_materiality_and_evidence,
  mitigation_or_measurement_is_specific,
  decision_owner_is_named,
  review_time_is_named,
  trigger_or_follow_up_is_actionable_when_not_accept_now
}

DecisionQuality.sustainability_decision_quality_adequate := explicit ONLY IF
  decision_class_fits_materiality_and_evidence IS explicit
  AND mitigation_or_measurement_is_specific IS explicit_or_not_applicable
  AND decision_owner_is_named IS explicit
  AND review_time_is_named IS explicit
  AND trigger_or_follow_up_is_actionable_when_not_accept_now IS explicit_or_not_applicable
