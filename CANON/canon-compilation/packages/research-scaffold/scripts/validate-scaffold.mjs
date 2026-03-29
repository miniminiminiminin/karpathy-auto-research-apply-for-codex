import fs from 'node:fs/promises';
import path from 'node:path';
import process from 'node:process';

const REQUIRED_FILES = [
  'purpose.txt',
  'loop-status.md',
  'plan.md',
  'results.tsv',
  'run.log',
  'score.log',
];

const PLACEHOLDER_VALUES = new Set([
  'not yet recorded',
  'not assessed',
]);

function parseBulletMap(markdown) {
  const entries = new Map();

  for (const line of markdown.split('\n')) {
    const match = line.match(/^- ([^:]+):\s*(.*)$/);
    if (!match) {
      continue;
    }

    entries.set(match[1].trim().toLowerCase(), match[2].trim());
  }

  return entries;
}

function hasEvidence(logText) {
  const content = logText
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => line && !line.startsWith('#'));

  return content.length > 0;
}

async function readFileIfPresent(rootDir, relativePath, errors) {
  const absolutePath = path.join(rootDir, relativePath);

  try {
    return await fs.readFile(absolutePath, 'utf8');
  } catch (error) {
    if (error && error.code === 'ENOENT') {
      errors.push(`Missing required file: ${relativePath}`);
      return null;
    }

    throw error;
  }
}

async function hasIterationRecord(rootDir) {
  const iterationDir = path.join(rootDir, 'iterations');

  try {
    const entries = await fs.readdir(iterationDir, { withFileTypes: true });
    return entries.some((entry) => entry.isFile() && entry.name !== 'README.md');
  } catch (error) {
    if (error && error.code === 'ENOENT') {
      return false;
    }

    throw error;
  }
}

function isPlaceholder(value) {
  return !value || PLACEHOLDER_VALUES.has(value.toLowerCase());
}

function requirePlanField(plan, fieldName, errors) {
  const value = plan.get(fieldName);
  if (isPlaceholder(value)) {
    errors.push(`plan.md must define "${fieldName}" before execution or promotion.`);
  }
}

export async function validateScaffold(rootDir) {
  const errors = [];
  const files = new Map();

  for (const relativePath of REQUIRED_FILES) {
    files.set(relativePath, await readFileIfPresent(rootDir, relativePath, errors));
  }

  if (errors.length > 0) {
    return { ok: false, errors };
  }

  const rubricPath = path.join(rootDir, 'rubric.txt');
  try {
    await fs.access(rubricPath);
  } catch {
    errors.push('Bootstrap incomplete: rubric.txt is required before project execution starts.');
  }

  const loopStatus = parseBulletMap(files.get('loop-status.md'));
  const plan = parseBulletMap(files.get('plan.md'));
  const stage = (loopStatus.get('stage') || '').toLowerCase();
  const currentBlocker = (loopStatus.get('current blocker') || '').toLowerCase();
  const activeIteration = Number.parseInt(loopStatus.get('active iteration') || '0', 10);
  const executionStarted = stage !== 'bootstrap' || activeIteration > 0;

  if (currentBlocker.includes('rubric not generated')) {
    errors.push('loop-status.md still reports "rubric not generated"; bootstrap cannot be treated as complete.');
  }

  requirePlanField(plan, 'active slice', errors);
  requirePlanField(plan, 'proof path baseline', errors);
  requirePlanField(plan, 'proof path candidate checks', errors);
  requirePlanField(plan, 'promotion gate', errors);
  requirePlanField(plan, 'rollback trigger', errors);
  requirePlanField(plan, 'planner owner', errors);
  requirePlanField(plan, 'executor owner', errors);
  requirePlanField(plan, 'evaluator owner', errors);

  const resultsLines = files
    .get('results.tsv')
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean);

  if (executionStarted) {
    if (!(await hasIterationRecord(rootDir))) {
      errors.push('iterations/ must contain at least one iteration record after execution starts.');
    }

    if (!hasEvidence(files.get('run.log'))) {
      errors.push('run.log must contain fresh execution evidence after execution starts.');
    }

    if (!hasEvidence(files.get('score.log'))) {
      errors.push('score.log must contain rubric scoring evidence after execution starts.');
    }

    if (resultsLines.length < 2) {
      errors.push('results.tsv must contain at least one iteration row after execution starts.');
    }
  }

  return {
    ok: errors.length === 0,
    errors,
  };
}

async function main() {
  const targetDir = process.argv[2] ? path.resolve(process.argv[2]) : process.cwd();
  const result = await validateScaffold(targetDir);

  if (result.ok) {
    process.stdout.write(`Scaffold validation passed for ${targetDir}\n`);
    return;
  }

  for (const error of result.errors) {
    process.stderr.write(`- ${error}\n`);
  }

  process.exitCode = 1;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  await main();
}
