import os

# TryHackMe Files
thm_files = [
    "0day", "Agent Sudo", "Anonforce", "Anonymous", "Archangel", 
    "b3dr0ck", "Basic Pentesting", "c4ptur3-th3-fl4g", "Crack the hash", 
    "Cyberheroes", "CyberLens", "Dig Dug", "Ghostcat", "Hack Smarter Security", 
    "Ignite", "Jax sucks alot", "kiba", "Library", "Mindgames", 
    "Mr Robot CTF", "Mustacchio", "Plotted-TMS", "Poster", "Rabit-hole", 
    "Simple CTF", "Spring", "Startup", "Team", "TechSupp0rt1", 
    "U.A. High School", "UltraTech", "Unstable Twin", "Valley", 
    "VulnNet - Roasted", "Walkin", "Wekor", "Whiterose", "Wordpress - CVE-2021-29447"
]

# HackerOne Manual Entries
h1_entries = [
    {
        "title": "Stored XSS in User Profile",
        "tag": "VULN_REPORT",
        "desc": "Chain involving IDOR and Stored Cross-Site Scripting leading to account takeover.",
        "color": "accent-cyan",
        "category": "hackerone"
    },
    {
        "title": "Home Lab Setup",
        "tag": "NETWORK_SEC",
        "desc": "Documentation of setting up a Proxmox cluster with pfSense and Security Onion.",
        "color": "accent-cyan",
        "category": "hackerone"
    }
]

def generate_row(title, tag, desc, color, category):
    border_color = f"border-{color}" if "accent" not in color else "border-accent-cyan"
    text_color = f"text-{color}" if "accent" not in color else "text-accent-cyan"
    
    # Map raw color names for Tailwind if needed, but assuming custom.css or config handles these custom classes? 
    # Actually accent-cyan is in config. But text-red-500 is standard.
    # Let's handle the specific THM vs H1 styling logic in the generator loop to be safe.
    
    return f"""
            <div class="writeup-item group flex flex-col md:flex-row items-start md:items-center gap-4 p-6 border-b border-slate-800 hover:bg-slate-800/40 transition-all" data-category="{category}">
                <div class="flex-shrink-0 w-24">
                    <span class="text-xs font-mono py-1 px-2 rounded border {border_color} {text_color} opacity-80">{tag}</span>
                </div>
                <div class="flex-grow">
                    <h3 class="text-lg font-bold text-white group-hover:{text_color} transition-colors mb-1">{title}</h3>
                    <p class="text-slate-500 text-sm hidden md:block">{desc}</p>
                </div>
                <div class="flex-shrink-0 mt-2 md:mt-0">
                     <a href="#" class="text-slate-600 hover:{text_color} transition-colors text-lg"><i class="fa-solid fa-arrow-right-long"></i></a>
                </div>
            </div>"""

list_html = ""

# Add H1 Items
for item in h1_entries:
    list_html += generate_row(item["title"], item["tag"], item["desc"], "accent-cyan", "hackerone")

# Add THM Items
for title in thm_files:
    display_title = title.replace("-", " ")
    desc = "Comprehensive walkthrough and privilege escalation guide."
    tag = "CTF"
    color = "red-500"
    
    if "CVE" in title:
        desc = "Exploiting specific Common Vulnerabilities and Exposures."
        tag = "CVE"
    elif "Basic" in title or "Startup" in title:
        desc = "Foundational security concepts and enumeration techniques."
        tag = "LEARNING"
        
    list_html += generate_row(display_title, tag, desc, color, "tryhackme")


page_content = f"""<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Technical Intelligence Labs | Write-ups</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/custom.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Inter', 'sans-serif'], mono: ['JetBrains Mono', 'monospace'] }},
                    colors: {{ slate: {{ 900: '#0f172a' }}, accent: {{ green: '#22c55e', cyan: '#0ea5e9' }} }}
                }}
            }}
        }}
    </script>
</head>
<body class="antialiased selection:bg-accent-green selection:text-slate-900 flex flex-col min-h-screen bg-slate-900 text-slate-200">

    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-slate-700">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <!-- Logo -->
            <a href="index.html" class="logo-container group">
                <div class="logo-icon">
                    <div class="logo-shield"></div>
                    <div class="logo-node"></div>
                </div>
            </a>
            
            <div class="hidden lg:flex items-center gap-8 font-mono text-sm">
                <a href="index.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Home</a>
                <a href="about.html" class="text-slate-400 hover:text-accent-cyan transition-colors">About</a>
                
                <div class="relative group">
                    <button class="text-slate-400 hover:text-white flex items-center gap-1 transition-colors">
                        Projects <i class="fa-solid fa-chevron-down text-xs opacity-50"></i>
                    </button>
                    <div class="absolute left-1/2 -translate-x-1/2 top-full mt-4 w-64 bg-slate-900 border border-slate-700 rounded-lg shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 p-2">
                        <a href="cybersecurity.html" class="block px-4 py-2 rounded text-slate-400 hover:bg-slate-800 hover:text-accent-green text-xs">
                            <i class="fa-solid fa-shield-halved w-6"></i> Cybersecurity
                        </a>
                        <a href="networking.html" class="block px-4 py-2 rounded text-slate-400 hover:bg-slate-800 hover:text-accent-cyan text-xs">
                            <i class="fa-solid fa-network-wired w-6"></i> Networking
                        </a>
                        <a href="programming.html" class="block px-4 py-2 rounded text-slate-400 hover:bg-slate-800 hover:text-amber-400 text-xs">
                            <i class="fa-solid fa-code w-6"></i> Programming
                        </a>
                        <a href="hardware.html" class="block px-4 py-2 rounded text-slate-400 hover:bg-slate-800 hover:text-purple-400 text-xs">
                            <i class="fa-solid fa-microchip w-6"></i> Hardware
                        </a>
                        <a href="ai.html" class="block px-4 py-2 rounded text-slate-400 hover:bg-slate-800 hover:text-rose-400 text-xs">
                            <i class="fa-solid fa-brain w-6"></i> AI / Automation
                        </a>
                    </div>
                </div>

                <a href="writeups.html" class="text-white hover:text-accent-cyan transition-colors">Write-ups</a>
                <a href="certificates.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Certs</a>
                <a href="contact.html" class="text-slate-400 hover:text-accent-cyan transition-colors">Contact</a>
            </div>

            <button id="mobile-menu-btn" class="lg:hidden text-slate-400 hover:text-white p-2"><i class="fa-solid fa-bars text-xl"></i></button>
        </div>
        
        <div id="mobile-menu" class="hidden lg:hidden bg-slate-900 border-b border-slate-700 shadow-2xl">
            <div class="flex flex-col p-4 space-y-1">
                <a href="index.html" class="block px-4 py-3 rounded hover:bg-slate-800 text-slate-400 font-mono border-l-2 border-transparent">Home</a>
                <a href="about.html" class="block px-4 py-3 rounded hover:bg-slate-800 text-slate-400 font-mono border-l-2 border-transparent">About</a>
                <div class="py-2 px-4 text-xs font-bold text-slate-600 uppercase tracking-widest mt-2">Projects</div>
                <a href="cybersecurity.html" class="block px-4 py-2 text-slate-400 hover:text-accent-green pl-6 text-sm"><i class="fa-solid fa-shield-halved w-6"></i> Cybersecurity</a>
                <a href="networking.html" class="block px-4 py-2 text-slate-400 hover:text-accent-cyan pl-6 text-sm"><i class="fa-solid fa-network-wired w-6"></i> Networking</a>
                <a href="programming.html" class="block px-4 py-2 text-slate-400 hover:text-amber-400 pl-6 text-sm"><i class="fa-solid fa-code w-6"></i> Programming</a>
                <a href="hardware.html" class="block px-4 py-2 text-slate-400 hover:text-purple-400 pl-6 text-sm"><i class="fa-solid fa-microchip w-6"></i> Hardware</a>
                <a href="ai.html" class="block px-4 py-2 text-slate-400 hover:text-rose-400 pl-6 text-sm"><i class="fa-solid fa-brain w-6"></i> AI / Automation</a>
                <div class="h-px bg-slate-800 my-2"></div>
                <a href="writeups.html" class="block px-4 py-3 rounded hover:bg-slate-800 text-white font-mono border-l-2 border-accent-cyan">Write-ups</a>
                <a href="certificates.html" class="block px-4 py-3 rounded hover:bg-slate-800 text-slate-400 font-mono border-l-2 border-transparent">Certs</a>
                <a href="contact.html" class="block px-4 py-3 rounded hover:bg-slate-800 text-slate-400 font-mono border-l-2 border-transparent">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <section class="py-20 px-6 max-w-5xl mx-auto flex-grow">
        <div class="flex flex-col md:flex-row justify-between items-end md:items-center mb-12 gap-4">
            <h2 class="font-mono text-3xl text-accent-cyan flex items-center reveal">
                <i class="fa-solid fa-database mr-4"></i> Knowledge_Base
            </h2>
            
            <!-- Filters -->
            <div class="flex bg-slate-800 rounded p-1 gap-1 text-xs font-mono reveal">
                <button onclick="filterWriteups('all')" class="filter-btn active px-4 py-2 rounded hover:bg-slate-700 text-white transition-colors" data-filter="all">ALL</button>
                <button onclick="filterWriteups('hackerone')" class="filter-btn px-4 py-2 rounded hover:bg-slate-700 text-slate-400 hover:text-accent-cyan transition-colors" data-filter="hackerone">HACKERONE</button>
                <button onclick="filterWriteups('tryhackme')" class="filter-btn px-4 py-2 rounded hover:bg-slate-700 text-slate-400 hover:text-red-500 transition-colors" data-filter="tryhackme">TRYHACKME</button>
            </div>
        </div>

        <!-- List Container -->
        <div id="writeups-list" class="bg-slate-900 border border-slate-800 rounded-lg overflow-hidden reveal" style="transition-delay: 100ms">
            {list_html}
        </div>

    </section>

    <!-- Footer -->
    <footer class="py-12 text-center border-t border-slate-800 bg-slate-900">
        <p class="font-mono text-xs text-slate-600">&copy; 2025 Technical Intelligence Labs. Level Up.</p>
    </footer>

    <script src="js/main.js"></script>
    <script>
        function filterWriteups(category) {{
            const items = document.querySelectorAll('.writeup-item');
            const btns = document.querySelectorAll('.filter-btn');
            
            // Update Buttons
            btns.forEach(btn => {{
                if(btn.dataset.filter === category) {{
                    btn.classList.add('bg-slate-700', 'text-white');
                    btn.classList.remove('text-slate-400');
                }} else {{
                    btn.classList.remove('bg-slate-700', 'text-white');
                    btn.classList.add('text-slate-400');
                }}
            }});

            // Update Items
            items.forEach(item => {{
                if (category === 'all' || item.dataset.category === category) {{
                    item.style.display = 'flex';
                }} else {{
                    item.style.display = 'none';
                }}
            }});
        }}
        
        // Init active state logic in styles is handled by classes above, 
        // but let's ensure the default 'All' button looks active on load.
        document.querySelector('[data-filter="all"]').classList.add('bg-slate-700', 'text-white');
    </script>
</body>
</html>
"""

with open("writeups.html", "w") as f:
    f.write(page_content)

print("Successfully generated list view writeups.html")
