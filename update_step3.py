import os

js_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Update Quick Tags Reset and RunFilter mapping
# 100-200GB fix => maxT
replacement = """
        // Quick tags
        document.querySelectorAll('.qt-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const f = e.target.getAttribute('data-filter');
                document.getElementById('plan-filter').scrollIntoView({behavior: 'smooth', block: 'start'});
                
                // Reset all first
                pSelect.value = 'all'; 
                bSelect.innerHTML = '<option value="all">不限</option>';
                bSelect.value = 'all'; 
                tSelect.value = 'all';
                aiCheck.checked = false; streamCheck.checked = false; deviceCheck.checked = false; netCheck.checked = false;
                
                // Apply specific filter
                if(f === 'budget-20') { pSelect.value = 'monthly'; updateBudgetOptions(); bSelect.value = '20'; }
                if(f === 'budget-30') { pSelect.value = 'monthly'; updateBudgetOptions(); bSelect.value = '30'; }
                if(f === 'budget-year') { pSelect.value = 'annual'; updateBudgetOptions(); bSelect.value = '100'; }
                if(f === 'traffic-200') { tSelect.value = '100-200'; }
                if(f === 'traffic-500') { tSelect.value = '500'; }
                if(f === 'ai') { aiCheck.checked = true; }
                if(f === 'stream') { streamCheck.checked = true; }
                if(f === 'multidevice') { deviceCheck.checked = true; }
                if(f === 'onetime') { pSelect.value = 'onetime'; updateBudgetOptions(); }
                if(f === 'iplc') { netCheck.checked = true; }
                
                runFilter();
            });
        });
"""

# Find old quick tags logic and replace
start_token = "// Quick tags\n        document.querySelectorAll('.qt-btn')"
end_token = "});\n        });"

parts = js.split(start_token)
if len(parts) > 1:
    end_idx = parts[1].find(end_token)
    if end_idx != -1:
        js = parts[0] + replacement.strip() + parts[1][end_idx + len(end_token):]

# Now fix the traffic select options in index_html (I'll do that in another python script or just inject it here)
# Wait, I should also update runFilter logic in main.js!

run_filter_replacement = """
    function runFilter() {
        if(!window.siteProviders) return;
        const pMode = pSelect.value;
        const budget = bSelect.value === 'all' ? 99999 : parseFloat(bSelect.value);
        let minT = 0, maxT = 999999;
        if(tSelect.value !== 'all') {
            if(tSelect.value === '100-200') { minT = 100; maxT = 200; }
            else { minT = parseFloat(tSelect.value); }
        }
        
        const res = window.siteProviders.map(p => {
            if (aiCheck.checked && p.aiSupport !== '支持 AI') return null;
            if (streamCheck.checked && p.streamingSupport !== '支持流媒体解锁') return null;
            if (deviceCheck.checked && p.clientSupport !== '不限设备/支持多端' && !p.features.some(f => f.includes('多设备') || f.includes('不限设备'))) return null;
            if (netCheck.checked && !p.network.includes('专线')) return null;
            
            let matchedPlans = [];
            if (p.plans && p.plans.length > 0) {
                for (let pl of p.plans) {
                    let tf = 0;
                    if(pl.traffic && pl.traffic.toUpperCase().includes('GB')) tf = parseFloat(pl.traffic);
                    else if(pl.traffic && pl.traffic.toUpperCase().includes('TB')) tf = parseFloat(pl.traffic) * 1000;
                    if(minT > 0 && !pl.traffic.includes('不限')) {
                        if(tf < minT || tf > maxT) continue;
                    }
                    
                    let planPrice = 99999, planPriceStr = '';
                    if (pMode === 'monthly' || pMode === 'all') {
                        if (pl.monthly) {
                            let price = parseFloat(pl.monthly.replace(/[^0-9.]/g, ''));
                            if (price <= budget) {
                                if (price < planPrice) { planPrice = price; planPriceStr = pl.monthly + '/月'; }
                            }
                        }
                    }
                    if (pMode === 'annual' || pMode === 'all') {
                        if (pl.annual) {
                            let price = parseFloat(pl.annual.replace(/[^0-9.]/g, ''));
                            if (price <= budget) {
                                if (price < planPrice) { planPrice = price; planPriceStr = pl.annual + '/年'; }
                            }
                        }
                    }
                    if (pMode === 'onetime' || pMode === 'all') {
                        if (pl.oneTime) {
                            let price = parseFloat(pl.oneTime.replace(/[^0-9.]/g, ''));
                            if (price <= budget) {
                                if (price < planPrice) { planPrice = price; planPriceStr = pl.oneTime + '/次'; }
                            }
                        }
                    }
                    if(planPriceStr !== '') {
                         matchedPlans.push({ name: pl.name, traffic: pl.traffic, priceStr: planPriceStr, priceVal: planPrice });
                    }
                }
            } else if (pMode === 'all' && minT === 0 && budget === 99999) {
                 matchedPlans.push({ name: '基础套餐', traffic: p.tags[1] || '以官网为准', priceStr: '以官网为准', priceVal: 999 });
            }
            
            if (matchedPlans.length > 0) {
                // sort matched plans by price
                matchedPlans.sort((a,b) => a.priceVal - b.priceVal);
                return { ...p, matchedPlans };
            }
            return null;
        }).filter(p => p !== null);

        if (res.length === 0) {
            resInfo.innerHTML = '暂时没有完全符合这些条件的套餐，可以适当放宽预算或流量要求。';
            resContainer.innerHTML = '';
        } else {
            resInfo.innerHTML = `找到 ${res.length} 个符合条件的品牌：`;
            resContainer.innerHTML = res.map(p => `
                <div class="fr-card" style="display:flex; flex-direction:column; justify-content:space-between; height:100%;">
                  <div>
                      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                        <img src="${p.logoSrc}" style="width:24px;border-radius:50%">
                        <strong style="font-size:1.1rem">${p.name}</strong>
                      </div>
                      
                      <div style="background:#f8fafc; border-radius:6px; padding:10px; margin-bottom:12px; border:1px solid #e2e8f0;">
                          <div style="font-size:0.8rem; color:#64748b; margin-bottom:4px;">匹配套餐：</div>
                          <div style="font-weight:600; color:var(--c-deep); font-size:1rem;">${p.matchedPlans[0].name}</div>
                          <div style="display:flex; justify-content:space-between; margin-top:4px; font-size:0.9rem;">
                             <span style="color:#0ea5e9; font-weight:600;">${p.matchedPlans[0].priceStr}</span>
                             <span style="color:#475569;">${p.matchedPlans[0].traffic}</span>
                          </div>
                          ${p.matchedPlans.length > 1 ? `<div style="font-size:0.8rem; color:#94a3b8; margin-top:6px; border-top:1px dashed #cbd5e1; padding-top:6px;">另有 ${p.matchedPlans.length - 1} 个匹配套餐</div>` : ''}
                      </div>
    
                      <div style="font-size:0.9rem;color:#475569;margin-bottom:12px;">
                        <div>线路: ${p.network}</div>
                        <div style="margin-top:6px;">
                          ${p.tags.map(t=>`<span class="pill-badge">${t}</span>`).join('')}
                        </div>
                        ${(p.coupon && p.coupon !== '暂无优惠') ? `<div style="margin-top:8px; font-size:0.85rem; color:#f59e0b;">优惠码：${p.coupon} · ${p.couponDiscount || '优惠'}</div>` : ''}
                      </div>
                  </div>
                  <div style="display:flex;gap:8px; margin-top:auto;">
                    <a href="#provider-${p.slug}" class="btn btn-outline" style="flex:1;text-align:center;padding:6px;">查看详情</a>
                    <a href="${p.affUrl}" target="_blank" class="btn btn-primary" style="flex:1;text-align:center;padding:6px;">前往购买</a>
                  </div>
                </div>
            `).join('');
        }
    }
"""

start_token_filter = "function runFilter() {"
end_token_filter = "    // Copy code logic"
parts_filter = js.split(start_token_filter)
if len(parts_filter) > 1:
    end_idx_filter = parts_filter[1].find(end_token_filter)
    if end_idx_filter != -1:
        js = parts_filter[0] + run_filter_replacement.strip() + '\n\n' + end_token_filter + parts_filter[1][end_idx_filter + len(end_token_filter):]

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
