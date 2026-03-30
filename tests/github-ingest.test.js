import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import {
  findPrimaryMarkdownFile,
  ingestLocalRepository,
} from "../src/github-ingest.js";

test("findPrimaryMarkdownFile prefers README.md at the repository root", () => {
  const repoRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ux-library-repo-"));
  fs.writeFileSync(path.join(repoRoot, "README.md"), "# Root\n", "utf8");
  fs.mkdirSync(path.join(repoRoot, "docs"));
  fs.writeFileSync(path.join(repoRoot, "docs", "guide.md"), "# Guide\n", "utf8");

  assert.equal(findPrimaryMarkdownFile(repoRoot), path.join(repoRoot, "README.md"));
});

test("ingestLocalRepository passes through markdown content and sections", async () => {
  const repoRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ux-library-repo-"));
  const readme = [
    "### **Awesome UX** [![Awesome](https://example.com/badge.svg)](https://github.com/sindresorhus/awesome)",
    "",
    "A curated list of UX references.",
    "",
    "## Table of Contents",
    "",
    "- [Books](#books)",
    "",
    "## Books",
    "",
    "- About Face",
    "",
    "## Research",
    "",
    "- Measuring UX",
  ].join("\n");

  fs.writeFileSync(path.join(repoRoot, "README.md"), readme, "utf8");

  const result = await ingestLocalRepository({
    repoRoot,
    sourceUrl: "https://github.com/example/awesome-ux.git",
    splitSections: true,
  });

  assert.equal(result.metadata.title, "Awesome UX");
  assert.match(result.markdown, /^# Awesome UX/m);
  assert.doesNotMatch(result.markdown, /^## Table of Contents/m);
  assert.equal(result.sections.length, 2);
  assert.deepEqual(
    result.sections.map((section) => section.slug),
    ["books", "research"],
  );
});
