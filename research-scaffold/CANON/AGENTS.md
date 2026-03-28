# CANON Subtree Contract

These instructions apply to every file under `CANON/**`.

## Purpose

- Keep `CANON/` as the reusable operating law for downstream projects.
- Preserve a small, explicit top-level owner catalog instead of creating narrow duplicate skills.
- Favor durable routing, decision, proof, and review rules over source-specific prose.

## Owner Discipline

- Respect the current owner map described in `CANON/README.md`.
- Keep one primary owner per rule family even when multiple skills consume the result.
- Do not let one owner absorb neighboring concerns just because the source text sounds broad.
- Route repo-wide Canon maintenance, source absorption, and owner-boundary work through `CANON/skillsmith/**`.
- Keep deferred hardening explicit rather than hiding it behind completion language.

## Authoring Rules

- Prefer strengthening the owning `SKILL.md`, `assets/*.md`, and `references/*.md` before adding new files.
- Add new top-level owners only when an existing owner cannot absorb the rule without losing trigger clarity or output-contract force.
- Keep support-file selection rules aligned with live files.
- Make operator-facing records distinguish declared files, files read, and files used when the owner requires support files.
- Keep language imperative when the operator is expected to execute a sequence or satisfy a gate.
- Do not turn CANON files into run logs, changelogs, or narrative memory.

## Closure Rules

- Use explicit status semantics such as `partial`, `batched`, or `coverage-complete` instead of vague “done” claims.
- Name deferred work when a family is only partially hardened.
- When a closure claim depends on review, point to the concrete evaluation artifact or other auditable evidence.

## Scope Discipline

- Edit only files inside `CANON/**` when working under this subtree contract.
- Preserve unrelated concurrent changes unless they directly conflict with the owned Canon change.
- When scaffold parity is intended, sync `research-scaffold/CANON/` from the updated root Canon tree before publishing.
