---
title: "Feroxbuster Command List"
date: 2026-01-05
category: commands
enrich: false
tags: feroxbuster, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Feroxbuster in penetration testing.
---

# Feroxbuster Command Guide

**Feroxbuster** is a fast, simple, recursive content discovery tool written in Rust. It's often faster than Gobuster/Dirbuster due to Rust's efficiency.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
feroxbuster -u http://target.com
```
**Explanation:** Default scan. It handles recursion automatically.

### 2. Custom Wordlist
```bash
feroxbuster -u http://target.com -w /path/to/wordlist.txt
```
**Explanation:** Specifies a wordlist.

### 3. Extensions
```bash
feroxbuster -u http://target.com -x pdf,js,html
```
**Explanation:** Appends extensions to every word.

### 4. No Recursion
```bash
feroxbuster -u http://target.com -n
```
**Explanation:** Disables recursion (`-n`).

### 5. Filter Status Codes
```bash
feroxbuster -u http://target.com -s 200 301
```
**Explanation:** Only output 200 and 301 responses.

### 6. Filter by Size
```bash
feroxbuster -u http://target.com --filter-size 1234
```
**Explanation:** Hides all responses that are exactly 1234 bytes.

### 7. Extract Links
```bash
feroxbuster -u http://target.com --extract-links
```
**Explanation:** Automatically extracts links from response bodies and scans them.

### 8. Threads
```bash
feroxbuster -u http://target.com -t 100
```
**Explanation:** Sets thread count.

### 9. Proxy
```bash
feroxbuster -u http://target.com -p http://127.0.0.1:8080
```
**Explanation:** Tunnel through Burp/Zap.

### 10. Json Output
```bash
feroxbuster -u http://target.com --json -o output.json
```
**Explanation:** structured JSON output.

## The Most Powerful Command
```bash
feroxbuster -u http://target.com -w big.txt -x php,html -t 50 --extract-links --auto-tune --smart
```
**Explanation:** Uses "Smart" recursion, Auto-tuning (lowers rate if errors occur), and link extraction to find EVERYTHING.

