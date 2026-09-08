import re
text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
matches = re.findall(r'<script type="application/ld\+json">.*?</script>', text, re.DOTALL)
if matches:
    for m in matches:
        open('temp_schema.txt', 'a', encoding='utf-8').write(m + "\n")
