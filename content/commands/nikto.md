---
title: "Nikto Command List"
date: 2026-01-05
category: commands
enrich: false
tags: nikto, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Nikto in penetration testing.
---

# Nikto Command Guide

**Nikto** is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for multiple items, including over 6700 potentially dangerous files/programs, outdated versions of over 1250 servers, and version specific problems on over 270 servers.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
nikto -h http://example.com
```
**Explanation:** The most basic scan against a host (`-h`). Scans port 80 by default.

### 2. Scan SSL/HTTPS
```bash
nikto -h https://example.com
```
**Explanation:** Nikto automatically detects SSL, but specifying the protocol ensures it connects correctly.

### 3. Scan Specific Port
```bash
nikto -h example.com -p 8080
```
**Explanation:** Scans a non-standard port (`-p`) like 8080 or 8443.

### 4. Scan Multiple Ports
```bash
nikto -h example.com -p 80,443,8080
```
**Explanation:** Scans multiple ports on the same host in one go.

### 5. Using a Proxy
```bash
nikto -h example.com -useproxy http://127.0.0.1:8080
```
**Explanation:** Routes traffic through a proxy (like Burp or Zap) to capture and analyze the requests Nikto sends.

### 6. Output to File
```bash
nikto -h example.com -o scan_result.html
```
**Explanation:** Saves the results to a file. The format is guessed from the extension (HTML in this case).

### 7. Disable SSL Checking
```bash
nikto -h https://example.com -ssl
```
**Explanation:** Forces SSL mode (`-ssl`), useful if auto-detection fails.

### 8. Tuning (Scan Types)
```bash
nikto -h example.com -Tuning 2
```
**Explanation:** Runs only specific categories of tests (e.g., `2` is Misconfiguration / Default Files). Saves massive amounts of time.

### 9. Update Database
```bash
nikto -update
```
**Explanation:** Updates the plugin and database definitions to find the latest vulnerabilities.

### 10. Scan within a Directory
```bash
nikto -h http://example.com/subdir/
```
**Explanation:** Starts the scan inside a specific directory, useful if the target app isn't at the root.

## The Most Powerful Command

Comprehensive Scan with WAF Evasion and Logging:

```bash
nikto -h http://example.com -C all -evasion 1 -o scan.html -F html
```

**Why it's powerful:**
*   `-C all`: Forces checking of **all** CGI directories.
*   `-evasion 1`: Uses **Random URI encoding** to try and bypass simple WAF rules.
*   `-o scan.html -F html`: Saves a readable **HTML report**.

