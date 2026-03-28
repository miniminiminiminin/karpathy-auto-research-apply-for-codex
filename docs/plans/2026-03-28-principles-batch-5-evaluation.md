# principles.adactio Batch 5 Evaluation Criteria

## Batch Scope

- owner 1: `CANON/intake-and-routing/**`
- owner 2: `CANON/README.md` catalog and routing description
- goal:
  - absorb large-request decomposition, owner-aware routing, and minimum-viable-next-route principles into intake
  - make the root CANON catalog describe the actual current owner boundaries after batches 1 through 4
  - keep intake as routing law, not hidden planning or implementation

## Pass Criteria

### 1. Owner Boundary

PASS IF
- `intake-and-routing` owns restatement, boundary detection, ambiguity handling, next-owner choice, and seam parking
- `skillsmith` is explicitly chosen for repo-wide CANON or skill-system compilation work instead of letting intake silently absorb it
- the root catalog describes owners and entry order without taking over owner-level policy

FAIL IF
- intake starts behaving like planning, architecture, or implementation
- root catalog starts duplicating detailed owner rules instead of describing routing and discovery

### 2. Principle Fidelity

PASS IF
- “build services, not websites” becomes explicit routing toward service outcome owners instead of surface-level execution
- “do less” becomes minimum viable next route and one active batch at a time, not orchestration by habit
- “understand context” becomes explicit scale, ambiguity, severity, and owner-boundary checks before routing
- openness becomes explicit documentation of why alternatives lost, what is parked, and which owner receives the next move

FAIL IF
- routing still encourages mixed-owner execution without decomposition
- large source-absorption requests can still disappear into one giant edit pass

### 3. Operator Usability

PASS IF
- an operator can route a mixed or oversized request into one active batch and parked follow-ups
- a CANON-maintenance request can be routed to `skillsmith` cleanly
- the README makes it easier to choose the right owner after the recent absorption work

FAIL IF
- intake records sound correct but cannot capture parked work, active seam, or owner comparison
- the catalog is stale relative to the actual skill boundaries

### 4. Reviewability

PASS IF
- intake artifacts can fail when ambiguity, blocked actions, parked follow-ups, or rejected alternatives stay implicit
- README statements can be checked against live owners without hand-wavy overlap

FAIL IF
- a route can pass while hidden ambiguity or hidden backlog remains
- the catalog overstates absorption or owner clarity

## Evaluation Questions For Reviewers

1. Can intake now decompose oversized mixed-owner requests without drifting into planning?
2. Is `skillsmith` now clearly the owner for repo-wide CANON and skill-system absorption work?
3. Does the root README describe the current owner map accurately after batches 1 through 4?
4. Which remaining principle families are still deferred after this final routing/catalog batch?

## Required Review Outputs

- verdict: `pass`, `pass_with_revisions`, or `block`
- findings ordered by severity
- owner-boundary issues
- principle-fidelity issues
- operator-ambiguity issues
- deferred coverage still missing from this batch
