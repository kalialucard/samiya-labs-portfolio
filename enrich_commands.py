import os
import glob
import time
import yaml
import google.generativeai as genai
from dotenv import load_dotenv

# Load env for API Key
load_dotenv("/home/alucard/website/portfolio/.env")
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    # Try a fallback if .env fails or isn't loaded correctly in this context
    # In a real scenario, we rely on the env. 
    print("❌ Error: GOOGLE_API_KEY not found.")
    exit(1)

genai.configure(api_key=api_key)

COMMANDS_DIR = "/home/alucard/website/portfolio/content/commands"

# Models to try (rotation) - Prioritizing FLASH for higher quota
models = [
    'models/gemini-1.5-flash-latest',
    'models/gemini-flash-latest',
    'models/gemini-1.5-flash'
]

def enrich_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    
    # Check if already enriched (simple heuristic: look for "Top 10" header or lack of "Please generate")
    # But wait, our prompt asks for "Top 10", so the raw file HAS "Top 10" in the prompt.
    # The raw file has "Please generate a detailed...". The enriched one shouldn't have that instruction at the top.
    if "Please generate a detailed" not in content:
        print(f"⏩ Skipping {os.path.basename(filepath)} (Already enriched)")
        return

    print(f"🤖 Enriching {os.path.basename(filepath)}...")
    
    # Parse existing frontmatter to preserve it
    parts = content.split("---")
    if len(parts) >= 3:
        frontmatter_yaml = parts[1]
        body = "---".join(parts[2:])
    else:
        print(f"⚠️ Skipped {filepath} (Invalid format)")
        return

    prompt = f"""
    You are a Cybersecurity Mentor.
    Transform the following request into a detailed, beginner-friendly EDUCATIONAL GUIDE.
    
    REQUEST:
    {body}

    STRICT OUTPUT FORMAT:
    - NO preamble. start directly with the Introduction.
    - Use clear headings.
    - For the "Top 10 Commands", formatting is CRITICAL:
      - Command: `syntax` (Code Block)
      - Explanation: Plain text.
    - Tone: Encouraging, professional, precise.
    """

    generated_text = None
    for model_name in models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            generated_text = response.text
            break # Success
        except Exception as e:
            print(f"   ⚠️ Model {model_name} failed: {e}")
            if "Quota exceeded" in str(e) or "429" in str(e):
                print("      ⏳ Rate limit hit. Sleeping 60s...")
                time.sleep(60)
            else:
                time.sleep(2)
    
    if generated_text:
        # Update frontmatter
        try:
            metadata = yaml.safe_load(frontmatter_yaml)
            metadata['enrich'] = False # Mark as done
            metadata['last_enriched'] = "2026-01-05"
            # Maybe update description if AI gives a better one? 
            # For now, keep it simple.
            
            new_frontmatter = yaml.dump(metadata, sort_keys=False)
            new_content = f"---\n{new_frontmatter}---\n\n{generated_text}\n"
            
            with open(filepath, "w") as f:
                f.write(new_content)
            print(f"✅ Saved {os.path.basename(filepath)}")
            
        except Exception as e:
            print(f"❌ Failed to parse/save yaml: {e}")

    else:
        print(f"❌ Failed to generate content for {filepath}")

    # Rate Limit Protection - Aggressive self-throttling
    print("⏳ Sleeping 20s to prevent quota issues...")
    time.sleep(20)

def main():
    files = glob.glob(os.path.join(COMMANDS_DIR, "*.md"))
    files.sort()
    
    print(f"Found {len(files)} command files.")
    for f in files:
        enrich_file(f)

if __name__ == "__main__":
    main()
