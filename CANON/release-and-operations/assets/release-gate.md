# Release Gate

PASS IF
  declared_assets ARE named_or_none
  AND declared_references ARE named_or_none
  AND files_read_before_decision ARE explicit
  AND why_each_file_was_loaded IS explicit
  AND ship_candidate IS explicit
  AND risk_level IS explicit
  AND verification_status IS explicit
  AND evidence_freshness_status IS fresh
  AND evidence_timeframe IS explicit
  AND verification_time IS explicit
  AND cheapest_safe_path_chosen IS explicit
  AND chosen_rollout_shape IS explicit
  AND rollback_owner IS explicit
  AND rollback_trigger IS explicit_when_relevant
  AND monitoring_owner IS explicit
  AND open_risk_profile IS explicit
  AND evidence_source IS explicit
  AND uncertainty_label IS explicit
  AND evidence_confidence IS explicit
  AND review_release_consistency_status IS explicit
  AND next_signal_review_time IS explicit_when_shipping_or_monitoring
  AND threshold_trigger IS measurable_and_explicit_when_shipping_or_monitoring
  AND threshold_action IS explicit_and_trigger_bound_when_shipping_or_monitoring
  AND signal_threshold_matrix_is_explicit_when_shipping_or_monitoring_depends_on_runtime_signals
  AND sustainability_materiality IS explicit
  AND sustainability_decision_matrix_is_explicit_when_operational_sustainability_is_plausibly_material
  AND sustainability_decision_class IS explicit_when_sustainability_note_is_material
  AND sustainability_decision_or_mitigation IS explicit_when_sustainability_note_is_material
  AND first_action IS explicit

FAIL IF
  declared_assets ARE missing
  OR files_actually_used ARE missing
  OR ship_candidate IS missing
  OR verification_status IS implicit
  OR evidence_freshness_status IS stale_or_unknown
  OR evidence_timeframe IS missing
  OR verification_time IS missing
  OR chosen_rollout_shape IS missing
  OR rollback_owner IS missing
  OR rollback_trigger IS missing_when_relevant
  OR monitoring_owner IS missing
  OR open_risk_profile IS implicit
  OR evidence_source IS missing
  OR uncertainty_label IS implicit
  OR evidence_confidence IS implicit
  OR review_release_consistency_status IS missing_or_mismatched
  OR threshold_trigger IS missing_or_generic_when_shipping_or_monitoring
  OR threshold_action IS missing_or_unbound_when_shipping_or_monitoring
  OR signal_threshold_matrix_is_missing_when_shipping_or_monitoring_depends_on_runtime_signals
  OR sustainability_materiality IS implicit
  OR sustainability_decision_matrix_is_missing_when_operational_sustainability_is_plausibly_material
  OR sustainability_decision_class IS missing_when_sustainability_note_is_material
  OR sustainability_decision_or_mitigation IS missing_when_sustainability_note_is_material
  OR next_update_time IS missing WHEN current_mode = incident_response

## Support

- declared assets:
- declared references:
- files read before decision:
- why each file was loaded:
- files actually used:

## Candidate

- ship candidate:
- worktree or workspace path:
- change type:
- risk level:
- current mode:
- release owner:
- environment:
- rollout shape:
- rollout window:
- branch disposition option:
- base branch or merge target:

Candidate.worktree_or_workspace_path := current isolated workspace or execution path
Candidate.branch_disposition_option := merge_locally OR create_pr OR keep_branch_as_is OR discard_with_confirmation
Candidate.base_branch_or_merge_target := named merge target or review target

## Evidence

- verification status:
- evidence freshness status:
- evidence timeframe:
- verification time:
- unresolved defects:
- operational readiness:
- cheapest safe path chosen:
- chosen rollout shape:
- backfill, replay, or cutover proof:
- rollback owner:
- rollback method:
- rollback trigger:
- monitoring owner:
- security/privacy review:
- severity or incident state:
- open risk profile:
- evidence source:
- uncertainty label:
- evidence confidence:
- review and release consistency status:
- sustainability note when operationally material:
- sustainability materiality:
- sustainability decision matrix reviewed:
- sustainability decision class:
- sustainability decision or mitigation:

## Decision

- ship:
- ship with follow-up:
- hold:
- do not ship:
- mitigate and monitor:
- rollback:

## Follow-Up

- first action:
- monitoring owner:
- support owner:
- rebuild or restart trigger:
- escalation path:
- next signal review time:
- threshold trigger:
- threshold action:
- signal threshold matrix reviewed:
- next update time:
