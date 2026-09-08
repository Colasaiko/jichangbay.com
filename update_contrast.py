import os, re

# Update CSS for stronger contrast
css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Make btn-outline bolder and more legible
css = css.replace(
""".btn-outline {
  background: transparent;
  border: 1px solid var(--c-primary);
  color: var(--c-primary);
}""",
""".btn-outline {
  background: #ffffff;
  border: 1px solid var(--c-primary);
  color: var(--c-deep);
  font-weight: 600;
}"""
)
css = css.replace(
""".btn-outline:hover {
  background: var(--c-primary);
  color: white;
}""",
""".btn-outline:hover {
  background: var(--c-primary);
  color: white;
  border-color: var(--c-primary);
}"""
)

# Fix quick buy text colors
css = css.replace('color: #475569; margin-bottom: 12px;', 'color: #334155; margin-bottom: 12px; font-weight: 500;')
css = css.replace('color: #475569; font-size: 0.85rem;', 'color: #334155; font-size: 0.85rem; font-weight: 600;')
css = css.replace('.qt-btn:hover { background: #e2e8f0; color: var(--c-primary); border-color: var(--c-primary); }', '.qt-btn:hover { background: var(--c-primary); color: #ffffff; border-color: var(--c-primary); }')
css = css.replace('color: #64748b; font-size: 0.85rem;', 'color: #334155; font-size: 0.85rem; font-weight: 500;')

# Upgrade provider-section block
css = re.sub(r'/\* Independent Provider Cards \*/.*?@media \(max-width: 768px\) \{.*?\}\n\}', '', css, flags=re.DOTALL)

provider_card_css = """
/* Independent Provider Cards */
.provider-section {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  padding: 32px;
  margin-bottom: 40px;
  box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
  border-left: 4px solid var(--c-primary);
}

.provider-section h3 {
  color: #0f172a;
  margin-top: 0;
}

.provider-section .provider-short {
  color: #334155;
}

.provider-section .meta-item {
  color: #334155;
}

.provider-section .meta-item strong {
  color: #0f172a;
}

.provider-features h4, .provider-plans-table h4 {
  color: #0f172a;
}

.provider-plans-table {
  background: #f8fafc;
  border-radius: 8px;
  border: 1px solid #e2e8f0;
  padding: 16px;
  margin-top: 24px;
}

@media (max-width: 768px) {
  .provider-section {
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 24px;
  }
}
"""

css += "\n" + provider_card_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update index.ejs for text contrast
index_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = index_html.replace('color: #64748b;', 'color: #334155;')
index_html = index_html.replace('color:#64748b;', 'color:#334155;')
index_html = index_html.replace('color:#94a3b8;', 'color:#475569;')
index_html = index_html.replace('color:#475569;', 'color:#334155;')
index_html = index_html.replace('color: #475569;', 'color: #334155;')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

# Update JS for text contrast inline styles
js_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace('color:#64748b;', 'color:#334155;')
js = js.replace('color:#94a3b8;', 'color:#475569;')
js = js.replace('color:#475569;', 'color:#334155;')

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
