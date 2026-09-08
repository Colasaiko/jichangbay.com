import re
text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<div class="provider-header".*?</section>', text, re.DOTALL)
if matches: print(matches[0][:1200])
