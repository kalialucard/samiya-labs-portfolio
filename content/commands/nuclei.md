---
title: "Nuclei Command List"
date: 2026-01-05
category: commands
enrich: false
tags: nuclei, cybersecurity, command reference, beginner, web
description: Top 10 essential commands and a master guide for using Nuclei in penetration testing.
---

# Nuclei Command Guide

**Nuclei** is a template-based vulnerability scanner. It allows you to define complex vulnerabilities with simple YAML templates. It is arguably the most important modern scanner.

## Top 10 Useful Commands

### 1. Basic Scan (Templates)
```bash
nuclei -u http://target.com
```
**Explanation:** Scans target with default template set (finding misconfigs, simple CVEs).

### 2. Specific Template Directory
```bash
nuclei -u http://target.com -t cves/
```
**Explanation:** Scans using only templates in the `cves` folder.

### 3. Specific Template File
```bash
nuclei -u http://target.com -t cves/2021/CVE-2021-xxxx.yaml
```
**Explanation:** Checks for ONE specific vulnerability.

### 4. Severity Filter
```bash
nuclei -u http://target.com -s critical,high
```
**Explanation:** Only run templates tagged as Critical or High severity.

### 5. List Input
```bash
nuclei -l urls.txt
```
**Explanation:** Scans a list of URLs (mass scanning).

### 6. Rate Limit
```bash
nuclei -l urls.txt -rl 100
```
**Explanation:** 100 requests per second.

### 7. New Templates Only
```bash
nuclei -u target.com -nt
```
**Explanation:** Only runs templates added in the latest update.

### 8. Automatic Update
```bash
nuclei -update
```
**Explanation:** Updates the engine. `nuclei -ut` updates templates.

### 9. Output File
```bash
nuclei -u target.com -o results.txt
```
**Explanation:** Save findings.

### 10. Passive Scan
```bash
# (Technically nuclei is active, but can use passive templates)
```
**Explanation:** Some templates check passive leaks in responses.

## The Most Powerful Command
```bash
nuclei -l alive_subs.txt -t cves/ -t vulnerabilities/ -s critical,high,medium -rl 150 -o pwned.txt
```
**Explanation:** Mass scan a list of valid hosts for ALL known CVEs and Vulnerabilities of Medium+ severity at high speed.

