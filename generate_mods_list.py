import os
import json

mods_path = "./mods"
template_file = "./mods_template.html"
output_file = "./mods/index.html"

def get_mod_info(mod_dir):
    """Extract mod information from README.md or index.html"""
    mod_path = os.path.join(mods_path, mod_dir)
    
    # Use the folder name as the primary title
    title = mod_dir
    
    # Try to read README.md first
    readme_path = os.path.join(mod_path, "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Extract description (first paragraph after title)
            description = None
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith("#"):
                    description = line.strip()
                    break
            
            return {
                "title": title,
                "description": description or "A New Super Mario Bros. mod.",
                "path": f"{mod_dir}/"
            }
    
    # Fallback to index.html
    index_path = os.path.join(mod_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()
            
            # Try to extract description from first paragraph
            description = None
            if "<p>" in content:
                description = content.split("<p>")[1].split("</p>")[0].strip()
            
            return {
                "title": title,
                "description": description or "A New Super Mario Bros. mod.",
                "path": f"{mod_dir}/"
            }
    
    # Fallback to directory name
    return {
        "title": title,
        "description": "A New Super Mario Bros. mod.",
        "path": f"{mod_dir}/"
    }

# Get all mod directories except 'example'
mod_dirs = [d for d in os.listdir(mods_path) 
           if os.path.isdir(os.path.join(mods_path, d)) and d.lower() != "example"]

# Get information for each mod
mods_info = [get_mod_info(mod_dir) for mod_dir in mod_dirs]

# Generate the mod cards HTML with light theme styling
mod_cards = "\n".join([
    f'''            <div class="mod-card" data-href="{mod["path"]}">
                <h2>{mod["title"]}</h2>
                <p>{mod["description"]}</p>
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
