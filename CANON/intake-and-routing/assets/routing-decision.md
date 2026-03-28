# Routing Decision

```text
SUPPORT := {
  assets_declared_before_execution,
  references_declared_before_execution,
  files_read_before_routing,
  why_each_file_was_loaded,
  support_files_actually_used
}

DECISION := {
  request,
  intake_mode,
  request_scale,
  decomposition_seam,
  active_batch_now,
  parked_follow_ups,
  considered_skills,
  recommended_skill,
  route_type,
  rationale,
  alternate_skills_considered,
  rejected_because,
  route_confidence,
  material_ambiguity,
  freshness_status,
  revalidation_reason,
  one_focused_clarification_question,
  blocked_actions_before_routing
}

REQUEST_SCALE_RULE :=
  single_owner_single_batch -> one_owner_one_active_batch_now
  single_owner_multi_batch -> one_owner_now_with_parked_follow_ups
  mixed_owner_multi_batch -> one_active_batch_now_and_named_owners_for_parked_follow_ups

BOUNDARY := {
  in_scope_now,
  not_in_scope_now,
  approval_needed,
  verification_expectation,
  severity
}

OWNERS := {
  decision_owner,
  next_owner,
  escalation_owner,
  informed_stakeholders
}

PASS IF
  SUPPORT.assets_declared_before_execution IS named_or_none
  AND SUPPORT.references_declared_before_execution IS named_or_none
  AND SUPPORT.files_read_before_routing
  AND SUPPORT.why_each_file_was_loaded
  AND DECISION.request_scale
  AND DECISION.considered_skills
  AND DECISION.recommended_skill
  AND DECISION.rationale
  AND DECISION.freshness_status
  AND BOUNDARY.in_scope_now
  AND BOUNDARY.not_in_scope_now
  AND OWNERS.next_owner

FAIL IF
  DECISION.rejected_because IS missing
  OR DECISION.active_batch_now IS missing_when_request_is_oversized
  OR DECISION.parked_follow_ups IS missing_when_request_spans_multiple_batches
  OR DECISION.freshness_status IS stale_or_unknown AND DECISION.revalidation_reason IS missing
  OR DECISION.blocked_actions_before_routing IS missing
  OR SUPPORT.files_read_before_routing IS missing
  OR SUPPORT.support_files_actually_used IS missing
```
