---
title: Tcpdump Command List
date: 2026-01-05
category: commands
enrich: false
tags: tcpdump, cybersecurity, command reference, network
description: Top 10 essential commands for tcpdump.
---

# Tcpdump Command Guide

**Tcpdump** is a powerful command-line packet analyzer.

## Top 10 Useful Commands

### 1. Basic Capture
```bash
tcpdump -i eth0
```
**Explanation:** Capture on interface `eth0`.

### 2. Write to File (Pcap)
```bash
tcpdump -i eth0 -w capture.pcap
```
**Explanation:** Save packets to load in Wireshark later.

### 3. Read File
```bash
tcpdump -r capture.pcap
```
**Explanation:** Analyze a saved file.

### 4. Filter by IP
```bash
tcpdump host 10.10.10.10
```
**Explanation:** Only show traffic to/from this IP.

### 5. Filter by Port
```bash
tcpdump port 80
```
**Explanation:** Only web traffic.

### 6. ASCII Output
```bash
tcpdump -A
```
**Explanation:** Print packet contents in ASCII (good for seeing HTTP headers/passwords).

### 7. Protocol Filter
```bash
tcpdump icmp
```
**Explanation:** Only show Ping requests.

### 8. Combine Filters
```bash
tcpdump src 10.10.10.10 and port 22
```
**Explanation:** SSH traffic FROM 10.10.10.10.

### 9. No Name Resolution
```bash
tcpdump -n
```
**Explanation:** Don't resolve IP to Hostname (faster).

### 10. Specific Count
```bash
tcpdump -c 100
```
**Explanation:** Capture 100 packets then exit.

## The Most Powerful Command
```bash
tcpdump -i eth0 -n -A port 80 or port 8080
```
**Explanation:** Watch web traffic in real time, formatted as text, to capture clear-text API keys, cookies, or passwords passing on the wire.

