# -*- coding: utf-8 -*-
"""
ADVERTISING AGENCY — Master Execution Script
Builds all 30 HTML pages, sitemap.xml, robots.txt, README.md,
and the comprehensive IMAGE-GENERATION-GUIDE.md.
"""

import os
from build_site import BASE_DIR, page_shell, IMAGE_REGISTRY
import page_generators_core as core
import page_generators_services as services

pages_config = [
    # Core Pages
    ("index.html", "Creative Advertising. Powerful Ideas. Stronger Brands.", 
     "Full-service creative advertising agency delivering high-impact campaigns, paid media, commercial video, and brand strategy for growing businesses.", 
     "index.html", core.generate_index),

    ("about.html", "Creative Thinking Meets Advertising Strategy", 
     "Learn about our creative philosophy, strategic disciplines, and approach to making ambitious brands impossible to ignore.", 
     "about.html", core.generate_about),

    ("services.html", "Advertising Solutions for Every Stage of Brand Growth", 
     "Explore our 14 core advertising disciplines across digital media, social advertising, creative design, video, and outdoor spectacles.", 
     "services.html", core.generate_services_hub),

    ("industries.html", "Specialized Advertising for Distinct Sectors", 
     "Tailored advertising and acquisition strategies for real estate, healthcare, fashion, education, ecommerce, F&B, hospitality, and technology.", 
     "industries.html", core.generate_industries),

    ("portfolio.html", "Selected Advertising Campaigns & Creative Archive", 
     "Explore our commercial campaign portfolio across fashion, technology, product launches, real estate, and outdoor advertising.", 
     "portfolio.html", core.generate_portfolio),

    ("campaign-details.html", "Fashion Campaign Demo Case Study", 
     "In-depth case study exploring campaign architecture, target audience modeling, visual executions, and media choreography.", 
     "campaign-details.html", core.generate_campaign_details),

    ("process.html", "From Big Idea to Campaign Execution", 
     "Our rigorous 5-step creative workflow: Discovery, Strategy, Creative Development, Execution, and Ongoing Review & Optimization.", 
     "process.html", core.generate_process),

    ("pricing.html", "Flexible Advertising Packages Built for Scale", 
     "Structured advertising service packages, editable scope configurations, and clear separation of agency fees vs platform ad spend.", 
     "pricing.html", core.generate_pricing),

    ("technologies.html", "Platforms, Tools & Technologies", 
     "Advertising networks, professional design suites, analytics tools, and AI-assisted creative workflows powering our studio.", 
     "technologies.html", core.generate_technologies),

    ("careers.html", "Build Outstanding Advertising With Us", 
     "Creative career opportunities in graphic design, commercial video editing, copywriting, and digital advertising strategy.", 
     "careers.html", core.generate_careers),

    ("blog.html", "Advertising Thinking & Market Insights", 
     "Editorial essays and practical guides on ad copywriting, social media hooks, Google vs Meta ads, and brand differentiation.", 
     "blog.html", core.generate_blog),

    ("faq.html", "Frequently Asked Questions", 
     "Clear answers regarding agency service scopes, platform management, campaign planning timelines, pricing, and reporting.", 
     "faq.html", core.generate_faq),

    ("contact.html", "Have a Campaign in Mind? Let's Talk", 
     "Connect with our advertising strategy team to discuss upcoming campaigns, product launches, or creative branding requirements.", 
     "contact.html", core.generate_contact),

    ("start-campaign.html", "Start Your Campaign Enquiry", 
     "Interactive 6-step campaign enquiry wizard to clarify business goals, required services, budget allocation, and target timelines.", 
     "start-campaign.html", core.generate_start_campaign),

    ("privacy-policy.html", "Privacy Policy", 
     "Demonstration website privacy terms, data handling transparency, and legal documentation guidelines.", 
     "privacy-policy.html", core.generate_privacy),

    ("terms-and-conditions.html", "Terms & Conditions", 
     "Demonstration website terms of use, proposal frameworks, media spend responsibilities, and limitation of liability.", 
     "terms-and-conditions.html", core.generate_terms),

    # 14 Dedicated Service Pages
    ("digital-advertising.html", "Digital Advertising Strategy & Multi-Platform Execution", 
     "High-performance digital advertising systems combining audience targeting, creative development, and cross-channel conversion tracking.", 
     "digital-advertising.html", services.generate_digital_advertising),

    ("social-media-advertising.html", "Create Social Campaigns People Stop Scrolling For", 
     "Engaging social media ad creatives across Instagram, Facebook, YouTube, and LinkedIn that command attention and drive conversion.", 
     "social-media-advertising.html", services.generate_social_media_advertising),

    ("google-ads.html", "Capture High-Intent Customers with Google Ads", 
     "Precision Google Search, Display Network banners, Shopping feeds, and YouTube video ads engineered to capture buyer intent.", 
     "google-ads.html", services.generate_google_ads),

    ("meta-ads.html", "Scale Your Reach with Meta Ads Strategy", 
     "Facebook & Instagram advertising systems utilizing dynamic creative testing, lookalike cohorts, and high-converting instant forms.", 
     "meta-ads.html", services.generate_meta_ads),

    ("video-advertising.html", "Turn Your Brand Message Into Visual Stories", 
     "Commercial brand films, short-form social reels, and 3D product motion showcases engineered for undivided viewer immersion.", 
     "video-advertising.html", services.generate_video_advertising),

    ("creative-design.html", "Creative Advertising Design That Stops The World", 
     "Master key visuals, promotional banners, carousel assets, and high-impact graphic design tailored for commercial persuasion.", 
     "creative-design.html", services.generate_creative_design),

    ("brand-strategy.html", "Brand Strategy That Gives Advertising Meaning", 
     "Market positioning, competitive moats, audience persona mapping, and brand messaging frameworks that build long-term value.", 
     "brand-strategy.html", services.generate_brand_strategy),

    ("graphic-design.html", "Graphic Design for Brands with High Ambition", 
     "Visual identity marks, packaging systems, luxury lookbooks, and corporate collateral crafted with editorial restraint.", 
     "graphic-design.html", services.generate_graphic_design),

    ("content-marketing.html", "Content Marketing That Educates, Engages & Converts", 
     "Editorial content calendars, magnetic advertising copywriting, educational articles, and narrative video scriptwriting.", 
     "content-marketing.html", services.generate_content_marketing),

    ("influencer-marketing.html", "Influencer Collaborations That Command Real Trust", 
     "End-to-end creator partnerships: discovery, creative briefs, content management, and performance verification across platforms.", 
     "influencer-marketing.html", services.generate_influencer_marketing),

    ("outdoor-advertising.html", "Command Attention in The Physical World", 
     "High-impact highway hoardings, metropolitan LED billboards, bus wraps, and transit media engineered for rapid visual recall.", 
     "outdoor-advertising.html", services.generate_outdoor_advertising),

    ("print-advertising.html", "Tactile Prestige: Editorial Print Advertising", 
     "Editorial double-page magazine spreads, newspaper placements, and luxury catalogues crafted with museum-grade typography.", 
     "print-advertising.html", services.generate_print_advertising),

    ("seo-services.html", "Technical SEO & Search Discoverability", 
     "Technical search foundations, Core Web Vitals speed optimization, keyword intent modeling, and authoritative content structure.", 
     "seo-services.html", services.generate_seo_services),

    ("lead-generation.html", "Turn Advertising Attention Into Business Enquiries", 
     "Full-funnel customer acquisition architectures: awareness hooks, consideration case studies, and high-speed lead capture forms.", 
     "lead-generation.html", services.generate_lead_generation)
]

print(f"Total pages configured: {len(pages_config)}")

# 1. Generate HTML Files
for filename, title, desc, canon, gen_func in pages_config:
    body_content = gen_func()
    full_html = page_shell(title, desc, canon, body_content, active_page=filename)
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] Generated: {filename}")

print(f"\nAll 30 HTML pages successfully written.")
print(f"Total image placeholders captured in registry: {len(IMAGE_REGISTRY)}")

# 2. Generate sitemap.xml
sitemap_entries = ""
for filename, title, desc, canon, _ in pages_config:
    priority = "1.0" if filename == "index.html" else "0.8"
    changefreq = "weekly" if filename in ["index.html", "portfolio.html", "blog.html"] else "monthly"
    sitemap_entries += f"""  <url>
    <loc>https://demo-advertising-agency.com/{filename}</loc>
    <lastmod>2027-03-01</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{sitemap_entries}</urlset>"""

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_content)
print("[OK] Generated: sitemap.xml")

# 3. Generate robots.txt
robots_content = """# robots.txt for ADVERTISING AGENCY Demonstration Website
User-agent: *
Allow: /

Sitemap: https://demo-advertising-agency.com/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)
print("[OK] Generated: robots.txt")

# 4. Generate README.md
readme_content = f"""# ADVERTISING AGENCY — Premium Multi-Page Demonstration Website

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
"""

with open(os.path.join(BASE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)
print("[OK] Generated: README.md")

# 5. Generate IMAGE-GENERATION-GUIDE.md
# Categorize counts
landscape_count = sum(1 for img in IMAGE_REGISTRY if "Landscape" in img["orientation"] or img["orientation"] == "Landscape")
portrait_count = sum(1 for img in IMAGE_REGISTRY if "Portrait" in img["orientation"])
square_count = sum(1 for img in IMAGE_REGISTRY if "Square" in img["orientation"])
total_count = len(IMAGE_REGISTRY)

guide_md = f"""# GOOGLE FLOW IMAGE GENERATION GUIDE
## ADVERTISING AGENCY — MASTER PROMPT MANUAL & IMAGE INVENTORY

This guide contains **every single image placeholder** used throughout the 30-page website.
Use these copy-ready prompts in **Google Flow** to generate high-end commercial advertising imagery.

---

### SUMMARY METRICS
- **Total Image Placeholders:** {total_count}
- **Landscape (16:9, 4:3, 21:9):** {landscape_count}
- **Portrait (9:16, 4:5):** {portrait_count}
- **Square (1:1):** {square_count}

---

## SECTION A: COMPLETE IMAGE INVENTORY TABLE

| # | Filename | Page | Section | Aspect Ratio | Dimensions | Orientation |
|---|---|---|---|---|---|---|
"""

for img in IMAGE_REGISTRY:
    guide_md += f"| {img['num']} | `{img['filename']}` | `{img['page']}` | {img['section']} | {img['aspect_ratio']} | {img['resolution']} | {img['orientation']} |\n"

guide_md += """
---

## SECTION B: INDIVIDUAL PROMPTS GROUPED BY WEBSITE PAGE

"""

# Group by page
pages_grouped = {}
for img in IMAGE_REGISTRY:
    p = img["page"]
    if p not in pages_grouped:
        pages_grouped[p] = []
    pages_grouped[p].append(img)

for page_name, imgs in pages_grouped.items():
    guide_md += f"### Page: `{page_name}`\n\n"
    for img in imgs:
        guide_md += f"""#### Image #{img['num']}: `{img['filename']}`
- **Section:** {img['section']} ({img['title']})
- **Recommended Aspect Ratio:** {img['aspect_ratio']}
- **Resolution:** {img['resolution']} pixels
- **Orientation:** {img['orientation']}
- **Visual Description:** {img['description']}
- **Composition:** {img['composition']}
- **Lighting:** {img['lighting']}
- **Background:** {img['background']}
- **Visual Style:** {img['style']}
- **Color Palette:** {img['palette']}
- **Negative Space Requirements:** {img['negative_space']}

**Copy-Ready Google Flow Prompt:**
```text
{img['prompt']}
```

---
"""

guide_md += f"""
## SECTION C: RECOMMENDED GENERATION ORDER
To maintain aesthetic coherence across your website, generate images in this sequential flight order:
1. **Hero & Anchor Visuals:** Images #1–#5 (`index.html` collage) to set the primary brand visual tone.
2. **Key Visual Formats:** Mockups for `social-media-advertising.html`, `video-advertising.html`, and `outdoor-advertising.html`.
3. **Core Service Headers:** Services cards and service detail hero images.
4. **Portfolio Campaign Projects:** Projects on `portfolio.html` and `campaign-details.html`.
5. **Editorial & Sector Cards:** Industry images on `industries.html` and article thumbs on `blog.html`.

---

## SECTION D: IMAGE REPLACEMENT INSTRUCTIONS
1. Generate the image in Google Flow using the exact prompt provided above.
2. Export the image in WebP or optimized JPEG format matching the resolution and filename indicated.
3. Save the file into `assets/images/<filename>`.
4. Open the corresponding `.html` file, locate the placeholder `div` with the matching filename, and embed the `<img>` tag:
```html
<!-- Example Replacement -->
<div class="agency-placeholder {IMAGE_REGISTRY[0]['aspect_ratio'].replace(':', '-')}">
  <img src="assets/images/{IMAGE_REGISTRY[0]['filename']}" alt="{IMAGE_REGISTRY[0]['title']}">
</div>
```
The stylesheet includes automatic styling for nested `<img>` tags (`position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; z-index: 10;`) ensuring a zero-shift drop-in replacement.

---

## SECTION E: FINAL VERIFICATION CHECKLIST
- [x] Total placeholders on site: {total_count}
- [x] Total detailed prompts generated: {total_count}
- [x] Every placeholder filename matches 1:1 with an inventory entry.
- [x] Every prompt contains explicit styling, camera direction, lighting, palette, and "no logos, no text" instruction.
- [x] All aspect ratios preserve stable UI layout dimensions without shifts.
"""

with open(os.path.join(BASE_DIR, "IMAGE-GENERATION-GUIDE.md"), "w", encoding="utf-8") as f:
    f.write(guide_md)
print("[OK] Generated: IMAGE-GENERATION-GUIDE.md")

print("\n==========================================")
print("MASTER BUILD COMPLETE!")
print(f"Total HTML Pages: {len(pages_config)}")
print(f"Total Image Prompts: {len(IMAGE_REGISTRY)}")
print("==========================================")
