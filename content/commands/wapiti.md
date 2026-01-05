---
title: "Wapiti Command List"
date: 2026-01-05
category: commands
enrich: false
tags: wapiti, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Wapiti in penetration testing.
---

# Wapiti Command Guide

**Wapiti** is a web application vulnerability scanner. It performs "black-box" scans (it doesn't study the source code) of the web application by crawling the webpages of the deployed webapp, looking for scripts and forms where it can inject data.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
wapiti -u http://example.com
```
**Explanation:** Standard scan.

### 2. Scope
```bash
wapiti -u http://example.com -s folder
```
**Explanation:** Limit scope to the URL folder.

### 3. Modules
```bash
wapiti -u http://example.com -m xss,sql_blind
```
**Explanation:** Only test for XSS and Blind SQLi.

### 4. Auth
```bash
wapiti -u http://example.com -a user%password
```
**Explanation:** Basic authentication.

### 5. Cookie
```bash
wapiti -u http://example.com -c cookie.json
```
**Explanation:** Load cookies from file.

### 6. Exclude URL
```bash
wapiti -u http://example.com -x http://example.com/logout
```
**Explanation:** Do not scan logout page.

### 7. Output Format
```bash
wapiti -u http://example.com -f html -o report.html
```
**Explanation:** Generate HTML report.

### 8. Timeout
```bash
wapiti -u http://example.com --timeout 10
```
**Explanation:** Set request timeout.

### 9. Level (Depth)
```bash
wapiti -u http://example.com -d 5
```
**Explanation:** Crawling depth.

### 10. Verify SSL
```bash
wapiti -u https://example.com --verify-ssl 0
```
**Explanation:** Disable SSL verification.

## The Most Powerful Command
```bash
wapiti -u http://target.com -m all -f html -o report.html --color
```
**Explanation:** Full module scan with a readable HTML report output.

