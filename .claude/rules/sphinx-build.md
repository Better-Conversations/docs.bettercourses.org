# Sphinx Build Rules

## Build commands
- Development autobuild (live reload): `./development_autobuild.sh`
- Development link check: `./development_linkcheck.sh`
- Production build: `./production_build.sh`
- Production link check: `./production_linkcheck.sh`
- Direct targets: `make html`, `make linkcheck`

## Before committing
- Run `make html` and check for new warnings or errors
- Common warnings to watch for:
  - `toctree contains reference to nonexisting document` — page was moved or deleted but toctree not updated
  - `document isn't included in any toctree` — orphaned page, add to an index
  - `undefined label` — cross-reference target doesn't exist
  - `duplicate label` — two pages define the same reference label

## Safety
- Do not edit generated build output (`build/`)
- Avoid changing anything in `source/_ignore/` unless explicitly asked
- Keep changes focused and minimal; prefer small, verifiable edits
