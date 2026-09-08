import os, re

# Fix EJS
ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the deals section and remove the provider-divider within it
deals_start = html.find('<section id="deals"')
deals_end = html.find('</section>', deals_start)
deals_html = html[deals_start:deals_end]

# Remove the specific divider tag from the deals section
bad_divider = '<div class="provider-divider" style="border-bottom: 1px solid #e2e8f0; margin-top: 18px; margin-bottom: 24px;"></div>'
deals_html_fixed = deals_html.replace(bad_divider, '')
html = html[:deals_start] + deals_html_fixed + html[deals_end:]

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Fix CSS
css_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# We need to change .deals-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; }
css = re.sub(r'\.deals-grid\s*\{[^}]*\}', '', css)

deals_css = """
.deals-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}
@media (max-width: 1100px) {
  .deals-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
@media (max-width: 600px) {
  .deals-grid {
    grid-template-columns: 1fr;
  }
}
"""

css += "\n" + deals_css.strip()

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

