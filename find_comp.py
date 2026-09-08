import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<section id="comparison".*?<div class="comparison-container">', f, re.DOTALL)
print(matches[:1])
