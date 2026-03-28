# Spec Review

```text
PASS IF
  seam_is_named
  AND approved_artifact_is_named
  AND reviewer_is_named
  AND owner_is_named

FAIL IF
  seam_is_missing
  OR approved_artifact_is_missing

SUMMARY := { summary, next }
SCOPE := { seam, approved_artifact, reviewer, owner, reproduction_status, confidence, out_of_scope }
REQUIREMENT_FIT := { required_behavior_covered, extra_behavior_introduced, missing_behavior, boundary_drift, blocked_by_ambiguity }
EVIDENCE := {
  files_reviewed,
  verification_checked,
  smallest_high_value_verification_and_why,
  proof_freshness_or_evidence_gaps,
  behavior_covered,
  comparable_experience_covered,
  context_equivalence_matrix_covered_when_user_facing_or_fallback_claim_exists,
  responsibility_split_covered,
  god_object_risk_covered,
  oversized_file_split_decision_covered,
  large_file_exception_rationale_covered_when_applicable,
  threshold_trigger_covered_when_release_or_monitoring_claim_exists,
  threshold_action_covered_when_release_or_monitoring_claim_exists,
  sustainability_decision_class_covered_when_material,
  sustainability_decision_quality_covered,
  sustainability_decision_not_applicable_reason,
  sustainability_decision_covered_when_material,
  coverage_blind_spots,
  performance_regression_relevance,
  docs_reviewed,
  examples_exercised_or_inspected,
  remaining_operator_or_user_facing_risk,
  artifacts,
  impact,
  workaround,
  gaps
}
RISKS := { risks, open_questions }
DECISION := { pass, fail, required_fixes, regression_handoff }

FAIL IF
  DECISION.pass = true AND EVIDENCE.proof_freshness_or_evidence_gaps IS unresolved
  OR DECISION.pass = true AND EVIDENCE.comparable_experience_covered IS missing_when_user_facing
  OR DECISION.pass = true AND EVIDENCE.context_equivalence_matrix_covered_when_user_facing_or_fallback_claim_exists IS missing
  OR DECISION.pass = true AND EVIDENCE.responsibility_split_covered IS missing
  OR DECISION.pass = true AND EVIDENCE.god_object_risk_covered IS missing
  OR DECISION.pass = true AND EVIDENCE.oversized_file_split_decision_covered IS missing
  OR DECISION.pass = true AND EVIDENCE.large_file_exception_rationale_covered_when_applicable IS missing
  OR DECISION.pass = true AND EVIDENCE.threshold_trigger_covered_when_release_or_monitoring_claim_exists IS missing
  OR DECISION.pass = true AND EVIDENCE.threshold_action_covered_when_release_or_monitoring_claim_exists IS missing
  OR DECISION.pass = true AND EVIDENCE.sustainability_decision_class_covered_when_material IS missing
  OR DECISION.pass = true AND EVIDENCE.sustainability_decision_class_covered_when_material = not_applicable AND EVIDENCE.sustainability_decision_not_applicable_reason IS missing
  OR DECISION.pass = true AND EVIDENCE.sustainability_decision_quality_covered IS missing
  OR DECISION.pass = true AND EVIDENCE.sustainability_decision_covered_when_material IS missing
  OR DECISION.pass = true AND EVIDENCE.sustainability_decision_covered_when_material = not_applicable AND EVIDENCE.sustainability_decision_not_applicable_reason IS missing
```
