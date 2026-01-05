---
title: "Nmap Command List"
date: 2026-01-05
category: commands
enrich: false

tags: nmap, cybersecurity, command reference, beginner, network
description: Top 10 essential commands and a master guide for using Nmap in penetration testing.
---

# Nmap Command Guide

**Nmap (Network Mapper)** is the industry standard for network discovery and security auditing. It uses raw IP packets to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems they are running, and what packet filters/firewalls are in use.

## Top 10 Useful Commands

### 1. Basic Scan
```bash
nmap <target>
```
**Explanation:** The default scan. Scans the top 1000 most common ports. Useful for a quick overview of a target.

### 2. Service Version Detection
```bash
nmap -sV <target>
```
**Explanation:** Probes open ports to determine the service/version info. Crucial for identifying vulnerable software versions.

### 3. Aggressive Scan (The "All-in-One")
```bash
nmap -A <target>
```
**Explanation:** Enables OS detection, version detection, script scanning, and traceroute. It's loud but provides the most information in a single command.

### 4. Scan All Ports
```bash
nmap -p- <target>
```
**Explanation:** Scans all 65535 ports (1-65535). Taking significantly longer but ensures no services running on non-standard ports are missed.

### 5. OS Detection
```bash
nmap -O <target>
```
**Explanation:** Attempts to determine the operating system of the target by analyzing IP packet responses.

### 6. Vulnerability Scan (NSE)
```bash
nmap --script vuln <target>
```
**Explanation:** Uses the Nmap Scripting Engine (NSE) to run a set of scripts specifically designed to check for known vulnerabilities.

### 7. Fast Scan
```bash
nmap -F <target>
```
**Explanation:** Scans the 100 most common ports instead of the top 1000. Useful for very quick reconnaissance.

### 8. UDP Scan
```bash
nmap -sU <target>
```
**Explanation:** Scans for open UDP ports. UDP scanning is slower and more difficult than TCP but essential for finding services like DNS, SNMP, and DHCP.

### 9. Output to File
```bash
nmap -oN output.txt <target>
```
**Explanation:** Saves the scan results to a normal text file. You can also use `-oX` for XML or `-oA` for all formats.

### 10. Stealth Scan (SYN Scan)
```bash
nmap -sS <target>
```
**Explanation:** The default scan if run as root. It performs a "half-open" scan, which is faster and harder for firewalls to log than a full connect scan.

## The Most Powerful Command

The most powerful command for a situational awareness assessment is combining aggressive options with a full port scan:

```bash
nmap -p- -A -T4 <target>
```

**Why it's powerful:**
*   `-p-`: Scans **every single port**, ensuring nothing is hidden.
*   `-A`: Runs **OS detection**, **Version detection**, **Traceroute**, and **Scripts**.
*   `-T4`: Increases the speed (Timing Template 4) to make this heavy scan finish in a reasonable time.

This single command provides a complete map of the target's attack surface.

