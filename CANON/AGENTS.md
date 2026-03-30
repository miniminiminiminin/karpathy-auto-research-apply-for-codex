# Absolute Authority

Within `CANON/**`, Canon is not guidance. It is the law that governs reusable operating behavior.

- If any external best practice, prior memory, or local convenience conflicts with live Canon text, Canon wins without negotiation.
- Do not treat tone, familiarity, or historical structure as authority when the current owner map or package contract says otherwise.
- Do not invent a reusable Canon rule in passing. If it should persist, it must be routed, owned, and written explicitly.

## Non-Negotiable Execution Law

- Re-scan the owning Canon package before editing any Canon-governed file.
- Read the minimum live `SKILL.md`, `assets/*.md`, and `references/*.md` needed to justify the rule you are changing.
- Keep owner boundaries explicit. Do not merge neighboring owners just because the work feels related.
- Do not claim Canon work is complete, hardened, or safe unless the owning package's proof expectations are visibly satisfied.

## Routing Mandate

- Start routing from `CANON/README.md`.
- Route repo-wide Canon maintenance and reusable package-law revision through `CANON/canon-compilation/**`.
- Route decomposition and parallel convergence decisions through `CANON/multi-agent-orchestration/**` when independent owned slices exist.
- Route bootstrap and bounded planner -> executor -> evaluator loop control through `CANON/autonomous-app-loop/**`.

## Stop Conditions

- Stop if the current owner cannot decide the next move without redefining a neighboring concern.
- Stop if the change radius expands beyond the active owner's designed boundary.
- Stop if orchestration was materially possible but no explicit fan-out or no-fan-out decision has been recorded.

## Audit Rule

- Before concluding Canon work, self-audit for owner clarity, proof shape, reroute triggers, and deferred hardening visibility.
- Session-close reporting must name the larger Canon workstream, the seam completed now, and the next seam to continue.

# CANON Subtree Contract

These instructions apply to every file under `CANON/**`.

## Purpose

- Keep `CANON/` as the reusable operating law for downstream projects.
- Make `CANON/` self-sufficient: an operator should not need sibling scaffold prose outside Canon to understand bootstrap, routing, orchestration, rubric lock, execution, review, or release.
- Preserve a small, explicit top-level owner catalog instead of creating narrow duplicate skills.
- Favor durable routing, decision, proof, and review rules over source-specific prose.

## Entry And Routing Discipline

- Start owner selection from `CANON/README.md` and follow its live entry order.
- Choose the next owner by phase and dominant uncertainty, not by whichever package sounds broadly capable.
- Route repo-wide Canon maintenance, source absorption, reference compilation, owner-boundary work, and reusable package maintenance through `CANON/canon-compilation/**`.
- Route bounded bootstrap or planner -> executor -> evaluator loop work through `CANON/autonomous-app-loop/**`.
- Route decomposition, delegation, and convergence questions through `CANON/multi-agent-orchestration/**` when independent owned slices materially exist.
- If multiple owners are plausible, record why the rejected owners were not chosen instead of silently blending concerns.

## Owner Discipline

- Respect the current owner map described in `CANON/README.md`.
- Keep one primary owner per rule family even when multiple skills consume the result.
- Do not let one owner absorb neighboring concerns just because the source text sounds broad.
- Prefer the narrowest owner that can decide the next move without redefining neighboring concerns.
- Keep deferred hardening explicit rather than hiding it behind completion language.
- Require reroute or revalidation when change radius, seam count, or affected-owner count grows beyond what the active owner was meant to handle.

## Canon Editing Rules

- Before editing a Canon file, read the owning `SKILL.md` plus the minimum live `assets/*.md` or `references/*.md` needed for that rule family.
- Declare the support files that matter for the active Canon edit and keep the declared set small and exact.
- Record which declared files were actually read and which were actually used when the owner contract expects support-file accountability.
- Prefer strengthening the owning `SKILL.md`, `assets/*.md`, and `references/*.md` before adding new files.
- Add new top-level owners only when an existing owner cannot absorb the rule without losing trigger clarity or output-contract force.
- Keep support-file selection rules aligned with live files.
- Keep reusable package sources inside Canon-owned paths when downstream copy behavior is part of the operating law.
- Keep language imperative when the operator is expected to execute a sequence or satisfy a gate.
- Do not turn Canon files into run logs, changelogs, or narrative memory.

## Shared Output Discipline

- Operator-facing artifacts should make the next move obvious: name the current owner, next owner, next skill, and stop condition.
- Session-close reporting must make progress and continuation obvious: name the larger workstream, the specific seam completed in the current session, and the next seam that should be continued.
- Shared evidence concepts should be written in scan-friendly fields rather than buried in paragraphs.
- If a decision depends on freshness, record the freshness status and the revalidation trigger explicitly.
- If an exception is granted for file split, seam split, stale evidence, or comparable temporary debt, record the waiver ID, owner, and expiry or recheck trigger.
- If a change started as one seam and widened, record the change-radius growth and the reroute trigger explicitly.
- Do not claim completeness, safety, or readiness from narration alone when another owner expects proof-shaped fields.

## Orchestration And Delegation

- A strong skill catalog is not enough; the routing contract must make the correct owner easy to choose under pressure.
- Favor owner packages that expose a clear start asset, required reads, procedure, and output contract over owners that only describe principles.
- Subagent and orchestration behavior should be explicit enough in Canon that operators do not skip fan-out merely because a sibling scaffold README happened to explain more.
- If the user explicitly asks for subagents, delegation, parallel evaluation, or orchestration, make the orchestration decision explicit instead of letting a direct owner silently absorb it.
- When orchestration is materially considered and rejected, record the no-fan-out reason in the owning routing or orchestration artifact.
- Follow `CANON/multi-agent-orchestration/references/parallel-governance.md` when deciding whether fan-out is governed well enough to start.

## Closure Rules

- Use explicit status semantics such as `partial`, `batched`, or `coverage-complete` instead of vague completion language.
- Name deferred work when a family is only partially hardened.
- When a closure claim depends on review, point to the concrete evaluation artifact or other auditable evidence.

## Scope Discipline

- Edit only files inside `CANON/**` when working under this subtree contract.
- Preserve unrelated concurrent changes unless they directly conflict with the owned Canon change.
- Keep the reusable downstream shell under `CANON/canon-compilation/packages/research-scaffold/`.
- Do not require a sibling root scaffold directory for Canon correctness.
