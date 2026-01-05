---
title: "Dirsearch Command List"
date: 2026-01-05
category: commands
enrich: false
tags: dirsearch, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Dirsearch in penetration testing.
---

# Dirsearch Command Guide

**Dirsearch** is a mature, command-line web path scanner (brute-forcer) written in Python. It's known for its colorful output and smart heuristic detection.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
python3 dirsearch.py -u http://target.com
```
**Explanation:** Default scan using the built-in dictionary.

### 2. Custom Extensions
```bash
dirsearch -u http://target.com -e php,html,js
```
**Explanation:** Scans for specific extensions (`-e`).

### 3. Specific Wordlist
```bash
dirsearch -u http://target.com -w /path/to/wordlist.txt
```
**Explanation:** Uses a custom wordlist (`-w`).

### 4. Exclude Status Codes
```bash
dirsearch -u http://target.com -x 403,404,500
```
**Explanation:** Excludes specific HTTP status codes (`-x`) from the output.

### 5. Recursive Scan
```bash
dirsearch -u http://target.com -r --deep-recursive
```
**Explanation:** recursively scans found directories.

### 6. Threads
```bash
dirsearch -u http://target.com -t 50
```
**Explanation:** Increases threads (`-t`) to 50 for speed.

### 7. Random User Agent
```bash
dirsearch -u http://target.com --random-agent
```
**Explanation:** Randomizes the User-Agent header to evade WAFs.

### 8. Cookie/Auth
```bash
dirsearch -u http://target.com --cookie "SessionId=123"
```
**Explanation:** Scans as an authenticated user.

### 9. Simple Report
```bash
dirsearch -u http://target.com --simple-report=report.txt
```
**Explanation:** Saves a simplified text report.

### 10. Subdirs
```bash
dirsearch -u http://target.com --subdirs admin/,backup/
```
**Explanation:** Forces scanning specific subdirectories.

## The Most Powerful Command
```bash
dirsearch -u http://target.com -e php,html,js -x 400,403,404,500 -t 50 --random-agent -o report.json
```
**Explanation:** A fast, evasive, and clean scan that ignores error pages and output JSON.

