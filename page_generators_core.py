# -*- coding: utf-8 -*-
"""
ADVERTISING AGENCY — Core Pages Generators (16 Core Pages)
"""

from build_site import placeholder_html

def generate_index():
    content = f'''
    <!-- ==================== HERO CAMPAIGN COLLAGE ==================== -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 48px;">
          <div class="hero-content">
            <div class="badge badge-coral">Full-Service Advertising Agency</div>
            <h1 style="margin: 8px 0;">WE MAKE BRANDS IMPOSSIBLE TO IGNORE.</h1>
            <p class="lead-text">
              From powerful advertising campaigns to scroll-stopping creative content, we help businesses connect with audiences and build stronger brands.
            </p>
            <div class="btn-group" style="margin-top: 12px;">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Our Work</a>
            </div>
            
            <div style="display: flex; gap: 24px; margin-top: 24px; padding-top: 24px; border-top: 1px solid var(--border-subtle);">
              <div>
                <strong style="display: block; font-size: 1.5rem; font-family: var(--font-display); color: #FFF;">360°</strong>
                <span style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase;">Campaign Strategy</span>
              </div>
              <div style="width: 1px; background: var(--border-subtle);"></div>
              <div>
                <strong style="display: block; font-size: 1.5rem; font-family: var(--font-display); color: var(--accent-secondary);">14+</strong>
                <span style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase;">Specialist Disciplines</span>
              </div>
              <div style="width: 1px; background: var(--border-subtle);"></div>
              <div>
                <strong style="display: block; font-size: 1.5rem; font-family: var(--font-display); color: var(--accent-highlight);">100%</strong>
                <span style="font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase;">Creative Rigor</span>
              </div>
            </div>
          </div>

          <!-- Hero Campaign Collage (6 Layered Proportions) -->
          <div class="hero-collage-grid">
            <!-- 1. Fashion Ad Concept (Large Left) -->
            <div class="collage-item collage-item-1">
              {placeholder_html("hero-collage-fashion.webp", "Fashion Advertising Concept", "1200x1500", "aspect-4-5", "index.html", "Hero Collage",
                                "Haute couture fashion model in dramatic coral atmospheric studio lighting with architectural geometry",
                                "Avant-garde editorial fashion model posing dramatically against dark obsidian architectural monoliths, vibrant neon coral rim lighting, cinematic grain, razor sharp focus, 8k resolution, no logos, no text.")}
              <div class="collage-overlay">
                <span class="collage-tag">Fashion Advertising</span>
                <div class="collage-title">Vogue & Haute Couture Visuals</div>
              </div>
            </div>

            <!-- 2. Tech Product Ad (Top Right) -->
            <div class="collage-item collage-item-2">
              {placeholder_html("hero-collage-tech.webp", "Technology Product Advertisement", "1200x800", "aspect-16-9", "index.html", "Hero Collage",
                                "Sleek futuristic titanium device illuminated by vivid acid lime reflections",
                                "Minimalist luxury industrial tech hardware floating on dark reflective pool, illuminated by electric acid lime and white studio lights, commercial product photography, 8k, no text, no logos.")}
              <div class="collage-overlay">
                <span class="collage-tag">Product Advertising</span>
                <div class="collage-title">Next-Gen Audio Concept</div>
              </div>
            </div>

            <!-- 3. Food & Beverage Campaign (Bottom Right) -->
            <div class="collage-item collage-item-3">
              {placeholder_html("hero-collage-food.webp", "Food & Beverage Campaign", "1200x1200", "aspect-1-1", "index.html", "Hero Collage",
                                "Artisanal culinary gastronomy dish with explosive spice splash and warm rim light",
                                "High-end culinary commercial photography of a gourmet dish with smoke swirls and vibrant chili spices suspended in motion, dramatic black background, 8k, no logos, no text.")}
              <div class="collage-overlay">
                <span class="collage-tag">F&B Campaign</span>
                <div class="collage-title">Artisanal Gastronomy</div>
              </div>
            </div>

            <!-- 4. Real Estate Promotion (Small Bottom Left 1) -->
            <div class="collage-item collage-item-4">
              {placeholder_html("hero-collage-realestate.webp", "Real Estate Promotional Creative", "800x1000", "aspect-4-5", "index.html", "Hero Collage",
                                "Ultra-modern architectural villa at twilight with warm interior lighting and infinity pool",
                                "Architectural luxury villa at dusk with illuminated floor-to-ceiling glass walls reflecting across a calm dark pool, twilight blue sky, commercial real estate photography, 8k, no text, no logos.")}
              <div class="collage-overlay">
                <span class="collage-tag">Real Estate</span>
                <div class="collage-title">Skyline Residences</div>
              </div>
            </div>

            <!-- 5. Video Campaign Preview (Small Bottom Left 2) -->
            <div class="collage-item collage-item-5">
              {placeholder_html("hero-collage-video.webp", "Video Campaign Preview", "800x1000", "aspect-4-5", "index.html", "Hero Collage",
                                "Film production cinema camera rig filming a commercial set with vibrant backlight",
                                "Professional cinematic camera on heavy gimbal facing a brightly backlit commercial advertising set, warm golden flare, atmospheric smoke, 8k, no text, no logos.")}
              <div class="collage-overlay">
                <span class="collage-tag">Video Production</span>
                <div class="collage-title">Commercial Film Set</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== MARQUEE TICKER ==================== -->
    <div class="marquee-container" aria-hidden="true">
      <div class="marquee-content">
        <div class="marquee-item">CREATIVE ADVERTISING <span class="marquee-star">✦</span></div>
        <div class="marquee-item">BRAND STRATEGY <span class="marquee-star">✦</span></div>
        <div class="marquee-item">SOCIAL MEDIA CAMPAIGNS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">COMMERCIAL VIDEO PRODUCTION <span class="marquee-star">✦</span></div>
        <div class="marquee-item">GOOGLE & META ADS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">HIGH-CONVERTING FUNNELS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">OUTDOOR BILLBOARDS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">EDITORIAL DESIGN <span class="marquee-star">✦</span></div>
      </div>
      <div class="marquee-content" aria-hidden="true">
        <div class="marquee-item">CREATIVE ADVERTISING <span class="marquee-star">✦</span></div>
        <div class="marquee-item">BRAND STRATEGY <span class="marquee-star">✦</span></div>
        <div class="marquee-item">SOCIAL MEDIA CAMPAIGNS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">COMMERCIAL VIDEO PRODUCTION <span class="marquee-star">✦</span></div>
        <div class="marquee-item">GOOGLE & META ADS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">HIGH-CONVERTING FUNNELS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">OUTDOOR BILLBOARDS <span class="marquee-star">✦</span></div>
        <div class="marquee-item">EDITORIAL DESIGN <span class="marquee-star">✦</span></div>
      </div>
    </div>

    <!-- ==================== SELECTED CREATIVE CAMPAIGNS ==================== -->
    <section class="section">
      <div class="container">
        <div class="section-header" style="display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 20px;">
          <div>
            <span class="badge badge-lime">Selected Work</span>
            <h2>Featured Creative Campaigns</h2>
            <p>A curated look at our multi-format advertising concepts across key consumer categories.</p>
          </div>
          <a href="portfolio.html" class="btn btn-secondary">View All Campaigns →</a>
        </div>

        <div class="grid-3">
          <!-- Campaign 1 -->
          <div class="portfolio-item">
            {placeholder_html("campaign-fashion-demo.webp", "Fashion Campaign Demo", "1200x900", "aspect-4-3", "index.html", "Selected Campaigns",
                              "Editorial luxury fashion campaign showing haute couture model against brutalist concrete backdrop",
                              "Editorial fashion advertising campaign visual of a model in avant-garde black attire standing against raw textured concrete, sharp direct sunlight, stark shadow patterns, 8k, no text, no logos.")}
            <div class="portfolio-item-body">
              <span class="portfolio-item-category">Fashion & Apparel</span>
              <h3 class="portfolio-item-title">Fashion Campaign Demo</h3>
              <p style="font-size: 0.9rem; margin-bottom: 16px;">Multi-channel brand awareness and seasonal collection launch engineered for social, print, and digital billboards.</p>
              <div class="demo-disclaimer" style="margin-bottom: 16px;">Illustrative Demo Campaign — Not a Client Campaign</div>
              <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
                <a href="campaign-details.html" class="btn-link">Case Study →</a>
                <button class="btn btn-secondary btn-preview-campaign" style="padding: 6px 14px; font-size: 0.76rem;">Quick Preview</button>
              </div>
            </div>
          </div>

          <!-- Campaign 2 -->
          <div class="portfolio-item">
            {placeholder_html("campaign-product-demo.webp", "Product Launch Campaign Demo", "1200x900", "aspect-4-3", "index.html", "Selected Campaigns",
                              "Cosmetic product packaging hovering above glistening rippling water in studio",
                              "Commercial beauty product advertising visual, matte obsidian skincare bottle levitating over dark ripple water with caustic light patterns, 8k, no text, no logos.")}
            <div class="portfolio-item-body">
              <span class="portfolio-item-category">Product Advertising</span>
              <h3 class="portfolio-item-title">Product Launch Campaign Demo</h3>
              <p style="font-size: 0.9rem; margin-bottom: 16px;">High-conversion digital acquisition campaign combining 3D product visuals with targeted Meta feed and Google Shopping ads.</p>
              <div class="demo-disclaimer" style="margin-bottom: 16px;">Illustrative Demo Campaign — Not a Client Campaign</div>
              <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
                <a href="campaign-details.html" class="btn-link">Case Study →</a>
                <button class="btn btn-secondary btn-preview-campaign" style="padding: 6px 14px; font-size: 0.76rem;">Quick Preview</button>
              </div>
            </div>
          </div>

          <!-- Campaign 3 -->
          <div class="portfolio-item">
            {placeholder_html("campaign-realestate-demo.webp", "Real Estate Advertising Demo", "1200x900", "aspect-4-3", "index.html", "Selected Campaigns",
                              "Penthouse living room overlooking illuminated urban skyscraper skyline at night",
                              "High-end luxury real estate advertising visual of a modern penthouse terrace overlooking panoramic city skyscrapers at twilight, soft warm interior glow, 8k, no text, no logos.")}
            <div class="portfolio-item-body">
              <span class="portfolio-item-category">Real Estate</span>
              <h3 class="portfolio-item-title">Real Estate Advertising Demo</h3>
              <p style="font-size: 0.9rem; margin-bottom: 16px;">Ultra-targeted lead generation campaign designed to capture qualified high-net-worth property buyer enquiries.</p>
              <div class="demo-disclaimer" style="margin-bottom: 16px;">Illustrative Demo Campaign — Not a Client Campaign</div>
              <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
                <a href="campaign-details.html" class="btn-link">Case Study →</a>
                <button class="btn btn-secondary btn-preview-campaign" style="padding: 6px 14px; font-size: 0.76rem;">Quick Preview</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== WHAT WE DO / CORE SERVICES ==================== -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-coral">Comprehensive Capabilities</span>
          <h2>Advertising Solutions for Every Stage of Brand Growth</h2>
          <p>We blend creative intuition with performance engineering to make every advertising rupee deliver measurable brand stature.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <div style="font-size: 1.8rem; margin-bottom: 12px; color: var(--accent-main);">✦</div>
            <h3>Paid Media & Performance</h3>
            <p>Google Search, Display, Meta Ads, and multi-channel acquisition funnels tailored for scalable client enquiry generation.</p>
            <ul class="deliverables-list">
              <li>Google Search & Display</li>
              <li>Meta Feed & Reels Ads</li>
              <li>Audience Cohort Modeling</li>
            </ul>
            <a href="digital-advertising.html" class="btn-link">Explore Digital Ads →</a>
          </div>

          <div class="card">
            <div style="font-size: 1.8rem; margin-bottom: 12px; color: var(--accent-secondary);">✦</div>
            <h3>Creative Strategy & Art Direction</h3>
            <p>Campaign key visuals, editorial graphic design, storytelling systems, and high-impact social advertising creative suites.</p>
            <ul class="deliverables-list">
              <li>Master Key Visuals</li>
              <li>Brand Narrative Systems</li>
              <li>Social Media Ad Suites</li>
            </ul>
            <a href="creative-design.html" class="btn-link">Explore Creative Design →</a>
          </div>

          <div class="card">
            <div style="font-size: 1.8rem; margin-bottom: 12px; color: var(--accent-highlight);">✦</div>
            <h3>Commercial Video & Motion</h3>
            <p>From cinema brand commercials to dynamic social reels and product films that stop scrollers in their tracks.</p>
            <ul class="deliverables-list">
              <li>Brand Commercial Films</li>
              <li>Short-Form Social Reels</li>
              <li>Product Motion Graphics</li>
            </ul>
            <a href="video-advertising.html" class="btn-link">Explore Video Advertising →</a>
          </div>
        </div>

        <div style="text-align: center; margin-top: 40px;">
          <a href="services.html" class="btn btn-lime">Explore All 14 Advertising Disciplines</a>
        </div>
      </div>
    </section>

    <!-- ==================== 5-STEP CREATIVE PROCESS ==================== -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-violet">Our Methodology</span>
          <h2>From Big Idea to Campaign Execution</h2>
          <p>A rigorous five-phase workflow ensuring every creative asset is strategically grounded and commercially primed.</p>
        </div>

        <div class="process-grid">
          <div class="process-card">
            <div class="process-step-num">01</div>
            <h4>Discovery</h4>
            <p>Immerse in business objectives, target buyer psychographics, competitive landscape, and campaign milestones.</p>
          </div>
          <div class="process-card">
            <div class="process-step-num">02</div>
            <h4>Strategy</h4>
            <p>Architect positioning, creative angle, media channel allocation, messaging hierarchy, and KPI definitions.</p>
          </div>
          <div class="process-card">
            <div class="process-step-num">03</div>
            <h4>Creative Development</h4>
            <p>Craft key visuals, persuasive copywriting, motion storyboards, ad designs, and interactive mockups.</p>
          </div>
          <div class="process-card">
            <div class="process-step-num">04</div>
            <h4>Execution</h4>
            <p>Deploy campaigns across approved media networks, integrate tracking pixels, and configure conversion funnels.</p>
          </div>
          <div class="process-card">
            <div class="process-step-num">05</div>
            <h4>Review & Optimize</h4>
            <p>Evaluate response metrics, prune underperforming creatives, scale top performers, and iterate strategic direction.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== WHY ADVERTISING STRATEGY MATTERS ==================== -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="grid-2" style="align-items: center; gap: 48px;">
          <div>
            <span class="badge badge-coral">Strategic Imperative</span>
            <h2 style="margin: 16px 0;">Why Advertising Strategy Matters More Than Ever</h2>
            <p style="margin-bottom: 20px;">
              In an era where millions of messages compete for seconds of consumer attention, unremarkable advertising is completely invisible.
            </p>
            <p style="margin-bottom: 24px;">
              Without strategic direction, ad spend is wasted on mismatched audiences, generic creatives, and high churn rates. We unite analytical audience research with bold creative execution so that every single campaign asset works towards enduring brand equity and immediate commercial action.
            </p>
            <ul class="deliverables-list" style="border: none; padding: 0;">
              <li>Clarity of positioning prevents commoditization and price wars.</li>
              <li>High-craft creative assets lower customer acquisition costs.</li>
              <li>Omni-channel alignment builds trust across multiple customer touchpoints.</li>
            </ul>
          </div>
          <div>
            {placeholder_html("home-strategy-visual.webp", "Advertising Strategy Visualization", "1920x1080", "aspect-16-9", "index.html", "Strategy Section",
                              "Abstract glowing prism refracting white light into vivid advertising color beams",
                              "Conceptual advertising photography of a crystalline prism refracting a beam of brilliant white light into intense streams of coral orange and neon lime light against deep obsidian, 8k resolution, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== PROJECT ENQUIRY CTA ==================== -->
    <section class="section text-center" style="background: radial-gradient(circle at center, rgba(255, 90, 54, 0.15) 0%, transparent 70%);">
      <div class="container container-narrow">
        <span class="badge badge-lime">Start Your Campaign</span>
        <h2 style="margin: 16px 0;">Let's Build An Advertising Campaign That Gets Noticed</h2>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Whether you need a full-scale multi-platform product launch, high-converting social media creatives, or targeted lead generation, our team is ready to formulate your creative strategy.
        </p>
        <div class="btn-group" style="justify-content: center;">
          <a href="start-campaign.html" class="btn btn-primary" style="font-size: 1.05rem; padding: 16px 36px;">Launch Campaign Enquiry</a>
          <a href="contact.html" class="btn btn-secondary" style="font-size: 1.05rem; padding: 16px 36px;">Speak With Strategists</a>
        </div>
      </div>
    </section>
    '''
    return content

def generate_about():
    content = f'''
    <!-- About Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">About The Agency</span>
            <h1 style="margin: 16px 0;">Creative Thinking Meets Advertising Strategy</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              We are an advertising agency dedicated to making brands impossible to ignore. We operate at the intersection of cultural curiosity, strategic discipline, and visual perfection.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Work</a>
            </div>
          </div>
          <div>
            {placeholder_html("about-hero.webp", "Creative Studio Space", "1920x1080", "aspect-16-9", "about.html", "Hero Section",
                              "Architectural interior of an advertising creative studio with mood boards and high ceilings",
                              "Minimalist architectural photograph of a contemporary advertising agency design studio, high industrial ceilings, dark charcoal walls, large format mood boards illuminated by warm track lighting, 8k, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Agency Philosophy & Approach -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Our Philosophy</span>
          <h2>Ideas That Provoke. Systems That Deliver.</h2>
          <p>We reject cookie-cutter marketing playbooks in favor of custom creative systems built for your exact market reality.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Strategic Thinking</h4>
            <p>Every creative choice begins with deep commercial logic. We analyze consumer motivations, market blind spots, and category conventions to identify opportunities where a brand can stand completely distinct.</p>
          </div>
          <div class="card">
            <h4>Campaign Execution</h4>
            <p>Strategy is meaningless without relentless craft. From typographic refinement to cinematic motion and color grading, our production standards ensure your brand commands authority across any screen or billboard.</p>
          </div>
          <div class="card">
            <h4>Creative Collaboration</h4>
            <p>We work in transparent lockstep with business founders and marketing leaders. No hidden layers, no unnecessary bureaucracy—just agile creative teams focused on accelerating your commercial objectives.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Mission & Vision -->
    <section class="section">
      <div class="container">
        <div class="grid-2" style="gap: 40px;">
          <div class="card" style="border-left: 4px solid var(--accent-main);">
            <span class="badge badge-coral" style="margin-bottom: 14px;">Our Mission</span>
            <h3>Empowering Brands Through Uncompromising Creativity</h3>
            <p style="margin-top: 12px;">
              To help ambitious businesses transcend market indifference through bold visual storytelling, rigorous media planning, and advertising experiences that convert interest into measurable commercial value.
            </p>
          </div>
          <div class="card" style="border-left: 4px solid var(--accent-secondary);">
            <span class="badge badge-lime" style="margin-bottom: 14px;">Our Vision</span>
            <h3>Setting The Standard for Modern Creative Advertising</h3>
            <p style="margin-top: 12px;">
              To be the benchmark for modern advertising excellence—proving that creativity and analytical performance are not opposing forces, but essential partners in building iconic long-term brand value.
            </p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_services_hub():
    services_list = [
        ("Digital Advertising", "digital-advertising.html", "Multi-channel paid media strategies across search, display, and social networks.", ["Audience Cohort Modeling", "Placement Optimization", "Conversion Attribution"], "service-thumb-digital.webp"),
        ("Social Media Advertising", "social-media-advertising.html", "High-engagement social ad campaigns on Instagram, Facebook, and LinkedIn.", ["Story & Reel Creatives", "Carousel Storyboards", "Retargeting Architecture"], "service-thumb-social.webp"),
        ("Google Ads", "google-ads.html", "Search intent capture, Google Display Network, Shopping feeds, and YouTube ads.", ["High-Intent Search Ads", "Display Network Banners", "Dynamic Shopping Feeds"], "service-thumb-google.webp"),
        ("Meta Ads", "meta-ads.html", "Targeted audience scaling and creative testing on Facebook & Instagram ecosystems.", ["Lead Gen Instant Forms", "Lookalike Cohorts", "Creative Matrix Testing"], "service-thumb-meta.webp"),
        ("Video Advertising", "video-advertising.html", "Cinematic commercial films, short-form reels, and product motion showcases.", ["Commercial Brand Films", "Short-Form Social Video", "3D Product Animations"], "service-thumb-video.webp"),
        ("Creative Design", "creative-design.html", "Master key visuals, promotional banners, and campaign graphics that stop the scroll.", ["Master Key Visuals", "Social Creative Packs", "Digital Banner Formats"], "service-thumb-creative.webp"),
        ("Brand Strategy", "brand-strategy.html", "Market positioning, competitive moats, tonal guidelines, and campaign messaging.", ["Positioning Matrix", "Messaging Frameworks", "Audience Persona Maps"], "service-thumb-strategy.webp"),
        ("Graphic Design", "graphic-design.html", "Brand identity marks, packaging concepts, brochures, and corporate stationery.", ["Visual Identity Guidelines", "Packaging & Labels", "Editorial Collateral"], "service-thumb-graphic.webp"),
        ("Content Marketing", "content-marketing.html", "Strategic editorial calendars, copywriting, articles, and video scriptwriting.", ["Editorial Calendars", "Advertising Copywriting", "Scripting & Narratives"], "service-thumb-content.webp"),
        ("Influencer Marketing", "influencer-marketing.html", "Creator vetting, campaign briefs, collaborative content, and reach tracking.", ["Creator Vetting & Match", "Creative Brief Systems", "Performance Auditing"], "service-thumb-influencer.webp"),
        ("Outdoor Advertising", "outdoor-advertising.html", "Commanding highway billboards, digital LED displays, bus wraps, and retail signage.", ["Highway Billboards", "Digital Outdoor Displays", "Transit & Bus Wraps"], "service-thumb-outdoor.webp"),
        ("Print Advertising", "print-advertising.html", "Tactile luxury magazine spreads, newspaper display ads, and promotional print.", ["Magazine Ad Spreads", "Newspaper Placements", "Luxury Catalogues"], "service-thumb-print.webp"),
        ("SEO Services", "seo-services.html", "Technical search foundation, keyword intent research, and on-page discoverability.", ["Technical Site Audits", "Core Web Vitals Speed", "On-Page Optimization"], "service-thumb-seo.webp"),
        ("Lead Generation", "lead-generation.html", "Full-funnel customer acquisition funnels, landing pages, and qualified enquiry capture.", ["Acquisition Funnel Build", "Conversion Landing Pages", "Lead Qualification Forms"], "service-thumb-leadgen.webp"),
    ]

    cards_html = ""
    for title, link, desc, delivs, thumb_file in services_list:
        delivs_str = "".join([f"<li>{d}</li>" for d in delivs])
        cards_html += f'''
        <div class="card card-service">
          {placeholder_html(thumb_file, title, "800x450", "aspect-16-9", "services.html", "Service Cards",
                            f"Commercial creative asset visualization for {title}",
                            f"Clean commercial advertising photography representing {title}, dark background, luminous accents, 8k resolution, no logos, no text.")}
          <div class="card-service-body">
            <h3 class="card-service-title">{title}</h3>
            <p class="card-service-desc">{desc}</p>
            <ul class="deliverables-list">
              {delivs_str}
            </ul>
            <div class="card-service-actions">
              <a href="{link}" class="btn-link">Learn More →</a>
              <a href="start-campaign.html" class="btn btn-secondary" style="padding: 6px 14px; font-size: 0.78rem;">Enquire</a>
            </div>
          </div>
        </div>
        '''

    content = f'''
    <!-- Services Hub Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Comprehensive Agency Capabilities</span>
        <h1 style="margin: 16px 0;">Advertising Solutions for Every Stage of Brand Growth</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          From foundational brand positioning and high-craft creative design to multi-channel paid media campaigns and physical outdoor spectacles, explore our 14 core advertising disciplines.
        </p>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="grid-3">
          {cards_html}
        </div>
      </div>
    </section>
    '''
    return content

def generate_industries():
    industries_list = [
        ("Real Estate", "Skyline developments, luxury villas, and commercial spaces seeking high-net-worth investor enquiries.", "Lead generation funnels, virtual tour video ads, and architectural key visuals.", "industries-realestate.webp"),
        ("Healthcare & Wellness", "Clinics, specialty healthcare providers, and wellness retreats building patient trust.", "Educational video series, intent-based Google search ads, and local community outreach.", "industries-healthcare.webp"),
        ("Education & Academics", "Universities, specialized institutes, and executive learning platforms scaling student enrollments.", "Multi-tiered admission campaigns, student story reels, and Meta lead generation forms.", "industries-education.webp"),
        ("Fashion & Apparel", "Haute couture, streetwear labels, and contemporary apparel houses launching seasonal collections.", "Editorial lookbooks, dynamic Instagram Reels, fashion films, and outdoor billboards.", "industries-fashion.webp"),
        ("E-commerce & D2C", "Fast-growing consumer product brands driving direct sales and repeat purchase loyalty.", "Google Shopping feeds, Meta dynamic carousels, TikTok ads, and conversion landing pages.", "industries-ecommerce.webp"),
        ("Restaurants & F&B", "Gourmet dining establishments, artisanal food brands, and hospitality chains driving table bookings.", "Sensory macro food commercials, geo-fenced Instagram ads, and seasonal menu promotions.", "industries-food.webp"),
        ("Hospitality & Travel", "Boutique resorts, luxury travel experiences, and destination hotels attracting international guests.", "Immersive destination brand films, Google Search hospitality campaigns, and influencer trips.", "industries-hospitality.webp"),
        ("Interior Design & Architecture", "High-end interior studios and bespoke furniture makers attracting premium residential commissions.", "Editorial design portfolios, Pinterest & Instagram ad suites, and print magazine spreads.", "industries-interiors.webp"),
        ("Fitness & Athletics", "Premium gym chains, athletic wear brands, and fitness apps scaling recurring memberships.", "High-energy commercial video campaigns, transformation story reels, and seasonal challenges.", "industries-fitness.webp"),
        ("Technology & SaaS", "Software companies, hardware innovators, and enterprise tech startups acquiring commercial accounts.", "B2B LinkedIn sponsored content, explainer video animations, and intent-focused search ads.", "industries-tech.webp"),
        ("Retail & Consumer Goods", "Retail store chains and lifestyle outlets driving foot traffic and omnichannel shopping.", "Promotional festive flyers, outdoor transit hoardings, and targeted local digital ads.", "industries-retail.webp"),
        ("Professional Services", "Consultancies, legal advisory firms, and financial organizations seeking institutional clients.", "Authoritative brand strategy, executive thought-leadership content, and corporate identity design.", "industries-services.webp"),
    ]

    cards_html = ""
    for title, opps, concept, img_file in industries_list:
        cards_html += f'''
        <div class="card" style="padding: 0; overflow: hidden;">
          {placeholder_html(img_file, f"{title} Advertising Concept", "800x450", "aspect-16-9", "industries.html", "Industry Sectors",
                            f"Commercial advertising visual context for the {title} sector",
                            f"Commercial advertising concept photograph representing the {title} industry, sleek styling, dark modern atmosphere, 8k, no text, no logos.")}
          <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
            <span class="badge badge-coral" style="margin-bottom: 8px;">Industry Focus</span>
            <h3 style="font-size: 1.3rem; margin-bottom: 12px;">{title}</h3>
            <p style="font-size: 0.9rem; margin-bottom: 16px;"><strong>Advertising Opportunities:</strong> {opps}</p>
            <div style="background: rgba(255,255,255,0.03); padding: 12px; border-radius: 6px; border: 1px dashed var(--border-color); margin-bottom: 20px;">
              <div style="font-size: 0.76rem; color: var(--accent-secondary); font-weight: 700; text-transform: uppercase;">Sample Campaign Concept:</div>
              <div style="font-size: 0.85rem; color: var(--text-secondary); margin-top: 4px;">{concept}</div>
            </div>
            <div class="demo-disclaimer" style="margin-bottom: 16px;">Illustrative Industry Concept — Generic Demo</div>
            <div style="margin-top: auto;">
              <a href="start-campaign.html" class="btn btn-primary" style="width: 100%;">Plan {title} Campaign</a>
            </div>
          </div>
        </div>
        '''

    content = f'''
    <!-- Industries Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-lime">Tailored Industry Strategies</span>
        <h1 style="margin: 16px 0;">Specialized Advertising for Distinct Sectors</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Every industry has its own audience psychology, regulatory considerations, and conversion cycles. Explore our strategic frameworks across 12 major commercial categories.
        </p>
        <div class="demo-disclaimer">Illustrative Demo Showcase — Not Real Client Claims</div>
      </div>
    </section>

    <!-- Industries Grid -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="grid-3">
          {cards_html}
        </div>
      </div>
    </section>
    '''
    return content

def generate_portfolio():
    projects = [
        ("Fashion Campaign Demo", "Fashion & Apparel", "fashion", "campaign-fashion-full.webp", "Multi-channel autumn brand launch combining high-fashion street style reels, billboards, and print lookbooks."),
        ("Product Launch Campaign Demo", "Product Advertising", "product", "campaign-product-full.webp", "Global cosmetic brand launch featuring 3D levitation visuals, TikTok creator seeding, and Google Shopping."),
        ("Restaurant Promotion Demo", "Food & Beverage", "food", "campaign-food-full.webp", "Sensory gastronomic commercial campaign featuring high-speed splash video ads and localized Meta booking ads."),
        ("Real Estate Advertising Demo", "Real Estate", "realestate", "campaign-realestate-full.webp", "High-net-worth investor acquisition campaign for luxury skyline penthouses with multi-step enquiry qualification."),
        ("Technology Product Campaign Demo", "Technology", "tech", "campaign-tech-full.webp", "Futuristic wireless acoustic hardware reveal combining zero-gravity animations with B2B tech media display ads."),
        ("Healthcare Awareness Campaign Demo", "Healthcare", "healthcare", "campaign-healthcare-full.webp", "Compassionate educational video campaign raising public awareness for preventative cardiovascular health."),
        ("Brand Identity & Packaging Demo", "Brand Identity", "brand", "campaign-brand-full.webp", "Complete luxury packaging suite and graphic design system for a boutique organic lifestyle company."),
        ("Metropolitan Billboard Demo", "Outdoor Advertising", "outdoor", "campaign-outdoor-full.webp", "Monumental highway LED billboard takeover at twilight engineered with bold typography for instant recall."),
        ("Editorial Magazine Spread Demo", "Print Advertising", "print", "campaign-print-full.webp", "Double-page luxury magazine editorial advertisement typeset with museum-grade typographic standards."),
        ("Corporate Rebrand Campaign Demo", "Corporate", "corporate", "campaign-corporate-full.webp", "Strategic identity repositioning, executive brand film, and investor presentation collateral."),
    ]

    cards_html = ""
    for title, cat_name, cat_slug, img_file, desc in projects:
        cards_html += f'''
        <div class="portfolio-item" data-category="{cat_slug}">
          {placeholder_html(img_file, title, "1200x900", "aspect-4-3", "portfolio.html", "Portfolio Grid",
                            f"Commercial creative asset for {title}",
                            f"Commercial campaign photography representing {title}, dark studio styling, dramatic lighting, 8k resolution, no logos, no text.")}
          <div class="portfolio-item-body">
            <span class="portfolio-item-category">{cat_name}</span>
            <h3 class="portfolio-item-title">{title}</h3>
            <p style="font-size: 0.9rem; margin-bottom: 16px;">{desc}</p>
            <div class="demo-disclaimer" style="margin-bottom: 16px;">Illustrative Demo Campaign — Not a Client Campaign</div>
            <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center;">
              <a href="campaign-details.html" class="btn-link">Case Study Details →</a>
              <button class="btn btn-secondary btn-preview-campaign" style="padding: 6px 14px; font-size: 0.78rem;">Quick Preview</button>
            </div>
          </div>
        </div>
        '''

    content = f'''
    <!-- Portfolio Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Creative Archive</span>
        <h1 style="margin: 16px 0;">Selected Advertising Campaigns</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Explore our campaign gallery spanning digital advertising, commercial films, high-fashion key visuals, outdoor spectacles, and brand identities.
        </p>
        <div class="demo-disclaimer">Illustrative Demo Portfolio — All Projects Represent Concept Work</div>
      </div>
    </section>

    <!-- Filter Bar & Grid -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="portfolio-filter-bar">
          <button class="filter-btn active" data-filter="all">All Campaigns</button>
          <button class="filter-btn" data-filter="fashion">Fashion</button>
          <button class="filter-btn" data-filter="product">Product</button>
          <button class="filter-btn" data-filter="food">Food & Beverage</button>
          <button class="filter-btn" data-filter="realestate">Real Estate</button>
          <button class="filter-btn" data-filter="tech">Technology</button>
          <button class="filter-btn" data-filter="healthcare">Healthcare</button>
          <button class="filter-btn" data-filter="outdoor">Outdoor</button>
          <button class="filter-btn" data-filter="print">Print</button>
          <button class="filter-btn" data-filter="brand">Brand Identity</button>
          <button class="filter-btn" data-filter="corporate">Corporate</button>
        </div>

        <div class="portfolio-grid">
          {cards_html}
        </div>
      </div>
    </section>
    '''
    return content

def generate_campaign_details():
    content = f'''
    <!-- Campaign Details Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="container-narrow text-center">
          <span class="badge badge-coral">Campaign Case Study</span>
          <h1 style="margin: 16px 0;">Fashion Campaign Demo</h1>
          <p class="lead-text" style="margin: 0 auto 24px;">
            An illustrative multi-channel advertising case study demonstrating how seasonal fashion campaigns are strategically structured, visually crafted, and deployed across media channels.
          </p>
          <div class="demo-disclaimer">Illustrative Demo Campaign — Not a Real Client Campaign</div>
        </div>
      </div>
    </section>

    <!-- Master Key Visual -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        {placeholder_html("campaign-details-master-kv.webp", "Fashion Campaign Master Key Visual", "1920x1080", "aspect-16-9", "campaign-details.html", "Master KV",
                          "Panoramic haute couture fashion campaign key visual showing three models in monochromatic attire against sculptural slate walls",
                          "Cinematic panoramic commercial fashion campaign visual with three models posed with editorial restraint, dramatic directional lighting, rich obsidian and terracotta tones, 8k, no text, no logos.")}
      </div>
    </section>

    <!-- Case Study Structure -->
    <section class="section">
      <div class="container container-narrow">
        <div class="grid-2" style="margin-bottom: 40px; padding-bottom: 40px; border-bottom: 1px solid var(--border-color);">
          <div>
            <h4 style="color: var(--accent-secondary); margin-bottom: 8px;">Industry</h4>
            <p>Fashion, Luxury Apparel & Accessories</p>
          </div>
          <div>
            <h4 style="color: var(--accent-secondary); margin-bottom: 8px;">Campaign Formats</h4>
            <p>Digital Key Visuals, Social Reels (9:16), Outdoor Billboards, Editorial Magazine Print</p>
          </div>
          <div>
            <h4 style="color: var(--accent-secondary); margin-bottom: 8px;">Target Audience</h4>
            <p>Urban tastemakers, luxury fashion enthusiasts, and style-conscious digital consumers aged 22–38.</p>
          </div>
          <div>
            <h4 style="color: var(--accent-secondary); margin-bottom: 8px;">Core Objective</h4>
            <p>Establish high-prestige seasonal brand awareness, drive digital lookbook engagement, and maximize retail footfall.</p>
          </div>
        </div>

        <div style="margin-bottom: 40px;">
          <h3>The Creative Concept: Architectural Solitude</h3>
          <p style="margin-top: 14px;">
            The creative concept contrasts fluid, structured fabric silhouettes against brutalist basalt stone architecture. By stripping away distracting decorative elements and utilizing dramatic low-angle sunlight, the garments become the sole focal point of visual tension and luxury prestige.
          </p>
        </div>

        <div style="margin-bottom: 40px;">
          <h3>Advertising Strategy & Media Choreography</h3>
          <p style="margin-top: 14px;">
            Rather than blasting all channels simultaneously with identical creative, the campaign was structured across three phased flights:
          </p>
          <ul class="deliverables-list" style="margin-top: 16px;">
            <li><strong>Phase 1 (Teaser):</strong> 6-second vertical teaser reels and cryptic outdoor billboard key visuals teasing the collection date.</li>
            <li><strong>Phase 2 (Launch):</strong> Full commercial brand film drop, influencer lookbook seeding, and full-page editorial magazine spreads.</li>
            <li><strong>Phase 3 (Conversion):</strong> High-intent Meta carousel ads and Google Search remarketing driving scrollers directly to ecommerce checkout.</li>
          </ul>
        </div>

        <!-- Social Executions Sub-grid -->
        <h3 style="margin-bottom: 20px;">Visual Executions Across Channels</h3>
        <div class="grid-2" style="margin-bottom: 40px;">
          <div>
            {placeholder_html("campaign-exec-social.webp", "Social Media Execution", "1080x1080", "aspect-1-1", "campaign-details.html", "Executions",
                              "Square social media carousel ad showing close-up macro texture of luxury cashmere coat",
                              "Commercial fashion detail photograph showing macro textures of woven cashmere fabric with striking coral rim lighting, 8k, no text, no logos.")}
            <div style="text-align: center; margin-top: 10px; font-size: 0.82rem; color: var(--text-muted);">Social Media Square Asset</div>
          </div>
          <div>
            {placeholder_html("campaign-exec-outdoor.webp", "Outdoor Billboard Execution", "1080x1080", "aspect-1-1", "campaign-details.html", "Executions",
                              "Wide perspective shot of horizontal street billboard illuminated at dusk in shopping district",
                              "Outdoor horizontal billboard mounted on concrete architectural wall in high-end shopping district at dusk, 8k, no text, no logos.")}
            <div style="text-align: center; margin-top: 10px; font-size: 0.82rem; color: var(--text-muted);">Outdoor Street Media Asset</div>
          </div>
        </div>

        <div class="card" style="margin-bottom: 40px; background: rgba(255, 90, 54, 0.04); border-color: rgba(255, 90, 54, 0.2);">
          <h4 style="color: var(--accent-main); margin-bottom: 10px;">Strategic Considerations & Learnings</h4>
          <p style="font-size: 0.92rem;">
            This illustrative case study underscores the importance of visual coherence across diverse display formats. When outdoor key visuals match the tone and color palette of mobile social reels, brand recall increases substantially over fragmented, ad-hoc creative testing.
          </p>
        </div>

        <div style="text-align: center; padding-top: 20px;">
          <a href="start-campaign.html" class="btn btn-primary">Start Your Campaign Strategy</a>
        </div>
      </div>
    </section>
    '''
    return content

def generate_process():
    content = f'''
    <!-- Process Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Methodology</span>
        <h1 style="margin: 16px 0;">From Big Idea to Campaign Execution</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Predictable advertising success is not born from random sparks of luck. It is the result of a disciplined, repeatable 5-step creative process engineered to eliminate waste and maximize commercial impact.
        </p>
      </div>
    </section>

    <!-- 5 Steps In-Depth -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div style="display: flex; flex-direction: column; gap: 40px; max-width: 960px; margin: 0 auto;">
          <!-- Step 1 -->
          <div class="card" style="border-left: 6px solid var(--accent-main);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <span class="badge badge-coral">Step 01</span>
              <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--text-muted);">DISCOVERY & AUDIT</span>
            </div>
            <h2>Discovery: Understanding The Commercial Realities</h2>
            <p style="margin: 12px 0 16px;">
              Before writing a single headline or rendering an image, we conduct an exhaustive discovery session. We analyze your commercial objectives, product unit economics, target audience friction points, and competitor positioning.
            </p>
            <ul class="deliverables-list">
              <li>Comprehensive Brand & Competitor Audit</li>
              <li>Target Customer Persona & Psychographic Mapping</li>
              <li>Channel Feasibility & Budget Allocation Analysis</li>
            </ul>
          </div>

          <!-- Step 2 -->
          <div class="card" style="border-left: 6px solid var(--accent-secondary);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <span class="badge badge-lime">Step 02</span>
              <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--text-muted);">STRATEGY & ARCHITECTURE</span>
            </div>
            <h2>Strategy: Defining The Unfair Market Advantage</h2>
            <p style="margin: 12px 0 16px;">
              We distill our discovery insights into a singular strategic campaign angle. We determine which emotional triggers to pull, which media channels to prioritize, and what messages will separate your brand from existing alternatives.
            </p>
            <ul class="deliverables-list">
              <li>Campaign Positioning Thesis & Core Value Proposition</li>
              <li>Omnichannel Media Plan (Search, Social, Display, Outdoor)</li>
              <li>Funnel Architecture & Tracking Milestone Definitions</li>
            </ul>
          </div>

          <!-- Step 3 -->
          <div class="card" style="border-left: 6px solid var(--accent-highlight);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <span class="badge badge-violet">Step 03</span>
              <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--text-muted);">CREATIVE & ART DIRECTION</span>
            </div>
            <h2>Creative Development: Crafting Scroll-Stopping Assets</h2>
            <p style="margin: 12px 0 16px;">
              Our creative director, copywriters, and visual designers translate strategy into visceral reality. We build key visuals, storyboard video commercials, write magnetic ad headlines, and design pixel-perfect ad variations.
            </p>
            <ul class="deliverables-list">
              <li>Master Key Visuals (KV) and Campaign Design Systems</li>
              <li>Persuasive Ad Copywriting & Headline Matrix</li>
              <li>Commercial Video Storyboards and Motion Sequences</li>
            </ul>
          </div>

          <!-- Step 4 -->
          <div class="card" style="border-left: 6px solid #FFF;">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <span class="badge" style="background: rgba(255,255,255,0.1);">Step 04</span>
              <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--text-muted);">EXECUTION & LAUNCH</span>
            </div>
            <h2>Execution: Coordinating Flawless Media Deployment</h2>
            <p style="margin: 12px 0 16px;">
              Once creative assets are approved, our performance operations team prepares production deliveries, sets up advertising account architectures, verifies tracking events, and coordinates seamless live deployments.
            </p>
            <ul class="deliverables-list">
              <li>Campaign Pixel Integration & Conversion Event Setup</li>
              <li>Ad Set Deployment across Google, Meta & Partner Networks</li>
              <li>Production Asset Delivery for Print & Outdoor Vendors</li>
            </ul>
          </div>

          <!-- Step 5 -->
          <div class="card" style="border-left: 6px solid var(--accent-main);">
            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 12px;">
              <span class="badge badge-coral">Step 05</span>
              <span style="font-family: var(--font-mono); font-size: 0.82rem; color: var(--text-muted);">REVIEW & OPTIMIZATION</span>
            </div>
            <h2>Review & Optimization: Continuous Performance Scaling</h2>
            <p style="margin: 12px 0 16px;">
              A campaign is never finished at launch. We continuously monitor engagement, prune fatigue-prone creatives, reallocate budgets to high-performing cohorts, and provide transparent strategic optimization reports.
            </p>
            <ul class="deliverables-list">
              <li>Weekly Performance & Creative Analysis Audits</li>
              <li>A/B Hook & Headline Testing Cycles</li>
              <li>Strategic Recommendations for Next-Cycle Scaling</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Approvals & Feedback Workflow -->
    <section class="section">
      <div class="container container-narrow">
        <div class="card" style="padding: 36px;">
          <h3 style="margin-bottom: 16px;">Transparent Approvals & Feedback Cycles</h3>
          <p style="margin-bottom: 16px;">
            We believe in complete creative transparency. Every milestone—from initial strategy decks to final master video edits—features dedicated review rounds. You approve all creative assets and budgets prior to public launch.
          </p>
          <div class="demo-disclaimer">Generic Demo Workflow Guidelines</div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_pricing():
    content = f'''
    <!-- Pricing Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Advertising Engagements</span>
        <h1 style="margin: 16px 0;">Flexible Advertising Packages Built for Scale</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Every business has unique campaign requirements, platform priorities, and production scales. Review our structured service packages and customize your project scope.
        </p>
      </div>
    </section>

    <!-- Pricing Cards (3 Packages) -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="pricing-grid">
          <!-- Starter Package -->
          <div class="pricing-card">
            <h3 class="pricing-plan-name">Starter Advertising Package</h3>
            <p class="pricing-tagline">Ideal for growing businesses launching targeted paid campaigns on primary platforms.</p>
            
            <div class="pricing-proposal-callout">
              <span>Request a Custom Proposal</span>
              <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 4px;">Tailored scope based on requirements</div>
            </div>

            <ul class="pricing-features-list">
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 Advertising Platforms (Meta or Google)</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 8–12 Bespoke Creative Ad Assets / Month</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 Short-Form Social Reel Concepts</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Campaign Architecture & Audience Setup</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Bi-Weekly Performance Reporting</li>
            </ul>

            <a href="start-campaign.html" class="btn btn-secondary" style="width: 100%;">Enquire for Starter Scope</a>
          </div>

          <!-- Business Growth Package (Featured) -->
          <div class="pricing-card featured">
            <span class="pricing-badge-popular">Most Popular</span>
            <h3 class="pricing-plan-name">Business Growth Package</h3>
            <p class="pricing-tagline">Engineered for expanding brands seeking multi-channel acquisition and creative dominance.</p>
            
            <div class="pricing-proposal-callout">
              <span>Request a Custom Proposal</span>
              <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 4px;">Tailored scope based on requirements</div>
            </div>

            <ul class="pricing-features-list">
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Up to 4 Platforms (Google, Meta, YouTube, LinkedIn)</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 20–28 Bespoke Creative Ad Assets / Month</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 4 High-Production Video Commercials / Reels</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Dedicated Brand Strategy & Copywriting</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Landing Page Conversion Optimization</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Weekly Performance Review & Creative A/B Testing</li>
            </ul>

            <a href="start-campaign.html" class="btn btn-primary" style="width: 100%;">Enquire for Growth Scope</a>
          </div>

          <!-- Custom Campaign Package -->
          <div class="pricing-card">
            <h3 class="pricing-plan-name">Custom Campaign Package</h3>
            <p class="pricing-tagline">Comprehensive 360° campaign strategy for corporate launches, events, and nationwide media.</p>
            
            <div class="pricing-proposal-callout">
              <span>Request a Custom Proposal</span>
              <div style="font-size: 0.76rem; color: var(--text-muted); margin-top: 4px;">Tailored scope based on requirements</div>
            </div>

            <ul class="pricing-features-list">
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Full Omni-Channel Media (Digital, Outdoor, Print)</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Unlimited Creative Concept Iterations</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Cinema-Grade Brand Commercial Production</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Highway Billboard & Transit Pre-Press Delivery</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Dedicated Creative Director & Account Lead</li>
              <li><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Real-Time Analytics Dashboard & Priority Support</li>
            </ul>

            <a href="start-campaign.html" class="btn btn-secondary" style="width: 100%;">Enquire for Custom Scope</a>
          </div>
        </div>

        <!-- Scope Disclaimer -->
        <div class="pricing-disclaimer-box">
          <strong style="color: var(--accent-main); display: block; margin-bottom: 6px;">IMPORTANT NOTE REGARDING ADVERTISING SPEND & PRODUCTION COSTS:</strong>
          Our agency service fees cover strategic planning, creative copywriting, visual design, video editing, ad account setup, and ongoing campaign optimization. All third-party advertising media spend (paid directly to platforms such as Google Ads, Meta Ads, etc.) and physical production costs (outdoor billboard rental, printer fees) are separate and paid directly to respective third-party providers. Final pricing depends on client campaign requirements and approved scope.
        </div>
      </div>
    </section>

    <!-- Interactive Scope Estimator -->
    <section class="section">
      <div class="container container-narrow">
        <div class="section-header text-center">
          <span class="badge badge-lime">Interactive Scope Configurator</span>
          <h2>Estimate Your Campaign Scope</h2>
          <p>Adjust parameters to explore potential creative deliverables for your upcoming campaign.</p>
        </div>

        <div class="card" id="pricing-scope-estimator" style="padding: 36px;">
          <div style="margin-bottom: 24px;">
            <label class="form-label" style="display: block; margin-bottom: 12px;">1. Select Desired Advertising Channels:</label>
            <div class="checkbox-grid">
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check" checked> <span class="checkbox-tile-label">Google Ads (Search & Display)</span></label>
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check" checked> <span class="checkbox-tile-label">Meta Ads (Instagram & Facebook)</span></label>
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check"> <span class="checkbox-tile-label">YouTube Video Ads</span></label>
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check"> <span class="checkbox-tile-label">LinkedIn B2B Ads</span></label>
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check"> <span class="checkbox-tile-label">Outdoor Billboards (OOH)</span></label>
              <label class="checkbox-tile"><input type="checkbox" class="platform-calc-check"> <span class="checkbox-tile-label">Editorial Print Advertising</span></label>
            </div>
          </div>

          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
              <label class="form-label">2. Monthly Creative Ad Assets:</label>
              <span id="val-creatives-count" style="color: var(--accent-secondary); font-weight: 700;">12 Assets</span>
            </div>
            <input type="range" id="slider-creatives-count" min="4" max="40" step="4" value="12" style="width: 100%; accent-color: var(--accent-main);">
          </div>

          <div style="margin-bottom: 24px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 8px;">
              <label class="form-label">3. Monthly Commercial Video / Reels Count:</label>
              <span id="val-video-count" style="color: var(--accent-secondary); font-weight: 700;">2 Videos</span>
            </div>
            <input type="range" id="slider-video-count" min="0" max="10" step="1" value="2" style="width: 100%; accent-color: var(--accent-main);">
          </div>

          <div style="margin-bottom: 24px;">
            <label class="form-label" style="display: block; margin-bottom: 8px;">4. Preferred Campaign Duration:</label>
            <select id="select-duration" class="form-control">
              <option value="Single Launch Flight (1 Month)">Single Launch Flight (1 Month)</option>
              <option value="Quarterly Campaign (3 Months)" selected>Quarterly Campaign (3 Months)</option>
              <option value="Continuous Retainer (6+ Months)">Continuous Retainer (6+ Months)</option>
            </select>
          </div>

          <div style="background: rgba(255,255,255,0.03); border: 1px dashed var(--border-color); border-radius: 8px; padding: 20px; text-align: center; margin-bottom: 24px;">
            <div style="font-size: 0.78rem; text-transform: uppercase; color: var(--text-muted); margin-bottom: 4px;">Configured Campaign Scope Summary:</div>
            <div id="calc-scope-summary" style="font-size: 1.15rem; font-weight: 700; color: #FFF; font-family: var(--font-display);">
              2 Platforms | 12 Creatives/mo | 2 Videos/mo | Quarterly Campaign
            </div>
          </div>

          <a href="start-campaign.html" class="btn btn-primary" style="width: 100%;">Request Proposal for This Scope</a>
        </div>
      </div>
    </section>
    '''
    return content

def generate_technologies():
    content = f'''
    <!-- Technologies Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Tools & Infrastructure</span>
        <h1 style="margin: 16px 0;">Platforms, Tools & Technologies</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          We leverage industry-leading software suites and advertising ecosystems to engineer campaigns with precision and creative velocity.
        </p>
        <div class="demo-disclaimer">Illustrative Platform Capabilities — Not Claims of Official Partnership or Certification</div>
      </div>
    </section>

    <!-- Tech Grid in 4 Categories -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="grid-2" style="gap: 40px;">
          <!-- Category 1 -->
          <div class="card">
            <span class="badge badge-coral" style="margin-bottom: 14px;">Media Ecosystems</span>
            <h3>Advertising Platforms</h3>
            <p style="margin: 12px 0 20px;">Direct configuration and management of audience networks and programmatic distribution.</p>
            <div class="grid-2" style="gap: 16px;">
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Google Ads</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Search, Display, Shopping, YouTube Bumper & In-Stream formats.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Meta Ads Manager</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Instagram Feed, Stories, Reels, Facebook Lead Gen instant forms.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">YouTube Studio</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Video discovery, skippable in-stream, and shorts ad management.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">LinkedIn Campaign Mgr</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">B2B company demographic targeting and sponsored InMail.</p>
              </div>
            </div>
          </div>

          <!-- Category 2 -->
          <div class="card">
            <span class="badge badge-lime" style="margin-bottom: 14px;">Studio Craft</span>
            <h3>Creative & Design Suites</h3>
            <p style="margin: 12px 0 20px;">Industry-standard professional software for visual design, video editing, and motion typography.</p>
            <div class="grid-2" style="gap: 16px;">
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Adobe Photoshop & Illustrator</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Master key visuals, vector identity design, and typography.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Adobe Premiere & After Effects</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Cinema commercial editing, color grading, and motion graphics.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Figma</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Interactive ad prototypes, social design toolkits, and client boards.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Canva Enterprise</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Rapid modular templating for agile client social teams.</p>
              </div>
            </div>
          </div>

          <!-- Category 3 -->
          <div class="card">
            <span class="badge badge-violet" style="margin-bottom: 14px;">Data & Measurement</span>
            <h3>Analytics & Reporting</h3>
            <p style="margin: 12px 0 20px;">Measuring true business engagement, attribution funnels, and landing page performance.</p>
            <div class="grid-2" style="gap: 16px;">
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Google Analytics 4 (GA4)</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Event tracking, user journey analysis, and conversion funnels.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Google Tag Manager</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Server-side and client-side pixel and tag deployments.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Looker Studio</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Automated client reporting dashboards with live metrics.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Custom Attribution Tags</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">UTM parameters and cross-channel conversion validation.</p>
              </div>
            </div>
          </div>

          <!-- Category 4 -->
          <div class="card">
            <span class="badge" style="margin-bottom: 14px; background: rgba(255,255,255,0.1);">Future-Ready</span>
            <h3>AI-Assisted Creative Workflows</h3>
            <p style="margin: 12px 0 20px;">Harnessing cutting-edge artificial intelligence to accelerate ideation and storyboard velocity.</p>
            <div class="grid-2" style="gap: 16px;">
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">AI Image Generation Pipelines</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Rapid pre-visualization, mood-boarding, and style testing.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">AI Video Generation Tools</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Motion storyboard generation and visual effects ideation.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">AI Copywriting Systems</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Headline variant brainstorming and multilingual adaptation.</p>
              </div>
              <div style="background: rgba(255,255,255,0.03); padding: 14px; border-radius: 6px;">
                <strong style="color: #FFF;">Automated Voiceover Previews</strong>
                <p style="font-size: 0.82rem; margin-top: 4px;">Rapid scratch-audio pacing for commercial video animatics.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_careers():
    content = f'''
    <!-- Careers Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Talent & Culture</span>
        <h1 style="margin: 16px 0;">Build Outstanding Advertising With Us</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          We are always searching for gifted visual designers, copywriters, video editors, and digital advertising strategists who obsess over craft.
        </p>
        <div class="demo-disclaimer">Illustrative Sample Career Listings — Frontend Application Demo</div>
      </div>
    </section>

    <!-- Sample Positions Grid -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="grid-3" style="margin-bottom: 60px;">
          <div class="card">
            <span class="badge badge-coral" style="margin-bottom: 12px;">Creative Design</span>
            <h4>Senior Graphic Designer</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Leading campaign key visuals, brand identity manuals, packaging, and high-impact social media creatives.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Full-Time Studio</div>
          </div>

          <div class="card">
            <span class="badge badge-lime" style="margin-bottom: 12px;">Motion & Video</span>
            <h4>Commercial Video Editor</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Editing high-energy commercial reels, sound design, color grading, and short-form social video advertisements.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Full-Time Studio</div>
          </div>

          <div class="card">
            <span class="badge badge-violet" style="margin-bottom: 12px;">Paid Media</span>
            <h4>Digital Advertising Strategist</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Managing multi-platform Google & Meta ad accounts, conversion funnels, and data analytics.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Full-Time Studio</div>
          </div>

          <div class="card">
            <span class="badge" style="margin-bottom: 12px; background: rgba(255,255,255,0.1);">Strategy & Copy</span>
            <h4>Advertising Copywriter</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Writing magnetic ad headlines, brand storytelling scripts, campaign concepts, and persuasive landing page copy.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Full-Time Studio</div>
          </div>

          <div class="card">
            <span class="badge badge-coral" style="margin-bottom: 12px;">Social Operations</span>
            <h4>Social Media Manager</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Curating editorial schedules, creator partnerships, community discourse, and trends monitoring.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Full-Time Studio</div>
          </div>

          <div class="card">
            <span class="badge badge-lime" style="margin-bottom: 12px;">Emerging Talent</span>
            <h4>Creative Advertising Intern</h4>
            <p style="font-size: 0.88rem; margin: 8px 0 16px;">Hands-on exposure to live campaign conceptualization, design research, and digital advertising production.</p>
            <div style="font-size: 0.76rem; color: var(--text-muted);">Sample Profile • Internship Track</div>
          </div>
        </div>

        <!-- Frontend Demo Application Form -->
        <div class="container-narrow">
          <div class="card" style="padding: 36px;">
            <div class="section-header text-center" style="margin-bottom: 30px;">
              <span class="badge badge-coral">Frontend Demo Form</span>
              <h3>Submit An Illustrative Application</h3>
              <p>Experience our frontend application submission interaction. No actual applicant data is saved or transmitted.</p>
            </div>

            <form id="careers-application-form">
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Full Name *</label>
                  <input type="text" name="applicant_name" class="form-control" placeholder="Your Full Name" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Email Address *</label>
                  <input type="email" name="applicant_email" class="form-control" placeholder="you@example.com" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Phone Number *</label>
                  <input type="tel" name="applicant_phone" class="form-control" placeholder="0000000000" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Role of Interest</label>
                  <select name="applicant_role" class="form-control">
                    <option>Senior Graphic Designer</option>
                    <option>Commercial Video Editor</option>
                    <option>Digital Advertising Strategist</option>
                    <option>Advertising Copywriter</option>
                    <option>Social Media Manager</option>
                    <option>Creative Advertising Intern</option>
                  </select>
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Portfolio URL / Link</label>
                  <input type="url" name="applicant_portfolio" class="form-control" placeholder="https://yourportfolio.demo">
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Brief Note / Creative Introduction</label>
                  <textarea name="applicant_note" rows="4" class="form-control" placeholder="Tell us about your creative background..."></textarea>
                </div>
              </div>
              <div style="text-align: center; margin-top: 24px;">
                <button type="submit" class="btn btn-primary">Submit Demo Application</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_blog():
    articles = [
        ("Why Advertising Matters for Growing Businesses", "strategy", "March 2027", "6 min read", "Why passive word-of-mouth is not enough to survive in saturated markets, and how proactive advertising builds lasting pricing power.", "blog-thumb-1.webp"),
        ("How to Create Effective Social Media Ads", "social", "March 2027", "5 min read", "Deconstructing the first 3 seconds of a social ad: hook architecture, sound design, and mobile-native typography.", "blog-thumb-2.webp"),
        ("Google Ads vs Meta Ads: Choosing The Right Channel", "performance", "February 2027", "8 min read", "Comparing search intent capture versus social demand generation, and how to balance your budget between both ecosystems.", "blog-thumb-3.webp"),
        ("Why Video Advertising Works Better Than Static", "video", "February 2027", "7 min read", "The cognitive psychology of motion, sound, and visual emotion in driving superior brand recall and purchase intent.", "blog-thumb-4.webp"),
        ("Building a Strong Brand Identity in Competitive Markets", "branding", "January 2027", "9 min read", "Why a logo is just the beginning: creating typography systems, color rules, and brand voices that cannot be cloned.", "blog-thumb-5.webp"),
        ("How to Plan a Product Launch Advertising Campaign", "strategy", "January 2027", "8 min read", "The multi-flight campaign roadmap: teasing desire, orchestrating launch momentum, and maintaining sustained sales.", "blog-thumb-6.webp"),
        ("How Reels Advertising Can Support Brand Awareness", "social", "December 2026", "5 min read", "Mastering vertical 9:16 storytelling, pacing, trending audio aesthetics, and native in-app conversion hooks.", "blog-thumb-7.webp"),
        ("Common Advertising Mistakes Growing Brands Make", "strategy", "December 2026", "6 min read", "From changing creative too quickly to optimizing for vanity clicks instead of real commercial enquiry value.", "blog-thumb-8.webp"),
        ("How to Build a Campaign Creative Strategy", "branding", "November 2026", "7 min read", "Bridging the gap between spreadsheet data and evocative human emotions that prompt real-world action.", "blog-thumb-9.webp"),
        ("How to Measure Advertising Performance Accurately", "performance", "November 2026", "8 min read", "Moving beyond surface CTR to analyze cost-per-qualified-enquiry, blend CAC, and long-term customer value.", "blog-thumb-10.webp"),
    ]

    cards_html = ""
    for title, cat, date, read_time, excerpt, img_file in articles:
        cards_html += f'''
        <div class="card blog-card" data-category="{cat}" style="padding: 0; overflow: hidden;">
          {placeholder_html(img_file, title, "800x450", "aspect-16-9", "blog.html", "Articles",
                            f"Editorial header visual for article: {title}",
                            f"Editorial magazine photograph representing {title}, dark background, sharp typography book layout, 8k, no text, no logos.")}
          <div style="padding: 24px; display: flex; flex-direction: column; flex-grow: 1;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <span class="badge badge-coral" style="text-transform: capitalize;">{cat}</span>
              <span style="font-size: 0.76rem; color: var(--text-muted);">{read_time}</span>
            </div>
            <h3 class="blog-title" style="font-size: 1.2rem; margin-bottom: 10px;">{title}</h3>
            <p class="blog-excerpt" style="font-size: 0.88rem; margin-bottom: 16px;">{excerpt}</p>
            <div class="demo-disclaimer" style="margin-bottom: 16px;">Sample Demo Article</div>
            <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px solid var(--border-subtle);">
              <span style="font-size: 0.78rem; color: var(--text-muted);">{date}</span>
              <a href="contact.html" class="btn-link">Read More →</a>
            </div>
          </div>
        </div>
        '''

    content = f'''
    <!-- Blog Hero & Featured Post -->
    <section class="section section-hero">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-coral">Editorial & Insights</span>
          <h1 style="margin: 16px 0;">Advertising Thinking & Market Insights</h1>
          <p class="lead-text" style="margin: 0 auto 32px;">
            Perspectives on creative direction, media strategy, consumer psychology, and brand differentiation.
          </p>
          <div class="demo-disclaimer">Illustrative Editorial Sample Content</div>
        </div>

        <!-- Featured Post Spotlight -->
        <div class="card" style="padding: 0; overflow: hidden; margin-top: 30px;">
          <div class="grid-2" style="align-items: center;">
            {placeholder_html("blog-featured-hero.webp", "Featured Insight: The Architecture of Unforgettable Advertising", "1200x800", "aspect-16-9", "blog.html", "Featured Article",
                              "Architectural concrete monolith in vast desert landscape representing monumental brand permanence",
                              "Cinematic architectural photography of an obsidian monument standing in dramatic windswept desert at dusk, vivid coral horizon, atmospheric fog, 8k, no text, no logos.")}
            <div style="padding: 40px;">
              <span class="badge badge-lime" style="margin-bottom: 12px;">Featured Essay</span>
              <h2 style="font-size: 2rem; margin-bottom: 14px;">The Architecture of Unforgettable Advertising</h2>
              <p style="margin-bottom: 20px;">
                Why the greatest advertising campaigns in history do not sell features, but reorganize how human beings perceive their own status, belonging, and desires.
              </p>
              <div style="display: flex; gap: 16px; align-items: center; font-size: 0.82rem; color: var(--text-muted); margin-bottom: 24px;">
                <span>Editorial Team</span>
                <span>•</span>
                <span>March 2027</span>
                <span>•</span>
                <span>10 min read</span>
              </div>
              <a href="contact.html" class="btn btn-primary">Read Master Essay</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Search & Filter Controls -->
    <section class="section section-bg-secondary" style="padding-top: 40px;">
      <div class="container">
        <div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: space-between; align-items: center; margin-bottom: 40px;">
          <div style="display: flex; flex-wrap: wrap; gap: 10px;">
            <button class="filter-btn blog-filter-tag active" data-category="all">All Topics</button>
            <button class="filter-btn blog-filter-tag" data-category="strategy">Strategy</button>
            <button class="filter-btn blog-filter-tag" data-category="social">Social Media</button>
            <button class="filter-btn blog-filter-tag" data-category="performance">Performance & Ads</button>
            <button class="filter-btn blog-filter-tag" data-category="video">Video & Motion</button>
            <button class="filter-btn blog-filter-tag" data-category="branding">Branding & Design</button>
          </div>
          <div style="width: 100%; max-width: 320px;">
            <input type="text" id="blog-search-input" class="form-control" placeholder="Search insights by keyword...">
          </div>
        </div>

        <div class="grid-3">
          {cards_html}
        </div>
      </div>
    </section>
    '''
    return content

def generate_faq():
    faq_data = [
        ("General", [
            ("What advertising services do you offer?", "We provide end-to-end advertising and brand strategy solutions spanning digital advertising (Google, Meta, YouTube, LinkedIn), creative design, commercial video production, brand strategy, graphic design, content marketing, influencer marketing, outdoor billboards, and editorial print media."),
            ("How long does campaign planning take?", "Standard digital advertising campaigns typically require 1 to 2 weeks for discovery, audience modeling, copywriting, and creative asset production. Full 360° commercial launches involving video production or outdoor media generally take 3 to 5 weeks."),
            ("Can I request a custom advertising package?", "Yes. While we present structured starter and growth packages for convenience, most of our client engagements are custom-tailored based on target channels, required creative volume, and market objectives.")
        ]),
        ("Advertising Services & Management", [
            ("Which platforms can you advertise on?", "We manage advertising campaigns across Google Search, Google Display, Google Shopping, YouTube, Instagram, Facebook, LinkedIn, programmatic outdoor digital LED networks, and print publications."),
            ("Do you manage Google Ads campaigns?", "Yes. We configure and manage high-intent Google Search campaigns, Display Remarketing, Shopping feeds, and YouTube video ads with complete conversion tracking and bid optimization."),
            ("Can you create Meta Ads campaigns?", "Yes. We design and manage Facebook and Instagram campaigns, including Feed, Stories, Reels, carousel ads, and direct lead generation instant forms."),
            ("Do you provide campaign reports?", "Yes. Clients receive regular transparent performance reports breaking down impressions, qualified enquiries, audience responsiveness, and strategic optimization recommendations.")
        ]),
        ("Creative Design & Video", [
            ("Do you provide advertising creatives?", "Yes. All creative concepts, key visuals, graphic design assets, social media banners, and carousel graphics are crafted in-house by our dedicated art direction team."),
            ("Do you create promotional videos?", "Yes. We script, storyboard, shoot, and edit commercial brand films, social media reels, 3D product animations, and short-form video advertisements.")
        ]),
        ("Pricing & Budget Scopes", [
            ("How is advertising pricing calculated?", "Our agency service fees are determined by campaign scope, number of media platforms managed, creative asset production volume, and reporting frequency."),
            ("Is the advertising budget included in agency fees?", "No. To maintain complete financial transparency, agency service fees are separate from third-party advertising media spend (which is paid directly to platforms like Google or Meta)."),
            ("Do you require long-term contracts?", "We offer both individual launch campaign flights (1 to 3 months) and ongoing strategic monthly retainers based on your commercial preferences.")
        ])
    ]

    accordion_html = ""
    for category_name, items in faq_data:
        items_html = ""
        for q, a in items:
            items_html += f'''
            <div class="accordion-item">
              <button class="accordion-header">
                <span>{q}</span>
                <div class="accordion-icon">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </div>
              </button>
              <div class="accordion-content">
                <p>{a}</p>
              </div>
            </div>
            '''
        accordion_html += f'''
        <div style="margin-bottom: 36px;">
          <h3 style="font-size: 1.3rem; color: var(--accent-secondary); margin-bottom: 16px; text-transform: uppercase; letter-spacing: 0.05em;">{category_name}</h3>
          <div class="faq-accordion">
            {items_html}
          </div>
        </div>
        '''

    content = f'''
    <!-- FAQ Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Frequently Asked Questions</span>
        <h1 style="margin: 16px 0;">Everything You Need to Know</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          Find clear answers regarding our advertising services, platform capabilities, creative workflows, pricing structures, and reporting routines.
        </p>
      </div>
    </section>

    <!-- Accordion Section -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container container-narrow">
        {accordion_html}
      </div>
    </section>
    '''
    return content

def generate_contact():
    content = f'''
    <!-- Contact Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="gap: 48px; align-items: start;">
          <div>
            <span class="badge badge-coral">Connect With Strategists</span>
            <h1 style="margin: 16px 0;">Have a Campaign in Mind? Let's Talk.</h1>
            <p class="lead-text" style="margin-bottom: 32px;">
              Whether you are preparing a major product launch, scaling your digital lead flow, or reimagining your brand key visuals, we are here to discuss your goals.
            </p>

            <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 28px; margin-bottom: 28px;">
              <h3 style="font-size: 1.2rem; margin-bottom: 16px; color: var(--accent-secondary);">Demonstration Contact Details</h3>
              
              <div style="display: flex; flex-direction: column; gap: 14px; font-size: 0.95rem;">
                <div>
                  <span style="color: var(--text-muted); display: block; font-size: 0.8rem; text-transform: uppercase;">Direct Telephone:</span>
                  <strong style="color: #FFF;">0000000000</strong>
                </div>
                <div>
                  <span style="color: var(--text-muted); display: block; font-size: 0.8rem; text-transform: uppercase;">Alternative Contact:</span>
                  <strong style="color: #FFF;">0000000000</strong>
                </div>
                <div>
                  <span style="color: var(--text-muted); display: block; font-size: 0.8rem; text-transform: uppercase;">Email Enquiries:</span>
                  <strong style="color: #FFF;">demo@example.com</strong>
                </div>
                <div>
                  <span style="color: var(--text-muted); display: block; font-size: 0.8rem; text-transform: uppercase;">Studio Location:</span>
                  <span style="color: var(--text-secondary);">Plot No. 000, Demo Road, Sample Area, Hyderabad, Telangana – 000000.</span>
                </div>
                <div>
                  <span style="color: var(--text-muted); display: block; font-size: 0.8rem; text-transform: uppercase;">Working Hours:</span>
                  <span style="color: var(--text-secondary);">Monday–Saturday: 9:00 AM–6:00 PM</span>
                </div>
              </div>
              <div class="demo-disclaimer" style="margin-top: 16px;">Demonstration Details Only</div>
            </div>
          </div>

          <!-- Contact Form with Validation -->
          <div class="card" style="padding: 36px;">
            <h3 style="margin-bottom: 8px;">Project Enquiry Form</h3>
            <p style="font-size: 0.88rem; margin-bottom: 24px;">Complete the form below to receive an illustrative campaign briefing response.</p>

            <form id="agency-contact-form">
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Full Name *</label>
                  <input type="text" name="name" class="form-control" placeholder="Your Name" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Email Address *</label>
                  <input type="email" name="email" class="form-control" placeholder="you@company.com" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Phone Number *</label>
                  <input type="tel" name="phone" class="form-control" placeholder="0000000000" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Business Name</label>
                  <input type="text" name="business" class="form-control" placeholder="Company Name">
                </div>
                <div class="form-group">
                  <label class="form-label">Industry</label>
                  <select name="industry" class="form-control">
                    <option>Real Estate</option>
                    <option>Healthcare</option>
                    <option>Education</option>
                    <option>Fashion & Apparel</option>
                    <option>E-commerce</option>
                    <option>Restaurants & Food</option>
                    <option>Hospitality</option>
                    <option>Technology / SaaS</option>
                    <option>Other Category</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label">Primary Service Required</label>
                  <select name="service" class="form-control">
                    <option>Digital Advertising</option>
                    <option>Social Media Advertising</option>
                    <option>Commercial Video Advertising</option>
                    <option>Creative Design & Branding</option>
                    <option>Lead Generation Funnels</option>
                    <option>Full 360° Campaign Package</option>
                  </select>
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Campaign Objective</label>
                  <input type="text" name="objective" class="form-control" placeholder="e.g. Brand awareness, product launch, or lead generation">
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Tell Us About Your Campaign</label>
                  <textarea name="message" rows="4" class="form-control" placeholder="Brief description of requirements, target timeline..."></textarea>
                </div>
              </div>

              <div style="margin-top: 16px;">
                <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Demo Enquiry</button>
              </div>
              <div style="text-align: center; margin-top: 12px; font-size: 0.76rem; color: var(--text-muted);">
                Static Demonstration: No real data will be stored or transmitted.
              </div>
            </form>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_start_campaign():
    content = f'''
    <!-- Multi-Step Campaign Enquiry Form Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <span class="badge badge-coral">Interactive Campaign Wizard</span>
        <h1 style="margin: 16px 0;">Start Your Campaign Enquiry</h1>
        <p class="lead-text" style="margin: 0 auto 32px;">
          A guided 6-step campaign planner designed to clarify your target audience, services, budget, and media objectives.
        </p>
      </div>
    </section>

    <!-- Multi-step Form Container -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container">
        <div class="multistep-container">
          <!-- Step Indicator Bar -->
          <div class="step-indicator-bar">
            <div class="step-indicator-progress"></div>
            
            <div class="step-node active" data-step="1">
              <div class="step-circle">1</div>
              <span class="step-title">Business</span>
            </div>
            <div class="step-node" data-step="2">
              <div class="step-circle">2</div>
              <span class="step-title">Campaign</span>
            </div>
            <div class="step-node" data-step="3">
              <div class="step-circle">3</div>
              <span class="step-title">Services</span>
            </div>
            <div class="step-node" data-step="4">
              <div class="step-circle">4</div>
              <span class="step-title">Budget</span>
            </div>
            <div class="step-node" data-step="5">
              <div class="step-circle">5</div>
              <span class="step-title">Details</span>
            </div>
            <div class="step-node" data-step="6">
              <div class="step-circle">6</div>
              <span class="step-title">Review</span>
            </div>
          </div>

          <form id="multistep-campaign-form">
            <!-- STEP 1: Business Information -->
            <div class="form-step active" data-step="1">
              <h3 style="margin-bottom: 8px;">Step 1 — Business Information</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">Tell us about yourself and your company.</p>
              
              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Full Name *</label>
                  <input type="text" name="client_name" class="form-control" placeholder="Alex Morgan" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Business Name *</label>
                  <input type="text" name="business_name" class="form-control" placeholder="Apex Enterprises" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Work Email *</label>
                  <input type="email" name="client_email" class="form-control" placeholder="alex@apex.demo" required>
                </div>
                <div class="form-group">
                  <label class="form-label">Phone Number *</label>
                  <input type="tel" name="client_phone" class="form-control" placeholder="0000000000" required>
                </div>
              </div>

              <div class="step-buttons">
                <div></div>
                <button type="button" class="btn btn-primary btn-step-next">Next: Campaign Info →</button>
              </div>
            </div>

            <!-- STEP 2: Campaign Information -->
            <div class="form-step" data-step="2">
              <h3 style="margin-bottom: 8px;">Step 2 — Campaign Information</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">What product or service are we promoting?</p>

              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Industry *</label>
                  <select name="industry" class="form-control" required>
                    <option value="Real Estate">Real Estate</option>
                    <option value="Healthcare">Healthcare</option>
                    <option value="Education">Education</option>
                    <option value="Fashion & Apparel">Fashion & Apparel</option>
                    <option value="E-commerce">E-commerce</option>
                    <option value="Restaurants & Food">Restaurants & Food</option>
                    <option value="Hospitality">Hospitality</option>
                    <option value="Technology">Technology</option>
                    <option value="Other">Other Category</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label">Product / Service Name *</label>
                  <input type="text" name="product_name" class="form-control" placeholder="e.g. New Autumn Collection / Luxury Villas" required>
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Primary Campaign Objective *</label>
                  <select name="objective" class="form-control" required>
                    <option value="Brand Awareness & Prestige">Brand Awareness & Prestige</option>
                    <option value="Direct High-Intent Enquiries">Direct High-Intent Enquiries / Leads</option>
                    <option value="New Product Launch Acceleration">New Product Launch Acceleration</option>
                    <option value="Online E-commerce Sales Scale">Online E-commerce Sales Scale</option>
                    <option value="Event Promotion & Ticket Bookings">Event Promotion & Ticket Bookings</option>
                  </select>
                </div>
              </div>

              <div class="step-buttons">
                <button type="button" class="btn btn-secondary btn-step-prev">← Back</button>
                <button type="button" class="btn btn-primary btn-step-next">Next: Advertising Requirements →</button>
              </div>
            </div>

            <!-- STEP 3: Advertising Requirements -->
            <div class="form-step" data-step="3">
              <h3 style="margin-bottom: 8px;">Step 3 — Advertising Requirements</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">Select all required advertising and creative capabilities.</p>

              <div class="checkbox-grid">
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Social Media Advertising" checked> <span class="checkbox-tile-label">Social Media Advertising</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Google Search & Display" checked> <span class="checkbox-tile-label">Google Ads (Search & Display)</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Commercial Video Production"> <span class="checkbox-tile-label">Commercial Video Advertising</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Creative Design & Key Visuals"> <span class="checkbox-tile-label">Creative Design & Key Visuals</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Brand Strategy & Messaging"> <span class="checkbox-tile-label">Brand Strategy & Messaging</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Influencer Collaborations"> <span class="checkbox-tile-label">Influencer Marketing</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Outdoor Billboards (OOH)"> <span class="checkbox-tile-label">Outdoor Advertising</span></label>
                <label class="checkbox-tile"><input type="checkbox" name="services" value="Print Media Collateral"> <span class="checkbox-tile-label">Print Advertising</span></label>
              </div>

              <div class="step-buttons">
                <button type="button" class="btn btn-secondary btn-step-prev">← Back</button>
                <button type="button" class="btn btn-primary btn-step-next">Next: Budget & Timeline →</button>
              </div>
            </div>

            <!-- STEP 4: Budget and Timeline -->
            <div class="form-step" data-step="4">
              <h3 style="margin-bottom: 8px;">Step 4 — Budget & Timeline</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">Provide an estimated range to help us structure realistic recommendations.</p>

              <div class="form-grid">
                <div class="form-group">
                  <label class="form-label">Estimated Monthly Ad Spend (Paid to Platforms) *</label>
                  <select name="ad_budget" class="form-control" required>
                    <option value="Starter Allocation">Starter Allocation</option>
                    <option value="Growth Scale Allocation" selected>Growth Scale Allocation</option>
                    <option value="Aggressive Expansion Allocation">Aggressive Expansion Allocation</option>
                    <option value="Enterprise Nationwide Allocation">Enterprise Nationwide Allocation</option>
                  </select>
                </div>
                <div class="form-group">
                  <label class="form-label">Agency Creative & Management Scope *</label>
                  <select name="agency_budget" class="form-control" required>
                    <option value="Starter Package">Starter Package</option>
                    <option value="Business Growth Package" selected>Business Growth Package</option>
                    <option value="Custom 360 Campaign Package">Custom 360 Campaign Package</option>
                  </select>
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Preferred Launch Timeline *</label>
                  <select name="launch_timeline" class="form-control" required>
                    <option value="Immediate (Within 1-2 weeks)">Immediate (Within 1-2 weeks)</option>
                    <option value="Next Month (2-4 weeks)" selected>Next Month (2-4 weeks)</option>
                    <option value="Upcoming Quarter (1-3 months)">Upcoming Quarter (1-3 months)</option>
                    <option value="Exploratory Planning Only">Exploratory Planning Only</option>
                  </select>
                </div>
              </div>

              <div class="step-buttons">
                <button type="button" class="btn btn-secondary btn-step-prev">← Back</button>
                <button type="button" class="btn btn-primary btn-step-next">Next: Additional Details →</button>
              </div>
            </div>

            <!-- STEP 5: Additional Details -->
            <div class="form-step" data-step="5">
              <h3 style="margin-bottom: 8px;">Step 5 — Additional Details</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">Help us understand your target audience and specific vision.</p>

              <div class="form-grid">
                <div class="form-group full-width">
                  <label class="form-label">Target Audience Description</label>
                  <input type="text" name="target_audience" class="form-control" placeholder="e.g. Urban business owners, luxury property investors aged 30-55">
                </div>
                <div class="form-group full-width">
                  <label class="form-label">Campaign Brief / Special Requirements</label>
                  <textarea name="campaign_notes" rows="4" class="form-control" placeholder="Share any specific creative inspirations, tone preferences, or competitor reference points..."></textarea>
                </div>
              </div>

              <div class="step-buttons">
                <button type="button" class="btn btn-secondary btn-step-prev">← Back</button>
                <button type="button" class="btn btn-primary btn-step-next">Review Campaign Brief →</button>
              </div>
            </div>

            <!-- STEP 6: Review & Submit -->
            <div class="form-step" data-step="6">
              <h3 style="margin-bottom: 8px;">Step 6 — Review & Submit</h3>
              <p style="font-size: 0.88rem; margin-bottom: 24px;">Please review your compiled campaign briefing details before submitting.</p>

              <div id="campaign-review-summary" style="margin-bottom: 24px;">
                <!-- Dynamically populated via JS -->
              </div>

              <div class="demo-disclaimer-box">
                <div>
                  <strong>DEMONSTRATION SUBMISSION:</strong> This multi-step wizard is a frontend prototype. Clicking submit will demonstrate form validation and a confirmation message. No information will be transmitted or stored on an external server.
                </div>
              </div>

              <div class="step-buttons">
                <button type="button" class="btn btn-secondary btn-step-prev">← Edit Details</button>
                <button type="button" class="btn btn-lime btn-step-submit">Submit Campaign Brief (Demo)</button>
              </div>
            </div>
          </form>

          <!-- Success Card (Revealed via JS) -->
          <div id="campaign-demo-success" style="display: none; text-align: center; padding: 40px 20px;">
            <div style="width: 64px; height: 64px; border-radius: 50%; background: rgba(217, 255, 67, 0.15); border: 2px solid var(--accent-secondary); color: var(--accent-secondary); display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            <h2 style="margin-bottom: 12px;">Demo Campaign Brief Received!</h2>
            <p style="max-width: 580px; margin: 0 auto 24px; color: var(--text-secondary);">
              Your illustrative campaign enquiry has been compiled successfully. In an actual agency environment, our creative director and media planners would review this brief and deliver an initial proposal within 48 hours.
            </p>
            <div class="demo-disclaimer" style="margin-bottom: 24px;">Frontend Demo Only — No Server Data Transmitted</div>
            <div>
              <a href="index.html" class="btn btn-primary">Return to Homepage</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_privacy():
    content = f'''
    <!-- Privacy Policy Hero -->
    <section class="section section-hero">
      <div class="container container-narrow">
        <span class="badge badge-coral">Legal & Privacy</span>
        <h1 style="margin: 16px 0;">Privacy Policy</h1>
        <p class="lead-text" style="margin-bottom: 24px;">
          Demonstration Website Privacy Documentation & Data Notice.
        </p>
        <div class="demo-disclaimer">Sample Policy — Requires Professional Review Before Commercial Use</div>
      </div>
    </section>

    <!-- Privacy Content -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container container-narrow">
        <div class="card" style="padding: 40px; display: flex; flex-direction: column; gap: 24px;">
          <div>
            <h3>1. Demonstration Website Scope</h3>
            <p style="margin-top: 8px;">
              This website is an illustrative demonstration created for an advertising agency portfolio showcase. It uses generic brand identities and demonstration dummy contact information.
            </p>
          </div>

          <div>
            <h3>2. Information Entered in Forms</h3>
            <p style="margin-top: 8px;">
              All forms on this website—including the Contact Form, the Multi-Step Campaign Enquiry Form, and the Careers Application Form—are frontend demonstrations. Form submissions do not transmit, process, or store personal or commercial information on any external server or database.
            </p>
          </div>

          <div>
            <h3>3. Cookies and Browser Storage</h3>
            <p style="margin-top: 8px;">
              This static website does not set commercial advertising cookies, tracking pixels, or third-party profiling cookies. Any client-side state is handled transiently in memory for demonstration purposes only.
            </p>
          </div>

          <div>
            <h3>4. Analytics & Measurement</h3>
            <p style="margin-top: 8px;">
              Dashboards and metric charts shown on this website represent illustrative campaign mockups only. They do not represent live tracking or telemetry from actual advertising accounts.
            </p>
          </div>

          <div>
            <h3>5. Contact Information</h3>
            <p style="margin-top: 8px;">
              The phone numbers (0000000000) and email address (demo@example.com) displayed across this website are dummy placeholders intended for demonstration layout purposes only.
            </p>
          </div>

          <div>
            <h3>6. Policy Updates & Commercial Notice</h3>
            <p style="margin-top: 8px;">
              If this website template is adapted for real commercial operations, the site owner must draft and publish a formal privacy policy aligned with applicable data protection laws (such as GDPR, CCPA, or the Digital Personal Data Protection Act).
            </p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_terms():
    content = f'''
    <!-- Terms & Conditions Hero -->
    <section class="section section-hero">
      <div class="container container-narrow">
        <span class="badge badge-coral">Terms of Service</span>
        <h1 style="margin: 16px 0;">Terms & Conditions</h1>
        <p class="lead-text" style="margin-bottom: 24px;">
          Demonstration Website Usage Guidelines & General Terms.
        </p>
        <div class="demo-disclaimer">Sample Terms — Requires Professional Review Before Commercial Use</div>
      </div>
    </section>

    <!-- Terms Content -->
    <section class="section section-bg-secondary" style="padding-top: 0;">
      <div class="container container-narrow">
        <div class="card" style="padding: 40px; display: flex; flex-direction: column; gap: 24px;">
          <div>
            <h3>1. Website Usage & Purpose</h3>
            <p style="margin-top: 8px;">
              This website is provided as a static frontend demonstration designed to showcase creative advertising agency capabilities, campaign concepts, advertising mockups, and interaction design.
            </p>
          </div>

          <div>
            <h3>2. Illustrative Demo Campaigns</h3>
            <p style="margin-top: 8px;">
              All campaign case studies, portfolio projects, creative designs, and client names featured on this site are generic demonstration concepts. No actual client endorsements, affiliations, or live advertising results are claimed or implied.
            </p>
          </div>

          <div>
            <h3>3. Advertising Proposals & Agency Fees</h3>
            <p style="margin-top: 8px;">
              Any pricing packages, deliverables lists, or interactive scope calculators displayed on this website represent illustrative frameworks only. Actual commercial contracts require signed scope-of-work agreements.
            </p>
          </div>

          <div>
            <h3>4. Third-Party Media Spend & Production Costs</h3>
            <p style="margin-top: 8px;">
              Agency service fees cover creative conceptualization, copywriting, visual production, and media coordination. All third-party media advertising spend (paid directly to platforms such as Google, Meta, or out-of-home media owners) remains the sole financial responsibility of the advertising client.
            </p>
          </div>

          <div>
            <h3>5. Platform Policies & Compliance</h3>
            <p style="margin-top: 8px;">
              All live advertising campaigns deployed on third-party networks are subject to the advertising policies, community standards, and ad approval guidelines of the respective platform operators (Google, Meta, etc.).
            </p>
          </div>

          <div>
            <h3>6. Limitation of Liability</h3>
            <p style="margin-top: 8px;">
              This demonstration website is provided on an "as is" and "as available" basis without warranties of any kind. The creators accept no liability for reliance placed on demonstration content.
            </p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

print("Core pages generators loaded.")
