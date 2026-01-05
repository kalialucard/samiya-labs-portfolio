---
title: Bloodhound Command List
date: 2026-01-05
category: commands
enrich: false
tags: bloodhound, cybersecurity, command reference, ad
description: Top 10 essential commands for bloodhound.
---

# Bloodhound Command Guide

**BloodHound** uses graph theory to reveal the hidden and often unintended relationships within an Active Directory environment.

## Top 10 Useful Commands

### 1. Run SharpHound (Ingestor)
```bash
C:\> SharpHound.exe -c All
```
**Explanation:** Collects ALL data (Sessions, Groups, ACLs, Trusts, LocalAdmins) from the Windows domain.

### 2. Run Python Ingestor
```bash
bloodhound-python -d domain.local -u user -p pass -c All -ns 10.10.10.10
```
**Explanation:** Collect data from Linux without dropping an exe file.

### 3. Loop Collection
```bash
SharpHound.exe -c Session --Loop
```
**Explanation:** Continuously collect session usage to track where users log in over time.

### 4. Zip Data
```bash
# (Automatic)
```
**Explanation:** SharpHound creates a zip file to upload to the GUI.

### 5. Stealth Mode
```bash
SharpHound.exe --Stealth
```
**Explanation:** Reduces noise, but collects less data.

### 6. Domain Trust Only
```bash
SharpHound.exe -c DCOnly
```
**Explanation:** Only talk to the Domain Controller (quieter).

### 7. Upload to Neo4j
```bash
# (Drag and drop zip into GUI)
```

### 8. Query: Fastest Path
```bash
# Right Click User -> "Shortest Path to Domain Admin"
```
**Explanation:** The killer feature. Shows exactly how to jump from User A to DA.

### 9. Query: Kerberoastable
```bash
# "List all Kerberoastable Account"
```

### 10. Mark Owned
```bash
# Right Click Node -> "Mark as Owned"
```
**Explanation:** Updates graph to show new paths accessible from your compromised position.

## The Most Powerful Command
(Concept): **"Shortest Path from Owned Principals to Domain Admins"**
**Explanation:** This query tells you the exact attack path (e.g., User A -> Can RDP Host B -> Has Session User C -> Is Admin of Host D -> Has DC Session) to win.

