# 🤖 AI System Context & Architecture Handover

> **FOR FUTURE AI ASSISTANTS**: Read this file first to understand the system state, logic, and user preferences.

---

## 1. Project Overview
This is a **Technical Intelligence Portfolio** (`kalialucard.github.io`).
*   **Type**: Static Site Generator (Custom Python Engine).
*   **CMS**: Obsidian (Local Markdown files).
*   **Hosting**: GitHub Pages (Public Repo).
*   **Aesthetic**: Cyberpunk / Terminal / "Technical Intelligence".

## 2. The Core Protocol (`manage.py`)
The `manage.py` script is the heart of the build system.
*   **Build Command**: `python manage.py build`
*   **Input**: Scans `content/` recursively for `.md` files.
*   **Output**: Generates HTML files in `posts/` (and root mapping files like `writeups.html`).
*   **Exclusions**: Explicitly skips `content/templates/` and `content/drafts/`.
*   **Cleanup**: `shutil.rmtree(OUTPUT_DIR)` is run at the start of every build to ensure deleted source files are removed from the site.

### Key Logic Handlers
1.  **AI Enrichment**:
    *   If `enrich: true` in frontmatter, it calls Google Gemini.
    *   **CRITICAL**: It uses aggressive Regex (`re.sub`) to strip "Raw Dump" headers, platform checkboxes (`- [x]`), and other artifacts *after* the AI generates text. This ensures a clean output.
2.  **Visual Separators**:
    *   It automatically injects a horizontal rule (`---`) before the content body if one is missing.
3.  **Metadata**:
    *   Categories are derived from the frontmatter *or* the AI analysis of checkboxes.

## 3. File Structure (Obsidian Vault)
*   `content/` (🟢 **source**): The only folder you should edit content in.
    *   `writeups/` (⚡ **work area**): Active CTF writeups.
    *   `templates/` (🧩 **resources**): Templates (do not edit unless requested).
*   `posts/` (⚙️ **build output**): **READ-ONLY**. Do not write here manually. These are overwritten on every build.
*   `.obsidian/snippets/folder-colors.css`: Controls the distinct green/cyan/orange highlighting in the file explorer.

## 4. User Preferences
*   **Aesthetics**: High contrast, bold fonts, terminal vibes.
*   **Workflow**:
    1.  User creates checking into `content/writeups/` (via Obsidian).
    2.  User pushes to GitHub.
    3.  GitHub Action triggers `manage.py`.
    4.  Site updates automatically.
*   **Common Issues**:
    *   **"Push Rejected"**: Happens because the Bot commits built files. AI must always `git pull --rebase` before checking status.
    *   **"Missing Writeup"**: Likely saved as `Untitled.md`. AI must check filenames.

## 5. Future Maintenance Guide
*   **Adding New Categories**: Update `manage.py` (category filtering logic) and `index.html` (navigation).
*   **Changing Styles**: Edit `css/custom.css` (global) or `manage.py` (if injecting styles during build).
*   **Fixing AI Output**: Adjust the prompt in `ContentManager.ai_enrichment()` inside `manage.py`.

---
*Last Updated: 2025-12-31 // System Status: STABLE*
