---
title: "Knockpy Command List"
date: 2026-01-05
category: commands
enrich: false
tags: knockpy, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Knockpy in penetration testing.
---

# Knockpy Command Guide

**Knockpy** is a Python3 tool designed to enumerate subdomains on a target domain through a wordlist. It also checks for zone transfers.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
knockpy domain.com
```
**Explanation:** Scans using standard internal wordlist.

### 2. Custom Wordlist
```bash
knockpy domain.com -w wordlist.txt
```
**Explanation:** Use your own list.

### 3. Zone Transfer Check
```bash
# (Automatic)
```
**Explanation:** Knockpy checks for Zone Transfers (AXFR) automatically at start.

### 4. Save JSON
```bash
knockpy domain.com --json
```
**Explanation:** Outputs detailed JSON.

### 5. Scan & CSV
```bash
knockpy domain.com --save folder
```
**Explanation:** Saves report to a specific folder.

### 6. Timeout
```bash
knockpy domain.com -t 5
```
**Explanation:** Set timeout for responses.

### 7. Check Wildcard
```bash
# (Automatic)
```
**Explanation:** Checks for wildcard DNS responses to reduce false positives.

### 8. Resolve IP
```bash
# (Default)
```
**Explanation:** Always resolves IP and shows server type.

### 9. Ignore HTTP codes
```bash
# (Depends on version args)
```
**Explanation:** Often used to ignore 404s.

### 10. Virustotal
```bash
knockpy domain.com --apikey ...
```
**Explanation:** (If supported by ver) Can query VT API.

## The Most Powerful Command
```bash
knockpy domain.com -w subdomains_big.txt --save scan_report
```
**Explanation:** Detailed enumeration using a massive wordlist with persistent reporting.

