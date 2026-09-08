text = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').read()
idx = text.find('<section id="deals"')
print(text[idx:idx+1500])
