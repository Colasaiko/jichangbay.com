import re
ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'<script type="application/ld\+json">.*?</script>', html, re.DOTALL)
for i, m in enumerate(matches):
    open(f'temp_schema_{i}.txt', 'w', encoding='utf-8').write(m)
