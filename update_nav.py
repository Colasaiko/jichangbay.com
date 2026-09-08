import os, re

# Update index.ejs nav and mobile nav
index_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = re.sub(
    r'<nav class="desktop-nav">.*?</nav>',
    """<nav class="desktop-nav">
        <a href="#recommendations">选购</a>
        <a href="#deals">优惠</a>
        <a href="#comparison">对比</a>
        <a href="#how-to-choose">指南</a>
        <a href="#faq">FAQ</a>
      </nav>""",
    index_html, flags=re.DOTALL
)

index_html = re.sub(
    r'<div class="mobile-nav-menu">.*?</div>',
    """<div class="mobile-nav-menu">
      <a href="#recommendations">选购</a>
      <a href="#deals">优惠</a>
      <a href="#comparison">对比</a>
      <a href="#how-to-choose">指南</a>
      <a href="#faq">FAQ</a>
    </div>""",
    index_html, flags=re.DOTALL
)

# And remove 机场评测 from keywords
config_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\_config.yml"
with open(config_path, "r", encoding="utf-8") as f:
    config = f.read()
config = config.replace('机场评测,', '')
with open(config_path, "w", encoding="utf-8") as f:
    f.write(config)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
