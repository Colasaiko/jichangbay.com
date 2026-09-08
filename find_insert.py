import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'</section>\s*<!-- Comparison Section -->', f, re.DOTALL)
print(matches[:1])
