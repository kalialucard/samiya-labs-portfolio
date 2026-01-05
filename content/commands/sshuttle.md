---
title: Sshuttle Command List
date: 2026-01-05
category: commands
enrich: false
tags: sshuttle, cybersecurity, command reference, network
description: Top 10 essential commands for sshuttle.
---

# Sshuttle Command Guide

**Sshuttle** allows you to create a VPN connection from your machine to any remote server that you can connect to via ssh. No admin needed on the remote server.

## Top 10 Useful Commands

### 1. Basic Network Tunnel
```bash
sshuttle -r user@10.10.10.10 192.168.1.0/24
```
**Explanation:** "Route all traffic for subnet 192.168.1.0/24 through the SSH server at 10.10.10.10".

### 2. Auto-Detect Subnets
```bash
sshuttle -r user@10.10.10.10 -N
```
**Explanation:** Automatically determine the networks the remote server is connected to and route them.

### 3. Tunnel All Traffic
```bash
sshuttle -r user@10.10.10.10 0.0.0.0/0
```
**Explanation:** Forward EVERYTHING (like a full VPN).

### 4. SSH Key Auth
```bash
sshuttle -r user@10.10.10.10 --ssh-cmd "ssh -i key.pem" 10.0.0.0/8
```
**Explanation:** Use a key file.

### 5. DNS Forwarding
```bash
sshuttle --dns -r user@10.10.10.10 192.168.1.0/24
```
**Explanation:** Tunnel DNS queries too. Essential for Active Directory (resolving domain names).

### 6. Daemon Mode
```bash
sshuttle -D ...
```
**Explanation:** Run in background.

### 7. Verbose
```bash
sshuttle -v ...
```
**Explanation:** Show routed packet info.

### 8. Exclude Subnet
```bash
sshuttle -r ... 192.168.1.0/24 -x 192.168.1.5
```
**Explanation:** Route the subnet BUT exclude checking IP .5.

### 9. Use sudo
```bash
# sshuttle itself requires sudo locally to modify iptables
```

### 10. Stop
```bash
# Ctrl+C clears iptables headers automatically
```

## The Most Powerful Command
```bash
sshuttle --dns -r user@10.10.10.10 172.16.0.0/12
```
**Explanation:** Instantly gives you access to the target's entire internal cloud network, allowing you to run tools (browser, nmap, etc) directly from your machine against internal IPs, with DNS working.

