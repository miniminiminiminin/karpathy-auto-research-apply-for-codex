# principles.adactio Batch 4 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/implementation-backend/**`
- owner 2: `CANON/release-and-operations/**`
- goal:
  - absorb irreducible-core, reuse-before-bespoke, compatibility, and reliability principles into backend implementation rules
  - absorb fresh runtime evidence, rollout-by-change-shape, monitoring cadence, openness of operational risk, and operational sustainability into release and operations rules
  - keep backend focused on seam-safe implementation and keep release focused on ship, hold, mitigate, rollback, and runtime follow-up decisions

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `implementation-backend` owns contract-safe seam delivery, compatibility handling, idempotency, bounded runtime behavior, lineage, and implementation proof
- `release-and-operations` owns ship or hold judgment, rollout and rollback choice, current runtime evidence, monitoring ownership, incident posture, and follow-up cadence
- backend does not silently become release management or architecture planning
- release does not silently become implementation design or product policy

FAIL IF
- backend files begin deciding rollout posture or shipping readiness as if those are implementation concerns
- release files begin prescribing implementation detail or schema redesign as if operations owns the seam

### 2. Principle Fidelity

PASS IF
- GDS “do less” becomes explicit irreducible-core and reuse-before-bespoke checks, not a slogan
- robustness and compatibility become explicit rules for additive evolution, duplicates, partial failure, and consumer impact
- GDS “design with data” becomes fresh runtime evidence, observability, and monitoring-owner requirements before ship
- GDS “iterate” becomes explicit follow-up cadence and reusable-rule capture rather than vague “monitor later”
- openness becomes explicit risk, evidence, and handoff reporting instead of private intuition
- sustainability only lands where it changes an operational or release decision

FAIL IF
- source language is pasted without backend or release translation
- “reliable” or “safe to ship” remains a generic adjective with no record fields or fail gates
- sustainability becomes decorative language without an operating decision hook

### 3. Operator Usability

PASS IF
- a backend implementer can tell whether a seam is overbuilt relative to the irreducible core
- a backend operator can record compatibility risk, idempotency, and runtime behavior without inventing ceremony
- a release operator can fail a ship decision for stale evidence, vague rollback, or missing monitoring ownership
- assets ask for fields that can actually be filled from real release work

FAIL IF
- operators can satisfy the template while leaving rollout, rollback, or consumer risk implicit
- reuse and irreducible-core checks sound right but cannot reject overbuilt seams

### 4. Reviewability

PASS IF
- release assets can reject inherited confidence and require fresh runtime evidence
- backend assets can reject hidden contract drift, bespoke rebuilds of existing platform capability, and unbounded retry or duplicate behavior
- operations records can distinguish confirmed facts from uncertainty and name the next update or follow-up owner

FAIL IF
- completion can still be claimed from old notes, green builds, or vague rollout confidence
- backend can still claim success while consumer impact or compatibility drift remains implicit

### 5. Catalog Safety

PASS IF
- no new top-level owner is added
- rules strengthen existing backend and release files instead of introducing overlap
- backend and release remain complementary rather than duplicative

## Evaluation Questions For Reviewers

1. Did any irreducible-core, compatibility, or reliability rule land in the wrong owner?
2. Can backend now reject overbuilt or hidden-contract seams more concretely than before?
3. Can release now reject stale evidence, weak rollback posture, and vague monitoring ownership more reliably than before?
4. Which principle families are still deferred after this batch, especially context-for-everyone, openness, and sustainability?

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- principle-fidelity issues
- operator-ambiguity issues
- deferred coverage still missing from this batch
