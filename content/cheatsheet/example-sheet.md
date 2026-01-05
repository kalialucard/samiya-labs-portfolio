---
title: 'Example Cheatsheet: Regex'
date: '2026-01-05'
category: cheatsheet
enrich: false
image: assets/sheet-thumb.png
tags: cybersecurity, nmap, recon, enumeration, beginner, educational, walkthrough,
  network scanning, vulnerability analysis
description: A beginner-friendly walkthrough of common cybersecurity reconnaissance
  and enumeration techniques, focusing on interpreting Nmap scans and understanding
  the significance of open ports.
last_enriched: '2026-01-05'
---

Welcome, aspiring cybersecurity professionals! This walkthrough is designed to demystify the initial steps of a penetration test, focusing on how we gather information about a target system. We'll be using a powerful tool called Nmap to scan for open ports and services, and we'll explain *why* each piece of information is important from a security perspective.

Think of this like being a detective. Before you can solve a crime, you need to gather clues. In cybersecurity, our initial clues come from scanning the target system to see what services it's running and what doors (ports) are open.

## Reconnaissance

Reconnaissance is the first phase of a penetration test. It's all about gathering as much information as possible about the target without actively trying to break in. This helps us understand the "attack surface" – the parts of the system that an attacker could potentially interact with.

### Network Scanning with Nmap

We'll start by using Nmap (Network Mapper), a versatile tool for network discovery and security auditing. Let's imagine we've identified an IP address for our target and we want to see what's running on it.

A common initial scan is to look for all common TCP ports and try to identify the services running on them.

```bash
nmap -sC -sV 192.168.1.100
```

#### 🧠 Beginner Analysis

Let's break down this command:

*   `nmap`: This is the command to launch the Nmap tool.
*   `-sC`: This flag tells Nmap to run a set of default Nmap scripts. These scripts are incredibly useful because they can perform more advanced discovery and even detect common vulnerabilities. Think of them as automated helpers that do some of the initial "detective work" for us.
*   `-sV`: This flag is for "version detection." It tells Nmap to try and figure out the exact version of the software running on each open port (e.g., Apache 2.4.41, OpenSSH 8.2p1). Knowing the version is crucial because specific versions of software often have known vulnerabilities that we can exploit.
*   `192.168.1.100`: This is the target IP address we are scanning. In a real scenario, this would be the IP address of the machine we are testing.

Now, let's imagine we get some output from this scan.

```
Starting Nmap 7.91 ( https://nmap.org ) at 2023-10-27 10:30 EDT
Nmap scan report for 192.168.1.100
Host is up (0.00020s latency).
Not shown: 997 closed ports
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
139/tcp  open  netbios Microsoft Windows netblabla 6.1.7601
445/tcp  open  microsoft-ds Windows netblabla 6.1.7601
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.34 seconds
```

#### 🧠 Beginner Analysis

This is where the magic happens! Let's dissect the output line by line:

*   `Host is up (0.00020s latency)`: This tells us that our target IP address is active and responding. The latency is very low, meaning it's a quick connection.
*   `Not shown: 997 closed ports`: Nmap, by default, scans the most common 1000 TCP ports. This line indicates that out of those 1000 ports, 997 are closed. Closed ports are like locked doors – they aren't offering any services we can directly interact with at the moment.
*   `PORT     STATE SERVICE VERSION`: These are the headers for the important information that follows.
    *   `PORT`: The port number and protocol (e.g., `21/tcp`). Ports are like numbered doors into a computer.
    *   `STATE`: `open` means there's a service listening on this port. This is what we're looking for!
    *   `SERVICE`: The common name of the service running on that port.
    *   `VERSION`: The specific version of the service, as identified by `-sV`.

Now, let's look at the open ports and understand *why* they are interesting:

*   `21/tcp   open  ftp     vsftpd 3.0.3`:
    *   **Port 21 is for FTP (File Transfer Protocol).** This is an older protocol used for transferring files between a client and a server.
    *   **Why is it interesting?** FTP is often a target because it can sometimes be configured to allow anonymous logins, meaning you don't need a username or password. If anonymous login is enabled, we might be able to upload files to the server. Additionally, FTP can sometimes be used to download sensitive configuration files or even access user data.
    *   **Version:** `vsftpd 3.0.3`. Knowing this specific version (`vsftpd`) is important because we can search for known vulnerabilities associated with `vsftpd 3.0.3`.

*   `22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)`:
    *   **Port 22 is for SSH (Secure Shell).** This is a secure protocol used for remote command-line login and other secure network services between two networked computers. It's generally considered secure.
    *   **Why is it interesting?** While SSH is designed to be secure, attackers still try to gain access. This can be done through brute-force attacks (guessing passwords) if weak passwords are used, or by exploiting vulnerabilities in the SSH server software itself. The fact that it's running on Ubuntu Linux is also useful information.
    *   **Version:** `OpenSSH 8.2p1 Ubuntu 4ubuntu0.1`. Again, knowing the version allows us to research potential exploits.

*   `80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))`:
    *   **Port 80 is for HTTP (Hypertext Transfer Protocol).** This is the standard protocol used for delivering web pages over the internet. When you visit a website, your browser is using HTTP (or HTTPS on port 443).
    *   **Why is it interesting?** This indicates that a web server is running. Web servers are one of the most common entry points for attackers because websites are designed to be accessible and often interact with users. We'll want to explore this web server further to see what websites or web applications are hosted on it, as these can contain numerous vulnerabilities (like SQL injection, cross-site scripting, or insecure file uploads).
    *   **Version:** `Apache httpd 2.4.41`. Apache is a very popular web server. Knowing the specific version helps us find relevant exploits.

*   `139/tcp  open  netbios Microsoft Windows netblabla 6.1.7601`:
*   `445/tcp  open  microsoft-ds Windows netblabla 6.1.7601`:
    *   **Ports 139 and 445 are typically associated with SMB/CIFS (Server Message Block / Common Internet File System).** These protocols are used for file sharing, printer sharing, and inter-process communication in Windows networks.
    *   **Why are they interesting?** Historically, SMB has been a major source of vulnerabilities. For example, the infamous EternalBlue exploit (used in WannaCry ransomware) targeted a vulnerability in SMB. Even if there isn't a direct exploit available, misconfigured SMB shares can leak sensitive information or allow unauthorized access to files. The output suggests it's a Windows machine.
    *   **Version:** `Windows netblabla 6.1.7601`. This points towards a Windows 7 or Windows Server 2008 R2 system. Older Windows versions are more likely to have unpatched vulnerabilities.

This initial Nmap scan has given us a wealth of information! We know which doors are open and what services are behind them. Our next steps would involve investigating each of these open ports in more detail to find potential weaknesses.
