import os

css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

addition = """
.provider-section p, .provider-section li, .provider-section td, .provider-section th {
  color: #0f172a;
}
.provider-section .meta-item, .provider-section .provider-short {
  color: #334155;
  font-weight: 500;
}
"""

if ".provider-section p" not in css:
    css += "\n" + addition

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
