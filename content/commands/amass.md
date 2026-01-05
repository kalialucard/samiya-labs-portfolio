---
title: "Amass Command List"
date: 2026-01-05
category: commands
enrich: false
tags: amass, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Amass in penetration testing.
---

# Amass Command Guide

**Amass** is the industry standard for subdomain enumeration and attack surface mapping. It uses active and passive techniques to discover DNS subdomains and map network infrastructures.

## Top 10 Useful Commands

### 1. Basic Enum
```bash
amass enum -d example.com
```
**Explanation:** Performs standard enumeration using active and passive data sources.

### 2. Passive Only (Fast)
```bash
amass enum -passive -d example.com
```
**Explanation:** Only queries passive data sources (WHOIS, ASN, Certificate Transparency). Very fast and stealthy (no direct traffic to target).

### 3. Active Mode
```bash
amass enum -active -d example.com
```
**Explanation:** Enables active scanning methods like attempting to resolve the found names against the target's nameservers.

### 4. IP Resolution
```bash
amass enum -ip -d example.com
```
**Explanation:** Shows the IP addresses associated with discovered subdomains (`-ip`).

### 5. Brute Force
```bash
amass enum -brute -d example.com
```
**Explanation:** Enables brute-forcing subdomains using a built-in wordlist.

### 6. Custom Wordlist
```bash
amass enum -brute -w /path/to/wordlist.txt -d example.com
```
**Explanation:** Uses a custom wordlist (`-w`) for brute-forcing.

### 7. Visualization (D3.js)
```bash
amass viz -d3 -d example.com
```
**Explanation:** Generates an HTML visualization of the network graph.

### 8. Track Changes
```bash
amass track -d example.com
```
**Explanation:** Compares the current scan against previous scans to show what changed (new subdomains added/removed).

### 9. Whois Info
```bash
amass intel -d example.com -whois
```
**Explanation:** Performs reverse, whois, and other intelligence gathering operations.

### 10. Output to File
```bash
amass enum -d example.com -o results.txt
```
**Explanation:** Saves the findings to a text file.

## The Most Powerful Command
```bash
amass enum -active -brute -w /usr/share/wordlists/subdomains.txt -d example.com -ip -src
```
**Explanation:** Combines **active scanning**, **brute forcing** with a custom list, **IP resolution**, and shows the **data source** (`-src`) for each finding.

