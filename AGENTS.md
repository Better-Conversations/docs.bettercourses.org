# AGENTS.md

## Purpose
This repository contains the source for `https://docs.bettercourses.org`, built with Sphinx and the PyData theme.

## Technology
- Python + Sphinx documentation site
- MyST enabled (`.md` and `.rst` sources are both supported)
- Custom Sphinx extensions in `source/_ext/`
- Cloudflare Pages Functions in `functions/` for stable redirects

## Key Directories
- `source/`: documentation source content
- `source/documentation/`: main docs tree grouped by topic
- `source/_static/`: CSS, JavaScript, and images
- `source/_templates/`: custom theme templates
- `source/_ext/`: custom Sphinx extensions (`qms_header`, `llms`)
- `functions/l/[id].js`: stable link redirect map (`/l/:id`)
- `functions/bc/[id].js`: `/bc/:id` redirect handler
- `scripts/`: Typesense indexing helpers

## Environment Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`

## Build And Validation Commands
- Development autobuild (with live reload):
  - `./development_autobuild.sh`
- Development link check:
  - `./development_linkcheck.sh`
- Production-style build:
  - `./production_build.sh`
- Production external link checks:
  - `./production_linkcheck.sh`
- Direct Sphinx targets:
  - `make html`
  - `make linkcheck`

## Deployment
Deployment is handled by GitHub Actions (`.github/workflows/main.yml`):
- On push to `main` (or manual `workflow_dispatch`), the `build` job builds the
  Sphinx site to `build/html/` via `production_build.sh` and uploads it as the
  `html-build` artifact.
- The `deploy` job (gated to `main`, runs in the `deploy` environment) downloads
  that artifact and `rsync`s it over SSH to
  `docs-bettercourses@crumpet.amphora.cloud:public_html/` on port `1970`.
- SSH auth uses the private key from the `CRUMPET_ACCOUNT_SSH_KEY` secret (written
  to `~/.ssh/crumpet_key` at runtime); `StrictHostKeyChecking=no` is set.
- Caddy on `crumpet.amphora.cloud` serves the site from `public_html`.

## Authoring Rules
- Put new content under `source/documentation/...` in the most relevant section.
- Add new pages to the appropriate `index.rst` `toctree`; otherwise they are easy to orphan.
- Reuse templates when creating new docs:
  - `source/documentation/patterns/pattern-template.rst`
  - `source/documentation/insights/insight-template.rst`
  - `source/documentation/guides/guides-template.rst`
- For LLMS summaries:
  - RST: add `.. summary::`
  - Markdown: add `<!--summary: ... -->`
- For controlled document metadata blocks, use the `qms_header` directive pattern shown in `README.md`.

## Redirect And Stable Link Maintenance
- If you add or change a stable link in `source/stable-links.rst`, keep `functions/l/[id].js` in sync.
- Validate redirect targets after updates.

## Safety And Scope
- Do not edit generated build output (`build/`) unless explicitly asked.
- Avoid changing anything in `source/_ignore/` unless the task explicitly requires it.
- Keep changes focused and minimal; prefer small, verifiable edits.
