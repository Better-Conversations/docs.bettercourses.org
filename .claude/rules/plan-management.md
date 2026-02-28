# Plan Management

## Two levels of plan

1. **High-level plans** exist as both Linear documents (in the relevant project) and local files in this repo's `.claude/plans/` directory (not the global `~/.claude/plans/`). These must be kept in sync.
2. **Branch/task plans** are working plans for specific issues or branches. These live in this repo's `.claude/plans/` only and do not need a Linear counterpart.

## Session start
- Compare the Linear version and local version of any high-level plan
- If they differ, ask the user which one to use before proceeding

## Naming convention
Use descriptive names including the issue ID where relevant:
- `project-review-2026-02-28.md` (high-level)
- `BCTT-607-restructure-completion.md` (task plan)
- `BCOBS-1126-co-facilitation-pattern.md` (task plan)

## External references
Issue tracking, team structure, and project details are documented in the team plan (stored in Linear and locally in `.claude/plans/`). Keep Linear-specific details there rather than in this repo — the repo should be self-contained for anyone building and contributing to the documentation.
