# Visual Design Skill Rubric

```text
SCORE_BANDS := {
  0 := missing_or_harmful,
  1 := weak_and_ambiguous,
  2 := usable_but_soft,
  3 := strong_and_actionable,
  4 := excellent_and_hard_to_misread
}

CRITERIA := {
  boundary_clarity := {
    question := "Can an operator tell when to use visual-design instead of product-and-ux or implementation-frontend?",
    target := 4
  },
  ownership_force := {
    question := "Does the package give visual direction real authority instead of treating it as optional polish?",
    target := 4
  },
  anti_generic_pressure := {
    question := "Does the package actively prevent bland default SaaS output rather than merely asking for quality?",
    target := 4
  },
  implementation_survival := {
    question := "Are the rules specific enough that implementation can preserve the direction without inventing it?",
    target := 4
  },
  critique_hardness := {
    question := "Can the review assets reject weak work with concrete reasons instead of adjective swapping?",
    target := 4
  },
  state_and_responsive_coverage := {
    question := "Does the package treat loading, empty, error, blocked, and narrow-width behavior as part of visual quality?",
    target := 3
  },
  principle_grounding := {
    question := "Are external and local principles translated into concrete rules instead of name-dropping sources?",
    target := 3
  },
  role_and_asset_utility := {
    question := "Would the declared roles and assets actually help a future operator do better work?",
    target := 3
  },
  output_contract_strength := {
    question := "Does the package force a usable approval-ready output instead of vague design notes?",
    target := 4
  }
}

PASS_IF
  no_criterion_scores_below_2
  AND at_least_five_criteria_score_at_or_above_target_minus_1
  AND boundary_clarity_scores_at_least_3
  AND ownership_force_scores_at_least_3
  AND anti_generic_pressure_scores_at_least_3
  AND output_contract_strength_scores_at_least_3

REVIEW_OUTPUT := {
  scorecard,
  strongest_parts,
  weakest_parts,
  top_3_fixes,
  disposition := keep OR revise OR rethink
}
```
