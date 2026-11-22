/**
 * ADVERTISING AGENCY — PORTFOLIO & BLOG FILTER ENGINE
 */

document.addEventListener('DOMContentLoaded', () => {
  initPortfolioFilters();
  initBlogFilters();
  initCampaignLightbox();
});

/** Portfolio Category Filter */
function initPortfolioFilters() {
  const filterBtns = document.querySelectorAll('.portfolio-filter-bar .filter-btn');
  const portfolioItems = document.querySelectorAll('.portfolio-item');

  if (!filterBtns.length || !portfolioItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filterValue = btn.getAttribute('data-filter');

      portfolioItems.forEach(item => {
        const itemCategory = item.getAttribute('data-category');
        if (filterValue === 'all' || itemCategory === filterValue) {
          item.style.display = 'flex';
          setTimeout(() => {
            item.style.opacity = '1';
            item.style.transform = 'translateY(0)';
          }, 50);
        } else {
          item.style.opacity = '0';
          item.style.transform = 'translateY(10px)';
          setTimeout(() => {
            item.style.display = 'none';
          }, 300);
        }
      });
    });
  });
}

/** Blog Search & Category Filters */
function initBlogFilters() {
  const searchInput = document.getElementById('blog-search-input');
  const blogTags = document.querySelectorAll('.blog-filter-tag');
  const blogCards = document.querySelectorAll('.blog-card');

  if (!blogCards.length) return;

  let currentCategory = 'all';
  let searchTerm = '';

  const applyFilters = () => {
    blogCards.forEach(card => {
      const cardCategory = card.getAttribute('data-category') || '';
      const cardTitle = card.querySelector('.blog-title')?.textContent.toLowerCase() || '';
      const cardDesc = card.querySelector('.blog-excerpt')?.textContent.toLowerCase() || '';

      const matchesCat = (currentCategory === 'all' || cardCategory === currentCategory);
      const matchesSearch = (!searchTerm || cardTitle.includes(searchTerm) || cardDesc.includes(searchTerm));

      if (matchesCat && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  };

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchTerm = e.target.value.toLowerCase().trim();
      applyFilters();
    });
  }

  if (blogTags.length) {
    blogTags.forEach(tag => {
      tag.addEventListener('click', () => {
        blogTags.forEach(t => t.classList.remove('active'));
        tag.classList.add('active');
        currentCategory = tag.getAttribute('data-category') || 'all';
        applyFilters();
      });
    });
  }
}

/** Campaign Lightbox Modal */
function initCampaignLightbox() {
  const previewBtns = document.querySelectorAll('.btn-preview-campaign');
  if (!previewBtns.length) return;

  let modal = document.querySelector('.campaign-lightbox-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'campaign-lightbox-modal';
    modal.style.cssText = `
      position: fixed; inset: 0; background: rgba(0,0,0,0.85); backdrop-filter: blur(8px);
      z-index: 10000; display: none; align-items: center; justify-content: center; padding: 24px;
    `;
    modal.innerHTML = `
      <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; max-width: 800px; width: 100%; overflow: hidden; position: relative;">
        <button class="modal-close-btn" style="position: absolute; top: 16px; right: 16px; background: rgba(0,0,0,0.6); border: 1px solid var(--border-color); color: #FFF; width: 36px; height: 36px; border-radius: 50%; cursor: pointer; display: flex; align-items: center; justify-content: center; z-index: 10;">✕</button>
        <div class="modal-body" style="padding: 32px;"></div>
      </div>
    `;
    document.body.appendChild(modal);

    modal.querySelector('.modal-close-btn').addEventListener('click', () => {
      modal.style.display = 'none';
    });

    modal.addEventListener('click', (e) => {
      if (e.target === modal) modal.style.display = 'none';
    });
  }

  previewBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const parentCard = btn.closest('.portfolio-item') || btn.closest('.card');
      const title = parentCard?.querySelector('h3, h4')?.textContent || 'Illustrative Campaign Preview';
      const cat = parentCard?.querySelector('.portfolio-item-category')?.textContent || 'Creative Campaign';
      const placeholder = parentCard?.querySelector('.agency-placeholder');
      const img = placeholder?.querySelector('img');
      const imgSrc = img ? img.getAttribute('src') : '';
      const filename = imgSrc ? imgSrc.split('/').pop() : (placeholder?.querySelector('.placeholder-filename')?.textContent || 'campaign-preview.jpeg');

      const modalBody = modal.querySelector('.modal-body');
      modalBody.innerHTML = `
        <span class="badge badge-coral" style="margin-bottom: 12px;">${cat}</span>
        <h3 style="margin-bottom: 16px; font-family: var(--font-display);">${title}</h3>
        ${imgSrc ? `
        <div style="overflow: hidden; border-radius: 8px; margin-bottom: 20px; border: 1px solid var(--border-color); max-height: 440px; background: #0A0A0A;">
          <img src="${imgSrc}" alt="${title}" style="width: 100%; height: 100%; max-height: 440px; object-fit: contain; display: block; margin: 0 auto;">
        </div>` : `
        <div style="background: #141414; border: 1px dashed var(--border-color); border-radius: 8px; padding: 36px 20px; text-align: center; margin-bottom: 20px;">
          <div style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--accent-secondary); margin-bottom: 8px;">${filename}</div>
          <div style="font-size: 0.76rem; color: var(--text-muted); text-transform: uppercase;">Illustrative Demo Campaign Preview</div>
        </div>`}
        <p style="font-size: 0.92rem; color: var(--text-secondary); margin-bottom: 24px;">Commercial advertising concept demonstrating visual layout, lighting, color palette, and art direction engineered for high-impact social, digital, and outdoor media placement.</p>
        <a href="campaign-details.html" class="btn btn-primary" style="display: inline-block;">View Full Campaign Case Study</a>
      `;

      modal.style.display = 'flex';
    });
  });
}
