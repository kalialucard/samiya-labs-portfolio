---
title: Hashcat Command List
date: 2026-01-05
category: commands
enrich: false
tags: hashcat, cybersecurity, command reference
description: Top 10 essential commands for hashcat.
---

# Hashcat Command Guide

**Hashcat** is the world's fastest password cracker. It utilizes the power of GPUs to brute-force hashes.

## Top 10 Useful Commands

### 1. Basic Dictionary
```bash
hashcat -m 0 hash.txt wordlist.txt
```
**Explanation:** Crack MD5 (`-m 0`) using a wordlist (Straight mode `-a 0` default).

### 2. Identify Modes
```bash
hashcat --help | grep "NTLM"
```
**Explanation:** Find the mode number (`-m`) for a hash type (e.g., NTLM is 1000).

### 3. Rule Based
```bash
hashcat -m 0 hash.txt wordlist.txt -r rules/best64.rule
```
**Explanation:** Apply rules (like appending numbers/caps) to the wordlist. Vastly increases success.

### 4. Brute Force (Mask)
```bash
hashcat -a 3 -m 0 hash.txt ?a?a?a?a?a?a
```
**Explanation:** Attack mode 3 (Mask). Tries all 6-character combinations (`?a` = all alphanumeric).

### 5. NTLM Cracking
```bash
hashcat -m 1000 hashes.txt rockyou.txt
```
**Explanation:** Standard Windows password cracking.

### 6. Show Cracked
```bash
hashcat -m 0 hashes.txt --show
```
**Explanation:** Show previously cracked passwords for this hash file.

### 7. Optimize Kernel
```bash
hashcat -O ...
```
**Explanation:** Optimize for performance (improves speed but limits password length).

### 8. Benchmark
```bash
hashcat -b -m 0
```
**Explanation:** Test your GPU speed.

### 9. Session Resume
```bash
hashcat --session=mysession ...
```
**Explanation:** Name a session so you can restore it later (`--restore`).

### 10. Kerberoasting
```bash
hashcat -m 13100 kerberos_hashes.txt wordlist.txt
```
**Explanation:** Cracking Ticket Granting Service (TGS) tickets (Type 23).

## The Most Powerful Command
```bash
hashcat -m 1000 -a 0 ntlm.txt rockyou.txt -r rules/OneRuleToRuleThemAll.rule -O -w 3
```
**Explanation:** High workload (`-w 3`), Authorized optimization (`-O`), using a massive rule file against NTLM hashes.

