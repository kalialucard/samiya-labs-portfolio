---
title: "Gowitness Command List"
date: 2026-01-05
category: commands
enrich: false
tags: gowitness, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Gowitness in penetration testing.
---

# Gowitness Command Guide

**Gowitness** is a website screenshot utility written in Golang. Useful for visual reconnaissance of large lists of subdomains.

## Top 10 Useful Commands

### 1. Single Site
```bash
gowitness single --url http://example.com
```
**Explanation:** Screenshots one URL.

### 2. File Input
```bash
gowitness file -f urls.txt
```
**Explanation:** Screenshots every URL in the list.

### 3. Nmap Input
```bash
gowitness nmap -f scan.xml
```
**Explanation:** Parses an Nmap XML result and screenshots open web ports.

### 4. Threads
```bash
gowitness file -f urls.txt --threads 10
```
**Explanation:** Screenshots in parallel.

### 5. Server Mode
```bash
gowitness server
```
**Explanation:** Starts a web server to view the report gallery.

### 6. Resolution
```bash
gowitness single -u http://example.com --resolution 1920x1080
```
**Explanation:** Sets capture resolution.

### 7. Timeout
```bash
gowitness file -f urls.txt --timeout 10
```
**Explanation:** Sets timeout (seconds) per page.

### 8. Delay
```bash
gowitness file -f urls.txt --delay 5
```
**Explanation:** Waits 5 seconds before taking screenshot (waiting for animations/loading).

### 9. Database Name
```bash
gowitness file -f urls.txt --db scan.db
```
**Explanation:** Specify SQlite db file name.

### 10. Full Page
```bash
# (Older versions supported full page, modern usage relies on resolution)
```
**Explanation:** Gowitness focuses on viewport, ensure resolution is high for "full" feel.

## The Most Powerful Command
```bash
gowitness file -f alive_subdomains.txt --threads 20 --resolution 1280x1024; gowitness server
```
**Explanation:** Rapidly screenshot hundreds of hosts and then immediately spin up a local gallery to "scroll" through the targets visually.

