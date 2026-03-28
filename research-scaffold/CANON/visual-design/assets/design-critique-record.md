# Design Critique Record

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_review,
  why_each_file_was_loaded,
  files_actually_used
}

INPUT := {
  slice,
  intended_visual_goal,
  current_artifact,
  review_scope
}

FINDINGS := {
  hierarchy_failures,
  tone_or_brand_failures,
  typography_failures,
  color_and_contrast_failures,
  spacing_or_density_failures,
  state_expression_failures,
  responsive_failures,
  generic_ui_signals
}

REPAIR := {
  keep,
  remove,
  strengthen,
  system_rule_needed,
  implementation_warning,
  state_or_breakpoint_matrix_gaps
}

EVIDENCE := {
  author_role,
  reviewer_role,
  review_mode := user_approval OR independent_review,
  review_timestamp,
  artifacts_reviewed,
  states_reviewed,
  responsive_surfaces_reviewed,
  blockers_remaining
}

DECISION := {
  disposition := approve OR revise OR reject,
  approval_owner,
  disposition_rationale,
  next_owner_or_skill
}

FAIL IF
  EVIDENCE.reviewer_role IS missing
  OR EVIDENCE.artifacts_reviewed IS missing
  OR EVIDENCE.review_mode = independent_review AND EVIDENCE.reviewer_role = EVIDENCE.author_role
  OR DECISION.disposition = approve AND EVIDENCE.blockers_remaining != none
```
