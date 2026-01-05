---
title: "Waybackurls Command List"
date: 2026-01-05
category: commands
enrich: false
tags: waybackurls, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Waybackurls in penetration testing.
---

# Waybackurls Command Guide

**Waybackurls** (by TomNomNom) fetches all the URLs that the Wayback Machine knows about for a domain.

## Top 10 Useful Commands

### 1. Basic Usage
```bash
echo example.com | waybackurls
```
**Explanation:** Fetch everything for domain.

### 2. Include Subdomains
```bash
echo example.com | waybackurls -no-subs
```
**Explanation:** (Confusion: default usually gets subs if wildcarded, tool is simple). Note: Default gets known URLs.

### 3. User Filter
```bash
# Pipe to grep
echo example.com | waybackurls | grep "admin"
```
**Explanation:** Filter for admin paths.

### 4. Extensions
```bash
echo example.com | waybackurls | grep ".js"
```
**Explanation:** Find JS files.

### 5. Parameters
```bash
echo example.com | waybackurls | grep "="
```
**Explanation:** Find URLs with potential parameters (SQLi/XSS targets).

### 6. Unique
```bash
echo example.com | waybackurls | sort -u
```
**Explanation:** Remove duplicates.

### 7. Save
```bash
echo example.com | waybackurls > urls.txt
```
**Explanation:** Save to file.

### 8. Check Alive
```bash
echo example.com | waybackurls | httprobe
```
**Explanation:** Check which old URLs are still working.

### 9. Get Parameters Only (Unfurl)
```bash
echo example.com | waybackurls | unfurl keys
```
**Explanation:** (With Unfurl tool) Extract parameter names.

### 10. JSON (if supported)
```bash
echo example.com | waybackurls -json
```
# (Older versions are text only)

## The Most Powerful Command
```bash
echo target.com | waybackurls | sort -u | grep "=" | qsreplace "FUZZ" | freq
```
**Explanation:** Get all URLs, filter for params, replace values with FUZZ (ready for testing), and check frequency.

