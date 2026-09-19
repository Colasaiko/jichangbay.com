document.addEventListener('DOMContentLoaded', () => {
  // Mobile drawer setup
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const mobileDrawer = document.getElementById('mobileDrawer');
  const drawerCloseBtn = document.querySelector('.drawer-close');
  const tocList = document.getElementById('toc-list');
  const mobileTocContent = document.getElementById('mobileTocContent');
  
  // Clone TOC for mobile
  if (tocList && mobileTocContent) {
    const clonedToc = tocList.cloneNode(true);
    clonedToc.id = 'mobile-toc-list';
    mobileTocContent.appendChild(clonedToc);
  }

  // Create overlay
  const overlay = document.createElement('div');
  overlay.className = 'drawer-overlay';
  document.body.appendChild(overlay);

  function openDrawer() {
    mobileDrawer.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    mobileDrawer.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', openDrawer);
  }
  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', closeDrawer);
  }
  overlay.addEventListener('click', closeDrawer);

  // Close drawer when clicking a mobile TOC link
  mobileTocContent.addEventListener('click', (e) => {
    if (e.target.tagName.toLowerCase() === 'a') {
      closeDrawer();
    }
  });

  // Progress Bar & TOC Highlighting
  const progressBar = document.getElementById('progress-bar');
  const sections = document.querySelectorAll('section[id]');
  const tocLinks = document.querySelectorAll('.toc-link');
  const mobileTocLinks = document.querySelectorAll('#mobile-toc-list .toc-link');

  function updateScroll() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    if (progressBar) {
      progressBar.style.width = scrolled + '%';
    }

    // Highlighting
    let currentId = '';
    // Use an offset to detect section
    const scrollPosition = winScroll + 100;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        currentId = section.getAttribute('id');
      }
    });

    if (currentId) {
      [tocLinks, mobileTocLinks].forEach(links => {
        links.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + currentId) {
            link.classList.add('active');
          }
        });
      });
    }
  }

  window.addEventListener('scroll', updateScroll);
  // Trigger once on load
  updateScroll();
});


  // Drawer TOC Logic
  const tocBtn = document.getElementById('floating-toc-btn');
  const overlay = document.getElementById('drawer-overlay');
  const tocArea = document.querySelector('.toc-area');
  const tocLinks = document.querySelectorAll('.toc-link, .back-to-top');

  function toggleDrawer() {
    tocArea.classList.toggle('drawer-open');
    overlay.classList.toggle('active');
    document.body.style.overflow = tocArea.classList.contains('drawer-open') ? 'hidden' : '';
  }

  function closeDrawer() {
    tocArea.classList.remove('drawer-open');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (tocBtn && overlay) {
    tocBtn.addEventListener('click', toggleDrawer);
    overlay.addEventListener('click', closeDrawer);
  }

  tocLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (window.innerWidth < 1500) {
        closeDrawer();
      }
    });
  });


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
    }

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
                        <img src="${p.logoSrc}" alt="${p.name}" width="24" height="24" loading="lazy" decoding="async" style="width:24px;border-radius:50%;object-fit:cover;">
                        <strong style="font-size:1.1rem">${p.name}</strong>
                      </div>
                      
                      <div style="background:#f8fafc; border-radius:6px; padding:10px; margin-bottom:12px; border:1px solid #e2e8f0;">
                          <div style="font-size:0.8rem; color:#334155; margin-bottom:4px;">匹配套餐：</div>
                          <div style="font-weight:600; color:var(--c-deep); font-size:1rem;">${p.matchedPlans[0].name}</div>
                          <div style="display:flex; justify-content:space-between; margin-top:4px; font-size:0.9rem;">
                             <span style="color:#0ea5e9; font-weight:600;">${p.matchedPlans[0].priceStr}</span>
                             <span style="color:#334155;">${p.matchedPlans[0].traffic}</span>
                          </div>
                          ${p.matchedPlans.length > 1 ? `<div style="font-size:0.8rem; color:#334155; margin-top:6px; border-top:1px dashed #cbd5e1; padding-top:6px;">另有 ${p.matchedPlans.length - 1} 个匹配套餐</div>` : ''}
                      </div>
    
                      <div style="font-size:0.9rem;color:#334155;margin-bottom:12px;">
                        <div>线路: ${p.network}</div>
                        <div style="margin-top:6px;">
                          ${p.tags.map(t=>`<span class="pill-badge">${t}</span>`).join('')}
                        </div>
                        ${(p.coupon && p.coupon !== '暂无优惠') ? `<div style="margin-top:8px; font-size:0.85rem; color:#f59e0b;">优惠码：${p.coupon} · ${p.couponDiscount || '优惠'}</div>` : ''}
                      </div>
                  </div>
                  <div style="display:flex;gap:8px; margin-top:auto;">
                    <a href="#provider-${p.slug}" class="btn btn-outline" style="flex:1;text-align:center;padding:6px;">查看详情</a>
                    <a href="${p.affUrl}" target="_blank" rel="nofollow noopener" class="btn btn-primary" style="flex:1;text-align:center;padding:6px;">前往购买</a>
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


// Add Comparison Toolbar logic
document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById('comp-search-input');
    const sortSelect = document.getElementById('comp-sort-select');
    const resetBtn = document.getElementById('comp-reset-btn');
    const clearBtn = document.getElementById('comp-clear-btn');
    const noResults = document.getElementById('comp-no-results');
    const compTbody = document.querySelector('.comparison-table tbody');
    const compMobList = document.querySelector('.mobile-provider-list');
    
    if(!searchInput || !compTbody) return;
    
    // Store original nodes to easily sort/filter them
    const originalTrs = Array.from(compTbody.querySelectorAll('.comp-tr'));
    const originalCards = compMobList ? Array.from(compMobList.querySelectorAll('.comp-card')) : [];
    
    function applyFilterAndSort() {
        const query = searchInput.value.toLowerCase().trim();
        const sortVal = sortSelect.value;
        
        let visibleCount = 0;
        
        const filterAndSortArray = (arr, container) => {
            // First filter
            let filtered = arr.filter(el => {
                const name = el.getAttribute('data-name') || '';
                return name.includes(query) || query === '';
            });
            visibleCount = filtered.length;
            
            // Then sort
            filtered.sort((a, b) => {
                if (sortVal === 'default') {
                    return parseInt(a.getAttribute('data-order')) - parseInt(b.getAttribute('data-order'));
                } else if (sortVal === 'price-asc') {
                    return parseFloat(a.getAttribute('data-price')) - parseFloat(b.getAttribute('data-price'));
                } else if (sortVal === 'traffic-asc') {
                    return parseFloat(a.getAttribute('data-traffic')) - parseFloat(b.getAttribute('data-traffic'));
                } else if (sortVal === 'traffic-desc') {
                    return parseFloat(b.getAttribute('data-traffic')) - parseFloat(a.getAttribute('data-traffic'));
                }
                return 0;
            });
            
            // Re-append
            container.innerHTML = '';
            filtered.forEach(el => container.appendChild(el));
        };
        
        filterAndSortArray(originalTrs, compTbody);
        if (compMobList) {
            filterAndSortArray(originalCards, compMobList);
        }
        
        if (visibleCount === 0) {
            compTbody.parentElement.parentElement.style.display = 'none'; // hide the desktop table container
            if(compMobList) compMobList.style.display = 'none';
            noResults.style.display = 'block';
        } else {
            compTbody.parentElement.parentElement.style.display = 'block';
            if(compMobList) compMobList.style.display = 'block';
            noResults.style.display = 'none';
        }
    }
    
    searchInput.addEventListener('input', applyFilterAndSort);
    sortSelect.addEventListener('change', applyFilterAndSort);
    
    const doReset = () => {
        searchInput.value = '';
        sortSelect.value = 'default';
        applyFilterAndSort();
    };
    
    resetBtn.addEventListener('click', doReset);
    if(clearBtn) clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        applyFilterAndSort();
    });
});
