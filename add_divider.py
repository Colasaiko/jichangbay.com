import os

ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the divider to the brand card header
target = '</a>\n            </div>\n          \n          <div class="provider-meta">'
replacement = '</a>\n            </div>\n          </div>\n          <div class="provider-divider" style="border-bottom: 1px solid #e2e8f0; margin-top: 18px; margin-bottom: 24px;"></div>\n          <div class="provider-meta">'

if target in html:
    html = html.replace(target, replacement)
elif '</a>\n            </div>\n          </div>\n          <div class="provider-divider"' not in html:
    # If the divider is missing but the target string is slightly different
    # Let's use a regex replacement to ensure it's added.
    import re
    # Match the end of provider-header-cta
    html = re.sub(r'(class="btn btn-primary btn-small">[^<]*</a>\s*</div>)(\s*<div class="provider-meta">)', 
                  r'\1\n          </div>\n          <div class="provider-divider" style="border-bottom: 1px solid #e2e8f0; margin-top: 18px; margin-bottom: 24px;"></div>\2', 
                  html)

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)
