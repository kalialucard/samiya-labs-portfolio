import os
import glob

TAG_UPDATES = {
    "infrastructure": ["docker", "kubernetes", "wazuh", "virtualbox", "python-venv", "tmux"],
    "web": ["burpsuite", "zap", "sqlmap", "nikto", "gobuster", "ffuf", "wpscan", "commix", "wapiti", "dirbuster", "dirsearch", "feroxbuster", "httpx", "katana", "nuclei", "whatweb", "waybackurls", "gau"],
    "network": ["nmap", "wireshark", "tcpdump", "netcat", "chisel", "sshuttle", "masscan", "rustscan", "naabu", "socat", "proxychains"],
    "ad": ["bloodhound", "evil-winrm", "netexec", "responder", "impacket", "mimikatz", "rubeus", "sharphound", "kerbrute", "crackmapexec", "powerview", "winpeas"]
}

BASE_DIR = "/home/alucard/website/portfolio/content"

def update_file_tags(file_path, new_tag):
    with open(file_path, 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    new_lines = []
    updated = False
    
    for line in lines:
        if line.startswith('tags:'):
            # Parse existing tags
            try:
                raw_val = line.split(':', 1)[1].strip()
                # Remove artifacts from previous broken run (quotes, extra commas)
                clean_val = raw_val.replace('"', '').replace("'", "")
                current_tags = [t.strip() for t in clean_val.split(',') if t.strip()]
                
                if new_tag not in current_tags:
                    current_tags.append(new_tag)
                
                # Reconstruct
                clean_line = f'tags: {", ".join(current_tags)}'
                
                # Check if it actually changed (including format)
                if clean_line.strip() != line.strip():
                     new_lines.append(clean_line)
                     updated = True
                else:
                     new_lines.append(line)
            except:
                new_lines.append(line)

        else:
            new_lines.append(line)
            
    if updated:

        with open(file_path, 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"✅ Updated {os.path.basename(file_path)} with tag: {new_tag}")
    else:
        # print(f"⏩ (Skipped) {os.path.basename(file_path)} already has {new_tag}")
        pass

def main():
    print("🚀 Starting Batch Tag Update...")
    
    # 1. Update Tool Pages (content/tools/*.md)
    # 2. Update Command Pages (content/commands/*.md)
    
    for category, tools in TAG_UPDATES.items():
        print(f"\n📂 Processing Category: {category}...")
        for tool in tools:
            # Try finding the tool file in tools/
            tool_path = os.path.join(BASE_DIR, "tools", f"{tool}.md")
            if os.path.exists(tool_path):
                update_file_tags(tool_path, category)
                
            # Try finding the tool file in commands/
            cmd_path = os.path.join(BASE_DIR, "commands", f"{tool}.md")
            if os.path.exists(cmd_path):
                update_file_tags(cmd_path, category)
            # Try case-insensitive lookup if needed, but for now stick to lower
            
    print("\n✨ Tag Update Complete!")

if __name__ == "__main__":
    main()
