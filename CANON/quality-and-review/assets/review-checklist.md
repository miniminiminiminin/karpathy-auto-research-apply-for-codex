# Review Checklist

## Slice

- declared assets:
- declared references:
- files read before review:
- why each file was loaded:
- files actually used:
- name:
- commit:
- owner:
- decision owner:
- verification owner:
- impact scope:
- upstream dependencies:
- downstream dependencies:
- seam summary:
- receiver:

## Reviews

- spec review complete:
- code-quality review complete:
- security/privacy review complete:

## Findings

- blocking:
- non-blocking:
- remaining uncertainty:

## Verification

- command:
- fresh_command_run_in_this_session:
- result:
- feedback_item_verified_against_codebase_reality:
- proof freshness or evidence gaps:
- stale evidence:
- actual behavior checked:
- comparable experience checked:
- context equivalence matrix checked when user_facing_or_fallback_claim_exists:
- context equivalence not-applicable reason:
- responsive survival checked when relevant:
- user control checked when relevant:
- responsibility split checked:
- god object risk checked:
- oversized file split decision checked:
- large file exception rationale checked when applicable:
- split-trigger waiver checked when present:
- plan freshness checked:
- revalidation route checked when freshness changed:
- threshold trigger checked when release_or_monitoring_claim_exists:
- threshold action checked when release_or_monitoring_claim_exists:
- sustainability materiality checked:
- sustainability decision class checked when material:
- sustainability decision quality adequate:
- sustainability decision not-applicable reason:
- sustainability decision checked when material:
- docs or examples checked:
- examples exercised or only inspected:
- approvals verified:
- rollback owner named:
- release approval required:

## Decision

- approved:
- approved with follow-up:
- rejected:
- release escalation:
- required fixes:
- follow-up cleanup:
- next owner:

PASS IF
  declared_assets ARE named_or_none
  AND declared_references ARE named_or_none
  AND files_read_before_review ARE explicit
  AND why_each_file_was_loaded IS explicit
  AND fresh_command_run_in_this_session = yes
  AND stale_evidence IS none_or_no
  AND comparable_experience_checked IS explicit_or_not_applicable
  AND context_equivalence_matrix_checked_when_user_facing_or_fallback_claim_exists IS explicit_or_not_applicable_with_reason
  AND context_equivalence_not_applicable_reason IS explicit_or_not_applicable
  AND responsive_survival_checked_when_relevant IS explicit_or_not_applicable
  AND user_control_checked_when_relevant IS explicit_or_not_applicable
  AND responsibility_split_checked IS explicit
  AND god_object_risk_checked IS explicit
  AND oversized_file_split_decision_checked IS explicit
  AND large_file_exception_rationale_checked_when_applicable IS explicit_or_not_applicable
  AND split_trigger_waiver_checked_when_present IS explicit_or_not_applicable
  AND plan_freshness_checked IS explicit
  AND revalidation_route_checked_when_freshness_changed IS explicit_or_not_applicable
  AND threshold_trigger_checked_when_release_or_monitoring_claim_exists IS explicit_or_not_applicable
  AND threshold_action_checked_when_release_or_monitoring_claim_exists IS explicit_or_not_applicable
  AND sustainability_materiality_checked IS explicit
  AND sustainability_decision_class_checked_when_material IS explicit_or_not_applicable_with_reason
  AND sustainability_decision_quality_adequate IS explicit
  AND sustainability_decision_not_applicable_reason IS explicit_or_not_applicable
  AND sustainability_decision_checked_when_material IS explicit_or_not_applicable_with_reason
  AND next_owner IS explicit

FAIL IF
  files_actually_used ARE missing
  OR stale_evidence IS yes_or_unknown
  OR comparable_experience_checked IS missing
  OR context_equivalence_matrix_checked_when_user_facing_or_fallback_claim_exists IS missing
  OR context_equivalence_matrix_checked_when_user_facing_or_fallback_claim_exists = not_applicable AND context_equivalence_not_applicable_reason IS missing
  OR responsive_survival_checked_when_relevant IS missing
  OR user_control_checked_when_relevant IS missing
  OR responsibility_split_checked IS missing
  OR god_object_risk_checked IS missing
  OR oversized_file_split_decision_checked IS missing
  OR large_file_exception_rationale_checked_when_applicable IS missing
  OR split_trigger_waiver_checked_when_present IS missing
  OR plan_freshness_checked IS missing
  OR revalidation_route_checked_when_freshness_changed IS missing
  OR threshold_trigger_checked_when_release_or_monitoring_claim_exists IS missing
  OR threshold_action_checked_when_release_or_monitoring_claim_exists IS missing
  OR sustainability_materiality_checked IS missing
  OR sustainability_decision_class_checked_when_material IS missing
  OR sustainability_decision_class_checked_when_material = not_applicable AND sustainability_decision_not_applicable_reason IS missing
  OR sustainability_decision_quality_adequate IS missing
  OR sustainability_decision_checked_when_material IS missing
  OR sustainability_decision_checked_when_material = not_applicable AND sustainability_decision_not_applicable_reason IS missing

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
  OR fresh_command_run_in_this_session IS not_yes
