---
title: "Findomain Command List"
date: 2026-01-05
category: commands
enrich: false
tags: findomain, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Findomain in penetration testing.
---

# Findomain Command Guide

**Findomain** is known for being the fastest subdomain enumerator because it's written in Rust and uses parallelized data source querying.

## Top 10 Useful Commands

### 1. Basic Search
```bash
findomain -t example.com
```
**Explanation:** Searches for subdomains of the target (`-t`).

### 2. Save to Output
```bash
findomain -t example.com -o
```
**Explanation:** Automatically saves to `example.com.txt`.

### 3. Quiet Mode
```bash
findomain -t example.com -q
```
**Explanation:** Only prints subdomains (no banners).

### 4. IP resolution
```bash
findomain -t example.com -i
```
**Explanation:** Resolves the IP address for found subdomains.

### 5. Screenshotting (Experimental)
```bash
findomain -t example.com -s
```
**Explanation:** Attempts to screenshot valid domains.

### 6. Monitor Mode
```bash
findomain -t example.com -m
```
**Explanation:** Monitors transparency logs for NEW subdomains and notifies.

### 7. Webhook Notification
```bash
findomain -t example.com -m -w https://discord.com/api/webhooks...
```
**Explanation:** Sends new findings to Discord/Slack webhooks during monitoring.

### 8. Use Custom Resolvers
```bash
findomain -t example.com -r resolvers.txt
```
**Explanation:** Uses custom DNS resolvers for verification.

### 9. Httprobe Integration
```bash
findomain -t example.com -q | httprobe
```
**Explanation:** (Pipe) Check active domains immediately.

### 10. Valid Domains Only
```bash
findomain -t example.com --http
```
**Explanation:** only check/show resolved domains with http ports open.

## The Most Powerful Command
```bash
findomain -t example.com -i -o
```
**Explanation:** Blazing fast enumeration + IP resolution + File export.

