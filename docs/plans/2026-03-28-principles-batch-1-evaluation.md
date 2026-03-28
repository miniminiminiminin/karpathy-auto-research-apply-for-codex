# principles.adactio Batch 1 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/visual-design/**`
- owner 2: `CANON/product-and-ux/**`
- goal:
  - absorb responsive, inclusive, and service-design principles into the correct owner
  - prevent visual-design from swallowing product/service rules
  - make product-and-ux carry service continuity, expectation-setting, and comparable-experience rules explicitly

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `visual-design` only keeps principles that can be translated into hierarchy, composition, type, color, density, state, or responsive-surface rules
- `product-and-ux` owns purpose clarity, expectation-setting, no-dead-end flow, assistance path, choice/control, and comparable task completion
- no file implies that visual polish can substitute for product clarity

FAIL IF
- service design language is mostly added to `visual-design`
- visual surface rules are mostly added to `product-and-ux`
- routing between the two owners becomes blurrier than before

### 2. Principle Fidelity

PASS IF
- responsive principles become adaptability-first rules instead of device-specific slogans
- inclusive-design principles become comparable-experience and control rules, not generic accessibility virtue language
- service-design principles become flow and outcome rules, not broad manifesto text
- imported source language is distilled into repo-local operator guidance

FAIL IF
- source prose is copied with minimal translation
- biography, nostalgia, or source-specific theater is treated as reusable guidance
- “minimalism”, “taste”, or “good UX” remains an undefined adjective

### 3. Operator Usability

PASS IF
- the edited skills tell an operator what to read, what to decide, what to record, and when to stop
- the assets ask for concrete fields that can be filled during real work
- references are specific enough to guide future direction work without reopening source interpretation from scratch

FAIL IF
- the new guidance is inspiring but not actionable
- new fields are too vague to fill consistently
- the operator still has to infer which owner should absorb a principle

### 4. Approval And Reviewability

PASS IF
- visual assets can be reviewed against explicit evidence for states and responsive surfaces
- product assets can be reviewed for clarity, dead ends, assistance paths, and comparable experience
- the batch introduces explicit review hooks rather than “trust the author” language

FAIL IF
- approval stays narrative-only
- relevant states or contexts remain optional
- no measurable difference exists between “before” and “after” review quality

### 5. Catalog Safety

PASS IF
- no new top-level skill is added
- any new reference or asset has a clear owner and clear reason to exist
- adjacent files do not become more duplicative

FAIL IF
- the batch creates overlapping references without sharper ownership
- the work depends on hidden context outside the edited packages

## Evaluation Questions For Reviewers

1. Does each edited file make the owner boundary sharper or blurrier?
2. Which imported principle families are now materially easier to execute?
3. Which principles are still missing or mis-owned?
4. Where does the wording remain too abstract for a real operator?
5. Does any file still leak long-form source interpretation work into future runs?

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- principle-fidelity issues
- missing coverage or overreach
- recommended follow-up batch
