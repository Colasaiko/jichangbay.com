lines = open('public/index.html', 'r', encoding='utf-8').read().splitlines()
matches = [l for l in lines if 'Mac' in l][:3]
for m in matches: print(m)
