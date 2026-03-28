# principles.adactio.com Family Map

## Purpose

Turn the source library under `resources/principles.adactio.com-markdown/**` into durable principle families with one primary CANON owner each.

## Source Summary

- captured library: `resources/principles.adactio.com/README.md`
- structure inventory: `resources/principles.adactio.com/indexes/site-map.md`
- current target set: 58 entries, 97 markdown files, 5 categories
- current goal: compile reusable rules into existing CANON owners without adding unnecessary top-level skills

## Source Bands

### Band 1: Responsive And Context

- representative sources:
  - `resources/principles.adactio.com-markdown/personal/paul-robert-lloyd--responsive-principles.md`
  - `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md`
  - `resources/principles.adactio.com-markdown/software/android--principles.md`
- durable takeaways:
  - start from adaptable content and tasks
  - design for varied contexts, not one ideal surface
  - use systems that can be reasoned with
- primary owner:
  - `CANON/visual-design/**` for visual adaptability rules
- secondary consumers:
  - `CANON/product-and-ux/**`
  - `CANON/implementation-frontend/**`

### Band 2: Inclusive And Comparable Experience

- representative sources:
  - `resources/principles.adactio.com-markdown/software/inclusive-design--inclusive-design-principles.md`
  - `resources/principles.adactio.com-markdown/personal/heydon-pickering--what-the-heck-is-inclusive-design.md`
  - `resources/principles.adactio.com-markdown/personal/sandi-wassmer--the-ten-principles-of-inclusive-web-design.md`
- durable takeaways:
  - comparable experience beats accessibility bolt-ons
  - give control, offer choice, prioritise content
  - handle errors and change respectfully
- primary owner:
  - `CANON/product-and-ux/**`
- secondary consumers:
  - `CANON/visual-design/**`
  - `CANON/implementation-frontend/**`
  - `CANON/quality-and-review/**`

### Band 3: Service Outcome And Wayfinding

- representative sources:
  - `resources/principles.adactio.com-markdown/personal/lou-downe--15-principles-of-good-service-design.md`
  - `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md`
  - `resources/principles.adactio.com-markdown/organisational/national-health-service--design-principles.md`
- durable takeaways:
  - users should complete the outcome they came to complete
  - purpose, expectations, and next steps must be explicit
  - no dead ends; assistance paths must exist
- primary owner:
  - `CANON/product-and-ux/**`
- secondary consumers:
  - `CANON/intake-and-routing/**`
  - `CANON/quality-and-review/**`
  - `CANON/release-and-operations/**`

### Band 4: Simplicity, Clarity, And Irreducible Core

- representative sources:
  - `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md`
  - `resources/principles.adactio.com-markdown/personal/joshua-porter--principles-of-user-interface-design.md`
  - `resources/principles.adactio.com-markdown/personal/tim-berners-lee--principles.md`
- durable takeaways:
  - do less
  - do the hard work to make it simple
  - reduce to the irreducible core before adding mechanism
- primary owner:
  - `CANON/planning-and-scoping/**`
- secondary consumers:
  - `CANON/product-and-ux/**`
  - `CANON/architecture-and-design/**`
  - `CANON/implementation-backend/**`

### Band 5: Modularity, Maintainability, And Reuse

- representative sources:
  - `resources/principles.adactio.com-markdown/personal/bert-bos--maintainability.md`
  - `resources/principles.adactio.com-markdown/personal/bert-bos--modularity.md`
  - `resources/principles.adactio.com-markdown/personal/tim-berners-lee--designissues.md`
- durable takeaways:
  - separate concerns so parts can evolve independently
  - prefer reuse over redundant reinvention
  - keep systems reasoned-about and composable
- primary owner:
  - `CANON/architecture-and-design/**`
- secondary consumers:
  - `CANON/implementation-backend/**`
  - `CANON/implementation-frontend/**`
  - `CANON/planning-and-scoping/**`

### Band 6: Robustness, Compatibility, And Graceful Failure

- representative sources:
  - `resources/principles.adactio.com-markdown/personal/bert-bos--robustness.md`
  - `resources/principles.adactio.com-markdown/personal/bert-bos--compatibility.md`
  - `resources/principles.adactio.com-markdown/personal/bert-bos--interoperability.md`
- durable takeaways:
  - degraded conditions are normal design inputs
  - robust systems preserve meaning and continuity under failure
  - compatibility and interoperability are strategic, not cosmetic
- primary owner:
  - `CANON/architecture-and-design/**`
- secondary consumers:
  - `CANON/implementation-backend/**`
  - `CANON/release-and-operations/**`
  - `CANON/quality-and-review/**`

### Band 7: Consistency, Hierarchy, And Visual Restraint

- representative sources:
  - `resources/principles.adactio.com-markdown/personal/joshua-porter--principles-of-user-interface-design.md`
  - `resources/principles.adactio.com-markdown/personal/massimo-vignelli--canon.md`
  - `resources/principles.adactio.com-markdown/personal/dieter-rams--dieter-rams.md`
- durable takeaways:
  - strong hierarchy clarifies use
  - consistency should aid understanding, not flatten every surface
  - visual restraint means removing competing signals before adding polish
- primary owner:
  - `CANON/visual-design/**`
- secondary consumers:
  - `CANON/product-and-ux/**`
  - `CANON/implementation-frontend/**`
  - `CANON/quality-and-review/**`
- caution:
  - do not import biography or aesthetic mythology; keep only durable screen-level rules

### Band 8: Data, Iteration, And Open Improvement

- representative sources:
  - `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md`
  - `resources/principles.adactio.com-markdown/organisational/ethical-web-principles--ethical-web-principles.md`
  - `resources/principles.adactio.com-markdown/organisational/u-s-digital-services--playbook.md`
- durable takeaways:
  - design with data
  - iterate in public where possible
  - share patterns, evidence, and failures to raise the bar
- primary owner:
  - `CANON/quality-and-review/**`
- secondary consumers:
  - `CANON/planning-and-scoping/**`
  - `CANON/release-and-operations/**`
  - `CANON/skillsmith/**`

### Band 9: Implementation Translation And Open-Web Constraints

- representative sources:
  - `resources/principles.adactio.com-markdown/format/html5--html-design-principles.md`
  - `resources/principles.adactio.com-markdown/format/microformats--start-simple.md`
  - `resources/principles.adactio.com-markdown/software/front-end-development--nine-principles-design-implementation.md`
- durable takeaways:
  - start simple and preserve extensibility
  - prefer human- and machine-usable structures
  - keep implementation faithful to user-facing intent
- primary owner:
  - `CANON/implementation-frontend/**`
- secondary consumers:
  - `CANON/implementation-backend/**`
  - `CANON/architecture-and-design/**`

### Band 10: Operations, Longevity, And Sustainability

- representative sources:
  - `resources/principles.adactio.com-markdown/organisational/government-digital-service--government-design-principles.md`
  - `resources/principles.adactio.com-markdown/personal/dieter-rams--dieter-rams.md`
  - `resources/principles.adactio.com-markdown/personal/bert-bos--longevity.md`
- durable takeaways:
  - long-lived systems should stay maintainable and understandable
  - operational choices should favor durable usefulness over short-term theater
  - sustainability matters when it changes system or release decisions
- primary owner:
  - `CANON/release-and-operations/**`
- secondary consumers:
  - `CANON/architecture-and-design/**`
  - `CANON/implementation-backend/**`

## Principle Families

1. User-needs-first outcomes
2. Comparable experience
3. Adaptability to context
4. Simplicity through hard work
5. Consistency without blind uniformity
6. User control and meaningful choice
7. Content priority and wayfinding
8. Modularity and replaceable seams
9. Maintainability and longevity
10. Robustness and graceful degradation
11. Interoperability and openness
12. Evidence-driven iteration
13. Minimal viable scope
14. Cross-channel continuity
15. Sustainability when operationally material

## Recommended Batch Order

1. `CANON/skillsmith/**` ledger and dispatch contract
2. `CANON/visual-design/**` responsive and hierarchy families
3. `CANON/product-and-ux/**` inclusive, service, and wayfinding families
4. `CANON/architecture-and-design/**` modularity and robustness families
5. `CANON/planning-and-scoping/**` simplicity and bounded-slice families
6. `CANON/implementation-frontend/**` translation and responsive implementation families
7. `CANON/implementation-backend/**` maintainability and reliability families
8. `CANON/quality-and-review/**` evidence and comparable-experience review families
9. `CANON/release-and-operations/**` runtime continuity and sustainability families
10. `CANON/intake-and-routing/**` routing clarity for future absorption work

## Explicit Deferrals

- low-signal biography and historical context
- source-specific examples that do not survive framework or era change
- principles that are mostly duplicate wording until the primary owner batch lands
- layout-sensitive items that need original-page or image review before durable translation
