import re

ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add FAQ data at the top
faq_data = """<%
  const faqItems = [
    {
      q: "2026 机场推荐应该先看哪些参数？",
      a: "选择机场时，建议优先关注起步价格、每月可用流量、支持的线路类型（如 IPLC、IEPL 等专线或普通中转），以及是否支持你需要的特定流媒体或 AI 工具（如 ChatGPT）。不同用户的核心需求不同，看重延迟可选专线，看重性价比可选择便宜的大流量套餐。"
    },
    {
      q: "稳定机场推荐通常应该关注什么？",
      a: "寻找稳定机场推荐时，主要看该品牌是否具备足够的带宽冗余和优质的专线网络。公网中转容易在高峰期受到影响，而 IPLC 或 IEPL 专线虽然价格稍高，但在特殊时期表现更加坚挺。此外，查看商家的运营时间长短也能从侧面反映其稳定性。"
    },
    {
      q: "便宜机场推荐应该只看价格吗？",
      a: "绝不能只看价格。很多看似极低价格的套餐可能对设备数量有限制，或者在晚高峰时速度断崖式下跌。在筛选便宜机场推荐时，建议综合对比它的实际可用节点数和流量额度，避免买到难以正常连接的“残次品”。"
    },
    {
      q: "月付、年付和不限时机场套餐有什么区别？",
      a: "月付套餐灵活性最高，适合刚接触某个品牌的用户；年付通常有较大折扣，适合长期稳定使用的老用户；而不限时（按量计费）套餐则非常适合偶尔才有轻度外网需求的人群。建议新用户优先尝试月付机场，确认稳定后再考虑年付。"
    },
    {
      q: "100GB 流量一个月通常够用吗？",
      a: "这取决于你的使用习惯。如果只是日常查阅网页、使用聊天工具或偶尔看几段短视频，100GB 足以应对。但如果你经常观看 4K 高清流媒体、频繁下载大文件，建议选择 200GB 或更高额度的大流量机场推荐套餐。"
    },
    {
      q: "IPLC、IEPL 和普通中转线路有什么区别？",
      a: "IPLC 和 IEPL 均属于国际专线，网络传输不经过公共防火墙，因此具有延迟极低、高峰期不卡顿且几乎不会被封锁的特点，非常适合游戏和对稳定性要求极高的用户。而普通中转线路则是在公网上进行数据转发，成本较低但容易受网络波动影响。"
    },
    {
      q: "使用 ChatGPT、Gemini、Claude 时应该注意什么？",
      a: "这些前沿 AI 工具通常对 IP 的原生纯净度有严格要求，很多普通数据中心 IP 会被直接封锁。如果你的主要用途是 AI 交互，务必在购买前确认该机场的节点是否标注了“支持 ChatGPT”或“原生 IP”解锁能力。"
    },
    {
      q: "机场优惠码应该怎么使用？",
      a: "部分品牌会在特定节日或日常提供长期折扣码。通常你需要在其官网的注册购买页面、收银台或结账界面找到“优惠码”或“Promo Code”输入框，填入本站提供的机场优惠码并点击应用，即可享受对应折扣。"
    }
  ];
%>"""
if 'faqItems' not in html:
    html = faq_data + "\n" + html

# 2. Hero and H1 Update
html = re.sub(r'<h1>.*?</h1>', r'<h1>2026 机场推荐与 VPN 套餐选购指南</h1>', html)
html = re.sub(r'<p class="hero-subtitle">.*?</p>', r'<p class="hero-subtitle">机场湾整理：2026机场推荐、最新套餐价格（支持月付/年付）、每月流量规则、专线网络、AI工具解锁、流媒体支持情况及独家优惠码。用户可以根据自身预算与流量需求，直接筛选并前往官方入口购买最适合的科学上网服务。</p>', html)

# 3. Recommendations Description
html = re.sub(r'id="recommendations".*?<h2>(.*?)</h2>\s*<p.*?>.*?</p>', 
              r'id="recommendations" class="section-block">\n      <h2>\1</h2>\n      <p style="margin-bottom: 20px; color: #334155;">按照预算与需求快速找到适合的稳定机场推荐、便宜机场推荐与专线机场推荐。无论你是需要按量计费、大流量套餐、小流量轻度使用，还是月付/年付机场，都可以在此直接查找。</p>', html, flags=re.DOTALL)

# 4. Comparison Description
if '用户可以比较各品牌的套餐价格' not in html:
    html = re.sub(r'<h2>品牌总对比表</h2>', r'<h2>品牌总对比表</h2>\n      <p style="margin-bottom: 20px; color: #334155;">用户可以比较各品牌的套餐价格、流量、线路与适合场景。使用搜索框或通过价格、流量排序，快速在最新机场套餐对比中找到合适的优质机场推荐。</p>', html)

# 5. FAQ HTML Update
faq_html_new = """<section id="faq" class="section-block">
      <h2>常见问题 (FAQ)</h2>
      <% faqItems.forEach(item => { %>
      <div class="faq-item">
        <h4><%= item.q %></h4>
        <p><%= item.a %></p>
      </div>
      <% }) %>
    </section>"""
html = re.sub(r'<section id="faq".*?</section>', faq_html_new, html, flags=re.DOTALL)

# 6. Schema JSON-LD appended to end
schema_ld = """
<!-- SEO Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "<%= config.url %>/",
  "name": "<%= config.title %>",
  "description": "<%= config.description %>",
  "dateModified": "<%= config.lastUpdated %>"
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "2026 机场品牌列表",
  "url": "<%= config.url %>/",
  "itemListElement": [
    <% providers.forEach((p, i) => { %>
    {
      "@type": "ListItem",
      "position": <%= i + 1 %>,
      "name": "<%= p.name %>",
      "url": "<%= config.url %>/#provider-<%= p.slug %>"
    }<%= i < providers.length - 1 ? ',' : '' %>
    <% }) %>
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    <% faqItems.forEach((item, i) => { %>
    {
      "@type": "Question",
      "name": "<%= item.q %>",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "<%= item.a %>"
      }
    }<%= i < faqItems.length - 1 ? ',' : '' %>
    <% }) %>
  ]
}
</script>
"""
if 'FAQPage' not in html:
    html += "\n" + schema_ld

# Fix duplicate 200GB+ in select
if '<option value="traffic-200">200GB+</option>\n              <option value="traffic-200">200GB+</option>' in html:
    html = html.replace('<option value="traffic-200">200GB+</option>\n              <option value="traffic-200">200GB+</option>', '<option value="traffic-200">200GB+</option>')

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)
