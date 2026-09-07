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
