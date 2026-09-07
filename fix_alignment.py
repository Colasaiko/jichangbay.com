import re

# 1. Update EJS to add colgroup
file_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace table opening and thead
table_replacement = """
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
"""

html = re.sub(r'<table class="comparison-table">.*?</thead>', table_replacement.strip(), html, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update CSS
css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Replace the previous table css block entirely
new_css = """
/* --- COMPARISON TABLE OPTIMIZATIONS --- */
.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  margin: 20px 0;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
  border-radius: 8px;
  background: #ffffff;
}

.table-responsive::-webkit-scrollbar {
  height: 6px;
}
.table-responsive::-webkit-scrollbar-thumb {
  background-color: #cbd5e1;
  border-radius: 10px;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  text-align: left;
  min-width: 900px;
  font-size: 0.95rem;
}

.col-brand      { width: 19%; }
.col-price      { width: 14%; }
.col-traffic    { width: 11%; }
.col-network    { width: 12%; }
.col-scene      { width: 19%; }
.col-highlights { width: 19%; }
.col-detail     { width: 6%; }

.comparison-table th, 
.comparison-table td {
  box-sizing: border-box;
  vertical-align: middle;
  padding: 18px 14px;
  line-height: 1.5;
  border-bottom: 0;
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
  min-height: 26px;
  padding: 3px 8px;
  background-color: #e0f2fe;
  color: #0369a1;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  white-space: nowrap;
}

.col-action {
  text-align: center;
  white-space: nowrap;
}

.btn-detail {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 16px;
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

@media (max-width: 768px) {
  .table-responsive::before {
    content: "← 左右滑动查看完整表格 →";
    display: block;
    text-align: center;
    font-size: 0.8rem;
    color: #64748b;
    padding: 8px 0;
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
  }
}
/* --- END COMPARISON TABLE OPTIMIZATIONS --- */
"""

css = re.sub(r'/\* --- COMPARISON TABLE OPTIMIZATIONS --- \*/.*/\* --- END COMPARISON TABLE OPTIMIZATIONS --- \*/', new_css.strip(), css, flags=re.DOTALL)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
