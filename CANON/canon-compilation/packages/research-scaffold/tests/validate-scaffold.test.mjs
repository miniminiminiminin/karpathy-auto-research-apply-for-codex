import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

import { validateScaffold } from '../scripts/validate-scaffold.mjs';

const baseFiles = {
  'purpose.txt': 'Ship a useful product.\n',
  'loop-status.md': `# Loop Status

- Stage: bootstrap
- Active iteration: 0
- Next owner: intake-and-routing
- Current blocker: rubric not generated
- Evidence confidence: low
- Evidence confidence scale: low | medium | high
- Last decision: scaffold initialized
- Ship readiness: not assessed
`,
  'plan.md': `# Active Plan

- Approved direction: not yet recorded
- Active slice: not yet recorded
- Proof path baseline: not yet recorded
- Proof path candidate checks: not yet recorded
- Promotion gate: not yet recorded
- Rollback trigger: not yet recorded
- Planner owner: not yet recorded
- Executor owner: not yet recorded
- Evaluator owner: not yet recorded
- Implementation owner: not yet recorded
- Verification owner: not yet recorded
- Risk class: not yet recorded
- Non-goals: not yet recorded
- Acceptance threshold: not yet recorded
- Release condition: not yet recorded
`,
  'results.tsv': 'iteration\tstage\ttotal_score\tdelta\tstatus\tdescription\n',
  'run.log': '# Run Log\n\n',
  'score.log': '# Score Log\n\n',
  'iterations/README.md': '# iterations\n',
};

async function makeScaffold(overrides = {}) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), 'scaffold-'));
  const files = { ...baseFiles, ...overrides };

  await Promise.all(
    Object.entries(files).map(async ([relativePath, content]) => {
      const target = path.join(root, relativePath);
      await fs.mkdir(path.dirname(target), { recursive: true });
      await fs.writeFile(target, content);
    }),
  );

  return root;
}

test('fails bootstrap when rubric.txt is missing', async () => {
  const scaffoldRoot = await makeScaffold();

  const result = await validateScaffold(scaffoldRoot);

  assert.equal(result.ok, false);
  assert.match(result.errors.join('\n'), /rubric\.txt/);
});

test('fails active loop when score evidence is missing', async () => {
  const scaffoldRoot = await makeScaffold({
    'rubric.txt': '# Rubric\n\n- fixed scoring shape\n',
    'loop-status.md': `# Loop Status

- Stage: autonomous-loop
- Active iteration: 1
- Next owner: evaluator
- Current blocker: none
- Evidence confidence: medium
- Evidence confidence scale: low | medium | high
- Last decision: waiting on final gate check
- Ship readiness: not assessed
`,
    'plan.md': `# Active Plan

- Approved direction: improve activation flow
- Active slice: tighten signup completion path
- Proof path baseline: record current signup failure rate
- Proof path candidate checks: run flow smoke and contract checks
- Promotion gate: smoke passes and rubric threshold met
- Rollback trigger: signup completion rate regresses
- Planner owner: planner
- Executor owner: executor
- Evaluator owner: evaluator
- Implementation owner: software-engineer-frontend
- Verification owner: qa
- Risk class: medium
- Non-goals: redesign unrelated marketing pages
- Acceptance threshold: total score >= baseline + 1
- Release condition: keep iterating
`,
    'iterations/001-signup.md': '# Iteration 001\n',
    'run.log': '# Run Log\n\nExecuted smoke checks.\n',
    'score.log': '# Score Log\n\n',
  });

  const result = await validateScaffold(scaffoldRoot);

  assert.equal(result.ok, false);
  assert.match(result.errors.join('\n'), /score\.log/);
});

test('passes when scaffold state satisfies the minimum execution gates', async () => {
  const scaffoldRoot = await makeScaffold({
    'rubric.txt': '# Rubric\n\n- fixed scoring shape\n',
    'loop-status.md': `# Loop Status

- Stage: autonomous-loop
- Active iteration: 1
- Next owner: evaluator
- Current blocker: none
- Evidence confidence: high
- Evidence confidence scale: low | medium | high
- Last decision: candidate ready for scoring
- Ship readiness: not assessed
`,
    'plan.md': `# Active Plan

- Approved direction: improve activation flow
- Active slice: tighten signup completion path
- Proof path baseline: record current signup failure rate
- Proof path candidate checks: run flow smoke and contract checks
- Promotion gate: smoke passes and rubric threshold met
- Rollback trigger: signup completion rate regresses
- Planner owner: planner
- Executor owner: executor
- Evaluator owner: evaluator
- Implementation owner: software-engineer-frontend
- Verification owner: qa
- Risk class: medium
- Non-goals: redesign unrelated marketing pages
- Acceptance threshold: total score >= baseline + 1
- Release condition: keep iterating
`,
    'iterations/001-signup.md': '# Iteration 001\n',
    'run.log': '# Run Log\n\nExecuted smoke checks.\n',
    'score.log': '# Score Log\n\nIteration 001: score 8 -> 10.\n',
    'results.tsv': 'iteration\tstage\ttotal_score\tdelta\tstatus\tdescription\n001\tautonomous-loop\t10\t+2\tkeep\ttighten signup completion path\n',
  });

  const result = await validateScaffold(scaffoldRoot);

  assert.deepEqual(result, { ok: true, errors: [] });
});
