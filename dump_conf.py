import os
text = open('_config.yml', 'r', encoding='utf-8').read()
with open('temp_conf.txt', 'w', encoding='utf-8') as f:
    f.write(text)
