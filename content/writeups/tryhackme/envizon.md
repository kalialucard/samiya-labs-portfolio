```
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 cb:98:15:ed:13:41:b4:d5:53:72:53:54:c7:56:e6:6a (RSA)
|   256 c8:f2:71:60:0d:aa:f9:a0:d1:01:e5:61:30:97:ba:f7 (ECDSA)
|_  256 11:23:45:6f:40:7a:9c:e4:d4:f1:05:ac:45:d5:ff:1a (ED25519)
3000/tcp open  ssl/ppp?
|_ssl-date: TLS randomness does not represent time
| fingerprint-strings: 
|   DNSVersionBindReqTCP, GenericLines, RPCCheck, RTSPRequest: 
|     HTTP/1.1 400 Bad Request
|   GetRequest: 
|     HTTP/1.0 301 Moved Permanently
|     Location: https://localhost/scans
|     Content-Type: text/html
|     Cache-Control: no-cache
|     X-Request-Id: 7ec9a70c-cfe6-4fe4-93b6-bbcafe662c7c
|     X-Runtime: 0.002623
|     Strict-Transport-Security: max-age=31536000; includeSubDomains
|     Content-Length: 89
|     <html><body>You are being <a href="https://localhost/scans">redirected</a>.</body></html>
|   HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Content-Type: text/html; charset=UTF-8
|     X-Request-Id: 9fddd09f-c402-4c82-bd63-1e8272638e45
|     X-Runtime: 0.002201
|     Strict-Transport-Security: max-age=31536000; includeSubDomains
|     Content-Length: 1722
|     <!DOCTYPE html>
|     <html>
|     <head>
|     <title>The page you were looking for doesn't exist (404)</title>
|     <meta name="viewport" content="width=device-width,initial-scale=1">
|     <style>
|     .rails-default-error-page {
|     background-color: #EFEFEF;
|     color: #2E2F30;
|     text-align: center;
|     font-family: arial, sans-serif;
|     margin: 0;
|     .rails-default-error-page div.dialog {
|     width: 95%;
|     max-width: 33em;
|     margin: 4em auto 0;
|     .rails-default-error-page div.dialog > div {
|     border: 1px solid #CCC;
|     border-right-color: #999;
|     border-left-color: #999;
|     border-bottom-color: #BBB;
|     border-top: #B00100 solid 4px;
|_    border-top-left-radius: 9p
| ssl-cert: Subject: commonName=None/organizationName=evait/stateOrProvinceName=None/countryName=DE
| Not valid before: 2020-09-30T22:19:49
|_Not valid after:  2021-09-30T22:19:49
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3000-TCP:V=7.95%T=SSL%I=7%D=1/2%Time=6957BF33%P=x86_64-pc-linux-gnu
SF:%r(GenericLines,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(GetR
SF:equest,16D,"HTTP/1\.0\x20301\x20Moved\x20Permanently\r\nLocation:\x20ht
SF:tps://localhost/scans\r\nContent-Type:\x20text/html\r\nCache-Control:\x
SF:20no-cache\r\nX-Request-Id:\x207ec9a70c-cfe6-4fe4-93b6-bbcafe662c7c\r\n
SF:X-Runtime:\x200\.002623\r\nStrict-Transport-Security:\x20max-age=315360
SF:00;\x20includeSubDomains\r\nContent-Length:\x2089\r\n\r\n<html><body>Yo
SF:u\x20are\x20being\x20<a\x20href=\"https://localhost/scans\">redirected<
SF:/a>\.</body></html>")%r(HTTPOptions,79B,"HTTP/1\.0\x20404\x20Not\x20Fou
SF:nd\r\nContent-Type:\x20text/html;\x20charset=UTF-8\r\nX-Request-Id:\x20
SF:9fddd09f-c402-4c82-bd63-1e8272638e45\r\nX-Runtime:\x200\.002201\r\nStri
SF:ct-Transport-Security:\x20max-age=31536000;\x20includeSubDomains\r\nCon
SF:tent-Length:\x201722\r\n\r\n<!DOCTYPE\x20html>\n<html>\n<head>\n\x20\x2
SF:0<title>The\x20page\x20you\x20were\x20looking\x20for\x20doesn't\x20exis
SF:t\x20\(404\)</title>\n\x20\x20<meta\x20name=\"viewport\"\x20content=\"w
SF:idth=device-width,initial-scale=1\">\n\x20\x20<style>\n\x20\x20\.rails-
SF:default-error-page\x20{\n\x20\x20\x20\x20background-color:\x20#EFEFEF;\
SF:n\x20\x20\x20\x20color:\x20#2E2F30;\n\x20\x20\x20\x20text-align:\x20cen
SF:ter;\n\x20\x20\x20\x20font-family:\x20arial,\x20sans-serif;\n\x20\x20\x
SF:20\x20margin:\x200;\n\x20\x20}\n\n\x20\x20\.rails-default-error-page\x2
SF:0div\.dialog\x20{\n\x20\x20\x20\x20width:\x2095%;\n\x20\x20\x20\x20max-
SF:width:\x2033em;\n\x20\x20\x20\x20margin:\x204em\x20auto\x200;\n\x20\x20
SF:}\n\n\x20\x20\.rails-default-error-page\x20div\.dialog\x20>\x20div\x20{
SF:\n\x20\x20\x20\x20border:\x201px\x20solid\x20#CCC;\n\x20\x20\x20\x20bor
SF:der-right-color:\x20#999;\n\x20\x20\x20\x20border-left-color:\x20#999;\
SF:n\x20\x20\x20\x20border-bottom-color:\x20#BBB;\n\x20\x20\x20\x20border-
SF:top:\x20#B00100\x20solid\x204px;\n\x20\x20\x20\x20border-top-left-radiu
SF:s:\x209p")%r(RTSPRequest,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n
SF:")%r(RPCCheck,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n")%r(DNSVer
SF:sionBindReqTCP,1C,"HTTP/1\.1\x20400\x20Bad\x20Request\r\n\r\n");
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


```

```
└─$ gobuster dir -k -u https://10.66.188.149:3000 -w /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt 2>/dev/null

===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://10.66.188.149:3000
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/dirbuster/wordlists/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.8
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/admin                (Status: 302) [Size: 104] [--> https://10.66.188.149:3000/admin/login]
/reports              (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/issues               (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/groups               (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/clients              (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/notes                (Status: 302) [Size: 106] [--> https://10.66.188.149:3000/users/sign_in]
/404                  (Status: 200) [Size: 1722]
/500                  (Status: 200) [Size: 1635]
/422                  (Status: 200) [Size: 1705]
^C

```

```
https://10.66.188.149:3000/notes/1

![](https://10.66.188.149:3000/assets/logo/envizon-wide-export-white-a650bc5b488e5de846dd2e4e58df9449bd7e3a4908f2511677d18a70581a9644.svg)

](https://10.66.188.149:3000/)

- [_account_circle_Please sign in](https://10.66.188.149:3000/)

**Text:** Hi Paul, for security reasons I added hashids with a length of 30 characters to notes. I stored the password for this envizon instance in the note with id 380 and sent you the link by email. We may should consider to add more security layers to this gem (https://github.com/dtaniwaki/acts_as_hashids)
```

```

```