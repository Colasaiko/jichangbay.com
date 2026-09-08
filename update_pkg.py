import json
with open('package.json', 'r', encoding='utf-8') as f:
    pkg = json.load(f)

if "node tools/check-seo.js" not in pkg["scripts"]["build"]:
    pkg["scripts"]["build"] = "hexo generate && node tools/check-seo.js"

with open('package.json', 'w', encoding='utf-8') as f:
    json.dump(pkg, f, indent=2, ensure_ascii=False)
