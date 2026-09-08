import os, json, re

# 1. Update _config.yml
config_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\_config.yml"
with open(config_path, "r", encoding="utf-8") as f:
    config = f.read()

config = re.sub(r'description:\s*.*', "description: '2026年机场与VPN服务信息整理，提供套餐价格、流量、线路、AI与流媒体支持、优惠信息及选购指南，帮助用户快速比较并找到适合自己的服务。'", config)
config = re.sub(r'lastUpdated:\s*.*', "lastUpdated: '2026-09-08'", config)
config = config.replace('机场评测,', '')
with open(config_path, "w", encoding="utf-8") as f:
    f.write(config)

# 2. Update index.ejs
index_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

def replace_between(text, start_str, end_str, replacement):
    start = text.find(start_str)
    if start == -1: return text
    end = text.find(end_str, start)
    if end == -1: return text
    end += len(end_str)
    return text[:start] + replacement + text[end:]

# Replace Hero
hero_replacement = """
    <!-- Hero Section -->
    <section id="top" class="hero-section">
      <h1>2026 机场推荐与 VPN 使用指南</h1>
      <p class="hero-subtitle">集中整理机场与 VPN 服务的套餐价格、流量、线路、优惠与使用场景，帮助你更快找到适合自己的选择。</p>
      <p class="hero-meta">最后更新时间: <%= config.lastUpdated %></p>
      <div class="hero-actions">
        <a href="#recommendations" class="btn btn-primary">快速选购</a>
        <a href="#comparison" class="btn btn-outline">套餐对比</a>
        <a href="#deals" class="btn btn-outline">当前优惠</a>
      </div>
    </section>
"""
index_html = replace_between(index_html, '<!-- Hero Section -->', '</section>', hero_replacement.strip())


# Common sorting logic to be used everywhere
sorting_logic = """
          <% 
            let providers = site.data.providers ? JSON.parse(JSON.stringify(site.data.providers)) : [];
            const fixedFirst = '微风网络';
            const fixedSecond = '飞猫云';
            const pool = ['闪跃', '灵猫', 'firefly', '无忧链接', '跨界云'];
            
            // Randomize pool using a simple build-time shuffle
            for(let i = pool.length - 1; i > 0; i--){
              const j = Math.floor(Math.random() * (i + 1));
              [pool[i], pool[j]] = [pool[j], pool[i]];
            }
            
            const featuredOrder = [fixedFirst, fixedSecond, ...pool];
            
            providers = providers.sort((a, b) => {
              let idxA = featuredOrder.findIndex(name => name.toLowerCase() === a.name.toLowerCase());
              let idxB = featuredOrder.findIndex(name => name.toLowerCase() === b.name.toLowerCase());
              if(idxA === -1) idxA = 999;
              if(idxB === -1) idxB = 999;
              if(idxA !== idxB) return idxA - idxB;
              return 0; // fallback to original order
            });
            
            function getProviderMeta(p) {
                const firstPlan = p.plans && p.plans[0]; 
                let startPrice = '-';
                if (firstPlan) {
                  if (firstPlan.monthly) startPrice = firstPlan.monthly.replace('¥ ', '¥') + ' / 月起';
                  else if (firstPlan.annual) startPrice = firstPlan.annual.replace('¥ ', '¥') + ' / 年起';
                  else if (firstPlan.oneTime) startPrice = firstPlan.oneTime.replace('¥ ', '¥') + ' / 次起';
                }
                
                let startTraffic = (firstPlan ? firstPlan.traffic : '-') || '-';
                if(startTraffic !== '-') {
                   startTraffic = startTraffic.replace(/([0-9]+)\\s*(GB|TB)/i, '$1 $2').toUpperCase() + ' 起';
                }
                
                let network = '优质专线';
                if (p.features && p.features.some(f => f.toUpperCase().includes('IPLC'))) network = 'IPLC 专线';
                else if (p.features && p.features.some(f => f.toUpperCase().includes('IEPL'))) network = 'IEPL 专线';
                else if (p.features && p.features.some(f => f.toUpperCase().includes('BGP'))) network = 'BGP 中转';
                
                let tags = [];
                if (p.aiSupport === '支持 AI') tags.push('AI支持');
                if (p.streamingSupport === '支持流媒体解锁') tags.push('流媒体');
                if (p.clientSupport === '不限设备/支持多端') tags.push('多设备');
                if (p.plans && p.plans.some(pl => pl.oneTime)) tags.push('不限时');
                if (tags.length === 0) tags.push('优质线路');
                
                let bestForStr = Array.isArray(p.bestFor) ? p.bestFor.slice(0, 2).join(' / ') : '-';
                if (!bestForStr || bestForStr === '') bestForStr = '-';
                const logoSrc = p.logo || ('https://ui-avatars.com/api/?name=' + encodeURIComponent(p.name) + '&background=0f172a&color=fff&rounded=true&bold=true');
                
                return { startPrice, startTraffic, network, tags, bestForStr, logoSrc };
            }
          %>
"""

# Replace Recommendations Section with Quick Buy + Filter
quick_buy_filter = """
    <!-- Quick Buy Section -->
    <section id="recommendations" class="section-block">
      <h2>2026 机场快速选购</h2>
      <p style="margin-bottom: 20px; color: #64748b;">按照预算、流量与使用场景快速找到适合自己的套餐，无需逐个查看全部品牌。</p>
      """ + sorting_logic + """
      <div class="quick-buy-grid">
        <% providers.slice(0, 7).forEach((p, i) => {
            const meta = getProviderMeta(p);
        %>
          <div class="card <%= i < 2 ? 'card-featured' : 'card-small' %>">
            <div class="card-head">
              <strong><%= p.name %></strong>
            </div>
            <div class="card-stats">
              <span><%= meta.startPrice %></span>
              <span><%= meta.startTraffic %></span>
            </div>
            <a href="#provider-<%= p.slug %>" class="btn btn-outline btn-block">查看套餐</a>
          </div>
        <% }) %>
      </div>
      
      <div class="quick-tags-container" style="margin-top:24px;">
        <h4 style="margin-bottom:12px;font-size:1rem;">按需求快速找：</h4>
        <div class="quick-tags">
          <button class="qt-btn" data-filter="budget-20">¥20/月以内</button>
          <button class="qt-btn" data-filter="budget-30">¥30/月以内</button>
          <button class="qt-btn" data-filter="budget-year">年付低价</button>
          <button class="qt-btn" data-filter="traffic-200">100–200GB</button>
          <button class="qt-btn" data-filter="traffic-500">500GB+</button>
          <button class="qt-btn" data-filter="ai">AI 工具</button>
          <button class="qt-btn" data-filter="stream">流媒体</button>
          <button class="qt-btn" data-filter="onetime">不限时套餐</button>
          <button class="qt-btn" data-filter="multidevice">多设备</button>
          <button class="qt-btn" data-filter="iplc">专线线路</button>
        </div>
      </div>
    </section>

    <!-- Plan Filter Section -->
    <section id="plan-filter" class="section-block">
      <h2>按需求筛选套餐</h2>
      <p style="margin-bottom: 20px; color: #64748b;">选择预算、流量和使用需求，机场湾会从当前收录品牌中筛选符合条件的选项。</p>
      
      <div class="filter-controls">
        <div class="filter-group">
          <label>付款方式</label>
          <select id="filter-payment">
            <option value="all">全部</option>
            <option value="monthly">月付</option>
            <option value="annual">年付</option>
            <option value="onetime">不限时 / 一次性</option>
          </select>
        </div>
        <div class="filter-group">
          <label>预算</label>
          <select id="filter-budget">
            <option value="all">不限</option>
            <!-- Dynamically populated based on payment -->
          </select>
        </div>
        <div class="filter-group">
          <label>最低流量</label>
          <select id="filter-traffic">
            <option value="all">不限</option>
            <option value="50">50GB+</option>
            <option value="100">100GB+</option>
            <option value="200">200GB+</option>
            <option value="300">300GB+</option>
            <option value="500">500GB+</option>
            <option value="1000">1000GB+</option>
          </select>
        </div>
        <div class="filter-group filter-checkboxes">
          <label><input type="checkbox" id="filter-ai"> 支持 AI</label>
          <label><input type="checkbox" id="filter-stream"> 支持流媒体</label>
          <label><input type="checkbox" id="filter-device"> 多设备</label>
          <label><input type="checkbox" id="filter-network"> 专线</label>
        </div>
        <div class="filter-actions">
           <button id="btn-reset-filter" class="btn btn-outline" style="padding:4px 12px;font-size:0.8rem;">重置筛选</button>
        </div>
      </div>
      
      <div id="filter-results-info" style="margin-top: 20px; font-weight: 600;"></div>
      <div id="filter-results-container" class="filter-results-grid"></div>
      
      <script>
        // Inject provider data for JS filtering
        window.siteProviders = <%- JSON.stringify(providers.map(p => {
          let meta = getProviderMeta(p);
          return {
             name: p.name,
             slug: p.slug,
             plans: p.plans || [],
             features: p.features || [],
             aiSupport: p.aiSupport,
             streamingSupport: p.streamingSupport,
             clientSupport: p.clientSupport,
             coupon: p.coupon,
             couponDiscount: p.couponDiscount,
             affUrl: p.affUrl || p.officialUrl,
             logoSrc: meta.logoSrc,
             network: meta.network,
             tags: meta.tags,
             bestForStr: meta.bestForStr
          };
        })) %>;
      </script>
    </section>
    
    <!-- Deals Section -->
    <section id="deals" class="section-block">
      <h2>当前优惠与优惠码</h2>
      <p style="margin-bottom: 20px; color: #64748b;">这里集中整理目前数据中明确提供的优惠信息，具体活动以购买页面显示为准。</p>
      <div class="deals-grid">
        <% 
           const deals = providers.filter(p => p.coupon && !p.coupon.includes('暂无优惠'));
           deals.forEach(p => {
             const meta = getProviderMeta(p);
        %>
          <div class="deal-card">
            <div class="deal-header">
               <img src="<%= meta.logoSrc %>" alt="<%= p.name %>" class="mc-logo">
               <strong><%= p.name %></strong>
            </div>
            <div class="deal-discount"><%= p.couponDiscount || '专属优惠' %></div>
            <div class="deal-code">
               <span><%= p.coupon %></span>
               <button class="btn-copy-code" data-code="<%= p.coupon %>" aria-label="复制优惠码">复制优惠码</button>
            </div>
            <div class="deal-action" style="margin-top:10px;">
               <a href="<%= p.affUrl || p.officialUrl %>" target="_blank" rel="noopener nofollow" class="btn btn-primary btn-block">前往购买</a>
            </div>
          </div>
        <% }) %>
      </div>
    </section>
"""

# Replace Recommendations Section with Quick Buy + Filter + Deals
index_html = replace_between(index_html, '<!-- Recommendations Section -->', '</section>', quick_buy_filter.strip())

# IMPORTANT: we must update the Comparison Section to use our sorted `providers` array.
# The comparison section has: `let providers = site.data.providers || [];`
# We'll just remove that line so it uses the sorted `providers` from Quick Buy.
# AND remove its sorting logic
comparison_sort_regex = r"let providers = site\.data\.providers \|\| \[\];.*?providers = providers\.slice\(\)\.sort\(\(a, b\) => \{.*?return 0;\s*}\);"
index_html = re.sub(comparison_sort_regex, '', index_html, flags=re.DOTALL)


# Update Brand Details CTA
def replace_brand_details(text):
    start_token = '<section id="provider-<%= p.slug %>"'
    end_token = '</div>\n          <div class="provider-meta">'
    
    parts = text.split(start_token)
    if len(parts) < 2: return text
    
    out = [parts[0]]
    for i in range(1, len(parts)):
        part = parts[i]
        end_idx = part.find(end_token)
        if end_idx != -1:
            replacement = r"""
          <div class="provider-header" style="justify-content: space-between; flex-wrap: wrap;">
            <div style="display:flex; align-items:center; gap:15px;">
              <img src="<%= getProviderMeta(p).logoSrc %>" alt="<%= p.name %>" class="provider-logo">
              <div>
                <h3><%= p.name %></h3>
                <p class="provider-short"><%= p.shortDescription || getProviderMeta(p).bestForStr %></p>
              </div>
            </div>
            <div class="provider-header-cta" style="display:flex; flex-direction:column; gap:8px; align-items:flex-end;">
               <div style="font-weight:bold; color:var(--c-primary);"><%= getProviderMeta(p).startPrice %></div>
               <% if (p.coupon && !p.coupon.includes('暂无优惠')) { %>
                 <div style="font-size:0.85rem; color:#f59e0b;">优惠码：<%= p.coupon %> · <%= p.couponDiscount || '优惠' %></div>
               <% } %>
               <a href="<%= p.affUrl || p.officialUrl %>" target="_blank" rel="nofollow noopener" class="btn btn-primary btn-small">查看套餐 / 注册购买</a>
            </div>
          """
            out.append(start_token + replacement + part[end_idx + len('</div>'):])
        else:
            out.append(start_token + part)
            
    return "".join(out)

index_html = replace_brand_details(index_html)

# Update Details Buttons
index_html = index_html.replace('访问官网 / 注册购买', '查看套餐 / 注册购买')

# Update "How to Choose", "Knowledge", "FAQ", "About"
how_to_choose = """
    <!-- How to Choose -->
    <section id="how-to-choose" class="section-block">
      <h2>如何选择适合自己的服务？</h2>
      <p>选择合适的服务主要取决于您的核心需求：</p>
      <ul>
        <li><strong>日常查资料与看视频：</strong> 选择性价比高的常规线路，流量充足，价格实惠。</li>
        <li><strong>办公、视频或对线路稳定性要求较高：</strong> 可以优先关注标明 IPLC、IEPL 或其他专线架构的服务，同时结合预算、流量和节点地区进行选择。</li>
        <li><strong>更重视隐私政策：</strong> 购买前可以查看服务商公开的隐私说明、日志政策和运营信息。</li>
      </ul>
    </section>
"""
index_html = replace_between(index_html, '<!-- How to Choose -->', '</section>', how_to_choose.strip())

knowledge = """
    <!-- Knowledge -->
    <section id="knowledge" class="section-block">
      <h2>基础知识科普</h2>
      <p><strong>什么是机场？</strong> 机场通常指提供代理节点的服务商，因早期很多服务商使用飞机图标而得名。</p>
      <p><strong>专线是什么？</strong> IPLC 等专线通常用于跨境专用网络连接，其实际线路结构、稳定性和路由方式会因服务商方案而异。用户选购时应以服务商公开线路信息和实际套餐说明为准。</p>
    </section>
"""
index_html = replace_between(index_html, '<!-- Knowledge -->', '</section>', knowledge.strip())

about = """
    <!-- About -->
    <section id="about" class="section-block">
      <h2>关于机场湾 (JichangBay)</h2>
      <p>机场湾用于集中整理网络服务品牌的套餐、线路、适用场景与优惠信息，方便用户进行横向比较和选择。页面内容会根据品牌套餐与服务信息变化持续更新。</p>
      <p><strong>利益相关声明：</strong> 本站收录的部分或全部品牌属于本站关联或自营服务。页面中的注册或购买链接可能包含内部追踪参数，用于统计来源及运营分析。购买前请以对应服务页面展示的套餐、价格与服务条款为准。</p>
    </section>
"""
index_html = replace_between(index_html, '<!-- About -->', '</section>', about.strip())

# Update Nav
index_html = re.sub(
    r'<nav class="desktop-nav">.*?</nav>',
    """<nav class="desktop-nav">
        <a href="#recommendations">选购</a>
        <a href="#deals">优惠</a>
        <a href="#comparison">对比</a>
        <a href="#how-to-choose">指南</a>
        <a href="#faq">FAQ</a>
      </nav>""",
    index_html, flags=re.DOTALL
)

index_html = re.sub(
    r'<div class="mobile-nav-menu">.*?</div>',
    """<div class="mobile-nav-menu">
      <a href="#recommendations">选购</a>
      <a href="#deals">优惠</a>
      <a href="#comparison">对比</a>
      <a href="#how-to-choose">指南</a>
      <a href="#faq">FAQ</a>
    </div>""",
    index_html, flags=re.DOTALL
)

# Update TOC
toc_replacement = """
      <ul id="toc-list">
        <li><a href="#top" class="toc-link">首页</a></li>
        <li><a href="#recommendations" class="toc-link">快速选购</a></li>
        <li><a href="#plan-filter" class="toc-link">套餐筛选</a></li>
        <li><a href="#deals" class="toc-link">当前优惠</a></li>
        <li><a href="#comparison" class="toc-link">参数对比表</a></li>
        <% providers.forEach(function(p) { %>
          <li><a href="#provider-<%= p.slug %>" class="toc-link toc-child"><%= p.name %></a></li>
        <% }) %>
        <li><a href="#how-to-choose" class="toc-link">选择指南</a></li>
        <li><a href="#knowledge" class="toc-link">基础知识</a></li>
        <li><a href="#faq" class="toc-link">常见问题</a></li>
        <li><a href="#about" class="toc-link">关于我们</a></li>
      </ul>
"""
index_html = replace_between(index_html, '<ul id="toc-list">', '</ul>', toc_replacement.strip())


with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_html)

# 4. Update CSS
css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = """
/* Quick Buy & Filter & Deals */
.quick-buy-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
  margin-bottom: 24px;
}
.card-featured {
  grid-column: span 2;
  background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
  border: 1px solid #bae6fd;
}
@media (max-width: 768px) {
  .card-featured { grid-column: span 1; }
  .quick-buy-grid { grid-template-columns: 1fr; }
}
.card-head { font-size: 1.1rem; margin-bottom: 8px; color: var(--c-deep); }
.card-stats { display: flex; flex-direction: column; gap: 4px; font-size: 0.9rem; color: #475569; margin-bottom: 12px; }

.quick-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.qt-btn { background: #f1f5f9; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 999px; cursor: pointer; color: #475569; font-size: 0.85rem; transition: background 0.2s; }
.qt-btn:hover { background: #e2e8f0; color: var(--c-primary); border-color: var(--c-primary); }

.filter-controls { background: #f8fafc; padding: 16px; border-radius: 8px; border: 1px solid #e2e8f0; display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-end; }
.filter-group { display: flex; flex-direction: column; gap: 6px; min-width: 150px; }
.filter-group label { font-size: 0.85rem; font-weight: 600; color: #475569; }
.filter-group select { padding: 8px; border-radius: 6px; border: 1px solid #cbd5e1; outline: none; background: #fff; }
.filter-checkboxes { flex-direction: row; flex-wrap: wrap; align-items: center; gap: 12px; }
.filter-checkboxes label { font-weight: normal; cursor: pointer; display: flex; align-items: center; gap: 4px; }
.filter-actions { margin-left: auto; }

.filter-results-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin-top: 16px; }
.fr-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; }

.deals-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 16px; }
.deal-card { background: #fff; border: 1px dashed #0ea5e9; border-radius: 8px; padding: 16px; text-align: center; }
.deal-header { display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 12px; }
.deal-discount { font-size: 1.25rem; font-weight: bold; color: #f59e0b; margin-bottom: 8px; }
.deal-code { background: #fef3c7; padding: 8px; border-radius: 4px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-family: monospace; font-size: 1.1rem; }
.btn-copy-code { background: #f59e0b; color: #fff; border: none; padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 0.75rem; }
.btn-copy-code:hover { background: #d97706; }
.btn-block { display: block; width: 100%; text-align: center; }
.btn-small { padding: 4px 10px; font-size: 0.8rem; }
@media (max-width: 767px) {
  .provider-header-cta { align-items: flex-start !important; margin-top: 10px; }
}
"""

if "Quick Buy & Filter" not in css:
    css += "\n" + new_css
with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 5. Update main.js for filtering and clipboard
js_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

filter_js = """
// Filter Logic
document.addEventListener('DOMContentLoaded', () => {
    const pSelect = document.getElementById('filter-payment');
    const bSelect = document.getElementById('filter-budget');
    const tSelect = document.getElementById('filter-traffic');
    const aiCheck = document.getElementById('filter-ai');
    const streamCheck = document.getElementById('filter-stream');
    const deviceCheck = document.getElementById('filter-device');
    const netCheck = document.getElementById('filter-network');
    const resContainer = document.getElementById('filter-results-container');
    const resInfo = document.getElementById('filter-results-info');
    
    function updateBudgetOptions() {
        if(!pSelect) return;
        const p = pSelect.value;
        bSelect.innerHTML = '<option value="all">不限</option>';
        if (p === 'monthly') {
            bSelect.innerHTML += '<option value="20">¥20以内</option><option value="30">¥30以内</option><option value="50">¥50以内</option><option value="100">¥100以内</option>';
        } else if (p === 'annual') {
            bSelect.innerHTML += '<option value="100">¥100以内</option><option value="200">¥200以内</option><option value="300">¥300以内</option><option value="500">¥500以内</option>';
        } else if (p === 'onetime') {
            bSelect.innerHTML += '<option value="100">¥100以内</option><option value="200">¥200以内</option><option value="400">¥400以内</option>';
        }
    }
    if(pSelect) {
        pSelect.addEventListener('change', () => { updateBudgetOptions(); runFilter(); });
        bSelect.addEventListener('change', runFilter);
        tSelect.addEventListener('change', runFilter);
        aiCheck.addEventListener('change', runFilter);
        streamCheck.addEventListener('change', runFilter);
        deviceCheck.addEventListener('change', runFilter);
        netCheck.addEventListener('change', runFilter);
        updateBudgetOptions();
        
        document.getElementById('btn-reset-filter').addEventListener('click', () => {
            pSelect.value = 'all'; updateBudgetOptions(); tSelect.value = 'all'; bSelect.value = 'all';
            aiCheck.checked = false; streamCheck.checked = false; deviceCheck.checked = false; netCheck.checked = false;
            runFilter();
        });
        
        // Quick tags
        document.querySelectorAll('.qt-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const f = e.target.getAttribute('data-filter');
                document.getElementById('plan-filter').scrollIntoView({behavior: 'smooth', block: 'start'});
                if(f === 'budget-20') { pSelect.value = 'monthly'; updateBudgetOptions(); bSelect.value = '20'; }
                if(f === 'budget-30') { pSelect.value = 'monthly'; updateBudgetOptions(); bSelect.value = '30'; }
                if(f === 'budget-year') { pSelect.value = 'annual'; updateBudgetOptions(); bSelect.value = '100'; }
                if(f === 'traffic-200') { tSelect.value = '100'; }
                if(f === 'traffic-500') { tSelect.value = '500'; }
                if(f === 'ai') { aiCheck.checked = true; }
                if(f === 'stream') { streamCheck.checked = true; }
                if(f === 'multidevice') { deviceCheck.checked = true; }
                if(f === 'onetime') { pSelect.value = 'onetime'; updateBudgetOptions(); }
                if(f === 'iplc') { netCheck.checked = true; }
                runFilter();
            });
        });
    }

    function runFilter() {
        if(!window.siteProviders) return;
        const pMode = pSelect.value;
        const budget = bSelect.value === 'all' ? 99999 : parseFloat(bSelect.value);
        const minT = tSelect.value === 'all' ? 0 : parseFloat(tSelect.value);
        
        const res = window.siteProviders.filter(p => {
            if (aiCheck.checked && p.aiSupport !== '支持 AI') return false;
            if (streamCheck.checked && p.streamingSupport !== '支持流媒体解锁') return false;
            if (deviceCheck.checked && p.clientSupport !== '不限设备/支持多端' && !p.features.some(f => f.includes('多设备') || f.includes('不限设备'))) return false;
            if (netCheck.checked && !p.network.includes('专线')) return false;
            
            let matchedPlan = false;
            if (p.plans && p.plans.length > 0) {
                for (let pl of p.plans) {
                    let tf = 0;
                    if(pl.traffic && pl.traffic.toUpperCase().includes('GB')) tf = parseFloat(pl.traffic);
                    else if(pl.traffic && pl.traffic.toUpperCase().includes('TB')) tf = parseFloat(pl.traffic) * 1000;
                    if(tf < minT && minT > 0 && !pl.traffic.includes('不限')) continue;
                    
                    if (pMode === 'monthly' || pMode === 'all') {
                        if (pl.monthly) {
                            let price = parseFloat(pl.monthly.replace(/[^0-9.]/g, ''));
                            if (price <= budget) matchedPlan = true;
                        }
                    }
                    if (pMode === 'annual' || pMode === 'all') {
                        if (pl.annual) {
                            let price = parseFloat(pl.annual.replace(/[^0-9.]/g, ''));
                            if (price <= budget) matchedPlan = true;
                        }
                    }
                    if (pMode === 'onetime' || pMode === 'all') {
                        if (pl.oneTime) {
                            let price = parseFloat(pl.oneTime.replace(/[^0-9.]/g, ''));
                            if (price <= budget) matchedPlan = true;
                        }
                    }
                }
            } else if (pMode === 'all' && minT === 0 && budget === 99999) {
                matchedPlan = true;
            }
            return matchedPlan;
        });

        if (res.length === 0) {
            resInfo.innerHTML = '暂时没有完全符合这些条件的套餐，可以适当放宽预算或流量要求。';
            resContainer.innerHTML = '';
        } else {
            resInfo.innerHTML = `找到 ${res.length} 个符合条件的品牌：`;
            resContainer.innerHTML = res.map(p => `
                <div class="fr-card">
                  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                    <img src="${p.logoSrc}" style="width:24px;border-radius:50%">
                    <strong style="font-size:1.1rem">${p.name}</strong>
                  </div>
                  <div style="font-size:0.9rem;color:#475569;margin-bottom:12px;">
                    <div>线路: ${p.network}</div>
                    <div style="margin-top:6px;">
                      ${p.tags.map(t=>`<span class="pill-badge">${t}</span>`).join('')}
                    </div>
                  </div>
                  <div style="display:flex;gap:8px;">
                    <a href="#provider-${p.slug}" class="btn btn-outline" style="flex:1;text-align:center;padding:6px;">查看详情</a>
                    <a href="${p.affUrl}" target="_blank" class="btn btn-primary" style="flex:1;text-align:center;padding:6px;">前往购买</a>
                  </div>
                </div>
            `).join('');
        }
    }
    
    // Copy code logic
    document.querySelectorAll('.btn-copy-code').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const code = e.target.getAttribute('data-code');
            navigator.clipboard.writeText(code).then(() => {
                const old = e.target.innerHTML;
                e.target.innerHTML = '复制成功 ✓';
                e.target.style.background = '#10b981';
                setTimeout(() => {
                    e.target.innerHTML = old;
                    e.target.style.background = '';
                }, 2000);
            }).catch(() => {
                alert('复制失败，请手动复制: ' + code);
            });
        });
    });
});
"""

if "Filter Logic" not in js:
    js += "\n" + filter_js
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
