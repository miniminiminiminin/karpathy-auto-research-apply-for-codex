# Release Review Checklist

## Candidate

- name:
- change type:
- risk level:
- build or commit:
- release owner:
- decision owner:
- verification owner:
- impact scope:
- environment:

## Gates

- implementation review complete:
- qa review complete:
- security/privacy review complete:
- workspace isolation verified:
- runtime readiness reviewed:
- rollback owner named:
- rollback method recorded:
- rollback trigger recorded:
- evidence timeframe explicit:
- evidence source explicit:
- uncertainty labeled:
- monitoring owner named:
- cheapest safe rollout path named:
- chosen rollout shape named:
- next signal review time named:
- threshold trigger named:
- threshold action named:
- merge or pr option selected explicitly:

Gates.workspace_isolation_verified := TRUE OR FALSE
Gates.merge_or_pr_option_selected_explicitly := TRUE OR FALSE

## Risks

- blocking:
- non-blocking:

## Verification

- command:
- result:
- environment and runtime evidence reviewed:
- rollout plan recorded:
- approvals verified:
- open risk profile explicit:
- sustainability note explicit when material:
- sustainability decision explicit when material:

PASS IF
  Gates.workspace_isolation_verified = TRUE
  AND Gates.runtime_readiness_reviewed = TRUE
  AND Gates.rollback_owner_named = TRUE
  AND Gates.rollback_method_recorded = TRUE
  AND Gates.rollback_trigger_recorded = TRUE
  AND Gates.merge_or_pr_option_selected_explicitly = TRUE
  AND Gates.evidence_timeframe_explicit = TRUE
  AND Gates.evidence_source_explicit = TRUE
  AND Gates.uncertainty_labeled = TRUE
  AND Gates.monitoring_owner_named = TRUE
  AND Gates.cheapest_safe_rollout_path_named = TRUE
  AND Gates.chosen_rollout_shape_named = TRUE
  AND Gates.next_signal_review_time_named = TRUE
  AND Gates.threshold_trigger_named = TRUE
  AND Gates.threshold_action_named = TRUE
  AND open_risk_profile_explicit = yes
  AND sustainability_decision_explicit_when_material IS yes_or_not_applicable

FAIL IF
  Gates.workspace_isolation_verified = FALSE
  OR Gates.runtime_readiness_reviewed = FALSE
  OR Gates.rollback_owner_named = FALSE
  OR Gates.rollback_method_recorded = FALSE
  OR Gates.rollback_trigger_recorded = FALSE
  OR Gates.evidence_timeframe_explicit = FALSE
  OR Gates.evidence_source_explicit = FALSE
  OR Gates.uncertainty_labeled = FALSE
  OR Gates.monitoring_owner_named = FALSE
  OR Gates.cheapest_safe_rollout_path_named = FALSE
  OR Gates.chosen_rollout_shape_named = FALSE
  OR Gates.next_signal_review_time_named = FALSE
  OR Gates.threshold_trigger_named = FALSE
  OR Gates.threshold_action_named = FALSE
  OR open_risk_profile_explicit IS not_yes
  OR sustainability_decision_explicit_when_material IS missing_or_no

## Decision

- ship:
- ship with follow-up:
- hold:
- release escalation:
- required fixes or mitigations:
- follow-up cleanup:
- reusable rule:
