import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
f = f.replace('<option value="200">200GB+</option>\n            <option value="200">200GB+</option>', '<option value="200">200GB+</option>')
open('themes/jichangbay/layout/index.ejs', 'w', encoding='utf-8').write(f)
