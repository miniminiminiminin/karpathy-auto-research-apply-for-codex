# CANON Subtree Contract

These instructions apply to every file under `CANON/**`.

## Purpose

- Keep `CANON/` as the reusable operating law for downstream projects.
- Make `CANON/` self-sufficient: an operator should not need sibling scaffold prose outside Canon to understand bootstrap, routing, orchestration, rubric lock, execution, review, or release.
- Preserve a small, explicit top-level owner catalog instead of creating narrow duplicate skills.
- Favor durable routing, decision, proof, and review rules over source-specific prose.

## Owner Discipline

- Respect the current owner map described in `CANON/README.md`.
- Keep one primary owner per rule family even when multiple skills consume the result.
- Do not let one owner absorb neighboring concerns just because the source text sounds broad.
- Choose the next skill by phase and dominant uncertainty, not by whichever owner feels broadly capable.
- Prefer the narrowest owner that can decide the next move without redefining neighboring concerns.
- When multiple owners are plausible, make the rejection reason explicit instead of silently blending them.
- Route repo-wide Canon maintenance, source absorption, and owner-boundary work through `CANON/skillsmith/**`.
- Route reusable downstream scaffold packaging and copy-surface maintenance through `CANON/skillsmith/**`.
- Keep deferred hardening explicit rather than hiding it behind completion language.

## Authoring Rules

- Prefer strengthening the owning `SKILL.md`, `assets/*.md`, and `references/*.md` before adding new files.
- Add new top-level owners only when an existing owner cannot absorb the rule without losing trigger clarity or output-contract force.
- Keep support-file selection rules aligned with live files.
- Make operator-facing records distinguish declared files, files read, and files used when the owner requires support files.
- Keep common record fields consistent across owners when the concept is shared: freshness, revalidation trigger, waiver owner/expiry, next owner, next skill, and files actually used.
- Prefer exact gate language over advisory prose when a field should block progress.
- Do not let “not applicable,” “temporary,” or “we will split later” bypass ownership, expiry, or re-review requirements.
- Require reroute or revalidation when change radius, seam count, or affected-owner count grows beyond what the active owner was meant to handle.
- Keep reusable package sources inside Canon-owned paths when downstream copy behavior is part of the operating law.
- Keep language imperative when the operator is expected to execute a sequence or satisfy a gate.
- Do not turn CANON files into run logs, changelogs, or narrative memory.

## Shared Output Discipline

- Operator-facing artifacts should make the next move obvious: name the current owner, next owner, next skill, and stop condition.
- Shared evidence concepts should be written in scan-friendly fields rather than buried in paragraphs.
- If a decision depends on freshness, record the freshness status and the revalidation trigger explicitly.
- If an exception is granted for file split, seam split, stale evidence, or comparable temporary debt, record the waiver ID, owner, and expiry or recheck trigger.
- If a change started as one seam and widened, record the change-radius growth and the reroute trigger explicitly.
- Do not claim completeness, safety, or readiness from narration alone when another owner expects proof-shaped fields.

## Agent Use Guidance

- A strong skill catalog is not enough; the routing contract must make the correct owner easy to choose under pressure.
- Favor owner packages that expose a clear start asset, required reads, procedure, and output contract over owners that only describe principles.
- If a skill cannot reliably tell the operator when to start it, what files to read first, and what exact artifact to produce, it still needs hardening.
- Reuse shared phrasing for common cross-owner concepts instead of redefining the same field names differently in neighboring packages.
- Subagent and orchestration behavior should be explicit enough in Canon that operators do not skip fan-out merely because a sibling scaffold README happened to explain more.
- If the user explicitly asks for subagents, delegation, parallel evaluation, or orchestration, Canon must make the orchestration decision explicit instead of letting a direct owner silently absorb it.
- When orchestration is materially considered and rejected, record the no-fan-out reason in the owning routing or orchestration artifact.

## Closure Rules

- Use explicit status semantics such as `partial`, `batched`, or `coverage-complete` instead of vague “done” claims.
- Name deferred work when a family is only partially hardened.
- When a closure claim depends on review, point to the concrete evaluation artifact or other auditable evidence.

## Scope Discipline

- Edit only files inside `CANON/**` when working under this subtree contract.
- Preserve unrelated concurrent changes unless they directly conflict with the owned Canon change.
- Keep the reusable downstream shell under `CANON/skillsmith/packages/research-scaffold/`.
- Do not require a sibling root scaffold directory for Canon correctness.
