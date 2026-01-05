---
title: "Gospider Command List"
date: 2026-01-05
category: commands
enrich: false
tags: gospider, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Gospider in penetration testing.
---

# Gospider Command Guide

**Gospider** is a fast web spider written in Go. It crawls sites, Javascript files, and sitemaps to find URLs and subdomains.

## Top 10 Useful Commands

### 1. Basic Crawl
```bash
gospider -s "http://example.com/"
```
**Explanation:** Spiders a single site.

### 2. Site List
```bash
gospider -S sites.txt
```
**Explanation:** Spiders a list of URLs from a file.

### 3. Threads
```bash
gospider -s "http://example.com/" -t 20
```
**Explanation:** Sets number of concurrent threads.

### 4. Output Directory
```bash
gospider -s "http://example.com/" -o output/
```
**Explanation:** Saves results into specific directory.

### 5. Depth
```bash
gospider -s "http://example.com/" -d 3
```
**Explanation:** Sets crawling depth (how many links deep to follow).

### 6. Other Sources
```bash
gospider -s "http://example.com/" -a
```
**Explanation:** Also queries AlienVault, Wayback, CommonCrawl for URLs.

### 7. Robots.txt
```bash
gospider -s "http://example.com/" -r
```
**Explanation:** Specifically parsing robots.txt.

### 8. Sitemap
```bash
gospider -s "http://example.com/" --sitemap
```
**Explanation:** Forces sitemap parsing.

### 9. Cookie
```bash
gospider -s "http://example.com/" -c "cookie=value"
```
**Explanation:** Sets cookies for authenticated crawling.

### 10. No Redirects
```bash
gospider -s "http://example.com/" --no-redirect
```
**Explanation:** Do not follow redirects.

## The Most Powerful Command
```bash
gospider -S urls.txt -o results -c "cookie=session" -d 2 --other-source --include-subs
```
**Explanation:** Crawl a list of sites, deeply, checking 3rd party sources, including subdomains, as an authenticated user.

