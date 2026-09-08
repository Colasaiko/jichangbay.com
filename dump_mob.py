import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<div class="mobile-provider-list">.*?</div>\s*</div>', f, re.DOTALL)
open('temp4.txt', 'w', encoding='utf-8').write(matches[0][:800])
