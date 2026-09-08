import os

index_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

index_html = index_html.replace('<option value="100">100GB+</option>', '<option value="100-200">100-200GB</option>\n            <option value="200">200GB+</option>')
# We already have 200GB+, so replacing 100GB+ with 100-200GB and putting 200GB+ back if we overwrite it? Actually I'll just replace `<option value="100">100GB+</option>` with `<option value="100-200">100–200GB</option>` since 200GB+ is already there!
index_html = index_html.replace('<option value="100">100GB+</option>\n            <option value="200">200GB+</option>', '<option value="100-200">100–200GB</option>\n            <option value="200">200GB+</option>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)
