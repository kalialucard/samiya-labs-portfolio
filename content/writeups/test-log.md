---
title: Test Raw Log
date: '2025-01-01'
category: writeups
enrich: false
description: This walkthrough details the initial reconnaissance and enumeration phases
  against a target machine, starting with an Nmap scan to identify open ports and
  services, followed by an in-depth exploration of an identified Samba service using
  `smbclient`. We specifically focus on the discovery of open SMB shares and the critical
  finding of successful anonymous login.
tags:
- nmap
- samba
- smbclient
- enumeration
- linux
- networking
- vulnerability assessment
- beginner
- cybersecurity
last_enriched: '2026-01-07'
---

Welcome to this educational walkthrough! Today, we'll be breaking down the initial steps of assessing a target system, focusing on how to gather information using common cybersecurity tools. Our goal is to understand what services are running, how they are configured, and what potential vulnerabilities might exist. We'll start with network scanning and then move into enumerating specific services.

## Reconnaissance

The very first step in any penetration test or security assessment is reconnaissance, where we gather as much information as possible about our target. We often begin with a network scanner to identify active hosts and open ports.

Our target for today is `10.10.10.27`. We'll start by running an Nmap scan to discover what ports are open and what services are running on them.

```bash
Nmap scan report for 10.10.10.27
Host is up (0.14s latency).
PORT    STATE SERVICE      VERSION
22/tcp  open  ssh          OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
139/tcp open  netbios-ssn  Samba smbd 4.6.2
445/tcp open  microsoft-ds Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

🧠 **Beginner Analysis**

Let's break down this Nmap output line by line to understand what we've discovered:

*   **`Nmap scan report for 10.10.10.27`**: This simply confirms the target IP address that Nmap scanned.
*   **`Host is up (0.14s latency).`**: This tells us that the target machine is online and responsive. The latency indicates how long it took for our machine to receive a response, giving us an idea of network speed.
*   **`PORT STATE SERVICE VERSION`**: This is the core of Nmap's findings.
    *   **`PORT`**: The port number and protocol (e.g., `22/tcp` means port 22 using the TCP protocol).
    *   **`STATE`**: The state of the port. `open` means the port is actively listening for connections, indicating a service is running.
    *   **`SERVICE`**: Nmap's best guess for the service running on that port (e.g., `ssh`, `netbios-ssn`).
    *   **`VERSION`**: A crucial piece of information! This is the specific software and its version detected on the open port. Knowing the version helps us research known vulnerabilities.
*   **`22/tcp open ssh OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)`**:
    *   Port 22 is commonly used for **SSH (Secure Shell)**. SSH allows secure remote login and command execution. An open SSH port means we *might* be able to log in if we have credentials or can exploit a vulnerability in the SSH service itself. The version `OpenSSH 8.2p1` tells us the specific software and its version, which is important for checking for known vulnerabilities later.
*   **`139/tcp open netbios-ssn Samba smbd 4.6.2`**:
    *   Port 139 is associated with **NetBIOS Session Service**, often used by **Samba** on Linux/Unix systems to provide **SMB/CIFS** services, which are protocols for file sharing and printer sharing over a network.
*   **`445/tcp open microsoft-ds Samba smbd 4.6.2`**:
    *   Port 445 is also used by **SMB (Server Message Block)** directly, without NetBIOS. This is the more modern way SMB operates. The fact that both 139 and 445 are open, and both are identified as `Samba smbd 4.6.2`, strongly indicates that the target machine is running a Samba file-sharing server. This is a very interesting finding, as SMB services are often misconfigured or have exploitable vulnerabilities.
*   **`Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel`**:
    *   This provides additional information about the target's operating system. Nmap has fingerprinted the OS as **Linux**. The `CPE` (Common Platform Enumeration) string is a standardized naming scheme for software, operating systems, and hardware.

**In summary from our Nmap scan, we know:**
1.  The target is a Linux machine.
2.  It has an SSH service running (`OpenSSH 8.2p1`).
3.  Most importantly, it has a **Samba file-sharing service** running (`Samba smbd 4.6.2`) accessible via both ports 139 and 445. This service provides a potential avenue for enumeration and exploitation.

## Enumeration

Now that we know a Samba service is running, our next logical step is to enumerate it. Enumeration involves actively querying a service to extract more detailed information about its configuration, users, shares, and other potential weaknesses. For Samba, the `smbclient` tool is invaluable.

We will use `smbclient` with the `-L` flag to list the available shares on the target IP address.

```bash
$ smbclient -L //10.10.10.27
Sharename       Type      Comment
---------       ----      -------
print$          Disk      Printer Drivers
backups         Disk      System Backups
IPC$            IPC       IPC Service (Samba 4.6.2)
Anonymous login successful
```

🧠 **Beginner Analysis**

Let's dissect this `smbclient` command and its output:

*   **`$ smbclient -L //10.10.10.27`**:
    *   `smbclient`: This is a command-line utility used to access SMB/CIFS shares on network servers. It acts like a client for the Samba server.
    *   `-L`: This flag tells `smbclient` to list the services (shares) available on the specified host.
    *   `//10.10.10.27`: This is the standard UNC (Universal Naming Convention) path format for specifying a network host. The double slashes `//` indicate a network resource, followed by the IP address of the target server.
*   **`Sharename Type Comment`**: These are the columns describing the discovered shares.
    *   `Sharename`: The name of the shared resource.
    *   `Type`: The type of share, typically `Disk` for file shares or `IPC` for inter-process communication shares.
    *   `Comment`: An optional description provided by the server administrator.
*   **`print$ Disk Printer Drivers`**: This is a common share for printer drivers. The `$` at the end often signifies a hidden share, though it's still listed here. While it might contain sensitive information, it's typically less interesting than other shares for initial access.
*   **`backups Disk System Backups`**: This share is immediately very interesting! A share named `backups` that contains "System Backups" is a prime target for further investigation. Backup files often contain sensitive data, configuration files, or even user credentials. Gaining access to this share could lead to significant information disclosure.
*   **`IPC$ IPC IPC Service (Samba 4.6.2)`**: `IPC$` (Inter-Process Communication) is a default, special share used by SMB for network communication between client and server. It's not a file share in the traditional sense but is necessary for many SMB operations. It's generally not directly exploitable for data access.
*   **`Anonymous login successful`**: This is a **critical finding**! It means that we were able to connect to the Samba server and list its shares *without providing any username or password*. This is often referred to as "anonymous access" or "null session login."

**Why is "Anonymous login successful" significant?**

Anonymous access to SMB shares is a serious misconfiguration. It means anyone on the network can potentially:
1.  **List shares**: As we just did, revealing potentially sensitive share names.
2.  **Access shares**: If any of the listed shares (especially `backups` in our case) are also configured for anonymous read or write access, an attacker could browse, download, or even upload/modify files without any authentication. This could lead to:
    *   **Information Disclosure**: Accessing sensitive documents, configuration files, or user data.
    *   **Code Execution**: If an anonymous user can write to a share that's executed by the system (e.g., a web root, or a script directory), they might be able to upload malicious code.

**Next Steps**

Given the `backups` share and the successful anonymous login, our next steps would be to attempt to connect to the `backups` share using `smbclient` (without credentials) and explore its contents. We would look for sensitive files, configuration files, password hashes, or anything that could give us further access to the system or elevate our privileges.
