import re
text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<section id="faq".*?</section>', text, re.DOTALL)
open('temp_faq.txt', 'w', encoding='utf-8').write(matches[0] if matches else 'None')
