import re
layout_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\layout.ejs'
with open(layout_path, 'r', encoding='utf-8') as f:
    layout = f.read()

# Update Schema
layout = re.sub(r'<script type="application/ld\+json">.*?</script>', '', layout, flags=re.DOTALL)
# Remove og:image reference
layout = re.sub(r'<meta property="og:image".*?>\n', '', layout)

with open(layout_path, 'w', encoding='utf-8') as f:
    f.write(layout)
