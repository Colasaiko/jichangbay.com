import os, re

index_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Move the sorting logic block to the very top, before the Hero section
sorting_block_start = "<% \n            let providers = site.data.providers"
sorting_block_end = "function getProviderMeta(p) {"
# Let's find the exact block using regex
match = re.search(r'(<% \s*let providers = site\.data\.providers.*?\n          %>)\n', index_html, flags=re.DOTALL)
if match:
    sorting_code = match.group(1)
    index_html = index_html.replace(sorting_code + '\n', '') # remove it from where it is
    # insert it right after <article class="content-area">
    index_html = index_html.replace('<article class="content-area">', '<article class="content-area">\n' + sorting_code)

# 2. Fix the brand sections forEach loop
index_html = index_html.replace('<% if (site.data.providers) { %>', '<% if (providers.length) { %>')
index_html = index_html.replace('<% site.data.providers.forEach(function(p) { %>', '<% providers.forEach(function(p) { %>')

# 3. Update btn-outline in Hero section
index_html = index_html.replace('<a href="#comparison" class="btn btn-outline">套餐对比</a>', '<a href="#comparison" class="btn btn-outline-light">套餐对比</a>')
index_html = index_html.replace('<a href="#deals" class="btn btn-outline">当前优惠</a>', '<a href="#deals" class="btn btn-outline-light">当前优惠</a>')

# 4. Brand Section Header redesign
# The user wants a clean divider and structured header.
def replace_brand_details(text):
    start_token = '<section id="provider-<%= p.slug %>" class="section-block provider-section">'
    end_token = '</div>\n          <% if (p.features && p.features.length) { %>'
    
    parts = text.split(start_token)
    if len(parts) < 2: return text
    
    out = [parts[0]]
    for i in range(1, len(parts)):
        part = parts[i]
        
        # We also need to fix the provider-header CTA block to make sure colors are consistent
        # And we need to add a divider below the header
        if '<div class="provider-header" style="justify-content: space-between; flex-wrap: wrap;">' in part:
            part = part.replace(
                '<div class="provider-header-cta" style="display:flex; flex-direction:column; gap:8px; align-items:flex-end;">',
                '<div class="provider-header-cta" style="display:flex; flex-direction:column; gap:8px; align-items:flex-end;">'
            )
            # Find the end of provider-header to insert a divider
            idx = part.find('</a>\n            </div>\n          </div>')
            if idx != -1:
                idx += len('</a>\n            </div>\n          </div>')
                part = part[:idx] + '\n          <div class="provider-divider" style="border-bottom: 1px solid #e2e8f0; margin-top: 18px; margin-bottom: 20px;"></div>' + part[idx:]
        
        out.append(start_token + part)
            
    return "".join(out)

index_html = replace_brand_details(index_html)

# Also let's fix the td class flex issue in index_html for comparison table tags
index_html = index_html.replace('<td class="col-tags">', '<td class="col-tags"><div class="tags-inner">')
index_html = index_html.replace('</td>\n                  <td class="col-detail">', '</div></td>\n                  <td class="col-detail">')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

# -----------------
# UPDATE CONFIG
# -----------------
config_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\_config.yml"
with open(config_path, "r", encoding="utf-8") as f:
    config = f.read()

config = config.replace('机场评测,', '')
config = config.replace('评测', '')
config = config.replace('评分', '')

with open(config_path, "w", encoding="utf-8") as f:
    f.write(config)
