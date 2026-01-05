---
title: Proxychains Command List
date: 2026-01-05
category: commands
enrich: false
tags: proxychains, cybersecurity, command reference, network
description: Top 10 essential commands for proxychains.
---

# Proxychains Command Guide

**Proxychains** forces any TCP connection made by a given application to follow through a proxy like TOR or any other SOCKS4, SOCKS5 or HTTP(S) proxy.

## Top 10 Useful Commands

### 1. Basic Usage
```bash
proxychains nmap -sT 10.10.10.10
```
**Explanation:** Run command through the proxy defined in `/etc/proxychains4.conf`.

### 2. Using Firefox
```bash
proxychains firefox
```
**Explanation:** Forces the browser through the proxy chain (e.g., to browse internal sites via SOCKS).

### 3. Quiet Mode
```bash
proxychains -q nmap ...
```
**Explanation:** Don't print "S-chain... OK" logs to stdout.

### 4. Configuration
```bash
nano /etc/proxychains4.conf
```
**Explanation:** Edit this file to add your proxies (e.g., `socks5 127.0.0.1 1080`).

### 5. Dynamic Chain
```bash
# Set "dynamic_chain" in conf
```
**Explanation:** Skips dead proxies in the list.

### 6. Strict Chain
```bash
# Set "strict_chain" in conf
```
**Explanation:** Failing one proxy breaks the connection (good for strict anonymity paths).

### 7. Random Chain
```bash
# Set "random_chain" in conf
```
**Explanation:** Use random proxies from list.

### 8. DNS Proxying
```bash
# "proxy_dns" in conf
```
**Explanation:** Resolves DNS through the proxy (prevents DNS leaks).

### 9. With SSH Tunnel
```bash
ssh -D 1080 user@pivot
# Then run proxychains
```
**Explanation:** Use Dynamic Port Forwarding to pivot into a network.

### 10. With Metasploit
```bash
proxychains msfconsole
```
**Explanation:** Run the entire framework through a proxy.

## The Most Powerful Command
```bash
proxychains nmap -sT -Pn -n 192.168.1.10
```
**Explanation:** A "Full Pivot" scan. You are scanning an internal IP address (192.168.1.10) that your machine cannot see, by tunneling the Nmap request through a compromised jump host.

