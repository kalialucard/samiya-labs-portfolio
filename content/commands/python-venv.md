---
title: Python-venv Command List
date: 2026-01-05
category: commands
enrich: false
tags: python-venv, cybersecurity, command reference, infrastructure
description: Top 10 essential commands for python-venv.
---

# Python Venv Command Guide

**Venv** creates isolated Python environments.

## Top 10 Useful Commands

### 1. Create Env
```bash
python3 -m venv myenv
```
**Explanation:** Create 'myenv' folder.

### 2. Activate (Linux)
```bash
source myenv/bin/activate
```
**Explanation:** Enter the environment.

### 3. Activate (Windows)
```bash
myenv\Scripts\activate
```
**Explanation:** Enter on Windows.

### 4. Install Package
```bash
pip install requests
```
**Explanation:** Install into isolated env only.

### 5. Freeze
```bash
pip freeze > requirements.txt
```
**Explanation:** Save dependency list.

### 6. Install from File
```bash
pip install -r requirements.txt
```
**Explanation:** Restore dependencies.

### 7. Deactivate
```bash
deactivate
```
**Explanation:** Exit environment.

### 8. Check Path
```bash
which python
```
**Explanation:** Verify you are using the venv python.

### 9. Delete Env
```bash
rm -rf myenv/
```
**Explanation:** Delete the folder to remove env.

### 10. Upgrade Pip
```bash
pip install --upgrade pip
```
**Explanation:** Update pip inside env.

## The Most Powerful Command
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt
```
**Explanation:** The standard "bootstrapping" one-liner for any Python project.

