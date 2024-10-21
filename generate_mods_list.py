import os

mods_path = "./mods"
output_file = "./mods/index.html"

# Get the list of mod directories
mod_dirs = [d for d in os.listdir(mods_path) if os.path.isdir(os.path.join(mods_path, d))]

# Create the HTML content
html_content = "<html><body><h1>Mod List</h1><ul>\n"
for mod in mod_dirs:
    html_content += f'<li><a href="{mod}/">{mod}</a></li>\n'
html_content += "</ul></body></html>"

# Write to the index.html file
with open(output_file, "w") as f:
    f.write(html_content)
