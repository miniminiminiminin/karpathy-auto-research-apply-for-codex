import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

import { writeCaptureOutput } from "../src/write-output.js";

test("writeCaptureOutput writes metadata and the root markdown file", async () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ux-library-write-"));
  const captureRoot = path.join(tempRoot, "capture");

  const result = await writeCaptureOutput({
    captureRoot,
    markdown: "# Title\n\nBody",
    metadata: {
      title: "Title",
      sourceUrl: "https://example.com",
    },
    sections: [],
  });

  assert.equal(result.indexPath, path.join(captureRoot, "index.md"));
  assert.equal(result.metaPath, path.join(captureRoot, "meta.json"));
  assert.equal(fs.readFileSync(result.indexPath, "utf8"), "# Title\n\nBody");

  const savedMetadata = JSON.parse(fs.readFileSync(result.metaPath, "utf8"));
  assert.equal(savedMetadata.title, "Title");
  assert.equal(savedMetadata.sourceUrl, "https://example.com");
});

test("writeCaptureOutput writes section files only when sections are provided", async () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ux-library-write-"));
  const captureRoot = path.join(tempRoot, "capture");

  const result = await writeCaptureOutput({
    captureRoot,
    markdown: "# Title\n\nBody",
    metadata: {
      title: "Title",
      sourceUrl: "https://example.com",
    },
    sections: [
      {
        slug: "principles",
        content: "## Principles\n\nKeep evidence close.",
      },
    ],
  });

  assert.equal(result.sectionPaths.length, 1);
  assert.equal(result.sectionPaths[0], path.join(captureRoot, "sections", "principles.md"));
  assert.equal(
    fs.readFileSync(result.sectionPaths[0], "utf8"),
    "## Principles\n\nKeep evidence close.",
  );
});

test("writeCaptureOutput removes stale section files before writing new ones", async () => {
  const tempRoot = fs.mkdtempSync(path.join(os.tmpdir(), "ux-library-write-"));
  const captureRoot = path.join(tempRoot, "capture");
  const staleSectionsRoot = path.join(captureRoot, "sections");

  fs.mkdirSync(staleSectionsRoot, { recursive: true });
  fs.writeFileSync(path.join(staleSectionsRoot, "old.md"), "stale", "utf8");

  const result = await writeCaptureOutput({
    captureRoot,
    markdown: "# Title\n\nBody",
    metadata: {
      title: "Title",
      sourceUrl: "https://example.com",
    },
    sections: [
      {
        slug: "fresh",
        content: "## Fresh\n\nBody",
      },
    ],
  });

  assert.equal(fs.existsSync(path.join(staleSectionsRoot, "old.md")), false);
  assert.deepEqual(result.sectionPaths, [path.join(staleSectionsRoot, "fresh.md")]);
});
