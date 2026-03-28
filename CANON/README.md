# Skills

This exported SoloPilot pack keeps a small, standalone skill catalog under `.codex/skills/<skill-name>/`.

## Discovery Model

- keep the top-level catalog broad and curated rather than splintered into narrow duplicates
- keep every skill independently understandable
- keep each skill description trigger-first so nearby phases are easy to distinguish
- keep support material inside the same skill directory when it materially helps
- keep role prompts, reusable assets, and long-form references inside the owning skill package
- do not depend on removed root prompt or template directories
- when delegated work is involved, dispatch with explicit repo-local skills and support paths rather than generic role guesses
- compile useful `superpowers` behavior into existing repo-local skills first
- do not present imported `superpowers` as a second public catalog
- keep the skill system optimized for one goal: improving a project's ability to perform `purpose.txt`
- compile durable external principle libraries into existing owners with one active batch at a time and explicit parked follow-ups
- keep reusable downstream package sources inside Canon-owned paths when copy behavior is part of the operating law

## Entry Order

1. Start with `intake-and-routing` when the request, project state, or next slice is still unclear.
2. Move to `skillsmith` when the task is repo-wide CANON revision, external principle absorption, or skill-system maintenance across multiple owners.
3. Move to `product-and-ux` when the purpose still needs a direction package, UX framing, or user-facing trade-offs.
4. Move to `visual-design` when hierarchy, typography, color, density, or art direction still need explicit rules before implementation.
5. Move to `planning-and-scoping` only after the direction has been presented and approved.
6. Use `architecture-and-design` when seams, contracts, topology, or rollback shape are still open.
7. Use `autonomous-app-loop` when bootstrap, rubric lock, or one bounded slice in the planner -> executor -> evaluator loop is the next governed move in service of `purpose.txt`.
8. Use `implementation-*` only when the autonomous loop or plan has already assigned a concrete implementation seam.
9. Use `quality-and-review` for ordered review, fresh verification before completion claims, and acceptance gates.
10. Use `release-and-operations` for ship, hold, rollback, and branch-exit decisions after fresh evidence.
11. Use `multi-agent-orchestration` only when decomposition clearly improves delivery and slices can carry isolated context.

## Catalog

| Skill | Primary Job | Typical Roles | Typical Phases |
| --- | --- | --- | --- |
| `intake-and-routing` | restate a new request, choose the single best next skill, and park oversized follow-up seams | CTO, PM, lead | intake, triage |
| `product-and-ux` | turn evidence into product direction, UX trade-offs, and flow decisions | PM, UX, UI | discovery, design |
| `visual-design` | turn approved UX intent into explicit visual direction and a visual approval bar | UI, art direction, visual critic | design, critique, approval |
| `planning-and-scoping` | turn an approved direction into owned seams, non-goals, and proof | CTO, lead, implementer | planning, scoping |
| `architecture-and-design` | decide seams, contracts, and design trade-offs before implementation | CTO, lead, platform | architecture, design |
| `autonomous-app-loop` | own bootstrap, rubric lock, and one purpose-first planner -> executor -> evaluator iteration plus promotion | orchestrator, planner, executor, evaluator | bootstrap, execution, scoring, convergence |
| `implementation-frontend` | implement an approved UI seam with explicit state and accessibility proof | frontend, design-minded engineer | implementation, verification |
| `implementation-backend` | implement a chosen backend seam with contract-safe verification | backend, platform engineer | implementation, verification |
| `quality-and-review` | require fresh proof, ordered review, and acceptance before completion claims | reviewer, QA, lead | testing, review, acceptance |
| `security-review` | review trust-boundary changes and classify findings or lab follow-up | security reviewer, lead, implementer | review, remediation planning |
| `security-lab` | reproduce and regress security issues against self-owned Docker lab targets | attacker, defender, reporter | repro, verification, regression |
| `release-and-operations` | choose ship, hold, mitigate, rollback, or incident follow-up | release, DevOps, QA | release, operations |
| `multi-agent-orchestration` | dispatch disjoint slices with explicit skills, support paths, and convergence | CTO, lead | orchestration, integration |
| `skillsmith` | compile or revise repo-local skills, owner boundaries, and CANON-wide principle absorption work | CTO, skill author | skill design, packaging, canon maintenance |

## Packaging Rules

- required: `SKILL.md`
- recommended: `agents/openai.yaml`
- recommended when the skill owns execution roles: `agents/*.md`
- recommended when the skill owns repeatable records: `assets/*.md`
- optional: `references/`, `scripts/`
- avoid local scripts unless a repeated workflow is deterministic enough to justify them
- when a skill owns a deterministic CLI workflow, keep the authoritative scripts inside that skill package
- keep Canon-owned reusable package sources under the owning package path, currently `CANON/skillsmith/packages/**`
- do not require a sibling root scaffold directory when the Canon-owned package already carries the reusable shell

## Design Standard

High-quality SoloPilot skills should:

- have trigger-focused frontmatter
- describe the activation boundary in `description:` rather than a generic capability label
- own one broad but sharp operating concern
- stay procedural and concise
- make single-agent execution viable by default
- describe optional multi-agent use explicitly rather than implicitly
- name the supporting local roles and assets they can lean on
- keep asset and reference selection rules current with the live package contents
- refresh stale templates, records, and evidence-oriented references when the decision type or source inputs changed
- make delegated-work reporting traceable when a skill can dispatch or guide slices
- return a concrete output contract
- give visual direction its own owner when hierarchy, tone, or implementation-resistant screen rules would otherwise stay implicit
- make bootstrap and rubric-lock behavior legible from Canon without relying on sibling scaffold prose

## Promotion Rules

- routing or decision rules -> skills
- role behavior -> local `agents/*.md`
- reusable forms or checklists -> local `assets/*.md`
- one-off project notes -> outside the exported skillpack
- add a new top-level skill only when existing repo-local owners would lose trigger clarity or output-contract force

## Convergence Status

- current absorbed `superpowers` convergence status:
  - intake and skill-routing behavior absorbed into `intake-and-routing`
  - brainstorming behavior distributed across `intake-and-routing`, `product-and-ux`, and `planning-and-scoping`
  - writing-plans behavior absorbed into `planning-and-scoping`
  - test-driven-development behavior absorbed into `implementation-backend` and `implementation-frontend`
  - verification-before-completion, requesting-code-review, receiving-code-review, and systematic-debugging behavior absorbed into `quality-and-review`
  - subagent-driven-development and dispatching-parallel-agents behavior absorbed into `multi-agent-orchestration`
  - using-git-worktrees and executing-plans behavior absorbed into `planning-and-scoping`
  - finishing-a-development-branch behavior absorbed into `release-and-operations`
  - purpose-first planner/executor/evaluator loop control compiled into `autonomous-app-loop`
- current external principle absorption status:
  - `principles.adactio.com` families absorbed into `visual-design`, `product-and-ux`, `architecture-and-design`, `planning-and-scoping`, `implementation-frontend`, `implementation-backend`, `quality-and-review`, `release-and-operations`, and `intake-and-routing`
  - remaining hardening work stays explicit as deferred owner follow-up rather than hidden catalog claims
  - current named deferrals include stronger release-side sustainability gates, stricter iterate-with-data thresholds, and any remaining cross-owner hardening discovered by later audits
- reopen the admission gate only if a new source behavior cannot be compiled into an existing repo-local owner without weakening trigger clarity or output-contract force
