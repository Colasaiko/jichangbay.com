import os, re

f = open('themes/jichangbay/source/css/style.css', 'r', encoding='utf-8').read()
matches = [m.group(0) for m in re.finditer(r'\.btn-outline.*?\}', f, re.DOTALL)]
open('temp2.txt', 'w', encoding='utf-8').write('\n'.join(matches))
