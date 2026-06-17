import os
import html
import re

mods_path = "./mods"
template_file = "./mods_template.html"
output_file = "./mods/index.html"

def get_mod_info(mod_dir):
    """Extract mod information from README.md or index.html"""
    mod_path = os.path.join(mods_path, mod_dir)

    # Use the folder name as the primary title
    title = mod_dir

    # Prefer custom pages when present, matching CONTRIBUTING.md.
    index_path = os.path.join(mod_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()

            description = None
            if "<p>" in content:
                description = content.split("<p>", 1)[1].split("</p>", 1)[0].strip()

            return {
                "title": title,
                "description": clean_description(description) or "A New Super Mario Bros. mod.",
                "path": f"{mod_dir}/",
                "entry": "index"
            }

    # Fallback to README.md
    readme_path = os.path.join(mod_path, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

            # Extract description (first paragraph after title)
            description = None
            lines = content.split("\n")
            for line in lines:
                if line.strip() and not line.startswith("#"):
                    description = line.strip()
                    break

            return {
                "title": title,
                "description": clean_description(description) or "A New Super Mario Bros. mod.",
                "path": f"{mod_dir}/",
                "entry": "readme"
            }

    # Fallback to directory name
    return {
        "title": title,
        "description": "A New Super Mario Bros. mod.",
        "path": f"{mod_dir}/",
        "entry": "missing"
    }

def clean_description(description):
    if not description:
        return None

    without_tags = re.sub(r"<[^>]*>", " ", description)
    normalized = re.sub(r"\s+", " ", html.unescape(without_tags))
    return normalized.strip()

def html_attr(value):
    return html.escape(value, quote=True)

def html_text(value):
    return html.escape(value, quote=False)

# Get all mod directories except 'example'
mod_dirs = [d for d in os.listdir(mods_path) 
           if os.path.isdir(os.path.join(mods_path, d)) and d.lower() != "example"]

# Get information for each mod
mods_info = [get_mod_info(mod_dir) for mod_dir in mod_dirs]

# Generate the mod cards HTML with light theme styling
mod_cards = "\n".join([
    f'''            <div class="mod-card" data-href="{html_attr(mod["path"])}" data-entry="{html_attr(mod["entry"])}">
                <h2>{html_text(mod["title"])}</h2>
                <p>{html_text(mod["description"])}</p>
            </div>'''
    for mod in mods_info
])

# Read and process the template
with open(template_file, "r", encoding="utf-8") as f:
    template_content = f.read()

# Replace the placeholder with the generated mod cards
final_content = template_content.replace("<!-- MOD_CARDS -->", mod_cards)

# Write the output file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"Mod list generated and saved to {output_file}")
