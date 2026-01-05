---
title: Searchsploit Command List
date: 2026-01-05
category: commands
enrich: false
tags: searchsploit, cybersecurity, command reference
description: Top 10 essential commands for searchsploit.
---

# Searchsploit Command Guide

**Searchsploit** is a command line search tool for Exploit-DB. It allows you to take a copy of the Exploit Database with you offline.

## Top 10 Useful Commands

### 1. Basic Search
```bash
searchsploit wordpress 5.0
```
**Explanation:** Search for exploits related to terms.

### 2. Copy Exploit
```bash
searchsploit -m 12345
```
**Explanation:** Mirror (`-m`) the exploit ID 12345 to the current directory.

### 3. Examine Code
```bash
searchsploit -x 12345
```
**Explanation:** Read the exploit code/metadata.

### 4. Precise Match
```bash
searchsploit -t "Apache 2.4"
```
**Explanation:** Search the Title (`-t`) specifically.

### 5. Nmap Integration
```bash
searchsploit --nmap scan.xml
```
**Explanation:** Parses an Nmap XML output and searches exploits for detected service versions.

### 6. Exclude Terms
```bash
searchsploit apache --exclude="DoS"
```
**Explanation:** Search Apache but hide Denial of Service scripts.

### 7. Online Search
```bash
searchsploit -w wordpress
```
**Explanation:** Show the URL to Exploit-DB.com instead of local path.

### 8. Update DB
```bash
searchsploit -u
```
**Explanation:** Update the database.

### 9. Case Sensitive
```bash
searchsploit -c "Apache"
```
**Explanation:** Perform case-sensitive search.

### 10. Exact Version
```bash
searchsploit -s "Apache 2.4.49"
```
**Explanation:** Strict search only.

## The Most Powerful Command
```bash
searchsploit --nmap results.xml --exclude="DoS"
```
**Explanation:** Automate vulnerability checking by feeding directly from your nmap scan results, filtering out useless DoS scripts.

