import re
with open(r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs', 'r', encoding='utf-8') as f:
    text = f.read()
idx = text.find('id="provider-')
print(text[idx-20:idx+200])
