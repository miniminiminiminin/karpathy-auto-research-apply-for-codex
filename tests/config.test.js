import test from "node:test";
import assert from "node:assert/strict";
import path from "node:path";

import {
  createCapturePaths,
  getRepoRoot,
  resolveOutputRoot,
} from "../src/config.js";

test("resolveOutputRoot defaults to the repository resources directory", () => {
  const repoRoot = getRepoRoot();
  const outputRoot = resolveOutputRoot();

  assert.equal(outputRoot, path.join(repoRoot, "resources"));
});

test("resolveOutputRoot resolves relative output paths from the repository root", () => {
  const repoRoot = getRepoRoot();
  const outputRoot = resolveOutputRoot("custom/library");

  assert.equal(outputRoot, path.join(repoRoot, "custom/library"));
});

test("resolveOutputRoot preserves absolute output paths", () => {
  const absolutePath = path.join(process.cwd(), "tmp/output");

  assert.equal(resolveOutputRoot(absolutePath), absolutePath);
});

test("createCapturePaths produces a stable collection layout", () => {
  const outputRoot = resolveOutputRoot();
  const paths = createCapturePaths({
    outputRoot,
    collection: "ux/awesome-ux",
    sourceSlug: "github-awesome-ux",
  });

  assert.equal(paths.collectionRoot, path.join(outputRoot, "ux/awesome-ux"));
  assert.equal(paths.captureRoot, path.join(outputRoot, "ux/awesome-ux", "github-awesome-ux"));
});

test("createCapturePaths avoids duplicate nesting when the collection leaf matches the source slug", () => {
  const outputRoot = resolveOutputRoot();
  const paths = createCapturePaths({
    outputRoot,
    collection: "ux/awesome-ux",
    sourceSlug: "awesome-ux",
  });

  assert.equal(paths.captureRoot, path.join(outputRoot, "ux/awesome-ux"));
});
