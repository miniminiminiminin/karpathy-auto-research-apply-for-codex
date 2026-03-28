# Signal Translation Rules

```text
IF signal_is_research THEN
  separate(observation, interpretation)
  AND translate(observation -> decision_seam)

ELSE IF signal_is_feedback THEN
  tie(theme -> segment, journey_stage, likely_owner)
  AND translate(theme -> product_implication)

ELSE IF signal_is_competitive THEN
  prefer(differentiation AND customer_value)
  AND NOT parity_copying

ELSE IF signal_is_design_direction THEN
  define(option_set, component_priority, token_priority, review_criteria)

ELSE IF signal_is_service_or_principle_pack THEN
  translate(signal -> service_outcome, expectation_setting, no_dead_end_handling, assistance_path, comparable_experience_risk)

ELSE IF signal_is_cross_team_packaging THEN
  ROUTE -> planning-and-scoping

ELSE
  STOP("signal type is still ambiguous")

STOP IF
  evidence_is_stale_without_revalidation_trigger
  OR contradictory_signals_are_unresolved
  OR evidence_strength_is_too_weak_for_direction_claim

FAIL IF
  raw_quote_passes_through_unchanged
  OR visual_taste_becomes_direction
  OR service_manifesto_becomes_direction_without_flow_rules
  OR competitor_screenshot_becomes_strategy
```
