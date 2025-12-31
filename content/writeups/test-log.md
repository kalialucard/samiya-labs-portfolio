---
title: "Test Raw Log"
date: "2025-01-01"
category: "writeups"
enrich: true
---
Nmap scan report for 10.10.10.27
Host is up (0.14s latency).
PORT    STATE SERVICE      VERSION
22/tcp  open  ssh          OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
139/tcp open  netbios-ssn  Samba smbd 4.6.2
445/tcp open  microsoft-ds Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Ran smbclient:
$ smbclient -L //10.10.10.27
Sharename       Type      Comment
---------       ----      -------
print$          Disk      Printer Drivers
backups         Disk      System Backups
IPC$            IPC       IPC Service (Samba 4.6.2)
Anonymous login successful
