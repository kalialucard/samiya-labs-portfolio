---
title: "Spiderfoot Command List"
date: 2026-01-05
category: commands
enrich: false
tags: spiderfoot, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Spiderfoot in penetration testing.
---

# Spiderfoot Command Guide

**Spiderfoot** is an open source intelligence (OSINT) automation tool. It integrates with hundreds of data sources to gather intelligence on IP addresses, domain names, e-mail addresses, names and more.

## Top 10 Useful Commands

### 1. Start Web UI
```bash
sf.py -l 127.0.0.1:5001
```
**Explanation:** Starts the web interface. This is the primary way to use Spiderfoot.

### 2. CLI Scan
```bash
sf.py -s target.com -m all
```
**Explanation:** Runs a CLI scan using ALL modules.

### 3. List Modules
```bash
sf.py -M
```
**Explanation:** Lists available modules.

### 4. Specific Module
```bash
sf.py -s target.com -m s3bucket
```
**Explanation:** Run only S3 bucket enumeration.

### 5. Passive-Only
```bash
# (Configuration in UI)
```
**Explanation:** In CLI, ensure you select modules that don't touch target.

### 6. Export to CSV
```bash
# (UI Feature)
```
**Explanation:** Export findings from UI.

### 7. Filter by Type
```bash
sf.py -s target.com -t IP_ADDRESS
```
**Explanation:** Treat target strictly as IP.

### 8. API Key Setup
```bash
# (UI > Settings)
```
**Explanation:** Configure Shodan, VirusTotal keys.

### 9. Database Mode
```bash
sf.py -d results.db
```
**Explanation:** Specify database file.

### 10. Quiet Mode
```bash
sf.py -q
```
**Explanation:** Suppress logging.

## The Most Powerful Command
(Via UI): **"New Scan" -> Target: domain.com -> "All Modules" -> "Run"**
**Explanation:** Spiderfoot is designed to correlate data. Running ALL modules allows it to link emails to domains, domains to IPs, and IPs to locations.

