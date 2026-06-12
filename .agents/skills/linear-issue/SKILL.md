---
name: linear-issue
description: Pick up a Linear issue and work on it
argument-hint: "[issue-id, e.g. BCTT-738]"
allowed-tools: Bash, Read, Edit, Write, Glob, Grep, Skill
---

# Pick up a Linear issue and work on it

## Input

$ARGUMENTS — Linear issue identifier (e.g. BCTT-738 or BCOBS-1126) or a description to search for.

## Phase 1: Understand (no code changes)

1. **Find the issue**: Use Linear tools to look up the issue by ID or search for it. Display the issue title, description, status, priority, and any comments.

2. **Sync the repo and check for prior work**:
   - Run `git fetch origin` to get latest remote state
   - Check if a branch already exists for this issue: `git branch -a | grep -w <issue-id>` (use the exact issue number to avoid partial matches)
   - **If a branch exists**: Switch to it, run `git log --oneline main..HEAD` to see what's been done, review the diff. Summarise the current state to the user and ask how to proceed (continue, start fresh, or review).
   - **If no branch exists**: Ensure the default branch is current. Check what branch `origin/HEAD` points to — don't assume `main`. Confirm working tree is clean.
   - If there are uncommitted changes, stop and ask the user how to proceed.

3. **Explore the codebase**: Identify the files and components that would be affected. Read relevant files to understand the current state.

4. **Present a plan**: Summarise your understanding and proposed approach. Include:
   - **What the issue is asking for** (in your own words — flag any ambiguity)
   - **Files to change** (list specific files and what changes each needs)
   - **Approach** (how you'll implement it, any design decisions)
   - **Definition of done**:
     - `make html` must pass with no new warnings
     - Whether visual review is needed
     - Any acceptance criteria from the issue itself
   - **Questions or concerns**
   - **Estimated scope** (small/medium/large)

5. **Wait for approval**: Do NOT proceed until the user confirms the plan.

## Phase 2: Implement (after approval only)

6. **Create a branch**:
   - First ensure the default branch is current
   - Read the branch prefix from Codex.local.md. If not set, ask the user what prefix to use
   - Format: `prefix/<issue-id>-short-description`
   - Example: `chandimad/BCTT-738-review-flight-plan-todos`

7. **Update Linear**: Look up the available workflow states for this team first. Move the issue to the appropriate "in progress" state. Add a comment:
   ```
   Started work on branch `chandimad/BCTT-738-review-flight-plan-todos`

   Plan:
   - [brief summary of what will change]
   ```

8. **Implement the changes**: Follow all project rules. Use multiple commits if the work has logically separate steps.

9. **Validate**: Run the checks agreed in the definition of done. At minimum:
   - `make html` must pass with no new warnings
   - If validation fails: fix if straightforward, otherwise stop and discuss with the user.

10. **Commit**: Stage and commit with a clear message referencing the issue:
    - Example: `Review and update flight plan TODOs (BCTT-738)`

## Phase 3: Wrap up

11. **Update Linear**: Add a detailed comment to the issue:
    ```
    Changes complete on branch `chandimad/BCTT-738-review-flight-plan-todos`

    What changed:
    - [file1]: [what and why]
    - [file2]: [what and why]

    Validated:
    - [x] `make html` passes with no new warnings
    - [x] [other checks from definition of done]

    Open items:
    - [anything not done, follow-ups, or things to watch]
    ```
    Move the issue to the appropriate review/done state (check available states first).

12. **Next steps**: Tell the user clearly:
    - Whether a PR should be created (use `/linear-review` for this)
    - Whether there are open items or follow-up issues
    - Whether the issue is done or still needs work
