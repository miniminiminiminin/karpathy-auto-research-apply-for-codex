# Design Note

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_decision,
  why_each_file_was_loaded,
  files_actually_used
}

TARGET := {
  seam,
  decision_owner,
  affected_roles,
  constraints,
  current_state_evidence,
  current_risks_or_bottlenecks,
  target_state_framing,
  module_count_rationale,
  scaffold_shape,
  extension_points,
  split_trigger_for_large_or_multi_responsibility_units,
  split_trigger_waiver_id,
  split_trigger_waiver_owner,
  split_trigger_waiver_expiry_or_recheck_trigger,
  redundancy_risk,
  dependency_direction,
  workflow_graph_or_node_types,
  runtime_surface,
  control_plane,
  execution_plane,
  prompt_policy_plane,
  request_or_session_owner,
  workspace_artifact_boundary
}

ALTERNATIVES := {
  option_a,
  option_b,
  option_c,
  recommended_choice,
  why_losing_options_lost_now
}

TRADE_OFFS := {
  replaceability,
  maintainability_after_time,
  hidden_coupling_risk,
  redundancy_vs_reuse,
  implementation_cost,
  verification_impact,
  bridge_vs_direct_call,
  provider_vs_controller_split,
  service_vs_tool_split,
  responsibility_distribution,
  large_file_or_god_object_risk
}

MIGRATION := {
  first_increment,
  coexistence_or_cutover_plan,
  rollback_trigger,
  rollback_plan,
  rollback_owner
}

OBSERVABILITY := {
  seam_signals,
  error_categories,
  graceful_failure_modes,
  essential_dependencies_that_must_not_split,
  nonessential_dependencies_that_may_split,
  alert_owner,
  acceptance_metrics
}

ACCEPTANCE := {
  chosen_structure,
  entrypoint_and_dependency_direction,
  migration_or_compatibility_assumptions,
  streaming_and_cancel_contract,
  acceptance_conditions,
  recommended_next_owner,
  next_skill
}

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_decision
  AND SUPPORT.why_each_file_was_loaded
  AND TARGET.seam
  AND TARGET.current_state_evidence
  AND TARGET.module_count_rationale
  AND TARGET.scaffold_shape
  AND TARGET.split_trigger_for_large_or_multi_responsibility_units
  AND TARGET.dependency_direction
  AND ALTERNATIVES.recommended_choice
  AND ALTERNATIVES.why_losing_options_lost_now
  AND MIGRATION.rollback_trigger
  AND MIGRATION.rollback_owner
  AND OBSERVABILITY.seam_signals
  AND OBSERVABILITY.alert_owner
  AND ACCEPTANCE.recommended_next_owner
  AND ACCEPTANCE.next_skill

FAIL IF
  SUPPORT.files_actually_used IS missing
  OR TARGET.current_state_evidence IS generic
  OR TARGET.module_count_rationale IS implicit
  OR TARGET.scaffold_shape IS implicit
  OR TARGET.split_trigger_for_large_or_multi_responsibility_units IS missing
  OR TARGET.split_trigger_waiver_id IS present AND TARGET.split_trigger_waiver_owner IS missing
  OR TARGET.split_trigger_waiver_id IS present AND TARGET.split_trigger_waiver_expiry_or_recheck_trigger IS missing
  OR TARGET.dependency_direction IS implicit
  OR TRADE_OFFS.large_file_or_god_object_risk IS missing
  OR MIGRATION.rollback_plan IS generic
  OR OBSERVABILITY.graceful_failure_modes IS missing
  OR OBSERVABILITY.graceful_failure_modes IS generic
  OR OBSERVABILITY.acceptance_metrics IS missing
```
