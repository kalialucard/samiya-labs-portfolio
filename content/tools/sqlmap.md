---
title: "Sqlmap"
date: "2026-01-05"
category: "tools"
enrich: false
image: "assets/tool-thumb.png"
tags: "exploitation, sql-injection, python, automation"
description: "The primary tool for detecting and exploiting SQL injection flaws."
---

# Sqlmap

> **Type**: CLI
> **Language**: Python

**Sqlmap** is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

## Official Resources
*   **Official Website**: [sqlmap.org](https://sqlmap.org/)
*   **GitHub Repository**: [sqlmapproject/sqlmap](https://github.com/sqlmapproject/sqlmap)
*   **Wiki/Documentation**: [GitHub Wiki](https://github.com/sqlmapproject/sqlmap/wiki)

## Installation

### Option 1: Kali Linux / Debian (Recommended)
Sqlmap is pre-installed on Kali Linux. To install or update it:
```bash
sudo apt update
sudo apt install sqlmap
```

### Option 2: Git Clone (Manual)
To get the latest version directly from the source:
```bash
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev
cd sqlmap-dev
python3 sqlmap.py --help
```

### Option 3: Python Pip
```bash
pip install sqlmap
```

## Verification
Confirm installation by checking the version:
```bash
sqlmap --version
# Output: sqlmap/1.8.x#stable
```

## Basic Usage
To scan a simple URL:
```bash
sqlmap -u "http://target.com/index.php?id=1" --batch
```
