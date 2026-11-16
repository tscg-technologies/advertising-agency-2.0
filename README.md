# ADVERTISING AGENCY — Premium Multi-Page Demonstration Website

A bold, editorial, modern 30-page static website for a generic **ADVERTISING AGENCY**, showcasing creative campaigns, brand strategy, digital paid media, commercial video production, and conversion funnels.

Designed and engineered for static hosting on Hostinger or any modern static web server.

---

## 1. Project Overview & Identity Rules
- **Brand Identity:** Generic **ADVERTISING AGENCY** (Strictly no invented agency names, founders, or fake company histories).
- **Logo:** Abstract geometric SVG symbol with layered typography.
- **Contact Details:** Generic dummy details (Phone: `0000000000`, Email: `demo@example.com`, Address: `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000`).
- **Demo Verification:** All portfolio projects, dashboards, client listings, and career vacancies are clearly labeled as illustrative demonstrations.

---

## 2. Technology Stack
- **HTML5:** Semantic, accessible markup with Open Graph & Twitter Cards on every page.
- **CSS3:** Custom design system without external frameworks (No Bootstrap, Tailwind, or jQuery).
  - Modern dark editorial palette (`#0A0A0A`, `#141414`, `#1B1B1B`).
  - High-impact accents: `#FF5A36` (Coral Orange), `#D9FF43` (Acid Lime), `#A78BFA` (Violet).
  - Responsive across 360px, 390px, 768px, 1024px, 1440px, and 1920px.
- **Vanilla JavaScript (ES6+):**
  - Sticky navigation header with scroll detection.
  - Accessible mobile drawer menu with services accordion.
  - Interactive multi-step campaign enquiry wizard (6 steps with progress indicator & dynamic summary).
  - Portfolio category filtering with smooth transition animations.
  - Interactive FAQ accordion.
  - Interactive scope & pricing configurator.
  - Lightbox modal for campaign creative previews.
  - Form validation with simulated client-side feedback toasts.

---

## 3. Complete File Structure
```
advertising-agency/
│
├── index.html                     # Homepage (Hero collage, services, process, CTA)
├── about.html                     # Agency philosophy, strategy, mission, vision
├── services.html                  # Master hub for all 14 advertising disciplines
├── digital-advertising.html       # Multi-channel digital advertising & analytics
├── social-media-advertising.html  # Instagram, FB, LinkedIn ad creatives & mockups
├── google-ads.html                # Google Search, Display, Shopping & SERP mockup
├── meta-ads.html                  # Facebook & Instagram testing & lead forms
├── video-advertising.html         # Commercial brand films & demo video player
├── creative-design.html           # Master key visuals, banners & social art
├── brand-strategy.html            # Market positioning & brand messaging frameworks
├── graphic-design.html            # Packaging, identity systems & editorial print
├── content-marketing.html         # Content calendars & advertising copywriting
├── influencer-marketing.html      # Creator discovery & collaboration tiers
├── outdoor-advertising.html       # Highway hoardings & metropolitan LED mockups
├── print-advertising.html         # Editorial magazine spreads & luxury catalogues
├── seo-services.html              # Technical crawlability & search discoverability
├── lead-generation.html           # Full-funnel customer acquisition architecture
├── industries.html                # Dedicated strategies across 12 sectors
├── portfolio.html                 # Creative campaign archive with category filters
├── campaign-details.html          # Reusable campaign case study page
├── process.html                   # 5-step creative workflow & approvals guide
├── pricing.html                   # 3 structured packages & interactive scope estimator
├── technologies.html              # Tools, design suites, analytics & AI workflows
├── careers.html                   # Sample vacancies & frontend application demo
├── blog.html                      # 10 editorial advertising articles with search
├── faq.html                       # 8 categories of interactive questions
├── contact.html                   # Dummy studio details & validated contact form
├── start-campaign.html            # 6-step guided campaign enquiry wizard
├── privacy-policy.html            # Demonstration privacy terms & legal notice
├── terms-and-conditions.html      # Demonstration usage guidelines & disclaimer
│
├── assets/
│   ├── css/
│   │   ├── style.css              # Master tokens, typography, mockups, forms
│   │   ├── responsive.css         # Breakpoint handling (360px to 1920px)
│   │   └── animations.css         # Marquee, glow pulses, scroll reveals
│   │
│   ├── js/
│   │   ├── main.js                # Header, mobile drawer, scroll reveal, toasts
│   │   ├── interactions.js        # Accordion, 6-step form, video player, calc
│   │   └── portfolio.js           # Category filters, blog search, lightbox modal
│   │
│   ├── images/                    # [Location for Google Flow generated assets]
│   └── icons/                     # Inline SVG geometry and symbols
│
├── sitemap.xml                    # Complete XML sitemap (all 30 pages)
├── robots.txt                     # Crawler directives referencing sitemap
├── IMAGE-GENERATION-GUIDE.md      # Comprehensive Google Flow prompt manual
└── README.md                      # Documentation & deployment guide
```

---

## 4. How to Run Locally
1. Clone or copy the folder to your local computer.
2. Open any `.html` file (e.g. `index.html`) directly in any modern browser (Chrome, Edge, Firefox, Safari).
3. Alternatively, launch a local development server:
   ```bash
   # Using Python
   python -m http.server 8000
   # Then visit: http://localhost:8000
   ```

---

## 5. How to Deploy to Hostinger Static Hosting
1. Log into your **Hostinger hPanel**.
2. Navigate to **File Manager** under your domain.
3. Open the `public_html` directory.
4. Upload all files and the `assets/` directory directly into `public_html`.
5. Ensure `index.html`, `sitemap.xml`, and `robots.txt` are at the root of `public_html`.
6. Test your website on mobile and desktop browsers.

---

## 6. How to Replace Image Placeholders with Google Flow Assets
Every image placeholder in the website is structured with zero layout shift CSS and labeled with a specific future filename.
1. Refer to `IMAGE-GENERATION-GUIDE.md` for the exact prompt corresponding to each image number and filename.
2. Generate the image in **Google Flow** using the provided copy-ready prompt.
3. Save the generated asset in the exact recommended resolution (e.g. `1920x1080`, `1080x1350`, `1080x1080`) using the designated filename inside `assets/images/`.
4. In the respective HTML file, simply insert an `<img>` tag inside the placeholder container:
   ```html
   <div class="agency-placeholder aspect-16-9">
     <img src="assets/images/hero-advertising-campaign.webp" alt="Descriptive Campaign Visual">
   </div>
   ```
   The CSS automatically positions and sizes the image with `object-fit: cover` with zero cumulative layout shift.

---

## 7. How to Update Contact Information
To customize dummy contact details for commercial use:
1. Search across all HTML files for:
   - `0000000000` → Replace with your direct telephone number.
   - `demo@example.com` → Replace with your official enquiry email.
   - `Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000` → Replace with your studio address.
2. In `contact.html` and `start-campaign.html`, integrate your backend form endpoint (e.g. Formspree, Netlify Forms, or custom API).

---

## 8. Quality Assurance Checklist
- [x] All 30 HTML pages present and fully articulated.
- [x] All internal navigation links verified.
- [x] Dropdown navigation works seamlessly on desktop.
- [x] Responsive mobile hamburger drawer menu works smoothly.
- [x] Multi-step campaign enquiry form functions with step validation and review summary.
- [x] Portfolio category filter tabs function dynamically.
- [x] Blog search input and category tags filter in real-time.
- [x] Interactive FAQ accordions open and close with animated chevrons.
- [x] All image placeholders map 1:1 to `IMAGE-GENERATION-GUIDE.md`.
- [x] Valid `sitemap.xml` and `robots.txt` present.
- [x] No external framework dependencies; pure HTML5, CSS3, and Vanilla JS.
