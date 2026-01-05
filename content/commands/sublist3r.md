---
title: "Sublist3R Command List"
date: 2026-01-05
category: commands
enrich: false
tags: sublist3r, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Sublist3R in penetration testing.
---

# Sublist3r Command Guide

**Sublist3r** is a python tool designed to enumerate subdomains of websites using OSINT. It helps penetration testers collect and gather subdomains for the domain they are targeting.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
python sublist3r.py -d example.com
```
**Explanation:** Scans the domain using default engines.

### 2. Save Output
```bash
python sublist3r.py -d example.com -o subdomains.txt
```
**Explanation:** Save results to file.

### 3. Bruteforce
```bash
python sublist3r.py -d example.com -b
```
**Explanation:** Enables brute-force module (Subbrute).

### 4. Ports Check
```bash
python sublist3r.py -d example.com -p 80,443
```
**Explanation:** Checks if discovered subdomains have open ports 80/443.

### 5. Verbose
```bash
python sublist3r.py -d example.com -v
```
**Explanation:** Show real-time results.

### 6. Threads
```bash
python sublist3r.py -d example.com -t 20
```
**Explanation:** Set threads count.

### 7. Engines
```bash
python sublist3r.py -e google,yahoo,virustotal -d example.com
```
**Explanation:** Use only specific search engines.

### 8. Reverse
```bash
# (Not native)
```
**Explanation:** Sublist3r is forward lookup mostly.

### 9. Wordlist for Brute
```bash
# (Requires editing config/library in some versions)
```

### 10. Help
```bash
python sublist3r.py -h
```
**Explanation:** Show help menu.

## The Most Powerful Command
```bash
python sublist3r.py -d example.com -o subs.txt -b -t 50 -p 80,443,8080
```
**Explanation:** OSINT scan + Brute force + Port scan validation in one command.

