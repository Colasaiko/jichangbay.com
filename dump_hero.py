import re
text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<section id="top".*?<section id="recommendations"', text, re.DOTALL)
open('temp_hero.txt', 'w', encoding='utf-8').write(matches[0][:800] if matches else 'None')
