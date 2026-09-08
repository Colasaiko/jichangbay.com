import os
import yaml
import shutil
from difflib import SequenceMatcher

providers_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\source\_data\providers.yml'
images_dir = r'C:\Users\USER\Desktop\BLOG\品牌照片'
dest_dir = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\source\images\logos'

os.makedirs(dest_dir, exist_ok=True)

with open(providers_path, 'r', encoding='utf-8') as f:
    providers = yaml.safe_load(f)

# List all available images
images = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
images_lower = {img.lower(): img for img in images}
print("Available images:", images)

for p in providers:
    name = p['name']
    name_clean = name.replace(' ', '').lower()
    
    best_match = None
    # 1. Exact match in filename without extension
    for img in images:
        img_name = os.path.splitext(img)[0].replace(' ', '').lower()
        if img_name == name_clean or img_name in name_clean or name_clean in img_name:
            best_match = img
            break
    
    if best_match:
        print(f"Matched {name} -> {best_match}")
        # Copy image
        shutil.copy(os.path.join(images_dir, best_match), os.path.join(dest_dir, best_match))
        # Update provider logo path
        p['logo'] = f'/images/logos/{best_match}'
    else:
        print(f"No match for {name}")

# Write back to providers.yml
with open(providers_path, 'w', encoding='utf-8') as f:
    yaml.dump(providers, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

