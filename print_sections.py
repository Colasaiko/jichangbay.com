import re
with open(r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()
for m in re.finditer(r'<section[^>]*>', text):
    print(m.group(0))
