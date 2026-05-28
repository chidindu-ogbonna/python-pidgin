---
name: release-python-package
description: Automates the version bump and release workflow for Python packages, including git tagging and GitHub Actions PyPI publishing setup.
---

# Python Package Release Workflow

Use this skill whenever the user asks to "release", "deploy", or "publish" a Python package (e.g., "deploy/release this as v1.1.0" or "release a new version").

## Workflow Steps

### 1. Version Bump
1. Identify the new version the user wants (or ask them if not specified).
2. Update the version string in `pyproject.toml` (under `[project] version = "X.Y.Z"`) or `setup.py`.

### 2. GitHub Actions Setup (If Missing)
1. Check if a deployment workflow exists (e.g., `.github/workflows/publish.yml`).
2. If it does not exist, create it with a standard PyPA PyPI publish action (using Trusted Publishers):
   - It should trigger on `release: types: [published]` or pushed tags.
   - It requires `id-token: write` and `contents: read` permissions.
   - It should use `actions/checkout`, `actions/setup-python`, run `python -m build`, and use `pypa/gh-action-pypi-publish`.

### 3. Git Commit and Tag
1. Stage the modified files (like `pyproject.toml`).
2. Commit the changes with a standard message: `git commit -m "chore: release vX.Y.Z"`
3. Tag the new release: `git tag vX.Y.Z`

### 4. User Communication
1. Summarize the actions taken (version bump, commit, and tag).
2. Instruct the user to push the changes: `git push origin main && git push origin --tags`.
3. If setting up GitHub Actions for the first time, remind the user to configure PyPI Trusted Publishers for their GitHub repository in their PyPI account.
