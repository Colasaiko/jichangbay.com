import re

ejs_path = r'c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs'
with open(ejs_path, 'r', encoding='utf-8') as f:
    html = f.read()

# First, fix the raw JS text I accidentally dumped into the HTML output.
html = re.sub(r'let numPrice = 999999;\s*if \(firstPlan\) \{.*?\s*\}\s*<tr class="comp-tr"', 
              r'<% let numPrice = 999999; if (firstPlan) { if (firstPlan.monthly) numPrice = parseFloat(firstPlan.monthly.replace(/[^0-9.]/g, \'\')) || 0; else if (firstPlan.annual) numPrice = parseFloat(firstPlan.annual.replace(/[^0-9.]/g, \'\')) || 0; else if (firstPlan.oneTime) numPrice = parseFloat(firstPlan.oneTime.replace(/[^0-9.]/g, \'\')) || 0; } let numTraffic = 0; if (startTraffic !== \'-\') { let tStr = startTraffic.toUpperCase(); let numT = parseFloat(tStr.replace(/[^0-9.]/g, \'\')) || 0; if (tStr.includes(\'TB\')) numT *= 1000; numTraffic = numT; } %>\n                <tr class="comp-tr"', html, flags=re.DOTALL)

html = re.sub(r'let numPrice = 999999;\s*if \(firstPlan\) \{.*?\s*\}\s*<div class="mobile-card comp-card"', 
              r'<% let numPrice = 999999; if (firstPlan) { if (firstPlan.monthly) numPrice = parseFloat(firstPlan.monthly.replace(/[^0-9.]/g, \'\')) || 0; else if (firstPlan.annual) numPrice = parseFloat(firstPlan.annual.replace(/[^0-9.]/g, \'\')) || 0; else if (firstPlan.oneTime) numPrice = parseFloat(firstPlan.oneTime.replace(/[^0-9.]/g, \'\')) || 0; } let numTraffic = 0; if (startTraffic !== \'-\') { let tStr = startTraffic.toUpperCase(); let numT = parseFloat(tStr.replace(/[^0-9.]/g, \'\')) || 0; if (tStr.includes(\'TB\')) numT *= 1000; numTraffic = numT; } %>\n          <div class="mobile-card comp-card"', html, flags=re.DOTALL)

with open(ejs_path, 'w', encoding='utf-8') as f:
    f.write(html)
