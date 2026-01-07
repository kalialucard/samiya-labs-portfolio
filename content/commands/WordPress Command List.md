---
title: WordPress Command List
date: YYYY-MM-DD
category: commands
enrich: false
image: assets/cmd-thumb.png
tags: cybersecurity, nmap, wpscan, wordpress, reconnaissance, enumeration, web application
  security, beginner guide, hacking, network scanning, vulnerability analysis
description: A detailed, beginner-friendly walkthrough on using Nmap and WPScan for
  web application reconnaissance and enumeration, focusing on WordPress security.
last_enriched: '2026-01-07'
---

Welcome, aspiring cybersecurity professionals! Today, we embark on a journey to understand how attackers (and importantly, defenders!) explore and identify weaknesses in web applications, specifically those built on WordPress. We'll be using two powerful command-line tools: **Nmap** and **WPScan**. Our goal is to go from raw technical output to a clear, step-by-step educational walkthrough, so you can grasp the 'why' and 'how' behind each command.

## Reconnaissance

Reconnaissance is the crucial first step in any cybersecurity engagement. It's like being a detective; we gather as much information as possible about our target before making any moves. For web applications, this often involves understanding what services are running and what technologies are being used.

### Using Nmap for Initial Discovery

Nmap (Network Mapper) is a versatile tool for network discovery and security auditing. We'll start by using it to get a general sense of what's running on our target website.

```bash
nmap -sV --script http-wordpress-enum <target-url>
```

**🧠 Beginner Analysis**

Let's break down this command:

*   **`nmap`**: This is simply calling the Nmap tool to start our scan.
*   **`-sV`**: This flag stands for "Service Version detection." Nmap will try to determine the exact version of the software running on open ports. Knowing the version is critical because specific versions often have known vulnerabilities. For example, if we see an old version of Apache web server, we can look up vulnerabilities associated with *that specific version*.
*   **`--script http-wordpress-enum`**: This is where we tell Nmap to use a special, pre-written mini-program (a script) to help us. The `http-wordpress-enum` script is designed to specifically look for common WordPress components, like plugins and themes.
*   **`<target-url>`**: This is a placeholder for the actual web address of the website you are analyzing (e.g., `http://example.com`).

**What this command tells us:** We're launching Nmap, asking it to be thorough by checking service versions, and instructing it to use a script specifically designed to enumerate WordPress installations. This is a great way to quickly identify if a site is running WordPress and get an initial idea of its structure.

---

Sometimes, we want to focus our Nmap scans on specific services. For web servers, port 80 is the standard port for HTTP traffic.

```bash
nmap -p80 --script http-wordpress-users <target-url>
```

**🧠 Beginner Analysis**

*   **`-p80`**: This flag tells Nmap to *only* scan port 80. If the website is running on a different port (like 8080 or 443 for HTTPS), this scan wouldn't find it. For web servers, port 80 is the most common "front door."
*   **`http-wordpress-users`**: This is another Nmap script. This one is specifically looking for ways to enumerate usernames associated with the WordPress installation. Knowing valid usernames is a key step in attempting brute-force attacks later.

**What this command tells us:** We're telling Nmap to focus its efforts on the standard web port (80) and to use a script that tries to discover the names of users who can log into this WordPress site. This is a targeted approach to gather specific information about user accounts.

---

When we have a list of potential usernames, we might want to try and guess their passwords. Nmap can assist with this using brute-force techniques.

```bash
nmap -p80 --script http-wordpress-brute --script-args 'userdb=users.txt,passdb=passwords.txt' <target>
```

**🧠 Beginner Analysis**

*   **`http-wordpress-brute`**: This Nmap script is designed to attempt brute-force logins against WordPress. It will try to guess passwords for known or discovered usernames.
*   **`--script-args 'userdb=users.txt,passdb=passwords.txt'`**: This is how we provide custom information to the script.
    *   `userdb=users.txt`: This tells the script to use a file named `users.txt` which contains a list of usernames to try.
    *   `passdb=passwords.txt`: This tells the script to use a file named `passwords.txt` which contains a list of passwords to attempt.

**What this command tells us:** We are instructing Nmap to try and guess passwords for users on the WordPress site using a brute-force approach. We are providing Nmap with our own lists of usernames and potential passwords to make this process more efficient. **Important Note:** Brute-forcing can be noisy and may trigger security alerts or get your IP address blocked. Always ensure you have explicit permission before performing such actions.

---

Nmap has a powerful scripting engine (NSE) with many built-in scripts. You can tell Nmap to run all scripts related to a specific application.

```bash
nmap -p80 --script "http-wordpress-*" <target>
```

**🧠 Beginner Analysis**

*   **`"http-wordpress-*"`**: This is a wildcard. It tells Nmap to run *every single Nmap script* that starts with `http-wordpress-`. This is a very broad approach and can be useful for discovering a wide range of information about the WordPress site, from plugins and themes to user enumeration and potential vulnerabilities.

**What this command tells us:** This is a comprehensive command that tells Nmap to look for and run all available WordPress-related scripts. It's like saying, "Nmap, do everything you know about WordPress!" This can yield a lot of information but might also take longer and produce a lot of output.

---

Some WordPress scripts focus on identifying specific vulnerabilities or misconfigurations.

```bash
nmap -p80 --script http-wordpress-pingback <target>
```

**🧠 Beginner Analysis**

*   **`http-wordpress-pingback`**: This script specifically checks for the presence and configuration of the WordPress Pingback feature. Pingbacks can sometimes be exploited to make the target server send requests to other arbitrary hosts, which can be used in certain amplification attacks.

**What this command tells us:** We're using Nmap to specifically investigate the Pingback feature of the WordPress site. Understanding if this feature is enabled and how it's configured can reveal potential avenues for exploitation.

---

Beyond WordPress-specific enumeration, Nmap can also be used to find common sensitive files or directories that might have been left exposed.

```bash
nmap -p80 --script http-enum --script-args http-enum.basepath=/ <target>
```

**🧠 Beginner Analysis**

*   **`http-enum`**: This script attempts to discover common web application vulnerabilities and misconfigurations by looking for specific files and directories. It often checks for things like backup files (`.php.bak`), version control directories (`.git`), or administrative interfaces (`phpmyadmin`).
*   **`--script-args http-enum.basepath=/`**: This argument tells the `http-enum` script where to start its search. `basepath=/` means it should start from the root directory of the website. If you were targeting a specific subdirectory, you might set this to something like `/wordpress/`.

**What this command tells us:** We're using Nmap's `http-enum` script to actively scan the website for potentially sensitive files or directories that might be accidentally exposed. By starting from the root directory (`/`), we're ensuring a thorough search of the website's structure.

---

When using the broad `http-wordpress-*` script category, you might want to ensure you're getting the most comprehensive results possible.

```bash
nmap -sV --script http-wordpress-enum --script-args search-limit=all <target>
```

**🧠 Beginner Analysis**

*   **`search-limit=all`**: This argument modifies the behavior of the `http-wordpress-enum` script. By default, it might only check a limited number of known plugins and themes. Setting `search-limit=all` instructs the script to attempt to enumerate *all* plugins and themes that Nmap knows about. Nmap's database for plugins and themes can be quite extensive (potentially tens of thousands).

**What this command tells us:** We're enhancing our WordPress enumeration by telling Nmap to go beyond the default checks and try to identify every single plugin and theme it can. This significantly increases the chances of finding less common or custom components, which might also harbor vulnerabilities.

---

## Enumeration with WPScan

While Nmap is a general-purpose scanner, tools like WPScan are purpose-built for WordPress. They have a much deeper understanding of WordPress's unique structure and a more comprehensive database of vulnerabilities.

```bash
wpscan --url <target-url> --enumerate vp,vt,u --api-token <YOUR_TOKEN>
```

**🧠 Beginner Analysis**

*   **`wpscan`**: This is the command to launch the WPScan tool.
*   **`--url <target-url>`**: Similar to Nmap, this specifies the target website.
*   **`--enumerate vp,vt,u`**: This is a powerful option that tells WPScan to enumerate specific items:
    *   `vp`: **Vulnerable Plugins**. WPScan will search for installed plugins and check if they have known vulnerabilities.
    *   `vt`: **Vulnerable Themes**. Similar to plugins, it checks installed themes for known security flaws.
    *   `u`: **Users**. It will attempt to discover valid usernames on the WordPress site.
*   **`--api-token <YOUR_TOKEN>`**: WPScan utilizes an external API (often from WPScan's own service or other vulnerability databases) to get the latest vulnerability information. You'll need to sign up for an API token to use this feature effectively. This token allows WPScan to access a vast and up-to-date database of known WordPress exploits and vulnerabilities.

**What this command tells us:** We're using WPScan to perform a detailed enumeration of the WordPress site. We're specifically asking it to find vulnerabilities in plugins and themes, and to list out valid user accounts. The `--api-token` ensures WPScan is using the most current vulnerability intelligence available.

---

When trying to discover plugins, sometimes they are not immediately obvious. WPScan has techniques to uncover them.

```bash
wpscan --url <target-url> --plugins-detection mixed --stealthy
```

**🧠 Beginner Analysis**

*   **`--plugins-detection mixed`**: This tells WPScan to use a combination of detection methods for plugins. It might use passive methods (like looking at JavaScript files or HTTP headers) and aggressive methods (like sending specific requests that might reveal a plugin's presence). This increases the chances of finding plugins, especially those that try to hide.
*   **`--stealthy`**: This option makes WPScan operate more quietly. It will slow down its requests and try to avoid making obvious patterns that a web application firewall (WAF) or intrusion detection system (IDS) might flag. This is useful for avoiding detection while performing reconnaissance.

**What this command tells us:** We're instructing WPScan to be very thorough in its search for plugins, using multiple detection techniques. We're also telling it to be as discreet as possible to avoid alerting the website's security systems. This is a good approach when you suspect the target might have security measures in place.

---

A common attack vector against web applications is brute-forcing login credentials. WPScan can be used for this.

```bash
wpscan --url <target-url> -U admin -P /path/to/passwords.txt --throttle 1000
```

**🧠 Beginner Analysis**

*   **`-U admin`**: This flag specifies a particular username, in this case, `admin`, that we want to target. This is useful if you've already discovered a likely username (e.g., from `http-wordpress-users` or `wpscan --enumerate u`).
*   **`-P /path/to/passwords.txt`**: This flag tells WPScan to use the provided file (`/path/to/passwords.txt`) as a dictionary of passwords to try against the target username.
*   **`--throttle 1000`**: This is a crucial option for responsible scanning. It tells WPScan to wait 1000 milliseconds (1 second) between each login attempt. This prevents overwhelming the server with too many requests too quickly, which could cause it to crash or, more likely, to block your IP address.

**What this command tells us:** We're using WPScan to attempt to log in to the WordPress site by trying a specific username (`admin`) and a list of common passwords. The `--throttle` option ensures we're not being overly aggressive and potentially triggering security measures or disrupting the target server. **Again, always ensure you have explicit permission before attempting brute-force attacks.**

---

WPScan can also help discover different types of content beyond just plugins and themes.

```bash
wpscan --url <target-url> --enumerate cb,dbe
```

**🧠 Beginner Analysis**

*   **`--enumerate cb,dbe`**: This option tells WPScan to enumerate additional items:
    *   `cb`: **Comments found by the Blog**. This can sometimes reveal information about the site's structure or content.
    *   `dbe`: **Database Exporter**. This attempts to find configurations or endpoints related to database exports, which could be a sensitive finding.

**What this command tells us:** We're expanding our enumeration with WPScan to look for other interesting pieces of information, such as comments that might offer clues, and potential ways to access or export the site's database.

---

### Comparing Nmap and WPScan

| Feature            | Nmap                                                                 | WPScan                                                                             |
| :----------------- | :------------------------------------------------------------------- | :--------------------------------------------------------------------------------- |
| **Speed**          | Very Fast (excellent for initial port scanning and service discovery) | Slower (more thorough and specialized for WordPress, can take longer for full scans) |
| **Vulnerability Data** | General purpose, can use many NSE scripts.                            | Specialized, leverages a dedicated WordPress vulnerability database (WPVulnDB).     |
| **Version Detection** | Guesses based on banner information and service responses.             | Highly Accurate, leverages specific WordPress versioning techniques.                |
| **Hidden Files/Dirs**| Basic capabilities with `http-enum` and similar scripts.               | Advanced capabilities, designed to find WordPress-specific backups and database files. |

**🧠 Beginner Analysis**

Nmap is your general-purpose toolkit for network scanning. It's like a Swiss Army knife – useful for many tasks, especially in the initial phases of reconnaissance. WPScan, on the other hand, is a highly specialized tool, like a scalpel designed specifically for WordPress. It has a much deeper understanding of WordPress and its ecosystem, making it incredibly effective for finding WordPress-specific vulnerabilities and information that Nmap might miss. Often, you'll use Nmap for broad discovery and then switch to WPScan for a deep dive into WordPress.
