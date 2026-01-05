---
title: "Assetfinder Command List"
date: 2026-01-05
category: commands
enrich: false
tags: assetfinder, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Assetfinder in penetration testing.
---

# Assetfinder Command Guide

**Assetfinder** is a simple yet powerful Go tool by TomNomNom used to find domains and subdomains related to a given domain. It leverages sources like Facebook, builtwith, and crt.sh.

## Top 10 Useful Commands

### 1. Basic Usage
```bash
assetfinder example.com
```
**Explanation:** Finds subdomains for `example.com` and prints them to stdout.

### 2. Only Subdomains
```bash
assetfinder --subs-only example.com
```
**Explanation:** Filters out results that aren't strict subdomains (e.g., removes `example.com` itself if not desired, or unrelated domains).

### 3. Save to File
```bash
assetfinder example.com > domains.txt
```
**Explanation:** Redirects the output to a file for later use.

### 4. Combo with Httprobe
```bash
assetfinder example.com | httprobe
```
**Explanation:** Pipes found domains into `httprobe` to see which ones actually have running web servers.

### 5. Combo with Subjack
```bash
assetfinder example.com | subjack -w fingerprints.json -t 100 -ssl
```
**Explanation:** Pipes domains to `subjack` to checking for subdomain takeover vulnerabilities.

### 6. Unique Sort
```bash
assetfinder example.com | sort -u
```
**Explanation:** Ensures no duplicate domains are listed.

### 7. Recursive Hunting
```bash
echo example.com | assetfinder | tee -a domains.txt
```
**Explanation:** Echo a domain into it (scripting friendly) and append to a file.

### 8. Find Related Domains
```bash
assetfinder example.com
```
**Explanation:** Sometimes finds related domains (not just subdomains) depending on the data source.

### 9. Silent Mode (Bash Scripting)
```bash
assetfinder example.com > /dev/null
```
**Explanation:** Assetfinder is silent by default (no banners), making it perfect for scripts.

### 10. API Keys (Environment)
```bash
export VIRUSTOTAL_API_KEY=xxx; assetfinder example.com
```
**Explanation:** Assetfinder automatically picks up API keys from environment variables for deeper searches.

## The Most Powerful Command
```bash
assetfinder --subs-only example.com | sort -u | httprobe | tee alive_hosts.txt
```
**Explanation:** The "Recon Pipeline" starter: Finds unique subdomains, checks if they are alive (http/https), and saves the working list.

