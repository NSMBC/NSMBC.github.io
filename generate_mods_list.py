import os

mods_path = "./mods"
template_file = "./mods_template.html"
output_file = "./mods/index.html"

mod_dirs = [d for d in os.listdir(mods_path) if os.path.isdir(os.path.join(mods_path, d)) and d.lower() != "example"]

mod_list = "\n".join([f'\t\t\t<li><a href="{mod}/">{mod}</a></li>' for mod in mod_dirs])

with open(template_file, "r") as f:
    template_content = f.read()

final_content = template_content.replace("<!-- MOD_LIST -->", mod_list)

with open(output_file, "w") as f:
    f.write(final_content)

print(f"Mod list generated and saved to {output_file}")
