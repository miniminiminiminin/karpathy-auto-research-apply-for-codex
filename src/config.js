import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const repoRoot = path.resolve(__dirname, "..");

export function getRepoRoot() {
  return repoRoot;
}

export function resolveOutputRoot(outPath) {
  if (!outPath) {
    return path.join(repoRoot, "resources");
  }

  if (path.isAbsolute(outPath)) {
    return outPath;
  }

  return path.join(repoRoot, outPath);
}

export function slugifySegment(value) {
  return value
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .replace(/-{2,}/g, "-");
}

export function createCapturePaths({ outputRoot, collection, sourceSlug }) {
  const normalizedCollection = collection
    ? collection.split("/").filter(Boolean).join(path.sep)
    : "";
  const collectionRoot = normalizedCollection
    ? path.join(outputRoot, normalizedCollection)
    : outputRoot;
  const collectionLeaf = path.basename(collectionRoot);
  const captureRoot =
    collectionLeaf === sourceSlug
      ? collectionRoot
      : path.join(collectionRoot, sourceSlug);

  return {
    outputRoot,
    collectionRoot,
    captureRoot,
  };
}
