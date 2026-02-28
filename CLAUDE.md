# CLAUDE.md

See [AGENTS.md](AGENTS.md) for repository structure, build commands, and authoring rules.

## Project Plans

There are two levels of plan:

1. **High-level plans** exist as both Linear documents (in the relevant project) and local files in `.claude/plans/`. These must be kept in sync. When starting a session, compare the Linear version and the local version — if they differ, ask the user which one to use before proceeding.
2. **Branch/task plans** are working plans for specific issues or branches. These live in `.claude/plans/` only and do not need a Linear counterpart.

**Naming convention:** Use descriptive names including the issue ID where relevant, e.g.:
- `project-review-2026-02-28.md` (high-level)
- `BCTT-607-restructure-completion.md` (task plan)
- `BCOBS-1126-co-facilitation-pattern.md` (task plan)

## External References

Issue tracking, team structure, and project details are documented in the team plan (stored in Linear and locally in `.claude/plans/`). Keep Linear-specific details there rather than in this repo — the repo should be self-contained for anyone building and contributing to the documentation.

## Conventions

- Use `.. todo::` directives to mark planned work, referencing Linear issue IDs where possible (e.g., `BCOBS-1126: Description`)
- Pattern pages follow the template at `source/documentation/patterns/pattern-template.rst`
- Patterns and guidance notes are separate sections but should cross-reference each other
- The 4 empty pattern categories (roles, exercises, timing, visual-technical) are deferred — focus on core-delivery patterns
