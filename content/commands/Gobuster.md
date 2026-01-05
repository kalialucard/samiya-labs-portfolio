---
title: Gobuster
date: YYYY-MM-DD
category: commands
enrich: true
image: assets/cmd-thumb.png
tags: linux, shell, windows
description: Reference for command.
---

# Gobuster

> **Platform**: Linux / Windows


```
gobuster dir -u https://example.com -w /path/to/wordlist.txt
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`dir`**|"I want to look for hidden **folders** and **files**."|
|**`-u`**|"**URL.** This is the website I am targeting."|
|**`-w`**|"**Wordlist.** Use this giant list of names to guess folder names."|

```
gobuster dir -u <target> -w <list> -x php,txt,html
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`-x`**|"**Extensions.** Don't just look for 'admin', look for 'admin.php' or 'admin.txt'."|

```
gobuster dns -d example.com -w /path/to/subdomains.txt
```

|**This Part...**|**Means This in Simple English**|
|---|---|
|**`dns`**|"I want to look for **subdomains** (like https://www.google.com/search?q=dev.site.com or https://www.google.com/search?q=api.site.com)."|
|**`-d`**|"**Domain.** This is the main website address I’m checking."|
