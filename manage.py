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
    try:
        # Fallback list of models to try
        MODEL = genai.GenerativeModel('gemini-2.5-flash')
    except:
        try:
             MODEL = genai.GenerativeModel('gemini-3-flash')
        except:
             MODEL = genai.GenerativeModel('gemini-1.5-flash')
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
            # Synced image successfully
        except Exception as e:
            print(f"❌ Error syncing image {img_name}: {e}")

    def ai_enrichment(self, raw_content, metadata):
        if not GEN_API_KEY:
            print("⚠️ Missing GOOGLE_API_KEY. Skipping AI enrichment.")
            return raw_content, metadata

        print(f"🤖 AI is analyzing: {metadata.get('title', 'Unknown Post')}...")
        
        # Robust Logic: Try a list of models with timeout
        # Prioritize 2.5, fallback to 1.5, then 8b (cheapest/fastest)
        models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-1.5-flash-8b']
        
        prompt = f"""
        prioritizing educational value and beginner-friendly explanations.
        Your task is to transform raw technical notes/logs into a professional, high-standard engineering documentation or security research report.

        RAW DATA:
        {raw_content}

        INSTRUCTIONS:
        1. **Restructure & Organize**: 
           - The input is a "Raw Dump" of logs and notes. 
           - YOU must organize it into a chronological narrative: **Reconnaissance** -> **Enumeration** -> **Exploitation** -> **Privilege Escalation**.
           - Create H2 headers (##) for these sections to create the "Timeline" nodes.

        2. **Analyze Tool Outputs**: 
           - Identify raw tool output (Nmap, Gobuster, etc.).
           - PRESERVE the raw output in a code block.
           - IMMEDIATELY after, add a "🔍 Analysis" bullet list explaining the findings (e.g., "Anonymous FTP access allowed").

        3. **Bridge the Gaps (Context)**:
           - Use the user's brief notes (e.g., "got reverse shell") to write professional explanations.
           - Explain *HOW* the user moved from step A to B.
           - Example: User says "put shell in ftp", You write: "We identified that the FTP directory was web-accessible. We uploaded a PHP reverse shell..."

        4. **Professional Tone**:
           - Convert informal notes ("i find root running sh") into engineering language ("Identified a root-owned script `print.sh` executing via cron").

        5. **Strict Metadata**:
           - Generate a refined 'description'.
           - Generate relevant 'tags'.
           - Return the output in this EXACT format:
           ---
           description: [AI Generated Description]
           tags: [AI Generated Tags]
           ---
           [Professional Markdown Report Body]
        """
        
        for model_name in models_to_try:
            try:
                print(f"   Trying model: {model_name}...")
                model = genai.GenerativeModel(model_name)
                # Timeout is CRITICAL to prevent build hangs
                response = model.generate_content(prompt, request_options={'timeout': 30})
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
                        
                        print(f"✅ Success with {model_name}!")
                        return ai_body, metadata
                
                # If we got a result but formatted normally not needing special parsing (unlikely given prompt)
                print(f"✅ Success with {model_name} (No metadata update)!")
                return result, metadata

            except Exception as e:
                print(f"❌ Failed with {model_name}: {str(e)}")
                continue # Try next model
        
        print("❌ All AI models failed. Returning raw content.")
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
            
            # Date handling - normalize to string for HTML but keep raw compatible with sort later
            raw_date = metadata.get('date', datetime.now().date())
            # Ensure we always have a string for the template
            if isinstance(raw_date, str):
                date_str = raw_date
            else:
                date_str = raw_date.strftime("%Y-%m-%d")

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
                "date": date_str, # Always string for display
                "raw_date": raw_date, # Keep raw for sorting
                "category": category,
                "tags": tags,
                "description": description,
                "image": f"images/posts/{os.path.basename(image)}" if image else None,
                "url": f"posts/{slug}.html",
                "html": html_body,
                "filename": os.path.basename(file_path)
            }
            
            # Generate the HTML file for the post
            self.generate_post_html(post_data)
            processed_posts.append(post_data)
        
        # Sort helper
        def parse_date_sort(item):
            d = item['raw_date']
            if isinstance(d, str):
                try:
                    return datetime.strptime(d, "%Y-%m-%d").date()
                except ValueError:
                    return datetime.min.date()
            return d

        self.posts = sorted(processed_posts, key=parse_date_sort, reverse=True)
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
        .markdown-content {{ font-family: 'Inter', sans-serif; line-height: 1.7; color: #cbd5e1; max-width: 100%; margin: 0 auto; padding-left: 2rem; border-left: 2px solid rgba(255, 255, 255, 0.1); position: relative; }}
        .markdown-content h1 {{ font-size: 2.5rem; color: #fff; margin-bottom: 2rem; border-bottom: 1px solid #1e293b; padding-bottom: 1rem; font-family: 'JetBrains Mono', monospace; position: relative; }}
        .markdown-content h1::before {{ content: ''; position: absolute; left: -2.35rem; top: 50%; width: 10px; height: 10px; background: #fff; border-radius: 50%; box-shadow: 0 0 10px #22c55e; border: 2px solid #0f172a; transform: translateY(-50%); }}
        .markdown-content h2 {{ font-size: 1.75rem; color: #f8fafc; margin-top: 3rem; margin-bottom: 1rem; font-family: 'JetBrains Mono', monospace; position: relative; }}
        .markdown-content h2::before {{ content: ''; position: absolute; left: -2.35rem; top: 50%; width: 8px; height: 8px; background: #22c55e; border-radius: 50%; transform: translateY(-50%); border: 2px solid #0f172a; }}
        .markdown-content h3 {{ font-size: 1.25rem; color: #e2e8f0; margin-top: 2rem; margin-bottom: 0.75rem; font-family: 'JetBrains Mono', monospace; position: relative; }}
        .markdown-content h3::before {{ content: ''; position: absolute; left: -2.3rem; top: 50%; width: 6px; height: 6px; background: #0ea5e9; border-radius: 50%; transform: translateY(-50%); border: 2px solid #0f172a; }}
        .markdown-content code {{ background: #1e293b; color: #22c55e; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: 'JetBrains Mono', monospace; }}
        .markdown-content pre {{ background: #1e293b; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 2rem; border: 1px solid #334155; position: relative; }}
        .markdown-content pre::before {{ content: "CODE_BLOCK"; position: absolute; top: 0; right: 0; background: #334155; color: #cbd5e1; font-size: 0.6rem; padding: 0.2rem 0.5rem; font-family: 'JetBrains Mono', monospace; border-bottom-left-radius: 0.5rem; }}
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
            left: 0;
            background: #22c55e;
            color: #000;
            font-size: 0.6rem;
            font-weight: bold;
            padding: 2px 6px;
            font-family: 'JetBrains Mono', monospace;
        }}
        .markdown-content ul {{ list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.5rem; }}
        .markdown-content p {{ margin-bottom: 1.5rem; }}
        
        .diag-card {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 1rem;
            font-family: 'JetBrains Mono', monospace;
            position: relative;
            overflow: hidden;
        }}
        .diag-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 2px;
            height: 100%;
            background: #22c55e;
            opacity: 0.5;
        }}
        .diag-label {{
            display: block;
            font-size: 0.6rem;
            text-transform: uppercase;
            color: #64748b;
            margin-bottom: 0.25rem;
            letter-spacing: 0.1em;
        }}
        .diag-value {{
            font-size: 0.9rem;
            color: #cbd5e1;
        }}
        .diag-blink {{
            animation: blink 1s infinite;
        }}
        @keyframes blink {{ 50% {{ opacity: 0; }} }}
    </style>
</head>
<body class="bg-slate-950 text-slate-200 antialiased selection:bg-accent-green selection:text-slate-900 flex flex-col min-h-screen">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-slate-700">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <a href="../index.html" class="logo-container group flex items-center gap-3">
                 <img src="../images/logo.png" alt="Logo" class="h-10 w-auto group-hover:scale-105 transition-transform duration-300">
            </a>

            <div class="hidden lg:flex items-center gap-8 font-mono text-sm">
                <a href="../index.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Home</a>
                <a href="../about.html" class="text-slate-400 hover:text-accent-cyan transition-colors">About</a>
                <a href="../devhub.html" class="text-slate-400 hover:text-accent-cyan transition-colors">DevHub</a>
                <a href="../projects.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Projects</a>
                <a href="../writeups.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Write-ups</a>
                <a href="../certificates.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Certs</a>
                <a href="../contact.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="py-20 px-6 max-w-4xl mx-auto flex-grow w-full">
        <!-- Post Header -->
        <header class="mb-12 border-b border-slate-800 pb-12">
            <div class="flex items-center gap-4 text-xs font-mono text-slate-500 mb-6 uppercase tracking-widest">
                <span class="px-2 py-1 bg-slate-900 border border-slate-800 rounded text-accent-green">{category}</span>
                <span>// {date}</span>
                <span>// ID: REF-{title}</span>
            </div>
            
            <h1 class="text-3xl md:text-5xl font-bold text-white mb-8 leading-tight font-mono">{title}</h1>
            
            <div class="flex flex-wrap gap-2">
                <!-- Tags populated by python -->
                <!-- {tags} -->
            </div>
        </header>

        <!-- Markdown Body -->
        <div class="markdown-content">
            {html}
        </div>
    </main>

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
            "network-system-protection": "accent-green",
            "application-web-security": "accent-green",
            "ethical-hacking-vulnerability-testing": "accent-green",
            "threat-monitoring-incident-response": "accent-green",
            "cybersecurity-investigation-analysis": "accent-green",
            "security-policies-risk-management": "accent-green",
            "cloud-secure-development-operations": "accent-green",
            "ai-machine-learning": "rose-400",
            "networking-infrastructure": "accent-cyan",
            "software-engineering": "amber-400",
            "hardware-systems": "purple-500",
            "devsecops": "accent-green"
        }
        color = color_map.get(post['category'], "accent-cyan")
        
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
            "network-system-protection": "accent-green",
            "application-web-security": "accent-green",
            "ethical-hacking-vulnerability-testing": "accent-green",
            "threat-monitoring-incident-response": "accent-green",
            "cybersecurity-investigation-analysis": "accent-green",
            "security-policies-risk-management": "accent-green",
            "cloud-secure-development-operations": "accent-green",
            "ai-machine-learning": "rose-400",
            "networking-infrastructure": "accent-cyan",
            "software-engineering": "amber-400",
            "hardware-systems": "purple-500",
            "devsecops": "accent-green"
        }
        color = color_map.get(post['category'], "accent-cyan")
        
        # New fields from metadata
        one_line_summary = post.get('summary', post.get('description', '')[:100])
        skills = post.get('skills', post.get('tags', ''))
        tools = post.get('tools', 'Not specified')
        
        skills_html = "".join([f'<span class="px-2 py-0.5 rounded bg-{color}/5 text-{color}/80 border border-{color}/10 text-[9px] uppercase tracking-tighter">{s.strip()}</span>' for s in skills.split(',')])
        tools_html = "".join([f'<span class="px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700 text-[9px] uppercase tracking-tighter">{t.strip()}</span>' for t in tools.split(',')])

        links_html = ""
        if post.get('github'):
            links_html += f'<a href="{post["github"]}" target="_blank" class="text-xs font-mono text-slate-400 hover:text-white transition-colors flex items-center gap-1"><i class="fa-brands fa-github"></i> GITHUB</a>'
        if post.get('report'):
            links_html += f'<a href="{post["report"]}" target="_blank" class="text-xs font-mono text-slate-400 hover:text-white transition-colors flex items-center gap-1"><i class="fa-solid fa-file-lines"></i> REPORT</a>'
        if post.get('demo'):
            links_html += f'<a href="{post["demo"]}" target="_blank" class="text-xs font-mono text-slate-400 hover:text-white transition-colors flex items-center gap-1"><i class="fa-solid fa-flask"></i> DEMO</a>'
        
        if not links_html:
            links_html = f'<a href="{post["url"]}" class="text-xs font-mono text-{color} hover:underline">VIEW_FULL_INTELLIGENCE_REPORT</a>'

        img_html = ""
        if post.get('image'):
            img_html = f'<div class="md:w-1/3 h-56 rounded-lg overflow-hidden border border-slate-800 group-hover:border-{color}/30 transition-colors"><img src="{post["image"]}" alt="{post["title"]}" class="w-full h-full object-cover grayscale hover:grayscale-0 transition-all duration-500"></div>'

        return f"""
        <article class="group bg-slate-900/50 border border-slate-800/80 p-8 rounded-xl hover:bg-slate-900 hover:border-{color}/40 transition-all duration-500 reveal mb-8">
            <div class="flex flex-col md:flex-row gap-8">
                {img_html}
                <div class="flex-grow">
                    <div class="flex justify-between items-start mb-2">
                        <h3 class="text-2xl font-bold text-white group-hover:text-{color} transition-colors">{post['title']}</h3>
                        <span class="text-[9px] font-mono text-slate-600 uppercase tracking-widest bg-slate-950 px-2 py-1 rounded border border-slate-800">PROJECT_ID: {hash(post['title']) % 100000}</span>
                    </div>
                    <p class="text-{color} font-mono text-[11px] mb-4 uppercase tracking-tighter italic">{one_line_summary}</p>
                    
                    <p class="text-slate-400 text-sm leading-relaxed mb-6 line-clamp-4">
                        {post['description']}
                    </p>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                        <div>
                            <span class="block text-[8px] font-mono text-slate-500 uppercase tracking-widest mb-2">Skills_Used</span>
                            <div class="flex flex-wrap gap-2">
                                {skills_html}
                            </div>
                        </div>
                        <div>
                            <span class="block text-[8px] font-mono text-slate-500 uppercase tracking-widest mb-2">Tools_Used</span>
                            <div class="flex flex-wrap gap-2">
                                {tools_html}
                            </div>
                        </div>
                    </div>

                    <div class="flex items-center gap-6 pt-4 border-t border-slate-800/50">
                        {links_html}
                    </div>
                </div>
            </div>
        </article>"""

    def update_site_grids(self):
        target_files = [
            "index.html", "devhub.html", "writeups.html", "projects.html",
            "projects/network-system-protection.html",
            "projects/application-web-security.html",
            "projects/ethical-hacking-vulnerability-testing.html",
            "projects/threat-monitoring-incident-response.html",
            "projects/cybersecurity-investigation-analysis.html",
            "projects/security-policies-risk-management.html",
            "projects/cloud-secure-development-operations.html",
            "projects/ai-machine-learning.html",
            "projects/networking-infrastructure.html",
            "projects/software-engineering.html",
            "projects/hardware-systems.html"
        ]
        project_pages = [
            "projects.html",
            "projects/network-system-protection.html",
            "projects/application-web-security.html",
            "projects/ethical-hacking-vulnerability-testing.html",
            "projects/threat-monitoring-incident-response.html",
            "projects/cybersecurity-investigation-analysis.html",
            "projects/security-policies-risk-management.html",
            "projects/cloud-secure-development-operations.html",
            "projects/ai-machine-learning.html",
            "projects/networking-infrastructure.html",
            "projects/software-engineering.html",
            "projects/hardware-systems.html"
        ]
        
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
                    # Update image paths and links if we are in a subfolder
                    modified_posts = []
                    is_nested = "/" in filename
                    prefix = "../" if is_nested else ""
                    
                    for p in posts:
                        p_copy = p.copy()
                        if p_copy.get('image') and not p_copy['image'].startswith('http'):
                            p_copy['image'] = prefix + p_copy['image']
                        if p_copy.get('url') and not p_copy['url'].startswith('http'):
                            # The url is usually 'posts/slug.html'
                            # If we are in 'projects/page.html', we need '../posts/slug.html'
                            p_copy['url'] = prefix + p_copy['url']
                        modified_posts.append(p_copy)

                    if is_project_page:
                        cards_html = "\n".join([self.create_project_card(p) for p in modified_posts])
                    else:
                        cards_html = "\n".join([self.create_card(p) for p in modified_posts])
                        
                    pattern = f"{start_marker}.*?{end_marker}"
                    content = re.sub(pattern, f"{start_marker}\n{cards_html}\n{end_marker}", content, flags=re.DOTALL)
            
            # Special case for "Latest Reports" on index.html (Mixed Content)
            if filename == "index.html":
                start_marker = "<!-- AUTO_CARDS_START:recent -->"
                end_marker = "<!-- AUTO_CARDS_END:recent -->"
                if start_marker in content and end_marker in content:
                    mixed_posts = []
                    
                    # 1. Latest Writeup (from 'writeups' or subfolders like 'hackthebox', 'tryhackme')
                    latest_writeup = next((p for p in self.posts if 'writeups' in p['filename'] or p['category'] in ['writeups', 'hackthebox', 'tryhackme']), None)
                    if latest_writeup: mixed_posts.append(latest_writeup)

                    # 2. Latest DevHub (from 'blogs' or 'tools')
                    latest_devhub = next((p for p in self.posts if p['category'] in ['blogs', 'tools', 'testing', 'cheatsheet']), None)
                    if latest_devhub: mixed_posts.append(latest_devhub)

                    # 3. Latest Project (from 'projects')
                    latest_project = next((p for p in self.posts if 'projects' in p['filename'] or 'projects' in p.get('url', '')), None)
                    if latest_project: mixed_posts.append(latest_project)

                    recent_cards = "\n".join([self.create_card(p) for p in mixed_posts])
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
