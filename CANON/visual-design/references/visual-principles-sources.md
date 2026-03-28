# Visual Principles Sources

Use these principle families to ground visual direction in rules instead of taste shorthand.

```text
SOURCE_SET := {
  primary_sources := [
    CANON/product-and-ux/references/design-system-methodology.md,
    CANON/product-and-ux/references/screen-layout-visual-and-mobile-patterns.md,
    CANON/product-and-ux/references/inclusive-visual-review.md,
    resources/principles.adactio.com-markdown/software/inclusive-design--inclusive-design-principles.md
  ],
  scoped_sources := [
    resources/principles.adactio.com-markdown/personal/paul-robert-lloyd--responsive-principles.md,
    resources/principles.adactio.com-markdown/personal/heydon-pickering--what-the-heck-is-inclusive-design.md,
    resources/principles.adactio.com-markdown/organisational/government-digital-service--accessibility-principles.md,
    resources/principles.adactio.com-markdown/personal/bruce-tognazzini--principles-of-interaction-design.md,
    resources/principles.adactio.com-markdown/personal/joshua-porter--principles-of-user-interface-design.md,
    resources/principles.adactio.com-markdown/personal/lou-downe--15-principles-of-good-service-design.md,
    resources/principles.adactio.com-markdown/software/front-end-development--nine-principles-design-implementation.md,
    resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md,
    resources/principles.adactio.com-markdown/organisational/national-health-service--design-principles.md
  ],
  downgraded_or_conditional_sources := [
    resources/principles.adactio.com-markdown/format/wcag-2-0--intro.md,
    resources/principles.adactio.com-markdown/personal/sandi-wassmer--the-ten-principles-of-inclusive-web-design.md,
    resources/principles.adactio.com-markdown/organisational/google--ux.md,
    resources/principles.adactio.com-markdown/organisational/british-airways--digitaldesignprinciples-v2-2.md,
    resources/principles.adactio.com-markdown/software/harmony-by-intuit--design-principles.md,
    resources/principles.adactio.com-markdown/organisational/opower--opower-product-design-principles.md,
    resources/principles.adactio.com-markdown/organisational/calm-technology-institute--calm-tech-principles.md,
    resources/principles.adactio.com-markdown/organisational/design-patterns-for-mental-health--be-clear.md,
    resources/principles.adactio.com-markdown/organisational/design-patterns-for-mental-health--give-control.md,
    resources/principles.adactio.com-markdown/organisational/design-patterns-for-mental-health--create-a-safe-space.md,
    resources/principles.adactio.com-markdown/organisational/design-patterns-for-mental-health--make-it-human.md
  ]
}

DISTILLATION_RULE := PASS IF
  principle_sources_are_turned_into_concrete_visual_rules
  AND vague_adjectives_are_rewritten_as_hierarchy_color_type_density_or_state_constraints
  AND responsive_adaptability_starts_from_content_and_task_not_device_assumptions
  AND inclusive_design_is_treated_as_a_visual_quality_bar_not_a_post_hoc_check
  AND less_but_better_means_removing_competing_signals_before_adding_polish
  AND non_visual_service_principles_are_routed_back_to_product_and_ux

DO_NOT
  treat_principle_sources_as_style_dogma
  quote_authorities_without_translating_them_into_screen_rules
  import_mid_century_or_minimalist_taste_as_a_default_visual_answer
  OR let_service_clarity_or_assistance_path_logic_hide_inside_visual_language
```

## Source Quality

- `CANON/product-and-ux/references/design-system-methodology.md`: strong local source for tokens, hierarchy, and implementation survival.
- `CANON/product-and-ux/references/screen-layout-visual-and-mobile-patterns.md`: strong local source for layout, scanability, and mobile composition.
- `CANON/product-and-ux/references/inclusive-visual-review.md`: strong local source for visual dignity, specificity, and review risks.
- `resources/principles.adactio.com-markdown/software/inclusive-design--inclusive-design-principles.md`: strong external principle source for comparable experience, user control, and content prioritization.
- `resources/principles.adactio.com-markdown/personal/paul-robert-lloyd--responsive-principles.md`: supporting source for adaptability-first framing only.
- `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md` and `.../national-health-service--design-principles.md`: strong approval-gate sources for practical clarity and public-service discipline.
- `resources/principles.adactio.com-markdown/personal/bruce-tognazzini--principles-of-interaction-design.md`, `.../joshua-porter--principles-of-user-interface-design.md`, and `.../lou-downe--15-principles-of-good-service-design.md`: useful critique heuristics; translate before use.
- `resources/principles.adactio.com-markdown/organisational/british-airways--digitaldesignprinciples-v2-2.md`: unusable in current scrape; do not rely on it.

## Principle To Rule Mapping

- From Paul Robert Lloyd: start from the point of greatest adaptability, so visual direction should survive unknown widths and contexts before polish.
- From Inclusive Design Principles: comparable experience becomes visible state clarity, content priority, control over motion or emphasis, and resilient narrow-width behavior.

## Owner Boundary

- keep in `visual-design`: hierarchy, composition, typography, color, density, state clarity, and responsive-surface behavior
- route to `product-and-ux`: purpose clarity, expectation-setting, assistance paths, no-dead-end flow logic, and decision explanations
- route to `implementation-frontend`: ARIA, keyboard, announcement, and DOM/source-order proof requirements

```text
RULE_MAP := {
  adaptability_first -> {
    concrete_rule := "name narrow_width_behavior before wide_canvas_polish",
    visual_evidence := "breakpoint_matrix",
    verification_step := "review narrow_width_priority_preservation"
  },
  comparable_experience -> {
    concrete_rule := "do not let key state meaning live only in decorative visual treatment",
    visual_evidence := "state_matrix_with_non_color_signals",
    verification_step := "review error_loading_blocked_states"
  },
  situation_and_control -> {
    concrete_rule := "motion emphasis and dense layout choices must degrade safely under narrow width and reduced-attention conditions",
    visual_evidence := "breakpoint_matrix plus motion_or_emphasis_control_rules",
    verification_step := "review narrow_width_and_reduced_emphasis_survival"
  },
  consistency -> {
    concrete_rule := "repeat type_color_and_surface_roles across similar surfaces",
    visual_evidence := "named token roles and repeated surface rules",
    verification_step := "compare two similar surfaces for role drift"
  },
  interaction_clarity -> {
    concrete_rule := "one primary action per surface and visible next-step or recovery path for each relevant state",
    visual_evidence := "primary_action_per_state and next_step_or_recovery_visibility_per_state",
    verification_step := "review action competition and recovery visibility"
  },
  user_control -> {
    concrete_rule := "do not suppress zoom motion scaling or interruption controls when the platform offers them",
    visual_evidence := "user_controls_preserved and fallback rules",
    verification_step := "review control suppression and alternative path availability"
  },
  calm_and_trustworthy_feedback -> {
    concrete_rule := "use low-interruption status cues first and escalate only with real severity",
    visual_evidence := "status signaling and trust cues per state",
    verification_step := "review status accuracy and escalation logic"
  },
  prioritise_content -> {
    concrete_rule := "make the primary task visually dominant before supporting context gains decoration",
    visual_evidence := "named primary_focus and de-emphasized secondary_context",
    verification_step := "three_second_focus check"
  }
}
```
