import re

file_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update Quick Recommendations Section
quick_rec_replacement = """
    <!-- Recommendations Section -->
    <section id="recommendations" class="section-block">
      <h2>2026 精选整理与热门关注</h2>
      <p style="margin-bottom: 20px; color: #64748b;">以下是我们为您重点整理的部分热门品牌，您可以根据需求快速了解：</p>
      <div class="card-grid">
        <% 
          let providers_list = site.data.providers || [];
          const topFeatured = ['微风网络', '飞猫云', '闪跃'];
          topFeatured.forEach((featName, index) => {
            const p = providers_list.find(x => x.name.toLowerCase() === featName.toLowerCase());
            if (p) {
        %>
        <div class="card">
          <h3><%= index === 0 ? '优先浏览' : (index === 1 ? '热门关注' : '重点整理品牌') %></h3>
          <p><strong><%= p.name %></strong> - <%= (p.bestFor && p.bestFor.length) ? p.bestFor.slice(0, 3).join(' / ') : '提供多种套餐选择' %></p>
          <a href="#provider-<%= p.slug %>">查看 <%= p.name %></a>
        </div>
        <% } }) %>
      </div>
    </section>
"""

# Replace the whole recommendations block
html = re.sub(r'<!-- Recommendations Section -->.*?</section>', quick_rec_replacement.strip(), html, flags=re.DOTALL)

# Update Comparison Table Section
comparison_replacement = """
    <!-- Comparison Section -->
    <section id="comparison" class="section-block">
      <h2>品牌总对比表</h2>
      <div class="table-responsive">
        <table class="comparison-table">
          <thead>
            <tr>
              <th>品牌</th>
              <th>起步价格</th>
              <th>起步流量</th>
              <th>线路</th>
              <th>适合场景</th>
              <th>亮点标签</th>
              <th>详情</th>
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
                  if (firstPlan.monthly) startPrice = firstPlan.monthly + ' / 月';
                  else if (firstPlan.annual) startPrice = firstPlan.annual + ' / 年';
                  else if (firstPlan.oneTime) startPrice = firstPlan.oneTime + ' / 次';
                }
                const startTraffic = (firstPlan ? firstPlan.traffic : '-') || '-';
                
                // Determine network type
                let network = '优质专线';
                if (p.features && p.features.some(f => f.toUpperCase().includes('IPLC'))) network = 'IPLC 专线';
                else if (p.features && p.features.some(f => f.toUpperCase().includes('IEPL'))) network = 'IEPL 专线';
                else if (p.features && p.features.some(f => f.toUpperCase().includes('BGP'))) network = 'BGP 中转';
                
                // Determine tags
                let tags = [];
                if (p.aiSupport === '支持 AI') tags.push('AI支持');
                if (p.streamingSupport === '支持流媒体解锁') tags.push('流媒体');
                if (p.clientSupport === '不限设备/支持多端') tags.push('多设备');
                if (p.plans && p.plans.some(pl => pl.oneTime)) tags.push('不限时');
                if (tags.length === 0) tags.push('优质线路');
                tags = tags.slice(0, 3);
                
                let bestForStr = Array.isArray(p.bestFor) ? p.bestFor.slice(0, 2).join(' / ') : '-';
                if (!bestForStr || bestForStr === '') bestForStr = '-';
              %>
              <tr>
                <td class="brand-name">
                  <div class="brand-cell">
                    <img src="<%= p.logo || ('https://ui-avatars.com/api/?name=' + encodeURIComponent(p.name) + '&background=0f172a&color=fff&rounded=true&bold=true') %>" alt="<%= p.name %>" class="table-logo">
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
    </section>
"""

html = re.sub(r'<!-- Comparison Section -->.*?</section>', comparison_replacement.strip(), html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
