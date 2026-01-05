---
title: Tmux Command List
date: 2026-01-05
category: commands
enrich: false
tags: tmux, cybersecurity, command reference
description: Top 10 essential commands for tmux.
---

# Tmux Command Guide

**Tmux** is a terminal multiplexer.

## Top 10 Useful Commands (Prefix usually Ctrl+B)

### 1. New Session
```bash
tmux new -s hacking
```
**Explanation:** Create named session.

### 2. Detach
```bash
(Ctrl+B then d)
```
**Explanation:** Leave session running in background.

### 3. Attach
```bash
tmux a -t hacking
```
**Explanation:** Re-join session.

### 4. List Sessions
```bash
tmux ls
```
**Explanation:** See active sessions.

### 5. Split Vertical
```bash
(Ctrl+B then %)
```
**Explanation:** Split pane left/right.

### 6. Split Horizontal
```bash
(Ctrl+B then ")
```
**Explanation:** Split pane top/bottom.

### 7. New Window
```bash
(Ctrl+B then c)
```
**Explanation:** Create new tab/window.

### 8. Navigate Panes
```bash
(Ctrl+B then Arrows)
```
**Explanation:** Move focus.

### 9. Kill Pane
```bash
(Ctrl+B then x)
```
**Explanation:** Close current pane.

### 10. Rename Window
```bash
(Ctrl+B then ,)
```
**Explanation:** Rename tab.

## The Most Powerful Command
```bash
tmux a || tmux new -s main
```
**Explanation:** Attach to existing session or create a new one (shell alias).

