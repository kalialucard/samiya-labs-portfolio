---
title: WordPress Command List
date: YYYY-MM-DD
category: commands
enrich: true
image: assets/cmd-thumb.png
tags: linux, shell, windows
description: Reference for command.
---

# Command Name

> **Platform**: Linux / Windows

## Nmap

```
nmap -sV --script http-wordpress-enum <target-url>
```

| **This Part...**          | **Means This in Simple English**                                              |
| ------------------------- | ----------------------------------------------------------------------------- |
| **`nmap`**                | "Open the Nmap tool."                                                         |
| **`-sV`**                 | "Check the **Version**. Tell me exactly what version of software is running." |
| **`--script`**            | "Use a special pre-written mini-program (script) for this job."               |
| **`http-wordpress-enum`** | "Run the WordPress **Enumerator**. List every plugin and theme you find."     |

```
nmap -p80 --script http-wordpress-users <target-url>
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`-p80`**|"Only look at **Port 80** (the standard front door for websites)."|
|**`http-wordpress-users`**|"Find the names of people who can log in to this WordPress site."|

```
nmap -p80 --script http-wordpress-brute --script-args 'userdb=users.txt,passdb=passwords.txt' <target>
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`http-wordpress-brute`**|Try to guess the password for the site’s users.|
|**`--script-args`**|Provide the tool with your custom lists of usernames and passwords.|

```
nmap -p80 --script "http-wordpress-*" <target>
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`"http-wordpress-*"`**|**Run everything.** This tells Nmap to run every single WordPress-related script it has in its library at once.|

```
nmap -p80 --script http-wordpress-pingback <target>
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`http-enum`**|Look for common folders like `/wp-config.php.bak` or `.git` that shouldn't be public.|

```
nmap -p80 --script http-enum --script-args http-enum.basepath=/ <target>
```

|**Command Part**|**What it does**|
|---|---|
|**`http-enum`**|Spiders the site to find hidden folders and sensitive files (like `.git` or `phpmyadmin`).|
|**`basepath=/`**|Tells Nmap to start looking from the main folder of the website.|

```
nmap -sV --script http-wordpress-enum --script-args search-limit=all <target>

```

|**Command Part**|**What it does**|
|---|---|
|**`search-limit=all`**|Changes the search from the "top 100" to every plugin in Nmap's database (~14,000+).|

```
nmap -p80 --script "http-wordpress-*" <target>
```

---
## WpScan

```
wpscan --url <target-url> --enumerate vp,vt,u --api-token <YOUR_TOKEN>
```

| **This Part...**  | **Means This in Simple English**                                          |
| ----------------- | ------------------------------------------------------------------------- |
| **`--enumerate`** | "List out the following items."                                           |
| **`vp`**          | "**Vulnerable Plugins.** Only show me plugins with known security holes." |
| **`vt`**          | "**Vulnerable Themes.** Only show me themes that are dangerous."          |
| **`u`**           | "**Users.** Find the login names of people on the site."                  |
| **`--api-token`** | "Connect to the master database to check for real-world exploits."        |

```
wpscan --url <target-url> --plugins-detection mixed --stealthy
```

| **This Part...**                | **Means This in Simple English**                                                    |
| ------------------------------- | ----------------------------------------------------------------------------------- |
| **`--plugins-detection mixed`** | "Use every trick possible (passive and aggressive) to find hidden plugins."         |
| **`--stealthy`**                | "Slow down and hide my identity so the website doesn't realize it's being scanned." |

```
wpscan --url <target-url> -U admin -P /path/to/passwords.txt --throttle 1000
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`-U admin`**|"Target the user named **admin**."|
|**`-P passwords.txt`**|"Try every password in this text file."|
|**`--throttle 1000`**|"Wait 1 second between each try so the server doesn't crash or block me."|

```
wpscan --url <target-url> --enumerate cb,dbe

```

| **Feature**            | **Nmap**  | **WPScan**             |
| ---------------------- | --------- | ---------------------- |
| **Speed**              | Very Fast | Slower (More Thorough) |
| **Vulnerability Data** | General   | Specialized (WPVulnDB) |
| **Version Detection**  | Guesses   | Highly Accurate        |
| **Hidden Files**       | Basic     | Advanced (Backups/DBs) |

