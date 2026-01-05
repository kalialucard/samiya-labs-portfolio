import os
from datetime import datetime

tools_list = [
    "gobuster", "dirbuster", "dirsearch", "nmap", "hydra", "gowitness", "wpscan", 
    "amass", "finalrecon", "assetfinder", "hakrawler", "katana", "feroxbuster", 
    "nuclei", "nikto", "wfuzz", "ffuf", "findomain", "gospider", "sublist3r", 
    "wapiti", "knockpy", "sn1per", "spiderfoot", "waybackurls", "recon-ng", "chaos"
]

output_dir = "/home/alucard/website/portfolio/content/commands"
os.makedirs(output_dir, exist_ok=True)

for tool in tools_list:
    tool_formatted = tool.title()
    body_content = f"""# {tool_formatted} Command Guide

Please generate a detailed educational guide for the **{tool_formatted}** tool.
Follow this structure exactly:

1.  **Brief Explanation**: Explain what {tool_formatted} is and why it's used in cybersecurity.
2.  **Top 10 Useful Commands**: List the 10 most common/useful commands for this tool.
    *   For EACH command, provide the exact syntax in a code block.
    *   Explain what each flag does (`-x`, `-u`, etc.).
    *   Explain the *output* and *why* you would use this specific command.
3.  **The Most Powerful Command**: Highlight the single most powerful or "all-in-one" command for this tool and explain its power.

**Tone**: Educational, for a beginner student.
"""
    
    file_content = f"""---
title: "{tool_formatted} Command List"
date: 2026-01-05
category: commands
enrich: true
tags: {tool}, cybersecurity, command reference, beginner
description: Top 10 essential commands and a master guide for using {tool_formatted} in penetration testing.
---

{body_content}
"""
    
    filename = f"{tool.replace(' ', '-')}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Don't overwrite if exists (like WordPress or Gobuster)
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(file_content)
        print(f"✅ Created {filepath}")
    else:
        print(f"⏩ Skipped {filepath} (Exists)")
