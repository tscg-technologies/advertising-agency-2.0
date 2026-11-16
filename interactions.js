/**
 * ADVERTISING AGENCY — INTERACTIONS JAVASCRIPT
 * Accordions, Multi-Step Campaign Wizard, Form Validations, Demo Video Player
 */

document.addEventListener('DOMContentLoaded', () => {
  initAccordions();
  initMultiStepForm();
  initContactForm();
  initCareersForm();
  initDemoVideoPlayer();
  initScopeEstimator();
});

/** FAQ Accordion */
function initAccordions() {
  const accordionItems = document.querySelectorAll('.accordion-item');
  if (!accordionItems.length) return;

  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    const content = item.querySelector('.accordion-content');
    if (!header || !content) return;

    header.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      // Close all other accordions in this parent list
      const parent = item.closest('.faq-accordion');
      if (parent) {
        parent.querySelectorAll('.accordion-item').forEach(otherItem => {
          if (otherItem !== item) {
            otherItem.classList.remove('is-open');
            const otherContent = otherItem.querySelector('.accordion-content');
            if (otherContent) otherContent.style.maxHeight = null;
          }
        });
      }

      if (isOpen) {
        item.classList.remove('is-open');
        content.style.maxHeight = null;
      } else {
        item.classList.add('is-open');
        content.style.maxHeight = content.scrollHeight + 'px';
      }
    });
  });
}

/** Multi-Step Campaign Enquiry Form (start-campaign.html) */
function initMultiStepForm() {
  const form = document.getElementById('multistep-campaign-form');
  if (!form) return;

  let currentStep = 1;
  const totalSteps = 6;
  const steps = form.querySelectorAll('.form-step');
  const nodes = form.querySelectorAll('.step-node');
  const progressBar = document.querySelector('.step-indicator-progress');
  const nextBtns = form.querySelectorAll('.btn-step-next');
  const prevBtns = form.querySelectorAll('.btn-step-prev');
  const submitBtn = form.querySelector('.btn-step-submit');
  const summaryBox = document.getElementById('campaign-review-summary');
  const successCard = document.getElementById('campaign-demo-success');

  const updateStepView = (stepNum) => {
    steps.forEach((step, idx) => {
      if (idx + 1 === stepNum) {
        step.classList.add('active');
      } else {
        step.classList.remove('active');
      }
    });

    nodes.forEach((node, idx) => {
      const nodeStep = idx + 1;
      if (nodeStep === stepNum) {
        node.classList.add('active');
        node.classList.remove('completed');
      } else if (nodeStep < stepNum) {
        node.classList.add('completed');
        node.classList.remove('active');
      } else {
        node.classList.remove('active', 'completed');
      }
    });

    if (progressBar) {
      const progressPercent = ((stepNum - 1) / (totalSteps - 1)) * 100;
      progressBar.style.width = progressPercent + '%';
    }

    // Populate review summary at step 6
    if (stepNum === 6 && summaryBox) {
      renderSummary();
    }

    window.scrollTo({
      top: form.offsetTop - 120,
      behavior: 'smooth'
    });
  };

  const validateStep = (stepNum) => {
    const currentStepEl = form.querySelector(`.form-step[data-step="${stepNum}"]`);
    if (!currentStepEl) return true;

    const requiredInputs = currentStepEl.querySelectorAll('[required]');
    let isValid = true;

    requiredInputs.forEach(input => {
      if (input.type === 'checkbox' || input.type === 'radio') {
        const groupName = input.name;
        const checkedOne = currentStepEl.querySelector(`[name="${groupName}"]:checked`);
        if (!checkedOne) {
          isValid = false;
        }
      } else {
        if (!input.value.trim()) {
          isValid = false;
          input.style.borderColor = '#FF5A36';
        } else {
          input.style.borderColor = '';
        }
      }
    });

    if (!isValid) {
      alert('Please fill out the required fields in this step to proceed.');
    }

    return isValid;
  };

  const renderSummary = () => {
    const name = form.querySelector('[name="client_name"]')?.value || 'Not provided';
    const business = form.querySelector('[name="business_name"]')?.value || 'Not provided';
    const email = form.querySelector('[name="client_email"]')?.value || 'Not provided';
    const phone = form.querySelector('[name="client_phone"]')?.value || 'Not provided';
    const industry = form.querySelector('[name="industry"]')?.value || 'Not selected';
    const objective = form.querySelector('[name="objective"]')?.value || 'Not specified';
    
    // Services selected
    const checkedServices = [];
    form.querySelectorAll('[name="services"]:checked').forEach(cb => checkedServices.push(cb.value));
    const servicesText = checkedServices.length > 0 ? checkedServices.join(', ') : 'None selected';

    const adBudget = form.querySelector('[name="ad_budget"]')?.value || 'Not specified';
    const launchTimeline = form.querySelector('[name="launch_timeline"]')?.value || 'Flexible';
    const notes = form.querySelector('[name="campaign_notes"]')?.value || 'None provided';

    summaryBox.innerHTML = `
      <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border-color); border-radius: 8px; padding: 24px; display: flex; flex-direction: column; gap: 14px;">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px;">
          <span style="color: var(--text-muted); font-size: 0.85rem;">Client & Business:</span>
          <strong style="color: #FFF; font-size: 0.9rem;">${name} (${business})</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px;">
          <span style="color: var(--text-muted); font-size: 0.85rem;">Contact:</span>
          <strong style="color: #FFF; font-size: 0.9rem;">${email} | ${phone}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px;">
          <span style="color: var(--text-muted); font-size: 0.85rem;">Industry & Goal:</span>
          <strong style="color: #FFF; font-size: 0.9rem;">${industry} — ${objective}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px;">
          <span style="color: var(--text-muted); font-size: 0.85rem;">Selected Services:</span>
          <strong style="color: var(--accent-secondary); font-size: 0.9rem;">${servicesText}</strong>
        </div>
        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); padding-bottom: 8px;">
          <span style="color: var(--text-muted); font-size: 0.85rem;">Budget & Timeline:</span>
          <strong style="color: #FFF; font-size: 0.9rem;">${adBudget} | Launch: ${launchTimeline}</strong>
        </div>
        <div>
          <span style="color: var(--text-muted); font-size: 0.85rem;">Campaign Brief:</span>
          <p style="font-size: 0.9rem; color: var(--text-secondary); margin-top: 4px;">${notes}</p>
        </div>
      </div>
    `;
  };

  nextBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (validateStep(currentStep)) {
        if (currentStep < totalSteps) {
          currentStep++;
          updateStepView(currentStep);
        }
      }
    });
  });

  prevBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (currentStep > 1) {
        currentStep--;
        updateStepView(currentStep);
      }
    });
  });

  if (submitBtn) {
    submitBtn.addEventListener('click', (e) => {
      e.preventDefault();
      // Client-side demonstration only - no data transmitted
      if (successCard) {
        form.style.display = 'none';
        successCard.style.display = 'block';
      }
      if (typeof showToast === 'function') {
        showToast('Demo Campaign Enquiry Submitted Successfully! (No data stored)');
      }
    });
  }
}

/** Contact Form Validation & Simulated Submission */
function initContactForm() {
  const contactForm = document.getElementById('agency-contact-form');
  if (!contactForm) return;

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = contactForm.querySelector('[name="name"]')?.value;
    const email = contactForm.querySelector('[name="email"]')?.value;

    if (!name || !email) {
      alert('Please fill out your name and email address.');
      return;
    }

    const submitBtn = contactForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Submitting Demo...';
    submitBtn.disabled = true;

    setTimeout(() => {
      contactForm.reset();
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
      if (typeof showToast === 'function') {
        showToast('Enquiry received! This is a frontend demo — no data was transmitted.');
      }
    }, 800);
  });
}

/** Careers Form Validation & Simulated Submission */
function initCareersForm() {
  const form = document.getElementById('careers-application-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = form.querySelector('[name="applicant_name"]')?.value;
    if (!name) {
      alert('Please enter your full name.');
      return;
    }

    form.reset();
    if (typeof showToast === 'function') {
      showToast('Application demo received! Fictional posting — no data saved.');
    }
  });
}

/** Interactive Demo Video Player */
function initDemoVideoPlayer() {
  const playButtons = document.querySelectorAll('.video-play-btn');
  playButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const container = btn.closest('.video-player-container');
      if (!container) return;

      const isPlaying = container.classList.contains('is-playing');
      if (isPlaying) {
        container.classList.remove('is-playing');
        btn.innerHTML = `<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>`;
        if (typeof showToast === 'function') {
          showToast('Demo video paused.');
        }
      } else {
        container.classList.add('is-playing');
        btn.innerHTML = `<svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>`;
        if (typeof showToast === 'function') {
          showToast('Playing illustrative demo video reel.');
        }
      }
    });
  });
}

/** Interactive Scope & Pricing Estimator (pricing.html) */
function initScopeEstimator() {
  const estimator = document.getElementById('pricing-scope-estimator');
  if (!estimator) return;

  const platformsCheckboxes = estimator.querySelectorAll('.platform-calc-check');
  const videoSlider = estimator.getElementById?.('slider-video-count') || estimator.querySelector('#slider-video-count');
  const creativeSlider = estimator.getElementById?.('slider-creatives-count') || estimator.querySelector('#slider-creatives-count');
  const durationSelect = estimator.querySelector('#select-duration');
  
  const estimatedScopeLabel = estimator.querySelector('#calc-scope-summary');

  const recalculate = () => {
    let platformCount = 0;
    platformsCheckboxes.forEach(cb => {
      if (cb.checked) platformCount++;
    });

    const videos = videoSlider ? parseInt(videoSlider.value, 10) : 2;
    const creatives = creativeSlider ? parseInt(creativeSlider.value, 10) : 12;
    const duration = durationSelect ? durationSelect.value : 'Monthly Retainer';

    const videoValDisplay = estimator.querySelector('#val-video-count');
    const creativeValDisplay = estimator.querySelector('#val-creatives-count');

    if (videoValDisplay && videoSlider) videoValDisplay.textContent = videoSlider.value + ' Videos';
    if (creativeValDisplay && creativeSlider) creativeValDisplay.textContent = creativeSlider.value + ' Assets';

    if (estimatedScopeLabel) {
      estimatedScopeLabel.textContent = `${platformCount} Platforms | ${creatives} Creatives/mo | ${videos} Videos/mo | ${duration}`;
    }
  };

  platformsCheckboxes.forEach(cb => cb.addEventListener('change', recalculate));
  if (videoSlider) videoSlider.addEventListener('input', recalculate);
  if (creativeSlider) creativeSlider.addEventListener('input', recalculate);
  if (durationSelect) durationSelect.addEventListener('change', recalculate);

  recalculate();
}
