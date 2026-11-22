/**
 * ADVERTISING AGENCY — MAIN JAVASCRIPT
 * Header, Mobile Menu, Scroll Reveal, Back-To-Top, Toast Engine
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  initBackToTop();
  initScrollReveal();
  highlightActiveNav();
});

/** Sticky Navigation & Scroll Header */
function initStickyHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;

  const handleScroll = () => {
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll();
}

/** Mobile Drawer Navigation */
function initMobileMenu() {
  const toggleBtn = document.querySelector('.menu-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const backdrop = document.querySelector('.mobile-drawer-backdrop');
  const mobileServicesToggle = document.querySelector('.mobile-services-toggle');
  const mobileServicesList = document.querySelector('.mobile-services-accordion');

  if (!toggleBtn || !drawer) return;

  const openDrawer = () => {
    toggleBtn.classList.add('is-active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    drawer.classList.add('is-open');
    if (backdrop) backdrop.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  };

  const closeDrawer = () => {
    toggleBtn.classList.remove('is-active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    drawer.classList.remove('is-open');
    if (backdrop) backdrop.classList.remove('is-open');
    document.body.style.overflow = '';
  };

  toggleBtn.addEventListener('click', () => {
    const isOpen = drawer.classList.contains('is-open');
    if (isOpen) {
      closeDrawer();
    } else {
      openDrawer();
    }
  });

  if (backdrop) {
    backdrop.addEventListener('click', closeDrawer);
  }

  // Close drawer on ESC key
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('is-open')) {
      closeDrawer();
    }
  });

  // Expandable services sub-menu
  if (mobileServicesToggle && mobileServicesList) {
    mobileServicesToggle.addEventListener('click', (e) => {
      e.preventDefault();
      mobileServicesList.classList.toggle('is-open');
      const isExpanded = mobileServicesList.classList.contains('is-open');
      mobileServicesToggle.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
    });
  }
}

/** Back to Top Button */
function initBackToTop() {
  const btn = document.querySelector('.back-to-top-btn');
  if (!btn) return;

  btn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

/** Scroll Reveal with Intersection Observer */
function initScrollReveal() {
  const reveals = document.querySelectorAll('.reveal-on-scroll');
  if (!reveals.length) return;

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          obs.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -50px 0px',
      threshold: 0.1
    });

    reveals.forEach(el => observer.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('is-visible'));
  }
}

/** Active Nav Link Detection */
function highlightActiveNav() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-item a');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/** Global Demo Toast Notification Engine */
function showToast(message, duration = 4000) {
  let toast = document.querySelector('.toast-notification');
  if (!toast) {
    toast = document.createElement('div');
    toast.className = 'toast-notification';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D9FF43" stroke-width="2">
      <circle cx="12" cy="12" r="10"></circle>
      <polyline points="9 12 11 14 15 10"></polyline>
    </svg>
    <span>${message}</span>
  `;

  toast.classList.add('show');

  setTimeout(() => {
    toast.classList.remove('show');
  }, duration);
}
