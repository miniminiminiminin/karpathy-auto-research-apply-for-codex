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
- branch exit, isolated workspace setup, and release completion stay inside repo-local planning or release owners

## Entry Order

1. Start with `intake-and-routing` when the request is new or ambiguous.
2. Move to `product-and-ux` when the request implies creative work, new behavior, flow shaping, messaging, or design direction even if the scope looks small.
3. Move to `planning-and-scoping` only after the direction has been presented and approved.
4. Use `architecture-and-design` when seams, contracts, or trade-offs are still open.
5. Use `implementation-*` only after planning is execution-ready, with failing tests first and exact proof paths.
6. Use `quality-and-review` for ordered review, fresh verification before completion claims, debugging discipline, review request/response handling, and acceptance gating.
7. Use `release-and-operations` for ship, hold, rollback, incident follow-up, and branch exit decisions after fresh verification.
8. Use `multi-agent-orchestration` only when decomposition clearly improves delivery and slices can carry fresh isolated context.
9. If a failure, repeated difficulty, or environment quirk changes future behavior, use `failure-memory` before closing the task.
10. Use `skillsmith` when the task is to create or revise the skill system itself.

## Catalog

| Skill | Primary Job | Typical Roles | Typical Phases |
| --- | --- | --- | --- |
| `intake-and-routing` | restate a new request and choose the single best next skill | CTO, PM, lead | intake, triage |
| `planning-and-scoping` | turn an approved direction into owned seams, non-goals, and proof | CTO, lead, implementer | planning, scoping |
| `architecture-and-design` | decide seams, contracts, and design trade-offs before implementation | CTO, lead, platform | architecture, design |
| `implementation-frontend` | implement an approved UI seam with explicit state and accessibility proof | frontend, design-minded engineer | implementation, verification |
| `implementation-backend` | implement a chosen backend seam with contract-safe verification | backend, platform engineer | implementation, verification |
| `product-and-ux` | turn evidence into product direction, UX trade-offs, and flow decisions | PM, UX, UI | discovery, design |
| `quality-and-review` | require fresh proof, ordered review, and acceptance before completion claims | reviewer, QA, lead | testing, review, acceptance |
| `security-review` | review trust-boundary changes and classify findings or lab follow-up | security reviewer, lead, implementer | review, remediation planning |
| `security-lab` | reproduce and regress security issues against self-owned Docker lab targets | attacker, defender, reporter | repro, verification, regression |
| `release-and-operations` | choose ship, hold, mitigate, rollback, or incident follow-up | release, DevOps, QA | release, operations |
| `multi-agent-orchestration` | dispatch disjoint slices with explicit skills, support paths, and convergence | CTO, lead | orchestration, integration |
| `skillsmith` | compile or revise repo-local skills with explicit triggers and support files | CTO, skill author | skill design, packaging |
| `failure-memory` | turn failures and repeated workarounds into reusable repo-local lessons | CTO, reviewer, operator | debugging, review, operations |
| `batch-production` | run manifest-driven prompt or transformation batches with retries and resume | backend, operator, content systems | planning, implementation, operations |

## Packaging Rules

- required: `SKILL.md`
- recommended: `agents/openai.yaml`
- recommended when the skill owns execution roles: `agents/*.md`
- recommended when the skill owns repeatable records: `assets/*.md`
- optional: `references/`, `scripts/`
- avoid local scripts unless a repeated workflow is deterministic enough to justify them
- when a skill owns a deterministic CLI workflow, keep the authoritative scripts inside that skill package

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
- reopen the admission gate only if a new source behavior cannot be compiled into an existing repo-local owner without weakening trigger clarity or output-contract force
