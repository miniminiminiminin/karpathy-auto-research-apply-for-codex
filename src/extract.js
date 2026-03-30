import * as cheerio from "cheerio";

const NOISE_SELECTORS = [
  "nav",
  "footer",
  "aside",
  "[role='navigation']",
  ".sidebar",
  ".toc",
  ".table-of-contents",
];

export function extractPrimaryHtml(html) {
  const $ = cheerio.load(html);

  for (const selector of NOISE_SELECTORS) {
    $(selector).remove();
  }

  const primaryNode =
    $("main article").first() ||
    $("article").first() ||
    $("main").first() ||
    $("body").first();

  const selected = primaryNode.length > 0 ? primaryNode : $("body").first();

  return selected.html()?.trim() ?? "";
}
