import os, re

ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the broken section tag
broken_tag = '<section id="provider-<%= p.slug %>"\n          <div class="provider-header"'
fixed_tag = '<section id="provider-<%= p.slug %>" class="section-block provider-section">\n          <div class="provider-header"'
html = html.replace(broken_tag, fixed_tag)

# Make sure there is a divider! The user said:
# "Header 底部加一条很浅的分隔线：border-bottom: 1px solid #e2e8f0; padding-bottom: 18px; margin-bottom: 20px"
# Let's verify if the divider was added properly.
if 'class="provider-divider"' not in html:
    # If not, let's add it. But I already tried in step1. 
    # Let's do it cleanly:
    header_end = '</a>\n            </div>\n          </div>'
    header_end_with_divider = '</a>\n            </div>\n          </div>\n          <div class="provider-divider" style="border-bottom: 1px solid #e2e8f0; margin-top: 18px; margin-bottom: 24px;"></div>'
    html = html.replace(header_end, header_end_with_divider)

# Fix Mac button
mac_btn_old = 'class="btn btn-outline">Mac 客户端下载</a>'
mac_btn_new = 'class="btn mac-btn">Mac 客户端下载</a>'
html = html.replace(mac_btn_old, mac_btn_new)

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

mac_btn_css = """
/* Mac Download Button */
.mac-btn, .mac-btn:visited {
  background: #ffffff !important;
  border: 1px solid var(--c-primary) !important;
  color: var(--c-primary) !important;
  font-weight: 600 !important;
  opacity: 1 !important;
  pointer-events: auto !important;
  text-decoration: none !important;
}
.mac-btn:hover {
  background: var(--c-primary) !important;
  color: #ffffff !important;
}

/* Specific spacing within provider-section */
.provider-action {
  margin-top: 32px !important;
}

.provider-section {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 40px;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
  border-left: 4px solid var(--c-primary);
  display: block; /* ensure it's a block */
}

/* Ensure plans table is nicely contained */
.provider-plans-table {
  background: #f8fafc;
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  padding: 20px;
  margin-top: 24px;
  margin-bottom: 24px;
  overflow-x: auto;
}
.plans-table {
  width: 100%;
  border-collapse: collapse;
}
.plans-table th {
  background: #f1f5f9;
  color: #0f172a;
  padding: 10px 12px;
  border: 1px solid #e2e8f0;
  text-align: left;
}
.plans-table td {
  padding: 10px 12px;
  border: 1px solid #e2e8f0;
  color: #334155;
}

@media (max-width: 768px) {
  .provider-section {
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 24px;
  }
}
"""

if ".mac-btn" not in css:
    css += "\n" + mac_btn_css

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
