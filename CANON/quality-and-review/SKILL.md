---
name: quality-and-review
description: Use when a seam needs fresh proof, ordered review, acceptance, or handoff before anyone can call it done.
---

# Quality And Review

## Overview

Completion is an evidence decision.

**Core principle:** if proof, review scope, or handoff fidelity is weak, the work is not done.

Claiming work is complete without verification is dishonesty, not efficiency.

**Violating the letter of this rule is violating the spirit of this rule.**

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

<HARD-GATE>
Review order is fixed unless a narrower local rule says otherwise: spec fit first, code quality second, QA evidence third. Do not skip forward because the code "looks right."
</HARD-GATE>

<NON-NEGOTIABLE>
Every run must declare its exact local `assets/` and `references/` set before execution, read the required files before choosing review order, and record why each declared file was loaded.
Unnamed support files are out of contract and must not be relied on.
If no support files are needed, say `none` explicitly. Final outputs must report the declared set, the files actually read, and the files actually used.
</NON-NEGOTIABLE>

<NON-NEGOTIABLE>
Evidence beats narration. Fresh verification is required for completion claims, release confidence, and security claims.
</NON-NEGOTIABLE>

<LOOP-GATE>
review_loop := spec_fit THEN code_quality THEN qa_evidence.
implementation_report_is_not_acceptance_evidence.
</LOOP-GATE>

<VERIFICATION-GATE>
fresh_verification_before_completion_claims.
review_feedback_requires_technical_verification_before_implementation.
</VERIFICATION-GATE>

<OWNER-BOUNDARY>
Do not redesign the product or implementation from inside review.
Review owns acceptance, evidence sufficiency, and comparable-experience rejection logic; remediation design belongs to the implementation or product owner.
</OWNER-BOUNDARY>

<NON-NEGOTIABLE>
Do not approve code that hides multiple unrelated responsibilities in one class, one component, or one oversized file without a named irreducible reason and a recorded split decision.
</NON-NEGOTIABLE>

## The Iron Law

```text
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes.

```text
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed root cause investigation, you cannot propose fixes.

## When to Use

- someone claims work is done, fixed, accepted, or ready to ship
- proof exists but review order or evidence sufficiency is still unclear
- a handoff must become approve, revise, or block
- support evidence should be checked before engineering work widens

## Do Not Use

- intake or planning before implementation exists
- architecture work that still lacks a concrete design
- release approval once the work is already in the shipping lane

## Required Reads

```text
IF default_review THEN START -> assets/review-checklist.md
IF requirement_fit_is_primary_question THEN ADD -> assets/spec-review.md
IF comparable_experience_or_fallback_equivalence_is_under_review THEN ADD -> assets/context-equivalence-matrix.md
IF another_owner_needs_the_result THEN ADD -> assets/review-handoff.md

MUST READ -> references/review-sequencing.md BEFORE choosing_review_order
IF seam_has(explicit_acceptance_criteria OR approved_plan_steps OR spec_language) THEN MUST READ -> references/criterion-discipline.md
```

## The Gate Function

```text
BEFORE claiming any status or expressing satisfaction:

1. IDENTIFY: What command proves this claim?
2. RUN: Execute the FULL command (fresh, complete)
3. READ: Full output, check exit code, count failures
4. VERIFY: Does output confirm the claim?
   - If NO: State actual status with evidence
   - If YES: State claim WITH evidence
5. ONLY THEN: Make the claim

Skip any step = lying, not verifying
```

## Procedure

```text
INPUT := { seam, changed_files, fresh_proof, source_type, acceptance_source }

STEP_0 := declare(support_files := exact assets/ + references/ set OR none)
STEP_0A := read(required_assets_and_references_before_review)
STEP_0B := record(why_each_declared_file_was_loaded)
STEP_1 := gather(INPUT.seam, INPUT.changed_files, INPUT.fresh_proof, INPUT.acceptance_source)
IF INPUT.source_type = support_report THEN
  CAPTURE(symptom, impact, environment, repro_status, workaround)
  REPRODUCE(consistently_or_gather_more_data)

STEP_2 := review_in_fixed_order(spec_fit -> code_quality -> qa_evidence)
STEP_2A := reject(implementation_report_as_acceptance_evidence) IF code_or_artifact_check_is_missing
IF specialist_lens_is_needed THEN ROUTE -> bounded_specialist_lane

STEP_3 := investigate_root_cause(read_errors, reproduce, check_recent_changes, trace_data_flow)
STEP_4 := compare_against_working_examples_or_references
STEP_5 := form_single_hypothesis_and_test_minimally
STEP_6 := prefer(behavior_level_evidence) OVER(implementation_detail_proof) WHEN both_are_possible
STEP_7 := verify(review_feedback_against_codebase_reality) IF incoming_change_request = review_feedback
STEP_8 := identify(full_verification_command_required_for_claim)
STEP_9 := run_and_read(full_verification_command_fresh)
STEP_10 := record(proof_freshness, evidence_gaps, unresolved_risks, blocked_reproduction, root_cause_status, comparable_experience_risk, user_control_regressions, responsive_survival_gaps)
STEP_10B := record(context_equivalence := relevant_contexts + fallback_paths + equivalence_expectation + verified_evidence + unresolved_gap) IF user_facing_or_comparable_experience_claim_is_present
STEP_10A := record(structure_clarity, responsibility_split_status, god_object_risk, large_file_exception_rationale)
STEP_11 := route_to_failure_memory IF debugging_or_verification_workaround_repeats
STEP_12 := decide(approve OR approve_with_follow_up OR revise OR block)

IF decision = revise THEN ROUTE -> implementation_owner
ELSE ROUTE -> next_owner
```

## Debugging Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

Before attempting any fix:

1. Read error messages carefully
2. Reproduce consistently
3. Check recent changes
4. Gather evidence in multi-component systems
5. Trace data flow

### Phase 2: Pattern Analysis

1. Find working examples
2. Compare against references
3. Identify differences
4. Understand dependencies

### Phase 3: Hypothesis and Testing

1. Form a single hypothesis
2. Test minimally
3. Verify before continuing
4. When you don't know, say so and gather more evidence

### Phase 4: Remediation Handoff

1. Name the failing acceptance criterion
2. Name the owner that must fix it
3. Require fresh verification after the fix
4. If the same failure repeats, return to Phase 1
5. If repeated fixes fail, question the architecture or scope owner

## Review Request Contract

Review early, review often.

Mandatory:
- After each bounded task in multi-agent or chunked execution
- After completing a major feature
- Before merge to main or any equivalent completion lane

When dispatching review, provide precisely crafted context for evaluation, never your full session history. The reviewer should get:
- what was implemented
- what it should do
- the bounded diff or changed files
- the acceptance source or plan source
- the verification evidence already run

Act on feedback:
- Fix critical issues immediately
- Fix important issues before proceeding
- Push back if feedback is wrong, but only with technical reasoning and fresh verification

## Review Reception Contract

Code review requires technical evaluation, not emotional performance.

When receiving code review feedback:

1. Read complete feedback without reacting
2. Restate the technical requirement in your own words or ask
3. Verify against codebase reality
4. Evaluate whether it is technically sound for this codebase
5. Respond with technical acknowledgment or reasoned pushback
6. Implement one item at a time and test each

Never:
- blindly agree
- implement before verification
- batch unclear items and hope they are independent

If any item is unclear, stop and clarify before implementing anything.

If external review feedback conflicts with the actual codebase, existing tests, or human-approved direction, push back with technical reasoning.

## Red Flags - STOP

- Using "should", "probably", or "seems to" for completion claims
- Expressing satisfaction before verification
- About to commit, merge, or close work without fresh verification
- Trusting agent success reports without checking
- Relying on partial verification
- Thinking just this once
- Quick fix for now, investigate later
- Just try changing X and see if it works
- Add multiple changes and run tests
- Proposing solutions before tracing data flow
- One more fix attempt after multiple failed fixes

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "Should work now" | Run the verification. |
| "I'm confident" | Confidence is not evidence. |
| "Partial check is enough" | Partial proves nothing. |
| "Agent said success" | Verify independently. |
| "Different words so the rule doesn't apply" | Spirit over letter. |
| "Issue is simple, don't need process" | Simple issues have root causes too. |
| "Emergency, no time for process" | Systematic debugging is faster than thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "Reviewer is probably right" | Verify against this codebase first. |
| "I'll fix the clear items and ask later" | Partial understanding creates wrong implementation. |

## Choose Roles

```text
IF question = requirement_fit OR scope_drift THEN ROUTE -> agents/spec-reviewer.md
ELSE IF question = code_level_correctness OR regression_risk THEN ROUTE -> agents/reviewer.md
ELSE IF question = fresh_verification_evidence OR artifact_quality THEN ROUTE -> agents/qa.md
ELSE IF docs_or_examples_are_part_of_acceptance_claim THEN ROUTE -> agents/docs-reviewer.md
ELSE IF incoming_evidence = bug_report OR support_case OR user_facing_defect_handoff THEN ROUTE -> agents/support-triager.md
ELSE STOP("review lane must be explicit")
```

## Choose Assets

```text
IF default_ordered_review THEN START -> assets/review-checklist.md
IF requirement_fit_is_weak_point THEN START -> assets/spec-review.md
IF correctness_OR_maintainability_OR_regression_risk_dominate THEN START -> assets/code-review.md
IF verification_evidence_is_decision_gate THEN START -> assets/qa-verdict.md
IF another_owner_must_receive_result THEN START -> assets/review-handoff.md
IF delegated_review_needs_exact_contract THEN START -> assets/code-review-dispatch.md OR assets/worker-handoff.md
IF main_risk = seam_interaction THEN START -> assets/integration-checklist.md
IF support_evidence_needs_cleanup THEN START -> assets/repro-intake.md OR assets/support-case-review.md
IF seam_needs_bounded_security_lens THEN START -> assets/security-review-checklist.md
```

## Choose References

```text
IF review_order_is_disputed THEN READ -> references/review-sequencing.md
IF acceptance_check_is_criterion_by_criterion THEN READ -> references/criterion-discipline.md
IF bug_fix_claim_lacks(failure_classification OR prevention_logic) THEN READ -> references/root-cause-and-prevention.md
IF seam_starts_as(support_report OR bug_handoff) THEN READ -> references/support-triage-and-evidence.md
IF docs_or_examples_changed_materially THEN READ -> references/docs-as-code-review.md
IF visual_regression_or_accessibility_sensitive_presentation_matters THEN READ -> references/inclusive-visual-qa.md
IF seam_affects(workflows OR jobs OR lineage_sensitive_data_movement) THEN READ -> references/data-workflow-review-lens.md
IF trust_boundaries_changed THEN READ -> references/application-security-lenses.md OR references/web-auth-security-baseline.md
```

## Output Contract

Return a review record with:

- declared support files
- files read before review
- why each file was loaded
- seam reviewed
- review order used
- proof checked and proof freshness
- full verification command run before completion claim
- findings, evidence gaps, and remaining risk
- decision
- next owner or next skill
- files actually used
