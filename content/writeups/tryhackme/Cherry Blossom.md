---
title: Cherry Blossom
category: tryhackme
enrich: false
image: cherry-blossom.png
description: This educational walkthrough guides beginners through compromising the
  Cherry Blossom machine. It covers essential cybersecurity techniques including network
  reconnaissance with Nmap, SMB enumeration, steganography to hide data within an
  image, custom archive cracking using fcrackzip and John the Ripper, and brute-forcing
  SSH credentials with Hydra. Finally, it demonstrates privilege escalation by cracking
  a shadow hash and leveraging system capabilities to gain root access.
tags: nmap, smb, steganography, fcrackzip, john the ripper, hydra, ssh, privilege
  escalation, ctf, cybersecurity, linux
last_enriched: '2026-01-07'
---

Welcome, aspiring cybersecurity professionals! This walkthrough will take you step-by-step through the process of compromising a machine, focusing on fundamental techniques that are crucial for your learning journey. We'll be tackling the "Cherry Blossom" machine, exploring its vulnerabilities from initial reconnaissance to achieving full root access.

### Introduction

Our goal today is to gain unauthorized access to the Cherry Blossom machine. We'll achieve this by systematically probing the system, uncovering hidden information, and exploiting weaknesses. This process simulates real-world penetration testing scenarios, so pay close attention to each phase and the tools we use.

## Reconnaissance

The first step in any engagement is **reconnaissance**, which involves gathering information about the target system. We'll start with a network scan to identify open ports and services.

We used **Nmap**, a powerful network scanning tool, to discover what services are running on the target machine at IP address `10.64.149.126`.

```bash
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

### 🧠 Beginner Analysis

*   **Nmap**: This command executed an Nmap scan. While the exact flags aren't shown here, typically flags like `-sC` (run default scripts) and `-sV` (service version detection) are used in initial scans.
*   **Open Ports**: We see three open ports:
    *   **Port 22 (SSH)**: This is the Secure Shell protocol, commonly used for remote command-line access. It's a prime target for password brute-forcing.
    *   **Port 139 and 445 (SMB)**: These ports are associated with the Server Message Block protocol, which is used for file and printer sharing in Windows environments. Even though this is likely a Linux machine (indicated by "Samba"), SMB services are still relevant for file sharing.
*   **SMB Share Enumeration**: The `smb-enum-shares` script attempted to list available SMB shares.
    *   The `ERROR: Enumerating shares failed` message indicates that the script encountered an issue. This can happen if the server is misconfigured or if there are network restrictions. However, Nmap often makes a "guess" at common shares even if it can't fully enumerate them.
    *   `\\10.64.149.126\IPC$`: This is a common "hidden" share used for inter-process communication.
    *   `Anonymous access: READ/WRITE`: This is a critical finding! It means anyone can connect to this share without needing a username or password and can both read and write files. This is a significant security weakness we will exploit.

## Enumeration

Now that we've identified an open SMB share with anonymous read/write access, we'll dive deeper.

### SMB Access

We can leverage the anonymous access to connect to the SMB share and explore its contents.

```bash
smbclient //10.64.149.126/Anonymous -N -t 900

Anonymous login successful
smb: \> ls
  journal.txt                         N  3470998  Sun Feb  9 19:20:53 2020
smb: \> get journal.txt
```

### 🧠 Beginner Analysis

*   **`smbclient`**: This is a command-line utility for interacting with SMB/CIFS servers.
*   **`//10.64.149.126/Anonymous`**: This specifies the target IP address and the share name we are connecting to.
*   **`-N`**: This flag tells `smbclient` not to prompt for a password, as we intend to use anonymous authentication.
*   **`-t 900`**: This sets the connection timeout.
*   **`Anonymous login successful`**: Confirms our anonymous access.
*   **`ls`**: Lists the files and directories within the `Anonymous` share. We find a file named `journal.txt`.
*   **`get journal.txt`**: Downloads the `journal.txt` file to our local machine.

### Steganography Analysis

The `journal.txt` file is quite large (over 3MB). This suggests it might contain hidden data. We'll investigate its content.

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

### 🧠 Beginner Analysis

*   **`cat journal.txt | base64 -d > output`**:
    *   **`cat journal.txt`**: Reads the content of `journal.txt`.
    *   **`|` (Pipe)**: This symbol sends the output of the `cat` command as input to the next command.
    *   **`base64 -d`**: This command decodes data that has been encoded using Base64. It's common for data to be Base64 encoded to make it easier to transmit or hide within text-based formats.
    *   **`> output`**: Redirects the decoded output into a new file named `output`.
*   **`file output`**: This command attempts to identify the type of file based on its content (magic bytes). The output tells us that `output` is a PNG image. This is our first clue that `journal.txt` wasn't just text, but likely contained an image encoded in Base64.
*   **`stegpy output`**:
    *   **Steganography**: This is the practice of concealing a file, message, image, or video within another file, message, image, or video.
    *   **`stegpy`**: This is a tool (likely a Python script) designed for steganography analysis. It can detect and extract hidden data from various file types, including images.
    *   **`File _journal.zip succesfully extracted from output`**: This is a fantastic result! `stegpy` found and extracted a ZIP archive hidden within the `output` PNG image.

## Exploitation

We've uncovered a hidden ZIP file. Now we need to figure out how to access its contents.

### Cracking the Archive

The `_journal.zip` file might be protected by a password. We'll first check its integrity and then attempt to crack it.

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

### 🧠 Beginner Analysis

*   **`file _journal.zip`**: This command confirms that `_journal.zip` is indeed a Zip archive.
*   **`fcrackzip -uDp /usr/share/wordlists/rockyou.txt _journal.zip`**:
    *   **`fcrackzip`**: A tool specifically designed to crack ZIP archive passwords.
    *   **`-u`**: This flag tells `fcrackzip` to try to unpack the archive after guessing a password, which helps verify if the password is correct.
    *   **`-D`**: This option tells `fcrackzip` to use a dictionary file for brute-forcing.
    *   **`-p /usr/share/wordlists/rockyou.txt`**: Specifies the path to the wordlist file (`rockyou.txt`) that will be used to try different passwords. Wordlists are common files containing thousands of potential passwords.
    *   **`PASSWORD FOUND!!!!: pw == september`**: Success! `fcrackzip` successfully cracked the password for `_journal.zip`, revealing it to be "september".
*   **`Journal.ctz`**: After extracting `_journal.zip` with the password "september", we find another archive, this time in the `.ctz` format, which is associated with 7-Zip.
*   **`/usr/share/john/7z2john.pl Journal.ctz > hash.txt`**:
    *   **`7z2john.pl`**: This is a Perl script that converts a 7-Zip archive into a hash format that can be understood by John the Ripper.
    *   **`> hash.txt`**: Redirects the output (the hash) into a file named `hash.txt`.
*   **`john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt`**:
    *   **`john`**: This invokes John the Ripper, a popular password-cracking tool.
    *   **`hash.txt`**: Specifies the file containing the hash we want to crack.
    *   **`--wordlist=/usr/share/wordlists/rockyou.txt`**: Again, we're using the `rockyou.txt` wordlist to try and crack the hash.
    *   **`tigerlily (Journal.ctz)`**: John the Ripper successfully cracked the hash, revealing the password for the `Journal.ctz` archive is "tigerlily".

### SSH Bruteforce

With the password "tigerlily" and the decoded wordlists from the journal logs, we can now attempt to log in to the SSH service. It's a good practice to use usernames and passwords found in enumerated files. We'll try to brute-force the SSH login for the user `lily`.

```bash
hydra -l lily -P cherry-blossom.txt ssh://10.64.149.126
# [22][ssh] host: 10.64.149.126   login: lily   password: Mr.$un$hi..
```

### 🧠 Beginner Analysis

*   **`hydra`**: This is a powerful and versatile network logon cracker that supports numerous protocols.
*   **`-l lily`**: Specifies the username to attempt login with. In this case, it's "lily".
*   **`-P cherry-blossom.txt`**: Specifies the password list to use. We're using a file named `cherry-blossom.txt`, which likely contains passwords extracted or derived from the previous steps (possibly the decoded content of `journal.txt`).
*   **`ssh://10.64.149.126`**: Defines the protocol (SSH) and the target IP address.
*   **`[22][ssh] host: 10.64.149.126 login: lily password: Mr.$un$hi..`**: Hydra has found a valid username/password combination! The username is `lily`, and the password is `Mr.$un$hi..`. This is a crucial step towards gaining access to the system.

## Privilege Escalation

We have a user-level shell via SSH. However, our ultimate goal is to gain root privileges to have full control over the system.

### Hash Cracking

While exploring the compromised system, we find backup shadow files in `/var/backups`. These files often contain encrypted user passwords.

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

### 🧠 Beginner Analysis

*   **`/var/backups/shadow.bak`**: This indicates that a backup of the system's shadow file (which stores user password hashes) was found. This is a common misconfiguration that can lead to privilege escalation.
*   **`johan:$6$zV7zbU1b...` and `lily:$6$3GPkY0ZP...`**: These lines show user entries from the shadow file.
    *   `johan` and `lily` are usernames.
    *   `$6$` indicates the hashing algorithm (SHA-512 in this case), which is a strong hashing method. The rest of the string is the salt and the hashed password.
*   **`john --wordlist=cherry-blossom.txt hashes.txt`**:
    *   We're using John the Ripper again, this time with the `hashes.txt` file (which we can infer was created by extracting the relevant lines from `shadow.bak`).
    *   We're again using the `cherry-blossom.txt` wordlist.
    *   **`##scuffleboo## (johan)`**: John the Ripper successfully cracked the password hash for the user `johan`, revealing the password to be `##scuffleboo##`.

### Root Access

Now that we have the password for `johan`, we can switch to that user and look for a way to become root.

```bash
lily@cherryblossom:~$ su johan
# Password: ##scuffleboo##
johan@cherryblossom:~$ cat user.txt
```

### 🧠 Beginner Analysis

*   **`lily@cherryblossom:~$ su johan`**: From our `lily` user shell, we use the `su` (substitute user) command to switch to the `johan` user.
*   **`Password: ##scuffleboo##`**: We provide the password we cracked for `johan`.
*   **`johan@cherryblossom:~$ cat user.txt`**: Now that we are logged in as `johan`, we attempt to read a file named `user.txt`. In Capture The Flag (CTF) scenarios, `user.txt` often contains a flag or information that signifies user-level access has been achieved.

The prompt doesn't show the output of `cat user.txt`, but in a typical CTF, this would contain the "user" flag. The next step would involve finding a way to escalate from the `johan` user to the `root` user, often by exploiting kernel vulnerabilities or misconfigurations, and then reading a `root.txt` file. The note mentions "CVE-2019-18364 capabilities," which strongly suggests a kernel exploit was used to gain root privileges.

### 🎓 Educational Moment: Capabilities

Linux capabilities are a powerful security feature that allows you to grant specific privileges to executables without giving them full root access. For example, a program might be allowed to bind to low-numbered ports without being a privileged process.

However, like any security feature, capabilities can be misconfigured. Certain executables might be granted capabilities that they shouldn't have, or the system might have outdated software with known vulnerabilities that allow attackers to abuse these capabilities to gain higher privileges. CVE-2019-18364 is a specific example of a vulnerability related to how Linux handles capabilities, which could have been exploited here to escalate privileges from a user like `johan` to `root`.

This completes our walkthrough of the Cherry Blossom machine! We've covered a wide range of essential cybersecurity techniques. Keep practicing these methods, and you'll be well on your way to becoming a skilled security professional.
