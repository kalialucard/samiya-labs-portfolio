---
title: John Command List
date: 2026-01-05
category: commands
enrich: false
tags: john, cybersecurity, command reference
description: Top 10 essential commands for john.
---

# John the Ripper Command Guide

**John the Ripper (JtR)** is a fast password cracker. While Hashcat rules GPU, John is king of CPU support and huge variety of hash formats (jumbo).

## Top 10 Useful Commands

### 1. Basic Crack
```bash
john hash.txt
```
**Explanation:** Auto-detects hash type and cracks using default order (Single -> Wordlist -> Incremental).

### 2. Specify Format
```bash
john --format=NT hash.txt
```
**Explanation:** Force specific format (e.g., Windows NT).

### 3. Wordlist Mode
```bash
john --wordlist=/path/rockyou.txt hash.txt
```
**Explanation:** Use a dictionary.

### 4. Show Passwords
```bash
john --show hash.txt
```
**Explanation:** Display cracked credentials.

### 5. Zip/Rar Cracking
```bash
zip2john file.zip > hash.txt
john hash.txt
```
**Explanation:** Use a helper tool (`zip2john`) to extract the hash, then crack it.

### 6. SSH Key Cracking
```bash
ssh2john id_rsa > hash.txt
john hash.txt
```
**Explanation:** Crack a passphrase-protected SSH private key.

### 7. Rules
```bash
john --wordlist=pass.txt --rules hash.txt
```
**Explanation:** Enable wordlist mangling rules.

### 8. Incremental (Brute)
```bash
john --incremental hash.txt
```
**Explanation:** Try all character combinations (slow but exhaustive).

### 9. List Formats
```bash
john --list=formats
```
**Explanation:** Show supported hash types.

### 10. Restore Session
```bash
john --restore
```
**Explanation:** Continue an interrupted session.

## The Most Powerful Command
```bash
john --wordlist=rockyou.txt --rules --format=crypt /etc/shadow
```
**Explanation:** Attempting to crack Linux shadow file using a wordlist with rules enabled.

