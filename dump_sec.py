import re
text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
r_matches = re.findall(r'<section id="recommendations".*?class="quick-buy-grid">', text, re.DOTALL)
c_matches = re.findall(r'<section id="comparison".*?<div class="comp-toolbar">', text, re.DOTALL)
print("Recommendations:\n", r_matches[0] if r_matches else None)
print("Comparison:\n", c_matches[0] if c_matches else None)
