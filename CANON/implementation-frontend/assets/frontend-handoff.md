# Frontend Handoff

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_coding,
  why_each_file_was_loaded,
  files_actually_used
}

CHANGE := {
  name,
  sender_role,
  receiver_role,
  owner,
  parent_plan,
  impact_scope,
  route_or_component,
  primary_seam_count,
  adjacent_surface_changes,
  reroute_trigger_when_change_radius_grew
}

FILES := {
  changed_files,
  adjacent_files_untouched
}

BEHAVIOR := {
  user_facing_change,
  critical_states,
  accessibility_impact,
  pre_delivery_checklist_outcome_when_relevant,
  comparable_experience_notes,
  keyboard_and_focus_notes,
  responsive_notes,
  component_responsibility
}

DELIVERY := {
  work_completed,
  assumptions,
  split_trigger_waiver_id,
  split_trigger_waiver_owner,
  split_trigger_waiver_expiry_or_recheck_trigger,
  required_follow_up,
  receiving_owner
}

VERIFICATION := {
  command,
  exact_output_or_precise_summary,
  result,
  interactive_affordance_check_when_relevant,
  contrast_verification_note_when_relevant,
  performance_note,
  verification_owner
}

CLOSE := {
  risks,
  reusable_rule,
  stop_condition_reached
}

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_coding
  AND SUPPORT.why_each_file_was_loaded
  AND CHANGE.route_or_component
  AND CHANGE.primary_seam_count
  AND BEHAVIOR.critical_states
  AND VERIFICATION.command
  AND DELIVERY.receiving_owner

FAIL IF
  SUPPORT.files_actually_used IS missing
  OR CHANGE.primary_seam_count IS implicit
  OR CHANGE.primary_seam_count > 1 AND CHANGE.reroute_trigger_when_change_radius_grew IS missing
  OR DELIVERY.split_trigger_waiver_id IS present AND DELIVERY.split_trigger_waiver_owner IS missing
  OR DELIVERY.split_trigger_waiver_id IS present AND DELIVERY.split_trigger_waiver_expiry_or_recheck_trigger IS missing
  OR BEHAVIOR.accessibility_impact IS implicit
  OR VERIFICATION.result IS implicit
```
