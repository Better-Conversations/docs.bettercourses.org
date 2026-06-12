---
name: check-build
description: Run Sphinx build and report warnings/errors
disable-model-invocation: true
allowed-tools: Bash, Read, Grep
---

# Check Sphinx build

Run `make html` and report any warnings or errors.

1. Run `make html 2>&1` and capture all output
2. Filter for lines containing `WARNING` or `ERROR`
3. Group warnings by type:
   - **Orphaned pages** — pages not in any toctree
   - **Broken references** — undefined labels or missing documents
   - **Duplicate labels** — same reference defined in multiple places
   - **Other** — any remaining warnings
4. For each warning, identify the source file and suggest a fix
5. Report the total count and whether the build succeeded
