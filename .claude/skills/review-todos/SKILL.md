---
name: review-todos
description: Find all TODO directives and cross-reference with Linear issues
disable-model-invocation: true
allowed-tools: Bash, Read, Grep, Glob
---

# Review TODO directives

Find all `.. todo::` directives in the repo and cross-reference with Linear issues.

1. Search for all `.. todo::` directives across `source/` using Grep
2. Extract the Linear issue ID from each TODO (e.g. `BCOBS-1126`, `BCTT-738`)
3. For each issue ID found, look up the current status in Linear
4. Report a summary table:
   - File and line number
   - TODO text
   - Linear issue ID (if referenced)
   - Current Linear status (Done, In Progress, Todo, etc.)
   - Recommendation: keep, update, or remove
5. Flag any TODOs that:
   - Reference completed issues (should be removed or updated)
   - Have no issue ID (should get one or be reviewed)
   - Reference issues that don't exist in Linear
6. Report the total count and how many need attention
