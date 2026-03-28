# Pseudocode Style Rules

```text
GOAL := make routing, process, checklists, assets, and references scan like executable decision logic

ROUTING_RULE :=
  IF trigger_matches THEN ROUTE -> owned_skill
  ELSE IF blocker_present THEN ASK_OR_STOP
  ELSE DEFER

PROCESS_RULE :=
  STEP_n := imperative action
  IF precondition_fails THEN STOP(reason)
  IF escalation_needed THEN ROUTE -> next_owner

CHECKLIST_RULE :=
  PASS IF condition_1 AND condition_2 AND condition_3
  FAIL IF condition_1 = FALSE OR condition_2 = FALSE
  NOT_APPLICABLE IF seam_does_not_match

ASSET_RULE :=
  KEEP(forms_and_checklists_legible) WHEN asset_shape_carries_operator_value
  IF default_path THEN START -> assets/<default>.md
  IF narrower_mode THEN SWITCH -> assets/<narrower>.md

REFERENCE_RULE :=
  COMPRESS(references) WHEN decision_logic_becomes_clearer_without_dropping_substance
  IF signal_or_risk_matches THEN READ -> references/<rulebook>.md
  ELSE SKIP

WORDING_RULES :=
  USE(IF, ELSE, THEN, STOP, ROUTE, PASS, FAIL, AND, OR, NOT)
  USE(symbols) IF they_reduce_ambiguity_more_than_they_reduce_readability
  PREFER(compact code_fence_or_assignment_style)
  KEEP(enumerated_lists) WHEN the_list_itself_carries_operator_guidance
  AVOID(narrative parapraphs_that_hide_decision_logic)
  AVOID(checklists_without_boolean_meaning)
  AVOID(symbol_density_that_hides_edge_cases_or_evidence_requirements)
  KEEP(one_line_of_plain_language_only_when_pseudocode_needs_context)
```
