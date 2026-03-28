# Visual Direction Brief

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_direction,
  why_each_file_was_loaded,
  files_actually_used
}

SLICE := {
  route_or_component,
  user_goal,
  user_need_evidence,
  expected_behavior_change,
  measurement_signal,
  current_product_or_brand_context,
  visual_goal,
  current_visual_failure_or_risk,
  owner_boundary_note,
  upstream_product_direction_reference
}

HIERARCHY := {
  primary_focus,
  primary_action_strategy,
  secondary_context,
  reading_order,
  composition_model,
  disclosure_or_density_model,
  responsive_shift_points,
  narrow_width_priority_rule,
  elements_that_must_keep_priority_across_widths
}

SYSTEM := {
  typography_strategy,
  color_strategy,
  spacing_rhythm,
  variation_budget,
  surface_and_elevation_style,
  imagery_or_illustration_policy,
  state_expression_strategy,
  essential_meaning_without_color_only,
  motion_or_emphasis_control_rules
}

GUARDRAILS := {
  avoid_list,
  generic_ui_failure_modes,
  accessibility_and_contrast_notes,
  implementation_survival_notes,
  comparable_experience_visual_notes,
  user_control_preservation,
  proof_or_review_expectation,
  environmental_impact_note_for_media_or_motion,
  principles_translated_into_rules
}

MAPPING := {
  principle_to_rule,
  rule_to_surface_or_component,
  rule_to_visual_evidence,
  rule_to_verification_step
}

APPROVAL_EVIDENCE := {
  author_role,
  approver_role,
  approval_mode := user_approval OR independent_review,
  approval_timestamp,
  artifacts_reviewed,
  states_reviewed,
  responsive_surfaces_reviewed,
  open_blockers := none_or_listed,
  disposition_rationale
}

DECISION := {
  approval_owner,
  approval_status,
  next_skill_or_owner
}

PASS IF
  SUPPORT.files_actually_used IS named
  AND HIERARCHY.primary_focus
  AND HIERARCHY.primary_action_strategy
  AND SYSTEM.typography_strategy
  AND SYSTEM.color_strategy
  AND SYSTEM.state_expression_strategy
  AND user_need_evidence
  AND expected_behavior_change
  AND GUARDRAILS.user_control_preservation
  AND MAPPING.principle_to_rule
  AND APPROVAL_EVIDENCE.approver_role

FAIL IF
  approval_status = approved AND APPROVAL_EVIDENCE.open_blockers != none
  OR approval_status = approved AND APPROVAL_EVIDENCE.approval_mode IS missing
  OR APPROVAL_EVIDENCE.approval_mode = independent_review AND APPROVAL_EVIDENCE.approver_role = APPROVAL_EVIDENCE.author_role
  OR principle_remains_adjective_only
  OR owner_boundary_note IS missing
  OR upstream_product_direction_reference IS missing_when_visualizing_service_or_flow_rules
  OR implementation_survival_notes_are_missing
```
