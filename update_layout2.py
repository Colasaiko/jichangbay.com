import re

# 1. Edit style.css
css_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\css\style.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Change container max-width to 1500px
css = re.sub(r'\.container\s*\{\s*max-width:\s*1200px;', '.container {\n  max-width: 1500px;', css)

# Add Floating Button & Overlay styles, and Drawer logic
drawer_css = """
/* Drawer TOC & Floating Button */
.floating-toc-btn {
  display: none;
  position: fixed;
  right: 20px;
  bottom: 40px; /* Or top: 110px */
  background: var(--c-primary);
  color: #fff;
  border: none;
  padding: 10px 16px;
  border-radius: 999px;
  font-weight: 600;
  box-shadow: 0 4px 10px rgba(8, 145, 178, 0.3);
  z-index: 9998;
  cursor: pointer;
  align-items: center;
  gap: 6px;
}
.floating-toc-btn:hover {
  background: var(--c-primary-hover);
}

.drawer-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.5);
  z-index: 9999;
  backdrop-filter: blur(2px);
}
.drawer-overlay.active {
  display: block;
}

@media (max-width: 1499px) {
  .main-content {
    display: block;
  }
  
  .toc-area {
    position: fixed;
    top: 0;
    right: -320px;
    width: 280px;
    height: 100vh;
    background: #fff;
    z-index: 10000;
    box-shadow: -4px 0 15px rgba(0,0,0,0.1);
    transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 20px 10px;
    overflow-y: auto;
  }
  
  .toc-area.drawer-open {
    right: 0;
  }
  
  .floating-toc-btn {
    display: flex;
    top: 90px;
    bottom: auto;
  }
  
  /* Reset sticky TOC inside drawer */
  .sticky-toc {
    position: static;
    height: auto;
    overflow-y: visible;
  }
}
"""

if "Drawer TOC" not in css:
    css += "\n" + drawer_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 2. Edit EJS to add floating button and overlay
ejs_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\layout\index.ejs"
with open(ejs_path, "r", encoding="utf-8") as f:
    html = f.read()

btn_html = """
  <!-- Floating TOC Button and Overlay -->
  <button id="floating-toc-btn" class="floating-toc-btn">
    <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
    目录
  </button>
  <div id="drawer-overlay" class="drawer-overlay"></div>
  
  <!-- Desktop TOC -->
"""

if "floating-toc-btn" not in html:
    html = html.replace("<!-- Desktop TOC -->", btn_html)

with open(ejs_path, "w", encoding="utf-8") as f:
    f.write(html)

# 3. Update main.js
js_path = r"c:\Users\USER\Desktop\BLOG\jichangbay.com\themes\jichangbay\source\js\main.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

drawer_js = """
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
"""

if "Drawer TOC Logic" not in js:
    js += "\n" + drawer_js

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)
