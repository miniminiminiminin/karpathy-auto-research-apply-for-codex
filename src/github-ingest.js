import fs from "node:fs/promises";
import fsSync from "node:fs";
import path from "node:path";
import os from "node:os";
import { execFile } from "node:child_process";
import { promisify } from "node:util";

import { splitMarkdownIntoSections } from "./markdown.js";
import { slugifySegment } from "./config.js";

const execFileAsync = promisify(execFile);

export function findPrimaryMarkdownFile(repoRoot) {
  const candidates = [
    path.join(repoRoot, "README.md"),
    path.join(repoRoot, "readme.md"),
    path.join(repoRoot, "docs", "README.md"),
    path.join(repoRoot, "docs", "index.md"),
  ];

  for (const candidate of candidates) {
    try {
      if (candidate && requireFile(candidate)) {
        return candidate;
      }
    } catch {
      continue;
    }
  }

  throw new Error(`No primary markdown file found in ${repoRoot}`);
}

function requireFile(filePath) {
  return path.extname(filePath).toLowerCase() === ".md";
}

export async function ingestLocalRepository({ repoRoot, sourceUrl, splitSections }) {
  const markdownPath = findPrimaryMarkdownFile(repoRoot);
  const rawMarkdown = await fs.readFile(markdownPath, "utf8");
  const markdown = normalizeRepositoryMarkdown(rawMarkdown);
  const lines = markdown.split("\n");
  const firstHeading = lines.find((line) => /^#{1,6}\s+/.test(line));
  const title = firstHeading
    ? firstHeading.replace(/^#{1,6}\s+/, "").trim()
    : path.basename(repoRoot);
  const sections = splitSections ? splitMarkdownIntoSections(markdown) : [];

  return {
    markdown,
    sections,
    metadata: {
      title,
      sourceUrl,
      sourceType: "github",
      fetchedAt: new Date().toISOString(),
      sourceFile: path.relative(repoRoot, markdownPath),
    },
  };
}

export function normalizeRepositoryMarkdown(markdown) {
  let cleaned = markdown.replace(/\r\n/g, "\n");

  cleaned = cleaned.replace(
    /^#{1,6}\s+\*\*(.+?)\*\*.*$/m,
    (_, title) => `# ${title.trim()}`,
  );

  cleaned = cleaned.replace(
    /## Table of Contents[\s\S]*?(?=\n##\s)/m,
    "",
  );

  cleaned = cleaned.replace(
    /<p align="center">[\s\S]*?<\/p>/gm,
    "",
  );

  cleaned = cleaned.replace(
    /\[([^\]]+)\]\s+\((https?:\/\/[^)]+)\)/g,
    "[$1]($2)",
  );

  cleaned = cleaned.replace(
    /(\.\s*)-\s+\[Website wireframes: Mockingbird\]/g,
    ".\n- [Website wireframes: Mockingbird]",
  );

  cleaned = cleaned.replace(/\n{3,}/g, "\n\n");

  return cleaned.trim();
}

export async function cloneRepository(sourceUrl) {
  const tempRoot = await fs.mkdtemp(path.join(os.tmpdir(), "ux-library-clone-"));
  const repoName = slugifySegment(path.basename(sourceUrl).replace(/\.git$/, ""));
  const cloneRoot = path.join(tempRoot, repoName);

  await execFileAsync("git", ["clone", "--depth", "1", sourceUrl, cloneRoot]);

  return {
    tempRoot,
    cloneRoot,
  };
}

export function isLocalRepositoryPath(target) {
  return Boolean(target) && fsSync.existsSync(target) && fsSync.statSync(target).isDirectory();
}
