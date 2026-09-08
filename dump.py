import os, re

f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = [m.group(0) for m in re.finditer(r'<section.*?provider.*?/section>', f, re.DOTALL)]
open('temp.txt', 'w', encoding='utf-8').write(matches[0] if matches else "None")
