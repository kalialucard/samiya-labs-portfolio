---
title: Wazuh Command List
date: 2026-01-05
category: commands
enrich: false
tags: wazuh, cybersecurity, command reference, infrastructure
description: Top 10 essential commands for wazuh.
---

# Wazuh Command Guide

**Wazuh** is a SIEM/XDR platform. Steps generally involve the agent.

## Top 10 Useful Commands

### 1. Start Agent
```bash
systemctl start wazuh-agent
```
**Explanation:** Start the service.

### 2. Status
```bash
systemctl status wazuh-agent
```
**Explanation:** Check if connected to manager.

### 3. Log Test
```bash
/var/ossec/bin/wazuh-logtest
```
**Explanation:** Test how logs are parsed/decoded.

### 4. Agent Control (Manager)
```bash
/var/ossec/bin/agent_control -l
```
**Explanation:** List connected agents (on Manager).

### 5. Restart Helper
```bash
/var/ossec/bin/ossec-control restart
```
**Explanation:** Restart local processes.

### 6. Edit Config
```bash
nano /var/ossec/etc/ossec.conf
```
**Explanation:** Main configuration file.

### 7. Active Response Log
```bash
tail -f /var/ossec/logs/active-responses.log
```
**Explanation:** See if Wazuh blocked anything automatically.

### 8. Keys
```bash
/var/ossec/bin/manage_agents
```
**Explanation:** Add/Remove agent keys.

### 9. Upgrade Agent
```bash
/var/ossec/bin/agent_upgrade -a 001
```
**Explanation:** Upgrade remote agent.

### 10. Verify Config
```bash
/var/ossec/bin/verify-agent-conf
```
**Explanation:** Check config syntax.

## The Most Powerful Command
```bash
/var/ossec/bin/wazuh-logtest
```
**Explanation:** Interactively debug why your security rules aren't triggering on specific log lines.

