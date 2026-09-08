import os, re

css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Fix btn-outline and add btn-outline-light
css = css.replace(
""".btn-outline {
  background: transparent;
  border: 2px solid white;
  color: white;
}

.btn-outline:hover {
  background: white;
  color: var(--c-deep);
}""",
""".btn-outline-light {
  background: transparent;
  border: 1px solid rgba(255,255,255,0.8);
  color: white;
}
.btn-outline-light:hover {
  background: white;
  color: var(--c-deep);
}
.btn-outline {
  background: transparent;
  border: 1px solid var(--c-primary);
  color: var(--c-primary);
}
.btn-outline:hover {
  background: var(--c-primary);
  color: white;
}"""
)

# Fix brand-name display:flex issue
if ".brand-name {" in css:
    css = re.sub(r'\.brand-name\s*\{\s*display:\s*flex;.*?(?=\})\}', '', css, flags=re.DOTALL)
    css = re.sub(r'\.col-tags\s*\{\s*display:\s*flex;.*?(?=\})\}', '', css, flags=re.DOTALL)

# Add card styles for provider-section
new_css = """
/* Independent Provider Cards */
.provider-section {
  background: #fff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 24px 32px;
  margin-bottom: 32px;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.05);
  border-left: 4px solid var(--c-primary);
}

@media (max-width: 768px) {
  .provider-section {
    padding: 16px 20px;
    border-radius: 8px;
  }
}

/* Fix td flex issues */
.tags-inner {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}
.brand-cell {
  display: flex;
  align-items: center;
  gap: 8px;
}
"""

if "/* Independent Provider Cards */" not in css:
    css += "\n" + new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

