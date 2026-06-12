---
name: new-pattern
description: Scaffold a new pattern page from the template
argument-hint: "[pattern-name, e.g. co-facilitation]"
allowed-tools: Bash, Read, Edit, Write, Glob, Grep
---

# Create a new pattern page

Scaffold a new pattern page under `source/documentation/patterns/core-delivery/`.

1. **Read the template**: Read `source/documentation/patterns/pattern-template.rst` to understand the structure
2. **Create the file**: Create `source/documentation/patterns/core-delivery/$ARGUMENTS.rst` based on the template
   - Replace placeholder title with the pattern name (title case)
   - Add a `.. todo::` directive referencing the relevant Linear issue if known
   - Set up the standard sections from the template
3. **Update the toctree**: Add the new page to `source/documentation/patterns/core-delivery/index.rst`
4. **Verify the build**: Run `make html` and check for no new warnings
5. **Report**: Show the user the created file and suggest next steps (fill in content, create Linear issue if needed)
