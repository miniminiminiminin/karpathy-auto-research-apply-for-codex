import TurndownService from "turndown";

import { slugifySegment } from "./config.js";

const turndown = new TurndownService({
  headingStyle: "atx",
  codeBlockStyle: "fenced",
  bulletListMarker: "-",
});

export function convertHtmlToMarkdown(html) {
  return turndown
    .turndown(html)
    .replace(/^- {2,}/gm, "- ")
    .trim();
}

export function splitMarkdownIntoSections(markdown) {
  const lines = markdown.split("\n");
  const sections = [];
  let current = null;

  for (const line of lines) {
    if (line.startsWith("## ")) {
      if (current) {
        current.content = current.content.trim();
        sections.push(current);
      }

      const title = line.replace(/^## /, "").trim();
      current = {
        title,
        slug: slugifySegment(title),
        content: `${line}\n`,
      };
      continue;
    }

    if (current) {
      current.content += `${line}\n`;
    }
  }

  if (current) {
    current.content = current.content.trim();
    sections.push(current);
  }

  return sections;
}
