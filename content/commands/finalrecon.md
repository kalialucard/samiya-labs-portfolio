---
title: "Finalrecon Command List"
date: 2026-01-05
category: commands
enrich: false
tags: finalrecon, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Finalrecon in penetration testing.
---

# FinalRecon Command Guide

**FinalRecon** is an all-in-one OSINT tool for web reconnaissance. It aggregates headers, SSL info, whois, and crawling.

## Top 10 Useful Commands

### 1. Full Scan
```bash
python3 finalrecon.py --url http://example.com --full
```
**Explanation:** Runs all available modules (Header, SSL, Whois, Crawl, DNS).

### 2. Headers Only
```bash
python3 finalrecon.py --url http://example.com --headers
```
**Explanation:** Checks HTTP security headers.

### 3. SSL Info
```bash
python3 finalrecon.py --url https://example.com --ssl
```
**Explanation:** Dumps SSL certificate details.

### 4. Whois
```bash
python3 finalrecon.py --url http://example.com --whois
```
**Explanation:** Gets domain registration info.

### 5. Crawl
```bash
python3 finalrecon.py --url http://example.com --crawl
```
**Explanation:** Crawls the site to find internal links.

### 6. DNS Enum
```bash
python3 finalrecon.py --url http://example.com --dns
```
**Explanation:** Dumps DNS records (A, MX, NS, etc.).

### 7. Subdomain Enum
```bash
python3 finalrecon.py --url http://example.com --sub
```
**Explanation:** Searches for subdomains.

### 8. Directory Search
```bash
python3 finalrecon.py --url http://example.com --dir
```
**Explanation:** Checks for common directories.

### 9. Wayback Check
```bash
python3 finalrecon.py --url http://example.com --wayback
```
**Explanation:** Checks Wayback machine for archived URLs.

### 10. Output
```bash
# (Automatic)
```
**Explanation:** FinalRecon automatically creates a timestamped folder with logs.

## The Most Powerful Command
```bash
python3 finalrecon.py --url http://target.com --full
```
**Explanation:** The `--full` flag is the most powerful as it provides a complete dossier on the target in one go.

