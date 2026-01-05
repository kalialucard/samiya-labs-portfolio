import os

# Content map for Tool Installation Pages
# Format: "tool_basename": { "type": "CLI/GUI", "lang": "Go/Python/C", "desc": "...", "website": "...", "repo": "...", "install": "..." }

TOOLS_DB = {
    # --- SCANNING & RECON ---
    "nmap": {
        "type": "CLI", "lang": "C++", "desc": "The most popular network scanner.",
        "website": "https://nmap.org/", "repo": "https://github.com/nmap/nmap",
        "install": "sudo apt install nmap"
    },
    "gobuster": {
        "type": "CLI", "lang": "Go", "desc": "Fast directory/file & DNS busting tool.",
        "website": "https://github.com/OJ/gobuster", "repo": "https://github.com/OJ/gobuster",
        "install": "sudo apt install gobuster\n# OR\ngo install github.com/OJ/gobuster/v3@latest"
    },
    "dirbuster": {
        "type": "GUI/CLI", "lang": "Java", "desc": "Legacy Java directory brute forcer.",
        "website": "https://sourceforge.net/projects/dirbuster/", "repo": "https://gitlab.com/kalilinux/packages/dirbuster",
        "install": "sudo apt install dirbuster"
    },
    "amass": {
        "type": "CLI", "lang": "Go", "desc": "In-depth Attack Surface Mapping and Asset Discovery.",
        "website": "https://owasp.org/www-project-amass/", "repo": "https://github.com/owasp-amass/amass",
        "install": "sudo apt install amass\n# OR\ngo install github.com/owasp-amass/amass/v3/...@master"
    },
    "ffuf": {
        "type": "CLI", "lang": "Go", "desc": "Fast web fuzzer written in Go.",
        "website": "https://github.com/ffuf/ffuf", "repo": "https://github.com/ffuf/ffuf",
        "install": "go install github.com/ffuf/ffuf/v2@latest\n# OR\nsudo apt install ffuf"
    },
    "nuclei": {
        "type": "CLI", "lang": "Go", "desc": "Template based vulnerability scanner.",
        "website": "https://nuclei.projectdiscovery.io/", "repo": "https://github.com/projectdiscovery/nuclei",
        "install": "go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest"
    },
    "nikto": {
        "type": "CLI", "lang": "Perl", "desc": "Classic web server scanner.",
        "website": "https://cirt.net/Nikto2", "repo": "https://github.com/sullo/nikto",
        "install": "sudo apt install nikto\n# OR\ngit clone https://github.com/sullo/nikto.git"
    },
    "wpscan": {
        "type": "CLI", "lang": "Ruby", "desc": "WordPress vulnerability scanner.",
        "website": "https://wpscan.com/", "repo": "https://github.com/wpscanteam/wpscan",
        "install": "sudo apt install wpscan\n# OR\ngem install wpscan"
    },
     "sublist3r": {
        "type": "CLI", "lang": "Python", "desc": "Fast subdomains enumeration tool for penetration testers.",
        "website": "https://github.com/aboul3la/Sublist3r", "repo": "https://github.com/aboul3la/Sublist3r",
        "install": "git clone https://github.com/aboul3la/Sublist3r.git\ncd Sublist3r\npip install -r requirements.txt"
    },
    
    # --- EXPLOITATION ---
    "metasploit": {
        "type": "Framework", "lang": "Ruby", "desc": "The world's most used penetration testing framework.",
        "website": "https://www.metasploit.com/", "repo": "https://github.com/rapid7/metasploit-framework",
        "install": "curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall"
    },
    "searchsploit": {
        "type": "CLI", "lang": "Shell", "desc": "Command line search tool for Exploit-DB.",
        "website": "https://www.exploit-db.com/searchsploit", "repo": "https://gitlab.com/kalilinux/packages/exploitdb",
        "install": "sudo apt install exploitdb"
    },
    "commix": {
        "type": "CLI", "lang": "Python", "desc": "Automated All-in-One OS command injection exploitation tool.",
        "website": "https://commixproject.com/", "repo": "https://github.com/commixproject/commix",
        "install": "git clone https://github.com/commixproject/commix.git commix\ncd commix\npython3 commix.py --help"
    },
    "msfvenom": {
        "type": "CLI", "lang": "Ruby", "desc": "Metasploit standalone payload generator.",
        "website": "https://www.metasploit.com/", "repo": "https://github.com/rapid7/metasploit-framework",
        "install": "# Included in Metasploit Framework\nsudo apt install metasploit-framework"
    },

    # --- CRACKING ---
    "hashcat": {
        "type": "CLI", "lang": "C", "desc": "World's fastest password cracker.",
        "website": "https://hashcat.net/hashcat/", "repo": "https://github.com/hashcat/hashcat",
        "install": "sudo apt install hashcat"
    },
    "john": {
        "type": "CLI", "lang": "C", "desc": "John the Ripper password cracker.",
        "website": "https://www.openwall.com/john/", "repo": "https://github.com/openwall/john",
        "install": "sudo apt install john"
    },
    "hydra": {
        "type": "CLI", "lang": "C", "desc": "Parallelized login cracker.",
        "website": "https://github.com/vanhauser-thc/thc-hydra", "repo": "https://github.com/vanhauser-thc/thc-hydra",
        "install": "sudo apt install hydra"
    },

    # --- ACTIVE DIRECTORY ---
    "impacket": {
        "type": "Library/CLI", "lang": "Python", "desc": "Collection of Python classes for working with network protocols.",
        "website": "https://github.com/fortra/impacket", "repo": "https://github.com/fortra/impacket",
        "install": "pip install impacket\n# OR\ngit clone https://github.com/fortra/impacket.git; cd impacket; pip install ."
    },
    "netexec": {
        "type": "CLI", "lang": "Python", "desc": "The Swiss Army Knife of pentesting networks (formerly CrackMapExec).",
        "website": "https://github.com/Pennyw0rth/NetExec", "repo": "https://github.com/Pennyw0rth/NetExec",
        "install": "pip install netexec"
    },
    "evil-winrm": {
        "type": "CLI", "lang": "Ruby", "desc": "The ultimate WinRM shell for hacking/pentesting.",
        "website": "https://github.com/Hackplayers/evil-winrm", "repo": "https://github.com/Hackplayers/evil-winrm",
        "install": "gem install evil-winrm"
    },
    "bloodhound": {
        "type": "GUI/CLI", "lang": "JS/C#", "desc": "Six Degrees of Domain Admin.",
        "website": "https://github.com/BloodHoundAD/BloodHound", "repo": "https://github.com/BloodHoundAD/BloodHound",
        "install": "sudo apt install bloodhound neo4j"
    },
    "responder": {
        "type": "CLI", "lang": "Python", "desc": "LLMNR/NBT-NS Poisoner.",
        "website": "https://github.com/lgandx/Responder", "repo": "https://github.com/lgandx/Responder",
        "install": "git clone https://github.com/lgandx/Responder.git\ncd Responder\nsudo ./Responder.py -I eth0"
    },

    # --- NETWORKING ---
    "netcat": {
        "type": "CLI", "lang": "C", "desc": "The TCP/IP Swiss Army Knife.",
        "website": "http://netcat.sourceforge.net/", "repo": "https://github.com/diegocr/netcat",
        "install": "sudo apt install netcat-traditional"
    },
    "socat": {
        "type": "CLI", "lang": "C", "desc": "Multipurpose relay (SOcket CAT).",
        "website": "http://www.dest-unreach.org/socat/", "repo": "http://www.dest-unreach.org/socat/",
        "install": "sudo apt install socat"
    },
    "proxychains": {
        "type": "CLI", "lang": "C", "desc": "Redirect connections through proxy servers.",
        "website": "https://github.com/haad/proxychains", "repo": "https://github.com/haad/proxychains",
        "install": "sudo apt install proxychains"
    },
    "chisel": {
        "type": "CLI", "lang": "Go", "desc": "Fast TCP/UDP tunnel over HTTP.",
        "website": "https://github.com/jpillora/chisel", "repo": "https://github.com/jpillora/chisel",
        "install": "go install github.com/jpillora/chisel@latest"
    },
    "sshuttle": {
        "type": "CLI", "lang": "Python", "desc": "Transparent proxy server that works as a poor man's VPN.",
        "website": "https://github.com/sshuttle/sshuttle", "repo": "https://github.com/sshuttle/sshuttle",
        "install": "sudo apt install sshuttle\n# OR\npip install sshuttle"
    },
    "tcpdump": {
        "type": "CLI", "lang": "C", "desc": "Packet analyzer.",
        "website": "https://www.tcpdump.org/", "repo": "https://github.com/the-tcpdump-group/tcpdump",
        "install": "sudo apt install tcpdump"
    },

    # --- PRIVILEGE ESCALATION ---
    "linpeas": {
        "type": "Script", "lang": "Shell", "desc": "Linux Privilege Escalation Awesome Script.",
        "website": "https://github.com/carlospolop/PEASS-ng", "repo": "https://github.com/carlospolop/PEASS-ng",
        "install": "curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh > linpeas.sh; chmod +x linpeas.sh"
    },
    "winpeas": {
        "type": "Binary", "lang": "C#", "desc": "Windows Privilege Escalation Awesome Scripts.",
        "website": "https://github.com/carlospolop/PEASS-ng", "repo": "https://github.com/carlospolop/PEASS-ng",
        "install": "# Download latest exe release from GitHub\nhttps://github.com/carlospolop/PEASS-ng/releases"
    },
    
    # --- WEB ---
    "wfuzz": {
        "type": "CLI", "lang": "Python", "desc": "Web application bruteforcer.",
        "website": "https://wfuzz.readthedocs.io/", "repo": "https://github.com/xmendez/wfuzz",
        "install": "pip install wfuzz"
    },
    "wapiti": {
        "type": "CLI", "lang": "Python", "desc": "Web application vulnerability scanner.",
        "website": "https://wapiti.sourceforge.io/", "repo": "https://github.com/wapiti-scanner/wapiti",
        "install": "pip install wapiti3"
    },
    
    # --- PHASE 3: INFRASTRUCTURE & DEV ---
    "docker": {
        "type": "CLI/Engine", "lang": "Go", "desc": "Platform for developing, shipping, and running applications in containers.",
        "website": "https://www.docker.com/", "repo": "https://github.com/docker/docker-ce",
        "install": "sudo apt install docker.io docker-compose"
    },
    "kubernetes": {
        "type": "CLI (kubectl)", "lang": "Go", "desc": "Container orchestration system.",
        "website": "https://kubernetes.io/", "repo": "https://github.com/kubernetes/kubernetes",
        "install": "sudo apt install kubectl\n# OR (via snap)\nsudo snap install kubectl --classic"
    },
    "sniper": {
        "type": "Framework", "lang": "Shell", "desc": "Automated scanner that can be used during a penetration test to enumerate and scan for vulnerabilities.",
        "website": "https://github.com/1N3/Sn1per", "repo": "https://github.com/1N3/Sn1per",
        "install": "git clone https://github.com/1N3/Sn1per.git\ncd Sn1per\nsudo bash install.sh"
    },
    "virtualbox": {
        "type": "GUI", "lang": "C++", "desc": "Powerful x86 and AMD64/Intel64 virtualization product.",
        "website": "https://www.virtualbox.org/", "repo": "https://www.virtualbox.org/wiki/Downloads",
        "install": "sudo apt install virtualbox"
    },
    "wazuh": {
        "type": "Platform", "lang": "C/Python", "desc": "The Open Source Security Platform (SIEM/XDR).",
        "website": "https://wazuh.com/", "repo": "https://github.com/wazuh/wazuh",
        "install": "curl -sO https://packages.wazuh.com/4.7/wazuh-install.sh && sudo bash ./wazuh-install.sh -a"
    },
    "gh": {
        "type": "CLI", "lang": "Go", "desc": "GitHub’s official command line tool.",
        "website": "https://cli.github.com/", "repo": "https://github.com/cli/cli",
        "install": "sudo apt install gh"
    },
    "python-venv": {
        "type": "Library", "lang": "Python", "desc": "Creation of lightweight 'virtual environments' for Python.",
        "website": "https://docs.python.org/3/library/venv.html", "repo": "https://github.com/python/cpython",
        "install": "sudo apt install python3-venv\n# Usage:\npython3 -m venv myenv"
    },
    "wireshark": {
        "type": "GUI/CLI", "lang": "C", "desc": "The world's foremost network protocol analyzer.",
        "website": "https://www.wireshark.org/", "repo": "https://gitlab.com/wireshark/wireshark",
        "install": "sudo apt install wireshark"
    },
    "tmux": {
        "type": "CLI", "lang": "C", "desc": "Terminal multiplexer.",
        "website": "https://github.com/tmux/tmux", "repo": "https://github.com/tmux/tmux",
        "install": "sudo apt install tmux"
    },
    "burpsuite": {
        "type": "GUI", "lang": "Java", "desc": "Web vulnerability scanner and proxy.",
        "website": "https://portswigger.net/burp", "repo": "https://portswigger.net/burp/releases",
        "install": "sudo apt install burpsuite"
    }

}

DEST_DIR = "/home/alucard/website/portfolio/content/tools"
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

print(f"🚀 Injecting Tool Installation Guides...")

for name, info in TOOLS_DB.items():
    filename = f"{name}.md"
    filepath = os.path.join(DEST_DIR, filename)
    
    # Skip if exists? No, user wants update. But carefully.
    # We force enrich: false
    
    content = f"""---
title: "{name.capitalize()}"
date: "2026-01-05"
category: "tools"
enrich: false
image: "assets/tool-thumb.png"
tags: "{name}, cybersecurity, tool"
description: "{info['desc']}"
---

# {name.capitalize()}

> **Type**: {info['type']}
> **Language**: {info['lang']}

**{name.capitalize()}** {info['desc']}

## Official Resources
*   **Official Website**: [{info['website']}]({info['website']})
*   **GitHub Repository**: [{info['repo']}]({info['repo']})

## Installation

### Primary Method
```bash
{info['install']}
```

## Basic Usage
```bash
{name} --help
```
"""
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"✅ Created {filename}")
