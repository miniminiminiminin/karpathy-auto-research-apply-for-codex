# Slice Record

```text
SLICE := {
  name,
  fan_out_trigger,
  reason_for_slice,
  why_single_operator_is_insufficient,
  execution_pattern,
  owner_role,
  receiver,
  receiver_identity,
  required_skills
}

NO_FAN_OUT := {
  trigger,
  why_single_operator_is_sufficient,
  chosen_single_owner,
  next_skill
}

BOUNDARIES := {
  scope,
  owned_files_or_concerns,
  shared_read_seams,
  forbidden_files_or_concerns,
  dependencies,
  proof_expected,
  handoff_target
}

SUPPORT_CONTRACT := {
  local_agents_to_use,
  local_assets_to_use,
  local_references_to_use,
  local_scripts_to_use,
  files_read_before_dispatch,
  why_each_file_was_loaded
}

HANDOFF_MINIMUM := {
  declared_identity,
  summary,
  next_action,
  risks,
  open_questions,
  actual_skills_used,
  actual_local_support_used,
  deviations_from_dispatch
}

STATUS := {
  state,
  dispatched,
  in_progress,
  blocked,
  accepted
}

PASS IF
  SLICE.name
  AND SLICE.fan_out_trigger
  AND SLICE.required_skills
  AND SLICE.receiver_identity
  AND SLICE.why_single_operator_is_insufficient
  AND BOUNDARIES.owned_files_or_concerns
  AND BOUNDARIES.proof_expected
  AND SUPPORT_CONTRACT.local_assets_to_use
  AND SUPPORT_CONTRACT.files_read_before_dispatch
  AND SUPPORT_CONTRACT.why_each_file_was_loaded

FAIL IF
  BOUNDARIES.forbidden_files_or_concerns IS missing_when_overlap_risk_exists
  OR HANDOFF_MINIMUM.declared_identity IS omitted
  OR HANDOFF_MINIMUM.actual_local_support_used IS omitted
  OR HANDOFF_MINIMUM.deviations_from_dispatch IS hidden
  OR explicit_orchestration_consideration_exists AND NO_FAN_OUT.trigger IS missing_when_dispatch_did_not_happen
  OR explicit_orchestration_consideration_exists AND NO_FAN_OUT.why_single_operator_is_sufficient IS missing_when_dispatch_did_not_happen
  OR explicit_orchestration_consideration_exists AND NO_FAN_OUT.chosen_single_owner IS missing_when_dispatch_did_not_happen
  OR explicit_orchestration_consideration_exists AND NO_FAN_OUT.next_skill IS missing_when_dispatch_did_not_happen
```
