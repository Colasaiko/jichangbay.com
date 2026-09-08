import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<tbody>.*?</tbody>', f, re.DOTALL)
open('temp3.txt', 'w', encoding='utf-8').write(matches[0][:800])
