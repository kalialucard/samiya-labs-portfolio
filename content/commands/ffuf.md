---
title: "Ffuf Command List"
date: 2026-01-05
category: commands
enrich: false
tags: ffuf, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Ffuf in penetration testing.
---

# Ffuf Command Guide

**Ffuf (Fuzz Faster U Fool)** is a heavily used, extremely fast web fuzzer written in Go. It is the modern standard for web fuzzing.

## Top 10 Useful Commands

### 1. Directory Fuzzing
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt
```
**Explanation:** The keyword `FUZZ` is replaced by words from the list.

### 2. Extension Fuzzing
```bash
ffuf -u http://target.com/index.FUZZ -w extensions.txt
```
**Explanation:** Fuzzes the file extension.

### 3. VHost Discovery
```bash
ffuf -u http://target.com -H "Host: FUZZ.target.com" -w subdomains.txt
```
**Explanation:** Fuzzes the Host header to find virtual hosts.

### 4. POST Data Fuzzing
```bash
ffuf -u http://target.com/login -X POST -d "user=admin&pass=FUZZ" -w pass.txt
```
**Explanation:** Fuzzes POST body input.

### 5. Filter by Words
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -fw 50
```
**Explanation:** Filter Words (`-fw`): hides responses with 50 words.

### 6. Filter by Size
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -fs 1024
```
**Explanation:** Filter Size (`-fs`): hides responses of 1024 bytes.

### 7. Match Codes
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -mc 200,302
```
**Explanation:** Match Code (`-mc`): only show 200 and 302 statuses.

### 8. Recursion
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -recursion
```
**Explanation:** If a directory is found, it starts a new scan inside it.

### 9. Request File
```bash
ffuf -request req.txt -w wordlist.txt
```
**Explanation:** Loads a raw HTTP request from a file and replaces `FUZZ`. Great for complex headers.

### 10. Output HTML
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -o result.html -of html
```
**Explanation:** Saves a pretty HTML report.

## The Most Powerful Command
```bash
ffuf -u http://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 2 -e .php,.html -mc 200,302 -fs 4242 -c -t 100
```
**Explanation:** Recursive scan, checks extensions, matches good codes, filters bad sizes, color output, 100 threads.

