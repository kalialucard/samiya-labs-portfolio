---
title: "Sn1Per Command List"
date: 2026-01-05
category: commands
enrich: false
tags: sn1per, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Sn1Per in penetration testing.
---

# Sn1per Command Guide

**Sn1per** is an automated scanner that can be used during a penetration test to enumerate and scan for vulnerabilities. It integrates many tools (Nmap, Nikto, etc.).

## Top 10 Useful Commands

### 1. Normal Scan
```bash
sniper -t <target>
```
**Explanation:** Runs basic recon and scan.

### 2. Stealth Scan
```bash
sniper -t <target> -m stealth
```
**Explanation:** Non-intrusive scan mode.

### 3. Flyover (Recon)
```bash
sniper -t <target> -m flyover
```
**Explanation:** High-level overview, multi-threaded.

### 4. Airstrike (Multi-Target)
```bash
sniper -f targets.txt -m airstrike
```
**Explanation:** Mass scan a list of targets.

### 5. Nuke (Vulnerability)
```bash
sniper -t <target> -m nuke
```
**Explanation:** Weaponized audit (very loud, checks for major CVEs).

### 6. Discover
```bash
sniper -t <target> -m discover
```
**Explanation:** Focuses on subnet discovery.

### 7. Port Scan Only
```bash
sniper -t <target> -m port
```
**Explanation:** Only runs port scanning.

### 8. Web Scan
```bash
sniper -t <target> -m web
```
**Explanation:** Focuses on web app vectors (nikto, wpscan, etc).

### 9. Update
```bash
sniper -u
```
**Explanation:** Updates Sn1per scripts.

### 10. Report
```bash
# (Automatic)
```
**Explanation:** Sn1per generates reports in `loot/` automatically.

## The Most Powerful Command
```bash
sniper -t target.com -m webscan -w
```
**Explanation:** Runs a full web-focused vulnerability scan including crawling and exploit checking.

