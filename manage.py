import os
import glob
import markdown
import yaml
import re
import shutil
import google.generativeai as genai
from datetime import datetime

# Configuration
CONTENT_DIR = "content"
ASSETS_DIR = os.path.join(CONTENT_DIR, "assets")
OUTPUT_DIR = "posts"
PUBLIC_IMG_DIR = os.path.join("images", "posts")

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PUBLIC_IMG_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

# AI Integration
GEN_API_KEY = os.environ.get("GOOGLE_API_KEY")
if GEN_API_KEY:
    genai.configure(api_key=GEN_API_KEY)
    MODEL = genai.GenerativeModel('gemini-1.5-pro')
else:
    MODEL = None

# Post Template (Standard GitBook-like style)
PAGE_TEMPLATE_PATH = "posts/template_base.html" # We'll create this if it doesn't exist

class ContentManager:
    def __init__(self):
        self.posts = []

    def parse_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if content.startswith('---'):
            try:
                _, front_matter, body = content.split('---', 2)
                metadata = yaml.safe_load(front_matter)
                return metadata, body
            except ValueError:
                return {}, content
        return {}, content

    def handle_assets(self, md_body, metadata):
        # Sync the primary thumbnail image
        thumbnail = metadata.get('image', None)
        if thumbnail:
            self.sync_image(thumbnail)
        
        # Regex to find all internal images like ![[image.png]] or ![alt](image.png)
        # 1. Obsidian style: ![[image.png]]
        obsidian_imgs = re.findall(r'!\[\[(.*?)\]\]', md_body)
        for img in obsidian_imgs:
            # Obsidian sometimes adds pipe for width: ![[image.png|100]]
            img_name = img.split('|')[0]
            self.sync_image(img_name)
        
        # 2. Standard Markdown style: ![alt](image.png)
        standard_imgs = re.findall(r'!\[.*?\]\((.*?)\)', md_body)
        for img in standard_imgs:
            if not img.startswith('http'):
                self.sync_image(img)

    def sync_image(self, img_name):
        # Look for the image in content/assets or same dir as post
        source_path = os.path.join(ASSETS_DIR, img_name)
        if not os.path.exists(source_path):
            # Fallback search in all content subdirs
            search = glob.glob(os.path.join(CONTENT_DIR, "**", img_name), recursive=True)
            if search:
                source_path = search[0]
            else:
                return # Image not found

        target_path = os.path.join(PUBLIC_IMG_DIR, os.path.basename(img_name))
        try:
            shutil.copy2(source_path, target_path)
            # print(f"📸 Synced image: {img_name}")
        except Exception as e:
            print(f"❌ Error syncing image {img_name}: {e}")

    def ai_enrichment(self, raw_content, metadata):
        if not MODEL:
            print("⚠️ Missing GOOGLE_API_KEY. Skipping AI enrichment.")
            return raw_content, metadata

        print(f"🤖 AI is analyzing: {metadata.get('title', 'Unknown Post')}...")
        
        prompt = f"""
        You are an elite Senior Penetration Tester and Cyber Intelligence Analyst. 
        Your task is to transform raw technical notes/logs into a professional, high-end cybersecurity research report.

        RAW DATA:
        {raw_content}

        INSTRUCTIONS:
        1. Maintain all technical accuracy (IPs, ports, commands).
        2. Format the report into professional phases:
           - **Phase I: Tactical Reconnaissance & Enumeration**
           - **Phase II: Surface Analysis & Vulnerability Mapping**
           - **Phase III: Tactical Exploitation**
           - **Phase IV: Privilege Escalation & Persistence**
        3. Use a sophisticated, technical tone (e.g., instead of "found", use "identified" or "uncovered").
        4. Add an 'Executive Summary' at the beginning.
        5. Generate a refined 'description' (max 150 chars) and relevant 'tags' (comma separated).
        6. Return the output in this EXACT format:
           ---
           description: [AI Generated Description]
           tags: [AI Generated Tags]
           ---
           [Professional Markdown Report Body]
        """
        
        try:
            response = MODEL.generate_content(prompt)
            result = response.text
            
            # Parse the AI response to separate metadata and body
            if '---' in result:
                parts = result.split('---')
                if len(parts) >= 3:
                    ai_metadata = yaml.safe_load(parts[1])
                    ai_body = "---".join(parts[2:]).strip()
                    
                    # Update metadata if AI provided suggestions
                    if ai_metadata:
                        metadata['description'] = ai_metadata.get('description', metadata.get('description'))
                        metadata['tags'] = ai_metadata.get('tags', metadata.get('tags'))
                    
                    return ai_body, metadata
            return result, metadata
        except Exception as e:
            print(f"❌ AI Enrichment Failed: {e}")
            return raw_content, metadata

    def build(self):
        print("🚀 Starting Build Process...")
        all_md_files = glob.glob(os.path.join(CONTENT_DIR, "**", "*.md"), recursive=True)
        
        processed_posts = []
        for file_path in all_md_files:
            metadata, body = self.parse_file(file_path)
            
            # --- MAGIC AUTO-METADATA ---
            dir_category = os.path.basename(os.path.dirname(file_path))
            # If it's nested like writeups/tryhackme, get the parent too
            category = metadata.get('category', dir_category)
            
            # Default to ENRICH: True if it's in a writeups or projects folder
            is_auto_field = any(x in file_path for x in ["writeups", "projects", "blogs"])
            should_enrich = metadata.get('enrich', is_auto_field)

            if should_enrich:
                body, metadata = self.ai_enrichment(body, metadata)

            title = metadata.get('title', os.path.splitext(os.path.basename(file_path))[0])
            # Re-check category after enrichment in case AI updated it
            category = metadata.get('category', category)
            slug = metadata.get('slug', title.lower().replace(' ', '-').replace('_', '-').replace('/', '-'))
            slug = re.sub(r'[^a-z0-9\-]', '', slug) # Final sweep for weird characters
            date = metadata.get('date', datetime.now().strftime("%Y-%m-%d"))
            tags = metadata.get('tags', category)
            description = metadata.get('description', "Technical documentation and research.")
            image = metadata.get('image', None)
            
            # Handle asset syncing
            self.handle_assets(body, metadata)
            
            # Fix image paths in body for the web
            # Convert ![[img.png]] to <img src="../images/posts/img.png">
            body = re.sub(r'!\[\[(.*?)\]\]', r'![image](../images/posts/\1)', body)
            # Standard markdown images
            body = re.sub(r'!\[(.*?)\]\((.*?)\)', r'![\1](../images/posts/\2)', body)

            html_body = markdown.markdown(body, extensions=['extra', 'codehilite', 'nl2br'])
            
            post_data = {
                "title": title,
                "slug": slug,
                "date": date,
                "category": category,
                "tags": tags,
                "description": description,
                "image": f"images/posts/{os.path.basename(image)}" if image else None,
                "url": f"posts/{slug}.html",
                "html": html_body
            }
            
            # Generate the HTML file for the post
            self.generate_post_html(post_data)
            processed_posts.append(post_data)
        
        self.posts = sorted(processed_posts, key=lambda x: x['date'], reverse=True)
        self.update_site_grids()
        print(f"✅ Build Complete! Processed {len(self.posts)} posts.")

    def generate_post_html(self, post):
        # Using a simplified version of generate_content.py's template
        # For now, we'll write it directly to keep manage.py self-contained
        template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Technical Intelligence Labs</title>
    <link rel="stylesheet" href="../css/custom.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .markdown-content {{ font-family: 'Inter', sans-serif; line-height: 1.7; color: #cbd5e1; max-width: 100%; margin: 0 auto; }}
        .markdown-content h1 {{ font-size: 2.5rem; color: #fff; margin-bottom: 2rem; border-bottom: 1px solid #1e293b; padding-bottom: 1rem; font-family: 'JetBrains Mono', monospace; }}
        .markdown-content code {{ background: #1e293b; color: #22c55e; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: 'JetBrains Mono', monospace; }}
        .markdown-content pre {{ background: #1e293b; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 2rem; }}
        .markdown-content blockquote {{ 
            position: relative;
            border-left: 2px solid #22c55e; 
            padding: 1.5rem 0 1.5rem 1.75rem; 
            color: #cbd5e1; 
            margin-bottom: 2.5rem; 
            font-style: normal; 
            background: rgba(34, 197, 94, 0.03);
            border-radius: 0 4px 4px 0;
            box-shadow: inset 20px 0 20px -20px rgba(34, 197, 94, 0.15);
        }}
        .markdown-content blockquote::before {{
            content: "TECHNICAL_INTELLIGENCE";
            position: absolute;
            top: -9px;
            left: 12px;
            background: #0f172a;
            padding: 0 10px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 9px;
            color: #22c55e;
            letter-spacing: 2px;
            border: 1px solid rgba(34, 197, 94, 0.4);
            font-weight: 700;
            z-index: 10;
        }}
        .nav-index {{ color: #22c55e; opacity: 0.5; margin-right: 0.5rem; font-weight: bold; }}
        .diag-card {{ background: rgba(15, 23, 42, 0.5); border: 1px solid rgba(255, 255, 255, 0.05); padding: 1rem; font-family: 'JetBrains Mono', monospace; font-size: 10px; color: #64748b; border-radius: 4px; }}
        .diag-label {{ color: #94a3b8; text-transform: uppercase; margin-bottom: 4px; display: block; font-size: 8px; letter-spacing: 1px; }}
        .diag-value {{ color: #22c55e; }}
        .diag-blink {{ animation: blink 1s step-end infinite; }}
        @keyframes blink {{ 50% {{ opacity: 0; }} }}
        body {{ 
            background-image: 
                linear-gradient(to bottom, rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.95)),
                url('../images/world-map-bg.png');
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
            color: #cbd5e1; 
        }}
    </style>
</head>
<body class="p-8 md:p-16 bg-transparent selection:bg-accent-green selection:text-slate-900">
    <nav class="mb-12 font-mono text-sm">
        <a href="../index.html" class="text-accent-cyan hover:underline hover:text-white transition-colors">Return_to_Portfolio</a>
    </nav>
    <article class="max-w-7xl mx-auto">
        <header class="mb-12">
            <div class="text-accent-green font-mono text-sm mb-2 uppercase">{category}</div>
            <h1 class="text-4xl md:text-5xl font-bold text-white mb-4">{title}</h1>
            <div class="text-slate-500 text-sm">{date} • {tags}</div>
        </header>
        <div class="markdown-content">
            {html}
        </div>
    </article>

    <!-- Footer -->
    <footer class="py-16 text-center border-t border-slate-800 bg-transparent mt-24 relative overflow-hidden">
        <div class="max-w-7xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-4 mb-12">
            <div class="diag-card text-left">
                <span class="diag-label">Access_Level</span>
                <span class="diag-value">OMNI_READ_ONLY</span>
            </div>
            <div class="diag-card text-left">
                <span class="diag-label">Encryption</span>
                <span class="diag-value">AES-256-GCM<span class="diag-blink">_</span></span>
            </div>
            <div class="diag-card text-left">
                <span class="diag-label">Signal_Strength</span>
                <span class="diag-value text-blue-400">PURE_DATA_STREAM</span>
            </div>
            <div class="diag-card text-left">
                <span class="diag-label">System_Status</span>
                <span class="diag-value">STABLE_HARDENED</span>
            </div>
        </div>

        <div class="flex justify-center gap-6 mb-8">
            <a href="https://github.com/kalialucard" target="_blank"
                class="text-slate-400 hover:text-white transition-colors text-2xl" aria-label="GitHub"><i
                    class="fa-brands fa-github"></i></a>
            <a href="https://tryhackme.com/p/kalialucard" target="_blank"
                class="text-slate-400 hover:text-red-500 transition-colors text-2xl" aria-label="TryHackMe"
                title="TryHackMe"><i class="fa-solid fa-fire"></i></a>
            <a href="https://app.hackthebox.com/profile/2503089" target="_blank"
                class="text-slate-400 hover:text-green-400 transition-colors text-2xl" aria-label="HackTheBox"
                title="HackTheBox"><i class="fa-solid fa-cube"></i></a>
        </div>
        <p class="font-mono text-[10px] text-slate-600 uppercase tracking-widest text-center">Powered by kalialucard</p>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>"""
        output_path = os.path.join(OUTPUT_DIR, f"{post['slug']}.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template.format(
                title=post['title'],
                category=post['category'],
                date=post['date'],
                tags=post['tags'],
                html=post['html']
            ))

    def create_card(self, post):
        # Create a card based on the existing design system
        color_map = {
            "blogs": "amber-400",
            "writeups": "red-500",
            "tryhackme": "red-500",
            "hackthebox": "accent-cyan",
            "projects": "accent-cyan",
            "docs": "white",
            "testing": "purple-500",
            "cheatsheet": "accent-green",
            "cybersecurity": "accent-green",
            "networking": "accent-cyan",
            "programming": "amber-400",
            "hardware": "purple-500",
            "ai": "rose-400",
            "network-protection": "accent-green",
            "web-security": "accent-green",
            "ethical-hacking": "accent-green",
            "incident-response": "accent-green",
            "investigation": "accent-green",
            "risk-management": "accent-green",
            "devsecops": "accent-green"
        }
        color = color_map.get(post['category'], "accent-cyan")
        
        img_html = ""
        if post.get('image'):
            # Adjusted path for index vs subfolders handled in loop
            img_html = f'<div class="h-48 overflow-hidden"><img src="{post["image"]}" alt="{post["title"]}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"></div>'
        else:
            img_html = f'<div class="h-2 bg-{color}"></div>'

        return f"""
            <a href="{post['url']}" class="devhub-card group bg-slate-900 border border-slate-800 rounded-xl overflow-hidden hover:border-{color}/50 hover:shadow-xl hover:shadow-{color}/10 transition-all duration-300 block" data-category="{post['category']}" data-tags="{post['tags']}">
                {img_html}
                <div class="p-6">
                    <div class="flex justify-between items-start mb-4">
                        <span class="px-2 py-1 rounded text-xs font-bold bg-{color}/10 text-{color} border border-{color}/20 uppercase">{post['category']}</span>
                        <i class="fa-solid fa-arrow-right -rotate-45 text-slate-600 group-hover:text-{color} transition-colors"></i>
                    </div>
                    <h3 class="text-xl font-bold text-white mb-2 group-hover:text-{color} transition-colors">{post['title']}</h3>
                    <p class="text-slate-400 text-sm line-clamp-2">{post['description']}</p>
                </div>
            </a>"""

    def create_project_card(self, post):
        color_map = {
            "cybersecurity": "accent-green",
            "networking": "accent-cyan",
            "programming": "amber-400",
            "hardware": "purple-500",
            "ai": "rose-400",
            "network-protection": "accent-green",
            "web-security": "accent-green",
            "ethical-hacking": "accent-green",
            "incident-response": "accent-green",
            "investigation": "accent-green",
            "risk-management": "accent-green",
            "devsecops": "accent-green"
        }
        color = color_map.get(post['category'], "accent-cyan")
        
        tags_list = post['tags'].split(',')
        tag_spans = "".join([f'<span class="border border-{color}/30 px-2 py-1 rounded uppercase mr-2">{t.strip()}</span>' for t in tags_list])

        img_html = ""
        if post.get('image'):
            img_html = f'<div class="md:w-1/4 h-48 rounded overflow-hidden shadow-2xl border border-slate-700"><img src="{post["image"]}" alt="{post["title"]}" class="w-full h-full object-cover"></div>'

        return f"""
        <article class="mb-12 bg-slate-800/20 border border-slate-700 p-8 rounded hover:border-{color} transition-all reveal">
            <div class="flex flex-col md:flex-row gap-8">
                {img_html}
                <div class="{"md:w-3/4" if post.get('image') else "w-full"}">
                    <h3 class="text-2xl font-bold text-white mb-2">{post['title']}</h3>
                    <div class="flex gap-2 mb-4 text-xs font-mono text-{color}">
                        {tag_spans}
                    </div>
                    <p class="text-slate-400 mb-4 leading-relaxed">
                        {post['description']}
                    </p>
                    <a href="{post['url']}" class="text-xs font-mono text-{color} hover:underline">VIEW_FULL_INTELLIGENCE_REPORT</a>
                </div>
            </div>
        </article>"""

    def update_site_grids(self):
        target_files = ["index.html", "devhub.html", "writeups.html", "cybersecurity.html", "networking.html", "programming.html", "hardware.html", "ai.html"]
        project_pages = ["cybersecurity.html", "networking.html", "programming.html", "hardware.html", "ai.html"]
        
        # Categorize posts
        sections = {}
        for post in self.posts:
            cat = post['category']
            if cat not in sections: sections[cat] = []
            sections[cat].append(post)

        for filename in target_files:
            if not os.path.exists(filename): continue
            
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()

            is_project_page = filename in project_pages

            for cat, posts in sections.items():
                start_marker = f"<!-- AUTO_CARDS_START:{cat} -->"
                end_marker = f"<!-- AUTO_CARDS_END:{cat} -->"
                
                if start_marker in content and end_marker in content:
                    # Update image paths if we are in a subfolder
                    modified_posts = []
                    for p in posts:
                        p_copy = p.copy()
                        if p_copy.get('image'):
                            # Root pages like index.html need 'images/posts/...'
                            # Pages like posts/slug.html would need '../images/posts/...'
                            # Since this is for top-level pages (devhub.html, etc), 'images/posts' is correct.
                            pass 
                        modified_posts.append(p_copy)

                    if is_project_page:
                        cards_html = "\n".join([self.create_project_card(p) for p in modified_posts])
                    else:
                        cards_html = "\n".join([self.create_card(p) for p in modified_posts])
                        
                    pattern = f"{start_marker}.*?{end_marker}"
                    content = re.sub(pattern, f"{start_marker}\n{cards_html}\n{end_marker}", content, flags=re.DOTALL)
            
            # Special case for "Recent Intelligence" on index.html
            if filename == "index.html":
                start_marker = "<!-- AUTO_CARDS_START:recent -->"
                end_marker = "<!-- AUTO_CARDS_END:recent -->"
                if start_marker in content and end_marker in content:
                    recent_cards = "\n".join([self.create_card(p) for p in self.posts[:3]])
                    pattern = f"{start_marker}.*?{end_marker}"
                    content = re.sub(pattern, f"{start_marker}\n{recent_cards}\n{end_marker}", content, flags=re.DOTALL)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)

    def new_post(self, category):
        title = input("Enter Post Title: ")
        slug = title.lower().replace(' ', '-')
        filename = f"{slug}.md"
        filepath = os.path.join(CONTENT_DIR, category, filename)
        
        template = f"""---
title: "{title}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
category: "{category}"
enrich: true
image: "your-screenshot.png"
tags: "technical, research"
description: "Brief summary of this technical research."
---

# {title}

Start your technical deep dive here...
"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"📝 Created new post template: {filepath}")

if __name__ == "__main__":
    import sys
    manager = ContentManager()
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "build":
            manager.build()
        elif cmd == "new" and len(sys.argv) > 2:
            manager.new_post(sys.argv[2])
        else:
            print("Usage: python manage.py [build | new <category>]")
    else:
        print("Usage: python manage.py [build | new <category>]")
