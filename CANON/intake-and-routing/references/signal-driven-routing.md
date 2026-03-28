# Signal-Driven Routing

```text
IF dominant_signal IN { research, persona, journey }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal IN { feedback, complaints, churn_reasons }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal IN { redesign, flow_shaping }:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal = visual_direction:
  ROUTE -> `visual-design`
ELSE IF dominant_signal = competitive_direction_change:
  ROUTE -> `product-and-ux`
ELSE IF dominant_signal IN { repo_wide_canon_revision, skill_system_absorption, external_principle_compilation, owner_boundary_rewrite }:
  ROUTE -> `skillsmith`
ELSE IF dominant_signal = cross_team_specification_packaging_after_direction_is_accepted:
  ROUTE -> `planning-and-scoping`
ELSE IF dominant_signal = oversized_mixed_owner_request:
  ROUTE -> `intake-and-routing` THEN choose(one_active_batch_and_park_the_rest)
ELSE:
  ROUTE -> narrower_non_product_skill

STOP("do not force product routing") IF runtime_severity OR security_exposure OR implementation_ownership dominates
```
