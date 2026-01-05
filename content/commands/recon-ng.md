---
title: "Recon-Ng Command List"
date: 2026-01-05
category: commands
enrich: false
tags: recon-ng, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Recon-Ng in penetration testing.
---

# Recon-ng Command Guide

**Recon-ng** is a full-featured Web Reconnaissance framework written in Python. It looks and feels like Metasploit (modules, database, workspaces).

## Top 10 Useful Commands

### 1. Start Tool
```bash
recon-ng
```
**Explanation:** Enters the interactive shell.

### 2. Create Workspace
```bash
[recon-ng] > workspaces create google
```
**Explanation:** Isolates data into a project named "google".

### 3. Add Domain
```bash
[recon-ng] > db insert domains
```
**Explanation:** Manually add a target domain to the database.

### 4. Search Modules
```bash
[recon-ng] > modules search hackertarget
```
**Explanation:** Finds modules related to "hackertarget".

### 5. Load Module
```bash
[recon-ng] > modules load recon/domains-hosts/hackertarget
```
**Explanation:** Selects the module for use.

### 6. Run Module
```bash
[hackertarget] > run
```
**Explanation:** Executes the loaded module against DB targets.

### 7. Show Hosts
```bash
[recon-ng] > show hosts
```
**Explanation:** Displays all collected host data (subdomains).

### 8. Add Keys
```bash
[recon-ng] > keys add shodan_api <key>
```
**Explanation:** Adds API keys for modules that require them.

### 9. Install Modules
```bash
[recon-ng] > marketplace install all
```
**Explanation:** Installs all available community modules.

### 10. Generate Report
```bash
[recon-ng] > modules load reporting/html
[html] > run
```
**Explanation:** Generates an HTML report of findings.

## The Most Powerful Command
```bash
(Inside Recon-ng) marketplace install all; workspaces create target; db insert domains target.com; modules load recon/domains-hosts/*; run
```
**Explanation:** In concept: Install everything, set target, and run ALL domain discovery modules to aggregate massive data.

