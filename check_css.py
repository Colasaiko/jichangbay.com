import re
css = open('public/css/style.css', 'r', encoding='utf-8').read()
matches = re.finditer(r'\.provider-section.*?\}', css, re.DOTALL)
for i, m in enumerate(matches):
    if i < 3: print(m.group(0))
