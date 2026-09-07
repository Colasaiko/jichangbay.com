import re

# 1. Update EJS
file_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

comparison_replacement = r"""    <!-- Comparison Section -->
    <section id="comparison" class="section-block">
      <h2>品牌总对比表</h2>
      <div class="comparison-container">
        <!-- Desktop Table -->
        <div class="desktop-provider-table">
          <table class="comparison-table">
            <colgroup>
              <col class="col-brand">
              <col class="col-price">
              <col class="col-traffic">
              <col class="col-network">
              <col class="col-scene">
              <col class="col-highlights">
              <col class="col-detail">
            </colgroup>
            <thead>
              <tr>
                <th class="th-nowrap">品牌</th>
                <th class="th-nowrap">起步价格</th>
                <th class="th-nowrap">起步流量</th>
                <th class="th-nowrap">线路</th>
                <th class="th-nowrap">适合场景</th>
                <th class="th-nowrap">亮点标签</th>
                <th class="th-nowrap">详情</th>
              </tr>
            </thead>
            <tbody>
              <% 
                let providers = site.data.providers || [];
                const featuredOrder = ['微风网络', '飞猫云', '闪跃', '跨界云', '无忧链接', '灵猫', 'firefly'];
                providers = providers.slice().sort((a, b) => {
                  let idxA = featuredOrder.findIndex(name => name.toLowerCase() === a.name.toLowerCase());
                  let idxB = featuredOrder.findIndex(name => name.toLowerCase() === b.name.toLowerCase());
                  if(idxA === -1) idxA = 999;
                  if(idxB === -1) idxB = 999;
                  if(idxA !== idxB) return idxA - idxB;
                  return 0;
                });
              %>
              <% providers.forEach(function(p) { %>
                <% 
                  const firstPlan = p.plans && p.plans[0]; 
                  let startPrice = '-';
                  if (firstPlan) {
                    if (firstPlan.monthly) startPrice = firstPlan.monthly.replace('¥ ', '¥') + ' / 月';
                    else if (firstPlan.annual) startPrice = firstPlan.annual.replace('¥ ', '¥') + ' / 年';
                    else if (firstPlan.oneTime) startPrice = firstPlan.oneTime.replace('¥ ', '¥') + ' / 次';
                  }
                  
                  let startTraffic = (firstPlan ? firstPlan.traffic : '-') || '-';
                  if(startTraffic !== '-') {
                     startTraffic = startTraffic.replace(/([0-9]+)\s*(GB|TB)/i, '$1 $2').toUpperCase();
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
                  tags = tags.slice(0, 3);
                  
                  let bestForStr = Array.isArray(p.bestFor) ? p.bestFor.slice(0, 2).join(' / ') : '-';
                  if (!bestForStr || bestForStr === '') bestForStr = '-';
                  
                  const logoSrc = p.logo || ('https://ui-avatars.com/api/?name=' + encodeURIComponent(p.name) + '&background=0f172a&color=fff&rounded=true&bold=true');
                %>
                <tr>
                  <td class="brand-name">
                    <div class="brand-cell">
                      <img src="<%= logoSrc %>" alt="<%= p.name %>" class="table-logo">
                      <strong><%= p.name %></strong>
                    </div>
                  </td>
                  <td class="col-price"><%= startPrice %></td>
                  <td class="col-traffic"><%= startTraffic %></td>
                  <td class="col-network"><%= network %></td>
                  <td class="col-bestfor"><%= bestForStr %></td>
                  <td class="col-tags">
                    <% tags.forEach(function(t) { %>
                      <span class="pill-badge"><%= t %></span>
                    <% }) %>
                  </td>
                  <td class="col-action">
                    <a href="#provider-<%= p.slug %>" class="btn-detail">查看</a>
                  </td>
                </tr>
              <% }) %>
            </tbody>
          </table>
        </div>
        
        <!-- Mobile Cards -->
        <div class="mobile-provider-list">
          <% providers.forEach(function(p) { %>
            <% 
              const firstPlan = p.plans && p.plans[0]; 
              let startPrice = '-';
              if (firstPlan) {
                if (firstPlan.monthly) startPrice = firstPlan.monthly.replace('¥ ', '¥') + ' / 月';
                else if (firstPlan.annual) startPrice = firstPlan.annual.replace('¥ ', '¥') + ' / 年';
                else if (firstPlan.oneTime) startPrice = firstPlan.oneTime.replace('¥ ', '¥') + ' / 次';
              }
              
              let startTraffic = (firstPlan ? firstPlan.traffic : '-') || '-';
              if(startTraffic !== '-') {
                 startTraffic = startTraffic.replace(/([0-9]+)\s*(GB|TB)/i, '$1 $2').toUpperCase();
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
              tags = tags.slice(0, 3);
              
              let bestForStr = Array.isArray(p.bestFor) ? p.bestFor.slice(0, 2).join(' / ') : '-';
              if (!bestForStr || bestForStr === '') bestForStr = '-';
              const logoSrc = p.logo || ('https://ui-avatars.com/api/?name=' + encodeURIComponent(p.name) + '&background=0f172a&color=fff&rounded=true&bold=true');
            %>
            <div class="mobile-card">
              <div class="mc-header">
                <img src="<%= logoSrc %>" alt="<%= p.name %>" class="mc-logo">
                <strong class="mc-name"><%= p.name %></strong>
              </div>
              <div class="mc-body">
                <div class="mc-row">
                  <span class="mc-label">起步价格</span>
                  <span class="mc-value tabular"><%= startPrice %></span>
                </div>
                <div class="mc-row">
                  <span class="mc-label">起步流量</span>
                  <span class="mc-value tabular"><%= startTraffic %></span>
                </div>
                <div class="mc-row">
                  <span class="mc-label">线路</span>
                  <span class="mc-value"><%= network %></span>
                </div>
              </div>
              
              <% if (bestForStr !== '-') { %>
              <div class="mc-scene">
                <span class="mc-label-block">适合场景</span>
                <span class="mc-value-block"><%= bestForStr %></span>
              </div>
              <% } %>
              
              <div class="mc-tags">
                <% tags.forEach(function(t) { %>
                  <span class="pill-badge"><%= t %></span>
                <% }) %>
              </div>
              
              <div class="mc-action">
                <a href="#provider-<%= p.slug %>" class="mc-btn">查看详情 →</a>
              </div>
            </div>
          <% }) %>
        </div>
      </div>
    </section>"""

start_idx = html.find('<!-- Comparison Section -->')
end_idx = html.find('</section>', start_idx) + len('</section>')
html = html[:start_idx] + comparison_replacement + html[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)


# 2. Update CSS
css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = """/* --- COMPARISON TABLE OPTIMIZATIONS --- */
.comparison-container {
  width: 100%;
  max-width: 100%;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  background: #ffffff;
  overflow: hidden;
}

.desktop-provider-table {
  width: 100%;
  max-width: 100%;
  display: block;
}

.comparison-table {
  width: 100%;
  max-width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  text-align: left;
  font-size: 0.95rem;
}

.col-brand      { width: 18%; }
.col-price      { width: 14%; }
.col-traffic    { width: 11%; }
.col-network    { width: 12%; }
.col-scene      { width: 20%; }
.col-highlights { width: 17%; }
.col-detail     { width: 8%; }

.comparison-table th, 
.comparison-table td {
  box-sizing: border-box;
  vertical-align: middle;
  padding: 16px 12px;
  line-height: 1.5;
  border-bottom: 0;
  word-wrap: break-word;
}

.comparison-table tbody tr {
  border-bottom: 1px solid #e2e8f0;
}

.comparison-table th {
  background-color: #f8fafc;
  color: #475569;
  font-weight: 700;
  white-space: nowrap;
}

.comparison-table tbody tr:hover {
  background-color: #f1f5f9;
  transition: background-color 0.2s ease;
}

.brand-cell {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 34px;
}

.table-logo {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  object-fit: cover;
  flex: 0 0 auto;
}

.brand-cell strong {
  color: #0f172a;
  font-weight: 700;
  font-size: 1.05rem;
  line-height: 1.35;
}

.col-price, .col-traffic, .col-network {
  color: #334155;
  white-space: nowrap;
  font-variant-numeric: tabular-nums;
}

.col-scene {
  line-height: 1.55;
  color: #334155;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.col-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
}

.pill-badge {
  display: inline-flex;
  align-items: center;
  min-height: 24px;
  padding: 2px 8px;
  background-color: #e0f2fe;
  color: #0369a1;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  white-space: nowrap;
}

.col-action {
  text-align: right;
  white-space: nowrap;
}

.btn-detail {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 12px;
  background-color: #0891b2;
  color: #ffffff;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 500;
  transition: background-color 0.2s, transform 0.1s;
  white-space: nowrap;
}

.btn-detail:hover {
  background-color: #0e7490;
}

/* Mobile Cards */
.mobile-provider-list {
  display: none;
  padding: 16px;
  background-color: #f8fafc;
}

.mobile-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 16px;
}
.mobile-card:last-child {
  margin-bottom: 0;
}

.mc-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}
.mc-logo {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  flex: 0 0 auto;
}
.mc-name {
  font-size: 1.15rem;
  font-weight: 700;
  color: #0f172a;
}

.mc-body {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 14px;
}
.mc-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.mc-label {
  color: #64748b;
  font-size: 0.85rem;
}
.mc-value {
  color: #1e293b;
  font-size: 0.95rem;
  font-weight: 500;
}
.mc-value.tabular {
  font-variant-numeric: tabular-nums;
}

.mc-scene {
  margin-bottom: 14px;
}
.mc-label-block {
  display: block;
  color: #64748b;
  font-size: 0.85rem;
  margin-bottom: 4px;
}
.mc-value-block {
  display: block;
  color: #1e293b;
  font-size: 0.95rem;
  line-height: 1.5;
}

.mc-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}

.mc-action {
  text-align: right;
  border-top: 1px solid #f1f5f9;
  padding-top: 12px;
}
.mc-btn {
  display: inline-flex;
  align-items: center;
  color: #0891b2;
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none;
}
.mc-btn:hover {
  text-decoration: underline;
}

/* Media Query: < 1024px (Tablet & Mobile) */
@media (max-width: 1023px) {
  .desktop-provider-table {
    display: none;
  }
  .mobile-provider-list {
    display: block;
  }
  .comparison-container {
    background: transparent;
    box-shadow: none;
  }
}
/* --- END COMPARISON TABLE OPTIMIZATIONS --- */"""

start_idx = css.find('/* --- COMPARISON TABLE OPTIMIZATIONS --- */')
end_idx = css.find('/* --- END COMPARISON TABLE OPTIMIZATIONS --- */') + len('/* --- END COMPARISON TABLE OPTIMIZATIONS --- */')
css = css[:start_idx] + new_css + css[end_idx:]

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
