---
title: Wireshark Command List
date: 2026-01-05
category: commands
enrich: false
tags: wireshark, cybersecurity, command reference
description: Top 10 essential commands for wireshark.
---

# Wireshark/TShark Command Guide

**Wireshark** is for analysis. **TShark** is the CLI version.

## Top 10 Useful Commands

### 1. Start Capture (GUI)
```bash
wireshark &
```
**Explanation:** Launch GUI.

### 2. TShark Capture
```bash
tshark -i eth0
```
**Explanation:** Capture on interface cli.

### 3. Write to File
```bash
tshark -i eth0 -w capture.pcap
```
**Explanation:** Save packets.

### 4. Read File
```bash
tshark -r capture.pcap
```
**Explanation:** Analyze offline file.

### 5. Filter IP
```bash
ip.addr == 10.10.10.10
```
**Explanation:** (Display Filter) Show only this IP.

### 6. Filter HTTP
```bash
http.request.method == "POST"
```
**Explanation:** Show POST requests.

### 7. Follow Stream (CLI)
```bash
tshark -r file.pcap -z follow,tcp,ascii,0
```
**Explanation:** Reconstruct TCP stream 0.

### 8. Stats
```bash
capinfos capture.pcap
```
**Explanation:** Show duration/bitrate stats.

### 9. Extract Objects
```bash
tshark -r capture.pcap --export-objects http,destdir/
```
**Explanation:** Extract images/files from PCAP.

### 10. Credentials (Ngrep style)
```bash
tshark -r file.pcap -Y "http contains password"
```
**Explanation:** Search payload for strings.

## The Most Powerful Command
```bash
ip.addr == 192.168.1.5 && http
```
**Explanation:** Simple filter to isolate all web traffic for a specific target.

