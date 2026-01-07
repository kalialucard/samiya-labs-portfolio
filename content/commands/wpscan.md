---
title: "Wpscan Command List"
date: 2026-01-05
category: commands
enrich: false
tags: wpscan, cybersecurity, command reference, beginner, web
description: Top 10 essential commands and a master guide for using Wpscan in penetration testing.
---

# WPScan Command Guide

**WPScan** is a black box WordPress vulnerability scanner. It scans remote WordPress installations to find security issues such as vulnerable plugins, themes, weak passwords, and configuration/information leaks.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
wpscan --url http://example.com
```
**Explanation:** Performs a basic non-intrusive scan to detect version, theme, and basic headers.

### 2. Enumerate Vulnerable Plugins
```bash
wpscan --url http://example.com --enumerate vp
```
**Explanation:** Specifically searches for plugins (`p`) that have known vulnerabilities (`v`).

### 3. Enumerate All Users
```bash
wpscan --url http://example.com --enumerate u
```
**Explanation:** Attempts to harvest usernames (via author archives, REST API, etc.). Crucial for later brute-force attacks.

### 4. Enumerate Vulnerable Themes
```bash
wpscan --url http://example.com --enumerate vt
```
**Explanation:** Checks the installed theme against the database of known vulnerabilities.

### 5. Brute Force Login
```bash
wpscan --url http://example.com -U users.txt -P passwords.txt
```
**Explanation:** Tries to login using a list of users (`-U`) and passwords (`-P`) against `wp-login.php`.

### 6. Aggressive Detection
```bash
wpscan --url http://example.com --detection-mode aggressive
```
**Explanation:** Sends more intrusive requests to permit better detection, though prone to false positives or 403 blocks.

### 7. Use API Token (Deeper Scan)
```bash
wpscan --url http://example.com --api-token <YOUR_TOKEN>
```
**Explanation:** Uses the WPVulnDB API token (free account) to show vulnerability data in the output. Without this, you just see plugin versions.

### 8. Ignore SSL Verify
```bash
wpscan --url https://example.com --disable-tls-checks
```
**Explanation:** Useful for internal tests where certificates might be invalid or self-signed.

### 9. Scan via Proxy
```bash
wpscan --url http://example.com --proxy http://127.0.0.1:8080
```
**Explanation:** Routes traffic through Burp Suite or another proxy.

### 10. Timbs-out (Anti-WAF)
```bash
wpscan --url http://example.com --random-user-agent --throttle 500
```
**Explanation:** Randomized UA and throttled requests (500ms delay) to avoid WAF blocking.

## The Most Powerful Command

The "Full Audit" command:

```bash
wpscan --url http://target.com --enumerate vp,vt,tt,cb,dbe,u,m --plugins-detection aggressive
