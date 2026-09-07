import re

file_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(file_path, "r", encoding="utf-8") as f:
    css = f.read()

# Add new styles for the table
new_styles = """
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
  text-align: left;
  min-width: 800px; /* Force horizontal scroll on mobile */
  font-size: 0.95rem;
}

.comparison-table th, 
.comparison-table td {
  padding: 16px 12px;
  border-bottom: 1px solid #e2e8f0;
  vertical-align: middle;
}

.comparison-table th {
  background-color: #f8fafc;
  color: #475569;
  font-weight: 600;
  white-space: nowrap;
}

.comparison-table tbody tr:hover {
  background-color: #f1f5f9;
  transition: background-color 0.2s ease;
}

.brand-cell {
  display: flex;
  align-items: center;
  gap: 12px;
  white-space: nowrap;
}

.table-logo {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
  flex-shrink: 0;
}

.brand-cell strong {
  color: #0f172a;
  font-weight: 600;
  font-size: 1.05rem;
}

.col-price, .col-traffic, .col-network, .col-bestfor {
  color: #334155;
  white-space: nowrap;
}

.pill-badge {
  display: inline-block;
  background-color: #e0f2fe;
  color: #0369a1;
  padding: 4px 8px;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  margin: 2px;
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
  transform: translateY(-1px);
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

css += new_styles

with open(file_path, "w", encoding="utf-8") as f:
    f.write(css)
