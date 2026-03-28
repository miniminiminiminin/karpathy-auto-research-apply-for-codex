# principles.adactio Batch 3 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/implementation-frontend/**`
- owner 2: `CANON/quality-and-review/**`
- goal:
  - absorb responsive implementation, comparable experience, user control, and state degradation principles into implementation and review
  - keep implementation focused on translating approved direction into behavior and proof
  - keep review focused on evidence quality, acceptance discipline, and comparable-experience QA

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `implementation-frontend` owns seam-level translation into DOM structure, state coverage, keyboard/focus behavior, responsive behavior, and implementation proof
- `quality-and-review` owns independent acceptance, criterion-by-criterion review, evidence freshness, and rejection of weak comparable-experience claims
- implementation does not become product/service policy
- review does not become implementation guidance except when findings require named remediation

FAIL IF
- implementation files start deciding service policy or product trade-offs
- review files start prescribing UI architecture or coding patterns as if they owned implementation

### 2. Principle Fidelity

PASS IF
- responsive principles become content-first layout and reflow proof requirements
- inclusive-design principles become comparable task completion, user control, and non-color-only meaning checks
- Porter-style UI principles become clarity, primary action, attention, and next-step checks at implementation/review level
- GDS “this is for everyone” and “understand context” become explicit proof expectations, not slogans

FAIL IF
- source language is pasted without implementation or review translation
- “accessible” remains a generic adjective with no proof hook
- responsive coverage is reduced to breakpoint cosmetics

### 3. Operator Usability

PASS IF
- a frontend implementer can tell what states, checks, and proof are mandatory
- a reviewer can reject a seam for missing comparable experience, missing control, or missing responsive survival evidence
- assets ask for fields that can actually be filled during real delivery

FAIL IF
- the new rules sound right but are not operational
- proof depth is left to taste

### 4. Reviewability

PASS IF
- review and QA assets can fail a change for stale/partial evidence
- comparable experience is reviewable as a quality bar, not just a design aspiration
- UI review can reject motion, focus, or state meaning regressions even when the happy path passes

FAIL IF
- completion can still be claimed with weak evidence
- review still trusts implementation narration over observed behavior

### 5. Catalog Safety

PASS IF
- no new top-level owner is added
- any new rule strengthens an existing file rather than creating overlap
- implementation and review stay complementary

## Evaluation Questions For Reviewers

1. Did any principle land in the wrong owner?
2. Can implementation now prove responsive survival and comparable experience more concretely than before?
3. Can review now reject weak UI evidence more reliably than before?
4. Which principle families are still deferred to later owners like release or backend?

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- principle-fidelity issues
- operator-ambiguity issues
- deferred coverage still missing from this batch
