---
title: Sniper Command List
date: 2026-01-05
category: commands
enrich: false
tags: sniper, cybersecurity, command reference
description: Top 10 essential commands for sniper.
---

# Sn1per Command Guide

**Sn1per** is an automated scanner.

## Top 10 Useful Commands

### 1. Normal Scan
```bash
sniper -t target.com
```
**Explanation:** Standard scan.

### 2. Stealth Scan
```bash
sniper -t target.com -m stealth
```
**Explanation:** Less noise.

### 3. Flyover
```bash
sniper -t target.com -m flyover
```
**Explanation:** Fast scan (flyover).

### 4. Airstrike
```bash
sniper -f targets.txt -m airstrike
```
**Explanation:** Scan a list of targets quickly.

### 5. Nuke
```bash
sniper -t target.com -m nuke
```
**Explanation:** Full audit (very loud).

### 6. Discover
```bash
sniper -t 192.168.1.0/24 -m discover
```
**Explanation:** Subnet discovery.

### 7. Port Scan
```bash
sniper -t target.com -m port
```
**Explanation:** Only run port modules.

### 8. Web Scan
```bash
sniper -t target.com -m web
```
**Explanation:** Only run web modules.

### 9. Update
```bash
sniper -u
```
**Explanation:** Update tool.

### 10. Report
```bash
sniper --report
```
**Explanation:** Generate HTML report manually.

## The Most Powerful Command
```bash
sniper -t target.com -m nuke
```
**Explanation:** Unleashes every tool (Nmap, Nikto, Burp, etc.) against the target.

