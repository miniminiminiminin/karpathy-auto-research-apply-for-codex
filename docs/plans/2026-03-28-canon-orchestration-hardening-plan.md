# Canon Orchestration Hardening Plan

## Goal

Make `CANON/` self-sufficient not only for routing and bootstrap, but also for deciding when subagents and orchestration are required instead of optional.

## Problem

The current Canon catalog already has `multi-agent-orchestration`, but operators can still:

- stay in a direct owner even when the user explicitly asked for subagents or parallel evaluation
- use one broad owner without recording why fan-out was rejected
- dispatch informally without a strong enough orchestration artifact
- keep autonomous-loop work single-threaded even when planner, executor, evaluator, and review slices are independent

That means Canon can describe orchestration without always forcing it when the request or work shape requires it.

## Hardening Targets

1. `CANON/AGENTS.md`
   - make explicit that Canon must say when orchestration is required, not merely available
2. `CANON/intake-and-routing/**`
   - route explicit subagent/delegation/evaluation requests to `multi-agent-orchestration`
   - require a recorded no-fan-out reason when orchestration was materially considered and rejected
3. `CANON/multi-agent-orchestration/**`
   - require a stronger dispatch record for why one operator is insufficient
   - make subagent evaluation and convergence review explicit when requested
4. `CANON/autonomous-app-loop/**`
   - reroute to orchestration when the loop decomposes into independent planner/executor/evaluator/review slices

## Acceptance Criteria

- Canon can answer "when must I use subagents?" without needing scaffold-side prose
- explicit subagent requests cannot silently bypass `multi-agent-orchestration`
- orchestration artifacts record trigger, reason not to stay single-operator, and required review path
- autonomous-loop work reroutes when independent slices emerge instead of pretending one operator still owns everything

## Planned Edits

1. strengthen `CANON/AGENTS.md`
2. strengthen `CANON/intake-and-routing/SKILL.md`
3. strengthen `CANON/multi-agent-orchestration/SKILL.md`
4. strengthen `CANON/multi-agent-orchestration/assets/{slice-record,dispatch-handoff,convergence-record}.md`
5. strengthen `CANON/autonomous-app-loop/SKILL.md`
6. keep the Canon-owned scaffold package model aligned with root `CANON/**` contracts when packaging rules change
7. run subagent review on orchestration hardening
