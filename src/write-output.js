import fs from "node:fs/promises";
import path from "node:path";

export async function writeCaptureOutput({
  captureRoot,
  markdown,
  metadata,
  sections = [],
}) {
  await fs.mkdir(captureRoot, { recursive: true });

  const indexPath = path.join(captureRoot, "index.md");
  const metaPath = path.join(captureRoot, "meta.json");

  await fs.writeFile(indexPath, markdown, "utf8");
  await fs.writeFile(metaPath, JSON.stringify(metadata, null, 2), "utf8");

  const sectionPaths = [];

  if (sections.length > 0) {
    const sectionsRoot = path.join(captureRoot, "sections");
    await fs.rm(sectionsRoot, { recursive: true, force: true });
    await fs.mkdir(sectionsRoot, { recursive: true });

    for (const section of sections) {
      const sectionPath = path.join(sectionsRoot, `${section.slug}.md`);
      await fs.writeFile(sectionPath, section.content, "utf8");
      sectionPaths.push(sectionPath);
    }
  } else {
    await fs.rm(path.join(captureRoot, "sections"), { recursive: true, force: true });
  }

  return {
    indexPath,
    metaPath,
    sectionPaths,
  };
}
