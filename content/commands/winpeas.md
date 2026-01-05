---
title: Winpeas Command List
date: 2026-01-05
category: commands
enrich: false
tags: winpeas, cybersecurity, command reference, ad
description: Top 10 essential commands for winpeas.
---

# WinPEAS Command Guide

**WinPEAS** is the Windows counterpart. It enumerates registry, services, files, and updates to find privilege escalation vectors.

## Top 10 Useful Commands

### 1. Basic Run
```cmd
winpeas.exe
```
**Explanation:** Run checks.

### 2. Fast Scan
```cmd
winpeas.exe fast
```
**Explanation:** Skip heavy checks (like file analysis).

### 3. Search Passwords
```cmd
winpeas.exe searchfast
```
**Explanation:** Look for stored credentials/autologon specifically.

### 4. Cmd Only (No Color/Binary)
```cmd
winpeas.bat
```
**Explanation:** If you can't drop an EXE, use the Batch script version.

### 5. Services Check
```cmd
winpeas.exe servicesinfo
```
**Explanation:** Enumerate services, look for Unquoted Service Paths.

### 6. PowerShell Mode
```cmd
winpeas.ps1
```
**Explanation:** Powershell version. Runs in memory, better for AV evasion often.

### 7. System Info
```cmd
winpeas.exe systeminfo
```
**Explanation:** Check patch levels, OS version (Kernel exploits).

### 8. Process Info
```cmd
winpeas.exe processinfo
```
**Explanation:** Check running processes.

### 9. User Info
```cmd
winpeas.exe userinfo
```
**Explanation:** Check current user privileges (SeDebugPrivilege, etc).

### 10. Output
```cmd
winpeas.exe > report.txt
```

## The Most Powerful Command
```cmd
winpeas.exe quiet
```
**Explanation:** Like LinPEAS, running it and looking for **RED** text is the key. It highlights "AlwaysInstallElevated" or "Writable Service Exe" paths instantly.

