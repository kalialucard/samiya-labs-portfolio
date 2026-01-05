---
title: Gobuster
date: YYYY-MM-DD
category: commands
enrich: false
image: assets/cmd-thumb.png
tags: cybersecurity, penetration testing, ethical hacking, reconnaissance, enumeration,
  gobuster, web security, beginner
description: A detailed walkthrough of a simulated cybersecurity engagement, covering
  reconnaissance, enumeration, and exploitation using tools like Gobuster. Designed
  for entry-level students to understand practical hacking techniques.
last_enriched: '2026-01-05'
---

# Cybersecurity Engagement Walkthrough: A Beginner's Guide

Welcome, aspiring cybersecurity professionals! In this walkthrough, we'll be dissecting a simulated engagement, transforming raw technical notes into a comprehensive educational experience. Our goal is to understand the "why" and "how" behind each step, making complex concepts accessible for beginners. We'll cover essential phases like reconnaissance and enumeration, using practical examples and clear explanations.

## Reconnaissance

Reconnaissance is the first phase of any cybersecurity engagement. It's all about gathering information about the target system. Think of it like a detective gathering clues before making a move.

## Enumeration

Enumeration is where we start actively probing the target system to uncover more specific details, like open services and potential entry points. This is where we begin to find the "doors" and "windows" into the target.

# Gobuster Command Guide

**Gobuster** is a high-speed tool used to brute-force URIs (directories and files) in web sites, DNS subdomains, and Virtual Host names on target web servers. It is written in Go and is known for its speed.

## Top 10 Useful Commands

### 1. Directory/File Enum (Basic)
```bash
gobuster dir -u http://<target> -w /path/to/wordlist.txt
```
**Explanation:** The standard mode. Enumerates directories and files using a wordlist.

### 2. Extend/Add File Extensions
```bash
gobuster dir -u http://<target> -w wordlist.txt -x php,txt,html
```
**Explanation:** Appends extensions to each word in the wordlist to find specific files (e.g., `index.php`, `robots.txt`).

### 3. DNS Subdomain Enum
```bash
gobuster dns -d <domain.com> -w /path/to/subdomains.txt
```
**Explanation:** Uses DNS brute-forcing to find subdomains (e.g., `admin.example.com`, `dev.example.com`).

### 4. VHOST Enumeration
```bash
gobuster vhost -u http://<target> -w wordlist.txt
```
**Explanation:** Brute-forces virtual hosts. Essential when different sites are hosted on the same IP but served based on the `Host` header.

### 5. Disable SSL Verification
```bash
gobuster dir -k -u https://<target> -w wordlist.txt
```
**Explanation:** Skips SSL certificate verification (`-k`). Necessary for self-signed certs often found in CTFs or internal audits.

### 6. Set Thread Count
```bash
gobuster dir -u <target> -w wordlist.txt -t 50
```
**Explanation:** Increases threads to 50 (default is 10). Makes the scan faster but noisier.

### 7. Filter by Status Code
```bash
gobuster dir -u <target> -w wordlist.txt -s "200,204,301"
```
**Explanation:** Only shows results with specific HTTP status codes. Helps reduce noise.

### 8. Exclude Length (Hide False Positives)
```bash
gobuster dir -u <target> -w wordlist.txt --exclude-length 1234
```
**Explanation:** Hides responses of a specific size. Great for filtering out custom 404 pages that return "200 OK".

### 9. Use Proxy
```bash
gobuster dir -u <target> -w wordlist.txt --proxy http://127.0.0.1:8080
```
**Explanation:** Routes traffic through a proxy (like Burp Suite) for analysis or WAF evasion.

### 10. Output to File
```bash
gobuster dir -u <target> -w wordlist.txt -o results.txt
```
**Explanation:** Saves the findings to a file for reporting.

## The Most Powerful Command

For a thorough web assessment on a tough target:

```bash
gobuster dir -u https://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,sh,bak -k -t 40 --exclude-length 400 -o gobuster_scan.txt
```

**Why it's powerful:**
*   Checks for **5 common file extensions** simultaneously.
*   Ignores **SSL errors** (`-k`).
*   Runs fast with **40 threads**.
*   Filters out **false positives** (length 400).
*   Saves everything to a file.

### Discovering Hidden Directories and Files with Gobuster

One of the most common tasks during enumeration is to find hidden directories and files on a web server. These can often lead to sensitive information or administrative interfaces. We'll use a powerful tool called Gobuster for this.

Here's how we might use Gobuster to look for hidden content:

```bash
gobuster dir -u https://example.com -w /path/to/wordlist.txt
```

Let's break down this command:

*   **`gobuster`**: This is the name of the tool we are using. It's designed to brute-force web content discovery.
*   **`dir`**: This tells Gobuster that we want to perform directory and file enumeration. It means, "I want to look for hidden **folders** and **files**."
*   **`-u https://example.com`**: This is the target URL. The `-u` flag stands for **URL**. This is the website we are targeting for our scan. We are telling Gobuster to start looking on `https://example.com`.
*   **`-w /path/to/wordlist.txt`**: This specifies the **wordlist** file to use. A wordlist is simply a large text file containing a list of common directory and file names. Gobuster will try each name in this list against our target URL to see if it exists. The `-w` flag means, "Use this giant list of names to guess folder names."

**🧠 Beginner Analysis:**

When Gobuster runs this command, it will systematically send requests to `https://example.com/common_directory_name` for every entry in the `/path/to/wordlist.txt` file. If a directory or file exists, Gobuster will report it. This is incredibly useful because web developers often leave administrative interfaces, backup files, or configuration files in predictable locations that aren't directly linked from the main website.

### Searching for Specific File Types with Gobuster

Sometimes, we have an idea of the types of files we're looking for. For example, we might suspect there are PHP scripts or configuration files (like `.txt` or `.html`) that could be interesting. We can tell Gobuster to specifically look for these by adding the `-x` flag.

Here's an example:

```bash
gobuster dir -u <target> -w <list> -x php,txt,html
```

Let's explain the new part:

*   **`-x php,txt,html`**: This is the **extensions** flag. The `-x` tells Gobuster to append these file extensions to each word from the wordlist before making the request. So, instead of just looking for `admin`, it will also try `admin.php`, `admin.txt`, and `admin.html`. This significantly increases our chances of finding relevant files.

**🧠 Beginner Analysis:**

By using the `-x` flag, we're refining our search. If we know a web application is built with PHP, looking for `.php` files is a smart move. We might find administrative panels like `admin.php`, configuration files like `config.php.bak` (a common mistake is to leave backups with predictable names), or even error logs that expose sensitive data.

### Enumerating Subdomains with Gobuster

Many websites have associated subdomains. For instance, a company might have `blog.example.com`, `api.example.com`, or `dev.example.com`. These subdomains can host entirely different applications or services, some of which might be less secure than the main website. Gobuster can help us discover these.

Here's how we'd use Gobuster for subdomain enumeration:

```bash
gobuster dns -d example.com -w /path/to/subdomains.txt
```

Let's break this down:

*   **`gobuster`**: Again, the tool we're using.
*   **`dns`**: This tells Gobuster that we want to perform DNS (Domain Name System) enumeration. It means, "I want to look for **subdomains**."
*   **`-d example.com`**: This is the target **domain**. The `-d` flag specifies the main website address we are checking. Gobuster will use this domain as a base.
*   **`-w /path/to/subdomains.txt`**: Similar to before, this uses a **wordlist**, but this time the list contains potential subdomain names (like `www`, `mail`, `dev`, `admin`, `ftp`, etc.). Gobuster will try to resolve these names as subdomains of `example.com`.

**🧠 Beginner Analysis:**

When Gobuster runs `gobuster dns -d example.com -w /path/to/subdomains.txt`, it's essentially asking your DNS resolver (which is usually your internet provider's server) if names like `www.example.com`, `mail.example.com`, `dev.example.com`, etc., exist. If a subdomain is found, it means there's an active server associated with that name, and it becomes a new potential target for further investigation. Discovering subdomains is crucial because they can often be overlooked and may have weaker security controls.

***

We've now covered the initial steps of reconnaissance and enumeration, specifically using Gobuster to find hidden web content and subdomains. This is a fundamental skill for any budding cybersecurity professional! In the next stages of an engagement, we would typically analyze the discovered services and files for vulnerabilities and attempt to gain access.
