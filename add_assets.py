import os

css_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """
/* Before Buy Section */
.bb-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-bottom: 32px; }
.bb-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(15,23,42,0.03); }
.bb-icon { font-size: 1.5rem; margin-bottom: 12px; }
.bb-title { font-size: 1.05rem; font-weight: 700; color: #0f172a; margin-top: 0; margin-bottom: 8px; }
.bb-desc { font-size: 0.9rem; color: #334155; margin: 0; line-height: 1.5; }
@media (max-width: 1024px) { .bb-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 600px) { .bb-grid { grid-template-columns: 1fr; } }

/* Comp Toolbar */
.comp-toolbar { display: flex; flex-wrap: wrap; gap: 16px; align-items: center; background: #f8fafc; padding: 16px; border-radius: 12px; border: 1px solid #e2e8f0; margin-bottom: 24px; }
.comp-search { flex: 1; min-width: 200px; display: flex; align-items: center; }
.comp-search input { width: 100%; padding: 10px 12px; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; color: #0f172a; font-size: 0.95rem; }
.comp-search input:focus { border-color: var(--c-primary); box-shadow: 0 0 0 2px rgba(8, 145, 178, 0.2); }
.comp-sort { display: flex; align-items: center; gap: 8px; }
.comp-sort select { padding: 8px 12px; border-radius: 8px; border: 1px solid #cbd5e1; outline: none; background: #fff; color: #0f172a; font-size: 0.95rem; }
.comp-no-results { padding: 24px; text-align: center; color: #334155; background: #f8fafc; border: 1px dashed #cbd5e1; border-radius: 8px; margin-bottom: 24px; }
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0; }

@media (max-width: 768px) {
  .comp-toolbar { flex-direction: column; align-items: stretch; }
  .comp-search { flex: none; width: 100%; }
  .comp-sort { justify-content: space-between; }
  .comp-toolbar button { width: 100%; }
}
"""

if '/* Before Buy Section */' not in css:
    css += '\n' + new_css
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

js_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\js\main.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

new_js = """
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
"""

if 'comp-search-input' not in js:
    js += '\n' + new_js
with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
