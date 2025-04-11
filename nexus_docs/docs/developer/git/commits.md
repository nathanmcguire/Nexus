---
sidebar_label: 'Commit Message Guidelines'
sidebar_position: 3
---
# Git Commit Message Guidelines

## Commit Message Guidelines
A good commit message tells the story of a change. Follow this format:

### Commit Structure
```
<type>: <short summary>

[optional body with additional context]
```

### Allowed Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes only
- `style`: Formatting or stylistic changes (no logic changes)
- `refactor`: Code changes that neither fix a bug nor add a feature
- `test`: Adding or fixing tests
- `chore`: Routine tasks

### Examples
- `feat: add forgot password flow`
- `fix: resolve null reference on login`
- `docs: update README with setup instructions`
- `refactor: simplify token refresh logic`

### Tips
- Keep summaries under 72 characters.
- Use the imperative mood (e.g., "fix" not "fixed").
- Don’t include unrelated changes in a single commit.

## Why This Matters
Following these conventions helps:
- Speed up code reviews
- Simplify changelog generation
- Improve collaboration across the team

Clear commits = better collaboration. Stick to the format.
