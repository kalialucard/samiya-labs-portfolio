---
title: Gh Command List
date: 2026-01-05
category: commands
enrich: false
tags: gh, cybersecurity, command reference
description: Top 10 essential commands for gh.
---

# GitHub CLI Command Guide

**gh** is GitHub on the command line.

## Top 10 Useful Commands

### 1. Login
```bash
gh auth login
```
**Explanation:** Authenticate via web or token.

### 2. Clone
```bash
gh repo clone owner/repo
```
**Explanation:** Clone without needing full URL.

### 3. Create Repo
```bash
gh repo create my-project --public
```
**Explanation:** Create a new repo on GitHub.

### 4. Create Issue
```bash
gh issue create --title "Bug" --body "Details"
```
**Explanation:** File an issue.

### 5. Create PR
```bash
gh pr create
```
**Explanation:** Create a Pull Request from current branch.

### 6. Check PRs
```bash
gh pr list
```
**Explanation:** See open PRs.

### 7. View Gist
```bash
gh gist view <id>
```
**Explanation:** Read a gist.

### 8. Create Gist
```bash
gh gist create secret.txt
```
**Explanation:** Shared snippet.

### 9. Repo View
```bash
gh repo view
```
**Explanation:** Open standard browser to repo.

### 10. Check Status
```bash
gh status
```
**Explanation:** See notifications/PRs.

## The Most Powerful Command
```bash
gh repo fork owner/repo --clone
```
**Explanation:** Fork a repo and clone it to your machine in one step.

