#!/usr/bin/env node

import { captureRenderedPage } from "./capture.js";
import {
  createCapturePaths,
  resolveOutputRoot,
  slugifySegment,
} from "./config.js";
import { extractPrimaryHtml } from "./extract.js";
import { convertHtmlToMarkdown, splitMarkdownIntoSections } from "./markdown.js";
import { writeCaptureOutput } from "./write-output.js";
import {
  cloneRepository,
  ingestLocalRepository,
  isLocalRepositoryPath,
} from "./github-ingest.js";

function printHelp() {
  process.stdout.write(
    [
      "Usage:",
      "  ux-library capture-url <url> [--out <path>] [--collection <name>] [--split-sections]",
      "  ux-library capture-github <repo-url-or-local-path> [--out <path>] [--collection <name>] [--split-sections]",
    ].join("\n"),
  );
}

function parseArgs(argv) {
  const [command, target, ...rest] = argv;
  const options = {
    out: undefined,
    collection: undefined,
    splitSections: false,
  };

  for (let index = 0; index < rest.length; index += 1) {
    const token = rest[index];

    if (token === "--out") {
      options.out = rest[index + 1];
      index += 1;
      continue;
    }

    if (token === "--collection") {
      options.collection = rest[index + 1];
      index += 1;
      continue;
    }

    if (token === "--split-sections") {
      options.splitSections = true;
    }
  }

  return {
    command,
    target,
    options,
    outputRoot: resolveOutputRoot(options.out),
  };
}

async function runCaptureUrl(parsed) {
  if (!parsed.target) {
    throw new Error("capture-url requires a URL target");
  }

  const page = await captureRenderedPage(parsed.target);
  const primaryHtml = extractPrimaryHtml(page.html);
  const markdown = convertHtmlToMarkdown(primaryHtml);
  const sourceSlug = slugifySegment(page.title || parsed.target);
  const paths = createCapturePaths({
    outputRoot: parsed.outputRoot,
    collection: parsed.options.collection,
    sourceSlug,
  });
  const sections = parsed.options.splitSections
    ? splitMarkdownIntoSections(markdown)
    : [];

  const writeResult = await writeCaptureOutput({
    captureRoot: paths.captureRoot,
    markdown,
    metadata: {
      title: page.title,
      sourceUrl: parsed.target,
      finalUrl: page.finalUrl,
      fetchedAt: page.fetchedAt,
    },
    sections,
  });

  return {
    ...writeResult,
    captureRoot: paths.captureRoot,
    markdown,
  };
}

async function runCaptureGithub(parsed) {
  if (!parsed.target) {
    throw new Error("capture-github requires a repository URL target");
  }

  const cloneRoot = isLocalRepositoryPath(parsed.target)
    ? parsed.target
    : (await cloneRepository(parsed.target)).cloneRoot;
  const ingested = await ingestLocalRepository({
    repoRoot: cloneRoot,
    sourceUrl: parsed.target,
    splitSections: parsed.options.splitSections,
  });
  const sourceSlug = slugifySegment(ingested.metadata.title || parsed.target);
  const paths = createCapturePaths({
    outputRoot: parsed.outputRoot,
    collection: parsed.options.collection,
    sourceSlug,
  });

  const writeResult = await writeCaptureOutput({
    captureRoot: paths.captureRoot,
    markdown: ingested.markdown,
    metadata: ingested.metadata,
    sections: ingested.sections,
  });

  return {
    ...writeResult,
    captureRoot: paths.captureRoot,
  };
}

const parsed = parseArgs(process.argv.slice(2));

if (!parsed.command) {
  printHelp();
  process.exit(0);
}

if (parsed.command === "capture-url") {
  const result = await runCaptureUrl(parsed);
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  process.exit(0);
}

if (parsed.command === "capture-github") {
  const result = await runCaptureGithub(parsed);
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  process.exit(0);
}

process.stdout.write(
  JSON.stringify(
    {
      ...parsed,
      implemented: false,
    },
    null,
    2,
  ),
);
