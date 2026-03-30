import test from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";

import { extractPrimaryHtml } from "../src/extract.js";
import { convertHtmlToMarkdown, splitMarkdownIntoSections } from "../src/markdown.js";

const fixturePath = path.join(process.cwd(), "tests/fixtures/sample-article.html");
const fixtureHtml = fs.readFileSync(fixturePath, "utf8");

test("extractPrimaryHtml prefers the article content and removes navigation noise", () => {
  const extracted = extractPrimaryHtml(fixtureHtml);

  assert.match(extracted, /Design Systems Need Operating Rules/);
  assert.doesNotMatch(extracted, /Related Links/);
  assert.doesNotMatch(extracted, /Copyright footer noise/);
  assert.doesNotMatch(extracted, /Home/);
});

test("convertHtmlToMarkdown preserves headings, links, lists, and code blocks", () => {
  const extracted = extractPrimaryHtml(fixtureHtml);
  const markdown = convertHtmlToMarkdown(extracted);

  assert.match(markdown, /^# Design Systems Need Operating Rules/m);
  assert.match(markdown, /\[why rules exist\]\(https:\/\/example\.com\/rules\)/);
  assert.match(markdown, /- Prefer clarity over taste\./);
  assert.match(markdown, /```[\s\S]*const score = evaluateDesign\(input\);[\s\S]*```/m);
});

test("splitMarkdownIntoSections emits deterministic section files", () => {
  const extracted = extractPrimaryHtml(fixtureHtml);
  const markdown = convertHtmlToMarkdown(extracted);
  const sections = splitMarkdownIntoSections(markdown);

  assert.equal(sections.length, 2);
  assert.deepEqual(
    sections.map((section) => section.slug),
    ["principles", "code-example"],
  );
  assert.match(sections[0].content, /^## Principles/m);
  assert.match(sections[1].content, /^## Code Example/m);
});
