import re
f = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<select id="filter-traffic">.*?</select>', f, re.DOTALL)
if matches:
    print(matches[0])
