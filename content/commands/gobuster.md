---
title: Gobuster Command List
date: 2026-01-05
category: commands
enrich: false
tags:
- gobuster
- web enumeration
- directory brute-forcing
- cybersecurity
- penetration testing
- beginner
- educational
description: A comprehensive educational walkthrough of the Gobuster tool, designed
  for entry-level cybersecurity students. This guide explains Gobuster's purpose,
  provides detailed explanations of its most useful commands with practical examples,
  and highlights its most powerful use case.
last_enriched: '2026-01-05'
---

Welcome, aspiring cybersecurity professionals! Today, we're diving into a fundamental tool for web application penetration testing: **Gobuster**. If you've ever wondered how attackers find hidden pages or sensitive files on a website, Gobuster is likely involved. This guide will break down what it is, how it works, and how you can use it effectively.

## 1. Brief Explanation: What is Gobuster and Why is it Used?

**Gobuster** is an open-source tool written in Go (hence the "Go" in its name) that is primarily used for **brute-forcing directories and files** on web servers. Think of it as a highly efficient way to explore a website's hidden corners that aren't linked directly.

**Why is this important in cybersecurity?**

*   **Finding Hidden Content:** Websites often have administrative panels, backup files, configuration files, or other sensitive directories that are not intentionally made public but might be accessible if you know their names.
*   **Discovering API Endpoints:** Modern web applications heavily rely on APIs. Gobuster can help discover API endpoints that might be vulnerable or contain valuable information.
*   **Identifying Subdomains:** While not its primary function, Gobuster can also be used in conjunction with wordlists to discover subdomains.
*   **Enumerating Web Services:** It helps us understand the structure of a web application, which is a crucial step in identifying potential attack vectors.

In simpler terms, Gobuster helps us "guess" common or expected file and directory names on a web server to see if they exist and return a response.

## 2. Top 10 Useful Gobuster Commands

Let's get hands-on with some of the most common and powerful commands you'll use with Gobuster. We'll cover various scenarios to illustrate its versatility.

---

### Command 1: Basic Directory Brute-Forcing

This is the bread-and-butter of Gobuster. We'll use a common wordlist to find directories on a target website.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

**Flag Explanations:**

*   `-u http://testphp.vulnweb.com`: This specifies the *   `-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`: This tells Gobuster which **wordlist file** to use. A wordlist is simply a text file containing a list of potential directory or file names. `/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt` is a common location for such lists on Linux systems.

**Output and Why We Use It:**

Gobuster will start making requests to `http://testphp.vulnweb.com/directoryname` for every `directoryname` in the wordlist. It will report back the directories it finds that return a successful HTTP status code (usually 200 OK).

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Concurrent threads:       10
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 10] [Speed: 78 requests/sec] [HTTP errors: 0] [0:00:55<0:00:00] [CODE:200]: /images
[Threads: 10] [Speed: 85 requests/sec] [HTTP errors: 0] [0:00:57<0:00:00] [CODE:200]: /admin
[Threads: 10] [Speed: 75 requests/sec] [HTTP errors: 0] [0:01:00<0:00:00] [CODE:200]: /backup
...
```

This command is essential because it helps us discover parts of the website that are not immediately obvious. Finding an `/admin` directory, for example, might lead us to a login page we can then try to brute-force or exploit. Finding a `/backup` directory could expose old or sensitive files.

---

### Command 2: Brute-Forcing Specific File Extensions

Websites often use specific file extensions like `.php`, `.html`, `.asp`, etc. We can tell Gobuster to look for these.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,bak,txt
```

**Flag Explanations:**

*   `-x php,html,bak,txt`: This flag tells Gobuster to append these **file extensions** to each word in the wordlist before making a request. So, if the word is `config`, Gobuster will try `config.php`, `config.html`, `config.bak`, and `config.txt`.

**Output and Why We Use It:**

The output will be similar to the previous command, but it will now include results for files with the specified extensions.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
File extensions:          php,html,bak,txt
Concurrent threads:       10
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 10] [Speed: 90 requests/sec] [HTTP errors: 0] [0:00:45<0:00:00] [CODE:200]: /index.php
[Threads: 10] [Speed: 88 requests/sec] [HTTP errors: 0] [0:00:47<0:00:00] [CODE:200]: /config.txt
[Threads: 10] [Speed: 80 requests/sec] [HTTP errors: 0] [0:00:49<0:00:00] [CODE:200]: /backup.bak
...
```

This is extremely useful for finding configuration files (`config.txt`), backup files (`backup.bak`), or specific application scripts (`login.php`) that might be overlooked if we only search for directories.

---

### Command 3: Filtering by HTTP Status Code

Sometimes, we only care about specific responses. For instance, we might want to see only successful requests (200 OK) or perhaps redirects (301, 302).

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -s 200,301,302
```

**Flag Explanations:**

*   `-s 200,301,302`: This flag allows us to **specify which HTTP status codes** Gobuster should report. In this case, we're telling it to show us only directories/files that return a 200 OK (success), 301 (Moved Permanently), or 302 (Found/Moved Temporarily) status code.

**Output and Why We Use It:**

The output will be filtered to only display entries that match the specified status codes.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Status codes:             200,301,302
Concurrent threads:       10
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 10] [Speed: 80 requests/sec] [HTTP errors: 0] [0:00:50<0:00:00] [CODE:200]: /images
[Threads: 10] [Speed: 82 requests/sec] [HTTP errors: 0] [0:00:52<0:00:00] [CODE:302]: /login
[Threads: 10] [Speed: 78 requests/sec] [HTTP errors: 0] [0:00:55<0:00:00] [CODE:200]: /admin
...
```

Filtering by status codes helps us reduce noise. A 200 OK is a definitive "found it." A 301 or 302 redirect might point to a new location or a login page, which is also very valuable information. By excluding codes like 403 (Forbidden) or 404 (Not Found), we can focus on what's actually accessible or redirects us somewhere interesting.

---

### Command 4: Using a Custom Wordlist

If you have a specialized wordlist (perhaps found during reconnaissance or created yourself), you can use it.

```bash
gobuster dir -u http://testphp.vulnweb.com -w ./my_custom_wordlist.txt
```

**Flag Explanations:**

*   `-w ./my_custom_wordlist.txt`: This uses your **own wordlist file**. The `./` indicates that the file is in the current directory.

**Output and Why We Use It:**

The output will be based on the words in `my_custom_wordlist.txt`.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 ./my_custom_wordlist.txt
Concurrent threads:       10
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 10] [Speed: 70 requests/sec] [HTTP errors: 0] [CODE:200]: /internal
[Threads: 10] [Speed: 72 requests/sec] [HTTP errors: 0] [CODE:200]: /dev_config
...
```

Using custom wordlists is crucial when the standard ones miss something. You might have discovered during reconnaissance that the application uses a specific framework or company naming convention, allowing you to create a targeted wordlist.

---

### Command 5: Changing the Number of Threads

Gobuster can be fast, but sometimes you need to control how many requests it sends concurrently.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50
```

**Flag Explanations:**

*   `-t 50`: This sets the **number of concurrent threads**. Higher numbers mean more requests are sent at the same time, speeding up the scan. However, too many threads can overwhelm the target server, your own network, or trigger security defenses (like Intrusion Detection Systems - IDS).

**Output and Why We Use It:**

The scan will be faster if the server can handle the load.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Concurrent threads:       50
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 50] [Speed: 350 requests/sec] [HTTP errors: 0] [0:00:20<0:00:00] [CODE:200]: /images
[Threads: 50] [Speed: 360 requests/sec] [HTTP errors: 0] [0:00:21<0:00:00] [CODE:200]: /admin
...
```

We adjust the thread count to balance speed with stability. If a server is slow or has defenses, we might reduce the threads. If it's robust and we want results quickly, we increase them cautiously.

---

### Command 6: Setting a Timeout

This helps manage slow or unresponsive servers.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50 -timeout 15
```

**Flag Explanations:**

*   `-timeout 15`: This sets the **timeout in seconds** for each request. If the server doesn't respond within this time, Gobuster will consider the request timed out and move on.

**Output and Why We Use It:**

This prevents Gobuster from getting stuck on slow requests, making the overall scan more efficient, especially on unstable networks or with poorly performing web servers.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Concurrent threads:       50
Timeout:                  15
User Agent:               gobuster/3.1.0
] [Threads: 50] [Speed: 340 requests/sec] [HTTP errors: 0] [0:00:22<0:00:00] [CODE:200]: /images
[Threads: 50] [Speed: 330 requests/sec] [HTTP errors: 0] [0:00:23<0:00:00] [CODE:200]: /admin
... (No timed-out requests are reported if they don't return a specific error code)
```

We use this to ensure that a single slow server doesn't halt the entire scanning process.

---

### Command 7: Changing the User Agent

Some web servers might block requests from the default Gobuster user agent. Changing it can help bypass these basic filters.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
```

**Flag Explanations:**

*   `-a "Mozilla/5.0 ..."`: This flag allows you to specify a custom **User-Agent string**. A User-Agent string identifies the client (e.g., your browser) to the web server. Using a common browser's User-Agent can make your requests look like they are coming from a legitimate user.

**Output and Why We Use It:**

If the server was previously blocking Gobuster's default agent, this might allow the scan to proceed.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
User Agent:               Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36
Concurrent threads:       10
Timeout:                  10
] [Threads: 10] [Speed: 70 requests/sec] [HTTP errors: 0] [0:00:58<0:00:00] [CODE:200]: /images
[Threads: 10] [Speed: 75 requests/sec] [HTTP errors: 0] [0:01:00<0:00:00] [CODE:200]: /admin
...
```

This is a common evasion technique. By mimicking a real browser, we can sometimes get around simple WAF (Web Application Firewall) rules or server configurations that are designed to block automated tools.

---

### Command 8: Outputting to a File

It's crucial to save your results for later analysis.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o gobuster_results.txt
```

**Flag Explanations:**

*   `-o gobuster_results.txt`: This flag tells Gobuster to **write all output** to the specified file.

**Output and Why We Use It:**

The scan will run as usual, but all findings and progress will be logged into `gobuster_results.txt`.

```
(Gobuster runs, and all its output is redirected to the file)
```

Saving results is fundamental. We can then revisit them, filter them, or use them as input for other tools without having to re-run the scan. Imagine finding 500 directories – you wouldn't want to lose that information!

---

### Command 9: Recursive Directory Discovery (Use with Caution!)

Gobuster can recursively explore subdirectories it finds. This is powerful but can be very time-consuming and resource-intensive.

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -r
```

**Flag Explanations:**

*   `-r`: This flag enables **recursive discovery**. If Gobuster finds a directory, it will then attempt to enumerate that directory as well, effectively crawling the website's structure.

**Output and Why We Use It:**

The output will show findings from the initial scan and then continue to discover and report from any subdirectories found.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
URL:                      http://testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
Concurrent threads:       10
Timeout:                  10
User Agent:               gobuster/3.1.0
] [Threads: 10] [Speed: 78 requests/sec] [HTTP errors: 0] [0:00:55<0:00:00] [CODE:200]: /images
[Threads: 10] [Speed: 85 requests/sec] [HTTP errors: 0] [0:00:57<0:00:00] [CODE:200]: /admin
  -> /admin/js (CODE:200)
  -> /admin/css (CODE:200)
] [Threads: 10] [Speed: 75 requests/sec] [HTTP errors: 0] [0:01:00<0:00:00] [CODE:200]: /backup
  -> /backup/old (CODE:200)
...
```

This is incredibly useful for mapping out the entire accessible structure of a web application, potentially uncovering deeply nested or complex directories that might hold vulnerabilities. **However, always be mindful of the target's resources and your own network bandwidth when using recursion.**

---

### Command 10: Discovering Subdomains

While primarily for directories, Gobuster can also be used to find subdomains if you provide a list of potential subdomain names.

```bash
gobuster dns -d testphp.vulnweb.com -w /usr/share/wordlists/dnsrecon/dns-Jhaddix.txt
```

**Flag Explanations:**

*   `dns`: This subcommand tells Gobuster we're performing **DNS enumeration** (subdomain discovery).
*   `-d testphp.vulnweb.com`: The *   `-w /usr/share/wordlists/dnsrecon/dns-Jhaddix.txt`: A wordlist containing potential **subdomain names** (e.g., `www`, `mail`, `dev`, `ftp`, `blog`).

**Output and Why We Use It:**

Gobuster will try to resolve each word from the wordlist as a subdomain of the target domain.

```
Gobuster v3.1.0
By GoBuster team
===============================================================================
Domain:                   testphp.vulnweb.com
Wordlist:                 /usr/share/wordlists/dnsrecon/dns-Jhaddix.txt
Concurrent threads:       10
Timeout:                  10
] [Threads: 10] [Speed: 150 requests/sec] [DNS records: A]: www.testphp.vulnweb.com
] [Threads: 10] [Speed: 140 requests/sec] [DNS records: A]: dev.testphp.vulnweb.com
] [Threads: 10] [Speed: 135 requests/sec] [DNS records: A]: blog.testphp.vulnweb.com
...
```

Discovering subdomains is critical because each subdomain can host a different application or service, potentially with its own set of vulnerabilities. For example, `dev.testphp.vulnweb.com` might be an unstable development environment that's easier to exploit than the main `www.testphp.vulnweb.com` site.

---

## 3. The Most Powerful Command

While many commands are useful, the "most powerful" command often combines several features to provide a comprehensive view. For Gobuster, a very powerful command would look something like this:

```bash
gobuster dir -u http://testphp.vulnweb.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,html,txt,bak,old,dev -s 200,301,302,403 -t 80 -timeout 12 -o comprehensive_scan.txt
```

**Explanation of its Power:**

This command is powerful because it's **comprehensive and practical**:

1.  **Broad Directory & File Discovery (`-w`, `-x`):** It uses a standard, medium-sized wordlist to look for common directories and also specifically targets common file extensions (`.php`, `.html`, `.txt`, `.bak`, `.old`, `.dev`), increasing the chances of finding interesting files.
2.  **Relevant Status Codes (`-s 200,301,302,403`):** It captures successful responses (200 OK), redirects (301, 302) which often lead to login pages or other interesting areas, and even 403 Forbidden responses. A 403 error means the resource exists, but access is denied – this can sometimes be bypassed, making it valuable to note.
3.  **Optimized Speed and Stability (`-t 80`, `-timeout 12`):** It uses a higher number of threads (80) for speed but sets a reasonable timeout (12 seconds) to avoid getting stuck on slow servers. This is a good balance for many scenarios.
4.  **Results Preservation (`-o comprehensive_scan.txt`):** All findings are saved to a file for later, detailed analysis.

**Why we would use this command:**

This single command aims to cast a wide net, efficiently exploring a significant portion of a web application's accessible structure. It's designed to discover a broad range of potentially interesting endpoints – from publicly accessible pages and admin interfaces to backup files and API endpoints. By capturing redirects and even forbidden responses, it provides clues about the application's layout and security posture that might be missed by simpler scans. It’s a great starting point for deeper investigation into a web target.

---

Remember, Gobuster is a tool in your arsenal. Always use it ethically and with permission on systems you are authorized to test. Happy hunting!
