---
title: "Wfuzz Command List"
date: 2026-01-05
category: commands
enrich: false
tags: wfuzz, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Wfuzz in penetration testing.
---

# Wfuzz Command Guide

**Wfuzz** is a tool designed for bruteforcing Web Applications, it can be used for finding resources not linked (directories, servlets, scripts, etc), bruteforce GET and POST parameters for checking different kinds of injections (SQL, XSS, LDAP,etc), bruteforce Forms parameters (User/Password), Fuzzing, etc.

## Top 10 Useful Commands

### 1. Basic Directory Fuzzing
```bash
wfuzz -c -z file,wordlist.txt --hc 404 http://target.com/FUZZ
```
**Explanation:**
*   `-c`: Color output.
*   `-z file,wordlist.txt`: Defines the payload (wordlist).
*   `--hc 404`: Hides responses with code 404.
*   `FUZZ`: The keyword Wfuzz replaces with words from the list.

### 2. Fuzzing Extension
```bash
wfuzz -c -z file,wordlist.txt http://target.com/FUZZ.php
```
**Explanation:** Finds files with a specific extension (e.g., `.php`) by appending it to the FUZZ keyword.

### 3. Fuzzing Parameters (GET)
```bash
wfuzz -c -z file,wordlist.txt http://target.com/index.php?FUZZ=test
```
**Explanation:** Fuzzes the *parameter name* to find hidden GET parameters.

### 4. Fuzzing Values (Post)
```bash
wfuzz -c -z file,passwords.txt -d "user=admin&pass=FUZZ" http://target.com/login.php
```
**Explanation:** Fuzzes POST data (`-d`). Replaces `FUZZ` in the body payload (brute-forcing password).

### 5. Multiple Fuzzers (User + Pass)
```bash
wfuzz -c -z file,users.txt -z file,pass.txt -d "user=FUZZ&pass=FUZ2Z" http://target.com/login
```
**Explanation:** Uses multiple payloads. `FUZZ` maps to the first list, `FUZ2Z` maps to the second.

### 6. Filter by Words (Hide Small Pages)
```bash
wfuzz -c -z file,wordlist.txt --hw 50 http://target.com/FUZZ
```
**Explanation:** Hides results with a specific word count (`--hw`). Useful if all error pages have exactly 50 words.

### 7. Filter by Lines
```bash
wfuzz -c -z file,wordlist.txt --hl 100 http://target.com/FUZZ
```
**Explanation:** Hides results with a specific line count (`--hl`).

### 8. Use Proxy
```bash
wfuzz -c -z file,wordlist.txt -p 127.0.0.1:8080 http://target.com/FUZZ
```
**Explanation:** Routes traffic through a proxy (`-p`) like Burp Suite.

### 9. Scan for Subdomains
```bash
wfuzz -c -z file,subdomains.txt -H "Host: FUZZ.target.com" http://target.com
```
**Explanation:** Fuzzes the `Host` header to find internal virtual hosts or subdomains.

### 10. Save Output
```bash
wfuzz -c -z file,wordlist.txt -f results.json,json http://target.com/FUZZ
```
**Explanation:** Saves the results to a file (`-f filename,format`).

## The Most Powerful Command

Fuzzing for IDOR (Insecure Direct Object References) with immediate anomalies shown:

```bash
wfuzz -c -z range,1-1000 --hh 250 http://target.com/profile.php?id=FUZZ
```

**Why it's powerful:**
*   `-z range,1-1000`: Generates numbers 1 to 1000 automatically (no file needed).
*   `--hh 250`: Hides "Access Denied" pages (assuming they are 250 characters).
*   **Result:** Shows *only* the IDs that return a different/valid profile page.

