# UX Library CLI And Awesome UX Ingestion Implementation Plan

> **For agentic workers:** REQUIRED: Use the repo-local orchestration or execution path that owns this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a reusable CLI that captures rendered HTML content into Markdown under `resources/` and use it to create an initial curated UX library from `awesome-ux`.

**Architecture:** Add a small Node.js CLI with one rendering path based on Playwright and one normalization path that extracts `main` or `article` content, cleans navigation noise, converts HTML to Markdown, and writes source metadata plus Markdown files into a target directory. Keep repo acquisition separate from content extraction so the CLI can capture direct URLs now and later extend to repository and site ingestion without rewriting the markdown pipeline.

**Tech Stack:** Node.js ESM, Playwright, Cheerio, Turndown, built-in `node:test`

---

### Task 1: Scaffold the CLI workspace and path contract

**Files:**
- Create: `package.json`
- Create: `package-lock.json`
- Create: `src/cli.js`
- Create: `src/config.js`
- Create: `tests/config.test.js`
- Modify: `.gitignore`

**Step 1: Write the failing config-path tests**

- [ ] Add tests in `tests/config.test.js` for:
  - default output root resolving to `<repo>/resources`
  - relative `--out` resolving from repo root
  - absolute `--out` being preserved
  - nested resource collection paths being created predictably

**Step 2: Run the config tests to verify they fail**

- [ ] Run: `npm test -- --test-name-pattern="config"`
- [ ] Expected signal: failure because CLI config helpers do not exist yet

**Step 3: Implement the minimal config and CLI argument parsing**

- [ ] Create `src/config.js` with repo-root detection, output-path resolution, and source-slug helpers
- [ ] Create `src/cli.js` with subcommand parsing for URL capture and section splitting options

**Step 4: Run the config tests to verify they pass**

- [ ] Run: `npm test -- --test-name-pattern="config"`
- [ ] Expected signal: the config tests pass

**Step 5: Clean stop point**

- [ ] Stop when path resolution and CLI defaults are stable without implementing network capture yet

### Task 2: Lock the HTML-to-Markdown normalization pipeline with tests first

**Files:**
- Create: `src/extract.js`
- Create: `src/markdown.js`
- Create: `tests/fixtures/sample-article.html`
- Create: `tests/extract.test.js`

**Step 1: Write the failing extraction tests**

- [ ] Add tests that prove:
  - `main` or `article` content is preferred over full-body extraction
  - `nav`, `footer`, and repeated sidebars are removed
  - headings, lists, links, and code blocks survive Markdown conversion
  - `--split-sections` produces deterministic section fragments

**Step 2: Run the extraction tests to verify they fail**

- [ ] Run: `npm test -- --test-name-pattern="extract"`
- [ ] Expected signal: failure because extraction and markdown modules do not exist yet

**Step 3: Implement the minimal normalization pipeline**

- [ ] Create `src/extract.js` with DOM cleanup and content selection
- [ ] Create `src/markdown.js` with Turndown conversion and optional section splitting

**Step 4: Run the extraction tests to verify they pass**

- [ ] Run: `npm test -- --test-name-pattern="extract"`
- [ ] Expected signal: the extraction tests pass

**Step 5: Clean stop point**

- [ ] Stop when fixture HTML converts into clean Markdown and section splitting is deterministic

### Task 3: Add rendered-page capture and file writing

**Files:**
- Create: `src/capture.js`
- Create: `src/write-output.js`
- Create: `tests/write-output.test.js`
- Modify: `src/cli.js`

**Step 1: Write the failing output tests**

- [ ] Add tests for:
  - metadata plus markdown files written under the resolved collection path
  - overwrite-safe file naming for repeated captures
  - section files generated only when requested

**Step 2: Run the output tests to verify they fail**

- [ ] Run: `npm test -- --test-name-pattern="write-output"`
- [ ] Expected signal: failure because file-writing helpers do not exist yet

**Step 3: Implement capture and write modules**

- [ ] Create `src/capture.js` using Playwright to load a URL, wait for network idle, and return rendered HTML plus page metadata
- [ ] Create `src/write-output.js` to save `meta.json`, `index.md`, and optional section markdown files
- [ ] Wire the capture command in `src/cli.js`

**Step 4: Run focused tests and one local smoke check**

- [ ] Run: `npm test`
- [ ] Run: `node src/cli.js capture-url https://example.com --collection smoke-test`
- [ ] Expected signal: tests pass and `resources/smoke-test/...` is created with markdown output

**Step 5: Clean stop point**

- [ ] Stop when the CLI can capture one live URL into the default resources root

### Task 4: Ingest and curate the initial `awesome-ux` library slice

**Files:**
- Create: `src/github-ingest.js`
- Create: `tests/github-ingest.test.js`
- Modify: `src/cli.js`
- Create: `resources/ux/awesome-ux/README.md`
- Create: `resources/ux/awesome-ux/meta.json`
- Create additional curated markdown files under `resources/ux/awesome-ux/sections/`

**Step 1: Write the failing repo-ingest tests**

- [ ] Add tests for:
  - repository clone path resolution into a temp workspace
  - markdown source passthrough when the upstream content is already markdown
  - curated section export from a long README

**Step 2: Run the repo-ingest tests to verify they fail**

- [ ] Run: `npm test -- --test-name-pattern="github-ingest"`
- [ ] Expected signal: failure because repository ingestion helpers do not exist yet

**Step 3: Implement the minimal repository ingestion path**

- [ ] Create `src/github-ingest.js` to clone a repository into a temp directory, read the primary README or docs entry, and reuse the existing markdown writing pipeline
- [ ] Add a `capture-github` command in `src/cli.js`

**Step 4: Use the CLI plus browser inspection to build the first UX library slice**

- [ ] Clone `https://github.com/batoreh/awesome-ux.git`
- [ ] Inspect the repository and rendered GitHub page as needed to decide which sections are signal versus link dump
- [ ] Save a cleaned root markdown file and section files under `resources/ux/awesome-ux/`

**Step 5: Verify the curated result**

- [ ] Run: `npm test`
- [ ] Run: `node src/cli.js capture-github https://github.com/batoreh/awesome-ux.git --collection ux/awesome-ux --split-sections`
- [ ] Expected signal: tests pass and `resources/ux/awesome-ux/` contains readable, source-attributed markdown

### Task 5: Document usage and final verification

**Files:**
- Modify: `README.md`

**Step 1: Add the CLI usage section**

- [ ] Document install, browser setup, capture commands, output structure, and the `awesome-ux` example

**Step 2: Run end-to-end verification**

- [ ] Run: `npm test`
- [ ] Run: `node src/cli.js capture-url https://example.com --collection smoke-test`
- [ ] Run: `node src/cli.js capture-github https://github.com/batoreh/awesome-ux.git --collection ux/awesome-ux --split-sections`
- [ ] Expected signal: all commands succeed and outputs are present under `resources/`

**Step 3: Clean stop point**

- [ ] Stop when the CLI is documented, tests pass, and the initial UX library slice is checked into `resources/`
