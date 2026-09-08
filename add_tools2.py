import re

ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

before_buy = """
    <!-- Before Buy Section -->
    <section id="before-buy" class="section-block">
      <h2>购买前建议确认</h2>
      <p style="margin-bottom: 24px; color: #334155;">不同品牌和套餐的计费方式、流量规则与支持能力可能不同，购买前建议先确认以下信息。</p>
      <div class="bb-grid">
        <div class="bb-card">
          <div class="bb-icon">⏱️</div>
          <h4 class="bb-title">1. 套餐周期</h4>
          <p class="bb-desc">确认是月付、季付、年付或一次性/不限时。不要把年付套餐误认为月付。</p>
        </div>
        <div class="bb-card">
          <div class="bb-icon">📊</div>
          <h4 class="bb-title">2. 流量规则</h4>
          <p class="bb-desc">确认每月流量、套餐总流量、不限时流量是否重置。如果数据未明确，请以官网为准。</p>
        </div>
        <div class="bb-card">
          <div class="bb-icon">📱</div>
          <h4 class="bb-title">3. 设备支持</h4>
          <p class="bb-desc">确认是否限制设备数量，是否支持多设备同时在线。</p>
        </div>
        <div class="bb-card">
          <div class="bb-icon">🤖</div>
          <h4 class="bb-title">4. AI / 流媒体</h4>
          <p class="bb-desc">如果主要用途是 ChatGPT、Netflix 等，购买前确认对应品牌是否明确支持解锁。</p>
        </div>
        <div class="bb-card">
          <div class="bb-icon">🎫</div>
          <h4 class="bb-title">5. 优惠码</h4>
          <p class="bb-desc">如果当前有优惠码，确认是否需要在购买页面手动填写。</p>
        </div>
        <div class="bb-card">
          <div class="bb-icon">⚖️</div>
          <h4 class="bb-title">6. 服务条款</h4>
          <p class="bb-desc">价格、套餐、退款、节点和服务规则：以最终购买页面展示为准。</p>
        </div>
      </div>
    </section>

"""
if 'id="before-buy"' not in html:
    html = html.replace('<!-- Comparison Section -->', before_buy + '    <!-- Comparison Section -->')

toolbar = """
      <div class="comp-toolbar">
        <div class="comp-search">
          <label for="comp-search-input" class="sr-only">搜索品牌</label>
          <input type="text" id="comp-search-input" placeholder="搜索品牌，例如：微风、飞猫、firefly" />
        </div>
        <div class="comp-sort">
          <label for="comp-sort-select" style="font-size:0.9rem; font-weight:600; color:#0f172a;">排序：</label>
          <select id="comp-sort-select">
            <option value="default">默认顺序</option>
            <option value="price-asc">价格从低到高</option>
            <option value="traffic-asc">流量从小到大</option>
            <option value="traffic-desc">流量从大到小</option>
          </select>
        </div>
        <button id="comp-reset-btn" class="btn btn-outline" style="padding: 8px 16px;">重置</button>
      </div>
      <div id="comp-no-results" class="comp-no-results" aria-live="polite" style="display:none;">
        没有找到符合关键词的品牌。<button id="comp-clear-btn" class="btn btn-primary btn-small" style="margin-left: 10px;">清除搜索</button>
      </div>
"""
if 'class="comp-toolbar"' not in html:
    html = html.replace('<div class="comparison-container">', toolbar + '\n      <div class="comparison-container">')

def replacer_tr(match):
    return match.group(1) + """
                  let numPrice = 999999;
                  if (firstPlan) {
                      if (firstPlan.monthly) numPrice = parseFloat(firstPlan.monthly.replace(/[^0-9.]/g, '')) || 0;
                      else if (firstPlan.annual) numPrice = parseFloat(firstPlan.annual.replace(/[^0-9.]/g, '')) || 0;
                      else if (firstPlan.oneTime) numPrice = parseFloat(firstPlan.oneTime.replace(/[^0-9.]/g, '')) || 0;
                  }
                  let numTraffic = 0;
                  if (startTraffic !== '-') {
                      let tStr = startTraffic.toUpperCase();
                      let numT = parseFloat(tStr.replace(/[^0-9.]/g, '')) || 0;
                      if (tStr.includes('TB')) numT *= 1000;
                      numTraffic = numT;
                  }
                %>
                <tr class="comp-tr" data-name="<%= p.name.toLowerCase() %>" data-price="<%= numPrice %>" data-traffic="<%= numTraffic %>" data-order="<%= index %>">"""

# For EJS, I need to pass index: `providers.forEach(function(p, index) {`
html = html.replace('providers.forEach(function(p) {', 'providers.forEach(function(p, index) {')

# The TR replacement. The original is:
# startTraffic = startTraffic.replace(/([0-9]+)\s*(GB|TB)/i, '$1 $2').toUpperCase();
# }
# %>
# <tr
html = re.sub(r'(\s*startTraffic = startTraffic\.replace[^;]+;\s*\}\s*)%>\s*<tr>', replacer_tr, html)


def replacer_card(match):
    return match.group(1) + """
                  let numPrice = 999999;
                  if (firstPlan) {
                      if (firstPlan.monthly) numPrice = parseFloat(firstPlan.monthly.replace(/[^0-9.]/g, '')) || 0;
                      else if (firstPlan.annual) numPrice = parseFloat(firstPlan.annual.replace(/[^0-9.]/g, '')) || 0;
                      else if (firstPlan.oneTime) numPrice = parseFloat(firstPlan.oneTime.replace(/[^0-9.]/g, '')) || 0;
                  }
                  let numTraffic = 0;
                  if (startTraffic !== '-') {
                      let tStr = startTraffic.toUpperCase();
                      let numT = parseFloat(tStr.replace(/[^0-9.]/g, '')) || 0;
                      if (tStr.includes('TB')) numT *= 1000;
                      numTraffic = numT;
                  }
                %>
          <div class="mobile-card comp-card" data-name="<%= p.name.toLowerCase() %>" data-price="<%= numPrice %>" data-traffic="<%= numTraffic %>" data-order="<%= index %>">"""

html = re.sub(r'(\s*startTraffic = startTraffic\.replace[^;]+;\s*\}\s*)%>\s*<div class="mobile-card">', replacer_card, html)

toc_old = '<li><a href="#deals" class="toc-link">当前优惠</a></li>\n          <li><a href="#comparison" class="toc-link">参数对比表</a></li>'
toc_new = '<li><a href="#deals" class="toc-link">当前优惠</a></li>\n          <li><a href="#before-buy" class="toc-link">购买前确认</a></li>\n          <li><a href="#comparison" class="toc-link">参数对比表</a></li>'
html = html.replace(toc_old, toc_new)

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)
