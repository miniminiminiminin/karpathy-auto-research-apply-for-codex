# principles.adactio Batch 2 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/architecture-and-design/**`
- owner 2: `CANON/planning-and-scoping/**`
- goal:
  - absorb modularity, maintainability, robustness, and irreducible-core principles into the correct owner
  - keep architecture focused on seam quality, dependency direction, and graceful failure
  - keep planning focused on minimum viable slice, bounded steps, and anti-drift discipline

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `architecture-and-design` owns seam decomposition, replaceability, dependency direction, maintainability pressure, robustness baseline, and reusable/open contract logic
- `planning-and-scoping` owns minimum viable slice, one active step, irreducible core, anti-redundancy, and exact proof sequencing
- no planning file turns into architecture theory
- no architecture file turns into task sequencing or execution choreography

FAIL IF
- architecture starts prescribing detailed task ordering that belongs in planning
- planning starts deciding module boundaries without an explicit architectural owner

### 2. Principle Fidelity

PASS IF
- Bert Bos maintainability becomes readability/manageable-size/changeability guidance
- Bert Bos modularity becomes meaningful chunking and low-redundancy seam guidance
- Bert Bos robustness becomes graceful degradation and essential-vs-separable dependency guidance
- GDS “do less” becomes irreducible-core and reuse-before-reinvent logic
- imported principles are distilled into repo-local operator rules, not quoted as doctrine

FAIL IF
- long-form prose is copied into skill files
- robustness is reduced to generic “add logs”
- do-less is reduced to “smaller is better” without decision criteria

### 3. Operator Usability

PASS IF
- architecture outputs now force an operator to justify module count, dependency direction, and failure handling
- planning outputs now force an operator to justify why the current slice is the minimum useful slice
- assets ask for concrete fields that would actually improve a handoff

FAIL IF
- the rules are inspirational but not checkable
- a later worker still has to guess where to draw the seam or stop the plan

### 4. Reviewability

PASS IF
- architecture review has explicit reasons to reject generic rollback/observability notes
- planning review has explicit reasons to reject drift, parallel active steps, and hidden future-proofing
- review templates can fail an item for weak proof or redundant decomposition

FAIL IF
- approval remains narrative-only
- there is no way to reject a plan or architecture note for being “technically true but operationally vague”

### 5. Catalog Safety

PASS IF
- no new top-level owner is introduced
- any new reference or asset strengthens a clear existing owner
- adjacent files become more complementary, not more duplicative

## Evaluation Questions For Reviewers

1. Did any principle land in the wrong owner?
2. Are maintainability and modularity now materially easier to apply in architecture decisions?
3. Is “do less” now strong enough to constrain planning instead of acting as a slogan?
4. Can these assets reject a bad seam or bad active step more reliably than before?
5. What principle families still remain deferred to later batches?

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- principle-fidelity issues
- operator-ambiguity issues
- deferred coverage still missing from this batch
