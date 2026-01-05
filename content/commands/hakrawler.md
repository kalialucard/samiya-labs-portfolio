---
title: "Hakrawler Command List"
date: 2026-01-05
category: commands
enrich: false
tags: hakrawler, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Hakrawler in penetration testing.
---

# Hakrawler Command Guide

**Hakrawler** is a simple, go-based web crawler designed to find endpoints and assets quickly by piping stdin.

## Top 10 Useful Commands

### 1. Basic Pipe
```bash
echo http://example.com | hakrawler
```
**Explanation:** Basic usage. Pipe a URL in, get URLs out.

### 2. Depth
```bash
echo http://example.com | hakrawler -d 3
```
**Explanation:** Crawl 3 levels deep.

### 3. Plain Output
```bash
echo http://example.com | hakrawler -plain
```
**Explanation:** Only output the URLs (no prefixes like [href]).

### 4. Show Source
```bash
echo http://example.com | hakrawler -s
```
**Explanation:** Show the source code of the found assets.

### 5. Header Usage
```bash
echo http://example.com | hakrawler -h "Cookie: admin=1"
```
**Explanation:** Send custom header (auth).

### 6. Subdomains
```bash
echo http://example.com | hakrawler -subs
```
**Explanation:** Specifically look for and output subdomains.

### 7. Unique Output
```bash
echo http://example.com | hakrawler -u
```
**Explanation:** Ensure output URLs are unique.

### 8. Input List
```bash
cat urls.txt | hakrawler
```
**Explanation:** Crawl a massive list of domains.

### 9. Filter JS
```bash
echo http://example.com | hakrawler | grep ".js"
```
**Explanation:** Often used to find Javascript files.

### 10. Insecure SSL
```bash
echo https://example.com | hakrawler -insecure
```
**Explanation:** Ignore SSL errors.

## The Most Powerful Command
```bash
cat domains.txt | hakrawler -d 2 -plain -subs | grep "admin"
```
**Explanation:** Mass crawl a list of domains, go 2 levels deep, extract subdomains, and immediately grep for interesting "admin" endpoints.

