---
title: "Chaos Command List"
date: 2026-01-05
category: commands
enrich: false
tags: chaos, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Chaos in penetration testing.
---

# Chaos Command Guide

**Chaos** is a project discovery tool that interacts with the Chaos API (by ProjectDiscovery) to retrieve subdomains. It allows for instant enumeration if you have an API key.

## Top 10 Useful Commands

### 1. Basic Fetch
```bash
chaos -d example.com
```
**Explanation:** Fetches subdomains for the target from the Chaos dataset.

### 2. Download Everything
```bash
chaos -d example.com -o output.txt
```
**Explanation:** Saves the dataset to a file.

### 3. Filter by Bug Bounty Programs
```bash
chaos -bbq
```
**Explanation:** Lists all domains currently in public bug bounty programs indexed by Chaos.

### 4. Count Subdomains
```bash
chaos -d example.com -count
```
**Explanation:** Returns only the count of subdomains found, not the list.

### 5. Check API Key
```bash
chaos -key
```
**Explanation:** Checks if your PDCP_API_KEY is configured correctly.

### 6. JSON Output
```bash
chaos -d example.com -json
```
**Explanation:** Outputs data in JSON format for easy parsing by other tools.

### 7. Silent Mode
```bash
chaos -d example.com -silent
```
**Explanation:** Prints only the subdomains, no banners or metadata.

### 8. Fetch New Only
```bash
chaos -d example.com -new
```
**Explanation:** (If supported by easier version) Filters to show only newly added subdomains since last check.

### 9. Filter with Grep
```bash
chaos -d example.com | grep "dev"
```
**Explanation:** combine with standard linux tools to find interesting patterns like "dev" or "staging".

### 10. Piping to Httpx
```bash
chaos -d example.com | httpx
```
**Explanation:** Immediately check which of the chaos-found domains are alive.

## The Most Powerful Command
```bash
chaos -d example.com -silent | httpx -title -tech-detect -status-code
```
**Explanation:** Instantly retrieves thousands of subdomains and fingerprints the technology and status of every single one.

