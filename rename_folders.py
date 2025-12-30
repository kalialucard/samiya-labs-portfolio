import os
import shutil

# Mapping: Short Slug -> Full Domain Slug
MAPPING = {
    "ai": "ai-machine-learning",
    "devsecops": "cloud-secure-development-operations",
    # "ethical-hacking" is already "ethical-hacking", checking target...
    "ethical-hacking": "ethical-hacking-vulnerability-testing", 
    "hardware": "hardware-systems",
    "incident-response": "threat-monitoring-incident-response",
    "investigation": "cybersecurity-investigation-analysis",
    "networking": "networking-infrastructure",
    "network-protection": "network-system-protection",
    "programming": "software-engineering",
    "risk-management": "security-policies-risk-management",
    "web-security": "application-web-security"
}

PROJECTS_DIR = "content/projects"
HTML_FILES_DIR = "." # Root where index.html and projects.html live, plus subdirs

def rename_folders():
    print("📂 Renaming folders...")
    for short, full in MAPPING.items():
        src = os.path.join(PROJECTS_DIR, short)
        dst = os.path.join(PROJECTS_DIR, full)
        
        if os.path.exists(src):
            print(f"  Moving {src} -> {dst}")
            shutil.move(src, dst)
        else:
            print(f"  ⚠️ Source {src} not found (maybe already moved?)")

def update_markers():
    print("📝 Updating markers in HTML files...")
    # Walk through all HTML files
    for root, dirs, files in os.walk(HTML_FILES_DIR):
        if "node_modules" in root or ".git" in root: continue
        
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                for short, full in MAPPING.items():
                    # Replace START marker
                    content = content.replace(f"AUTO_CARDS_START:{short}", f"AUTO_CARDS_START:{full}")
                    # Replace END marker
                    content = content.replace(f"AUTO_CARDS_END:{short}", f"AUTO_CARDS_END:{full}")
                
                if content != original_content:
                    print(f"  Updated markers in {path}")
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)

if __name__ == "__main__":
    rename_folders()
    update_markers()
    print("✅ Done!")
