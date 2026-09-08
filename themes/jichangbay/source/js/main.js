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
