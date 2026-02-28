# Authoring Rules

- Put new content under `source/documentation/...` in the most relevant section
- Add new pages to the appropriate `index.rst` `toctree` — orphaned pages cause build warnings
- Use RST (`.rst`) for structured docs and MyST (`.md`) where simpler formatting suffices
- For LLMS summaries: RST uses `.. summary::`, Markdown uses `<!--summary: ... -->`
- For controlled document metadata, use the `qms_header` directive pattern shown in `README.md`
- Reuse templates when creating new docs:
  - Patterns: `source/documentation/patterns/pattern-template.rst`
  - Insights: `source/documentation/insights/insight-template.rst`
  - Guides: `source/documentation/guides/guides-template.rst`
