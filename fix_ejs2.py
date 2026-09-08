import re
lines = open('themes/jichangbay/layout/index.ejs', 'r', encoding='utf-8').readlines()
with open('themes/jichangbay/layout/index.ejs', 'w', encoding='utf-8') as f:
    for line in lines:
        if 'let numPrice = 999999;' in line and '<%' not in line:
            f.write('<% let numPrice = 999999; ')
        elif 'numTraffic = numT;' in line and '%>' not in line:
            f.write(line.replace('numTraffic = numT; }', 'numTraffic = numT; } %>'))
        else:
            f.write(line)
