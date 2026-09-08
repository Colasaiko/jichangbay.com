import re

with open('_config.yml', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Title
text = re.sub(r'title: .*', "title: 2026机场推荐｜稳定便宜专线机场与VPN推荐｜机场湾", text)
# Replace Description
text = re.sub(r"description: '.*?'", "description: '机场湾整理2026机场推荐、稳定机场推荐、便宜机场推荐与专线机场推荐，提供套餐价格、流量、优惠码、AI及流媒体支持，可按预算和流量快速筛选并查看购买入口。'", text)
# Replace Keywords
text = re.sub(r"keywords: '.*?'", "keywords: '机场推荐,2026机场推荐,稳定机场推荐,便宜机场推荐,专线机场推荐,VPN推荐,机场套餐,机场优惠码'", text)

with open('_config.yml', 'w', encoding='utf-8') as f:
    f.write(text)
