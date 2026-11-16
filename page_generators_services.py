# -*- coding: utf-8 -*-
"""
ADVERTISING AGENCY — Services Pages Generators (14 Dedicated Service Pages)
"""

from build_site import placeholder_html

def generate_digital_advertising():
    content = f'''
    <!-- Digital Advertising Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Multi-Channel Growth Engine</span>
            <h1 style="margin: 16px 0;">Digital Advertising Strategy & Multi-Platform Execution</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              From high-intent acquisition campaigns to multi-touch retargeting architecture, we engineer digital advertising systems designed to capture attention and scale business revenue.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="contact.html" class="btn btn-secondary">Request Consultation</a>
            </div>
          </div>
          <div>
            {placeholder_html("digital-advertising-hero.webp", "Digital Advertising Campaign Master", "1920x1080", "aspect-16-9", "digital-advertising.html", "Hero Section",
                              "Futuristic high-tech digital media analytics room with multi-screen ad dashboard visualizations",
                              "Cinematic commercial advertising photography of a creative control dashboard display showing digital advertising metrics, sleek obsidian interface, glowing coral and acid lime graphs, sharp focus, 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Illustrative Digital Ad Dashboard Mockup -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Interactive Analytics Preview</span>
          <h2>Digital Advertising Management Interface</h2>
          <p>An illustrative preview of how cross-platform digital advertising streams, budgets, audience segments, and conversions are monitored.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Demo Dashboard — Not Live Data</div>
        </div>

        <div class="mockup-dashboard">
          <div class="dashboard-metrics-grid">
            <div class="metric-card">
              <div class="metric-label">Cross-Channel Reach (Demo)</div>
              <div class="metric-value">1,480,200</div>
              <div class="metric-trend">↑ 28.4% vs Previous Cycle</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Engagement Interaction</div>
              <div class="metric-value">94,320</div>
              <div class="metric-trend">↑ 14.2% Optimization Lift</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">Target Conversion Actions</div>
              <div class="metric-value">4,810</div>
              <div class="metric-trend">↑ High Intent Enquiries</div>
            </div>
            <div class="metric-card">
              <div class="metric-label">System CTR Index</div>
              <div class="metric-value">3.86%</div>
              <div class="metric-trend">↑ Industry Benchmark Top Tier</div>
            </div>
          </div>

          <div class="dashboard-chart-area">
            <div class="chart-bar-group"><div class="chart-bar" style="height: 45%;"></div><span class="chart-label">W1 Search</span></div>
            <div class="chart-bar-group"><div class="chart-bar secondary" style="height: 60%;"></div><span class="chart-label">W1 Social</span></div>
            <div class="chart-bar-group"><div class="chart-bar" style="height: 70%;"></div><span class="chart-label">W2 Search</span></div>
            <div class="chart-bar-group"><div class="chart-bar secondary" style="height: 85%;"></div><span class="chart-label">W2 Social</span></div>
            <div class="chart-bar-group"><div class="chart-bar" style="height: 90%;"></div><span class="chart-label">W3 Search</span></div>
            <div class="chart-bar-group"><div class="chart-bar secondary" style="height: 95%;"></div><span class="chart-label">W3 Social</span></div>
            <div class="chart-bar-group"><div class="chart-bar" style="height: 100%;"></div><span class="chart-label">W4 Search</span></div>
            <div class="chart-bar-group"><div class="chart-bar secondary" style="height: 100%;"></div><span class="chart-label">W4 Social</span></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Strategic Pillars -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-violet">Execution Architecture</span>
          <h2>Digital Advertising Disciplines</h2>
          <p>Every campaign combines data rigor with standout visual execution across eight dedicated steps.</p>
        </div>

        <div class="grid-4">
          <div class="card">
            <h4>1. Campaign Planning</h4>
            <p>Formulating target objectives, channel selection, competitive benchmarking, and media budget allocation schedules.</p>
          </div>
          <div class="card">
            <h4>2. Audience Targeting</h4>
            <p>Demographic clustering, psychographic mapping, behavioral affinity, in-market audiences, and custom cohort modelling.</p>
          </div>
          <div class="card">
            <h4>3. Creative Development</h4>
            <p>Scroll-stopping ad visual concepts, high-impact headlines, persuasive body copy, and customized call-to-actions.</p>
          </div>
          <div class="card">
            <h4>4. Ad Placement Strategy</h4>
            <p>Strategic channel positioning across desktop, mobile feeds, stories, in-stream video, display, and search intent engines.</p>
          </div>
          <div class="card">
            <h4>5. Landing Page Alignment</h4>
            <p>Ensuring absolute consistency between ad promise, headline copy, visual tone, and clear friction-free enquiry triggers.</p>
          </div>
          <div class="card">
            <h4>6. Conversion Tracking</h4>
            <p>Event tagging architecture, tracking pixel integrations, custom event goals, and multi-device attribution pathways.</p>
          </div>
          <div class="card">
            <h4>7. Active Optimization</h4>
            <p>Continuous creative A/B testing, audience pruning, negative targeting, bid adjustments, and fatigue mitigation.</p>
          </div>
          <div class="card">
            <h4>8. Reporting & Insights</h4>
            <p>Transparent campaign breakdowns, creative performance metrics, and strategic optimization recommendations.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Bottom CTA -->
    <section class="section section-bg-secondary text-center">
      <div class="container container-narrow">
        <h2>Ready to Launch Your Digital Advertising?</h2>
        <p style="margin: 16px auto 28px;">Let us design an integrated digital advertising roadmap tailored to your specific commercial goals.</p>
        <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
      </div>
    </section>
    '''
    return content

def generate_social_media_advertising():
    content = f'''
    <!-- Social Media Advertising Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Social Ad Engine</span>
            <h1 style="margin: 16px 0;">Create Social Campaigns People Stop Scrolling For</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Social media is saturated with noise. We combine cultural insights, bespoke design, cinematic motion, and precise audience targeting to produce ad campaigns that captivate and convert.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Social Work</a>
            </div>
          </div>
          <div>
            {placeholder_html("social-media-hero-collage.webp", "Social Media Advertising Concepts", "1920x1080", "aspect-16-9", "social-media-advertising.html", "Hero Section",
                              "Editorial collage of futuristic smartphones displaying vibrant fashion and product advertisements",
                              "High-fashion commercial social media ad layouts displayed on sleek frameless mobile devices, dark backdrop with vibrant neon coral and acid lime rim lighting, sharp focus, 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Social Mockups Gallery: Story, Feed, Reels -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Creative Ad Mockup Library</span>
          <h2>Platform-Native Creative Formats</h2>
          <p>Explore illustrative social advertisement mockups built for Instagram, Facebook, and LinkedIn.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Demo Concepts — Not Real Client Posts</div>
        </div>

        <div class="grid-3" style="align-items: start;">
          <!-- Mockup 1: Instagram Story -->
          <div>
            <div class="mockup-vertical-frame">
              <div class="story-progress-bar">
                <div class="story-bar-segment active"></div>
                <div class="story-bar-segment"></div>
                <div class="story-bar-segment"></div>
              </div>
              <div class="story-top-profile">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <div class="mockup-avatar">AA</div>
                  <div>
                    <div style="font-size: 0.75rem; font-weight: 700; color: #FFF;">advertising_agency_demo</div>
                    <div style="font-size: 0.65rem; color: #CCC;">Sponsored • Demo</div>
                  </div>
                </div>
              </div>
              {placeholder_html("social-story-mockup.webp", "Instagram Story Ad Creative", "1080x1920", "aspect-9-16", "social-media-advertising.html", "Story Mockup",
                                "Vibrant vertical fashion campaign visual featuring dynamic typography styling and energetic lighting",
                                "High-fashion commercial photography formatted for vertical 9:16 mobile story advertisement, dramatic studio lighting, modern street style model, neon coral accents, high energy, 8k, no text, no logos.")}
              <div class="story-swipe-up">
                <span>Swipe Up</span>
                <span style="font-size: 0.65rem;">Explore Campaign</span>
              </div>
            </div>
            <div style="text-align: center; margin-top: 14px; font-size: 0.85rem; font-weight: 600;">Vertical Story Concept (9:16)</div>
          </div>

          <!-- Mockup 2: Instagram Feed Post -->
          <div>
            <div class="mockup-frame">
              <div class="mockup-header">
                <div class="mockup-user-info">
                  <div class="mockup-avatar">AA</div>
                  <div>
                    <div class="mockup-username">advertising_agency_demo <span style="color: var(--accent-secondary);">✓</span></div>
                    <span class="mockup-tag-sponsored">Sponsored • Illustrative Demo</span>
                  </div>
                </div>
                <span style="color: var(--text-muted); font-size: 0.8rem;">•••</span>
              </div>
              {placeholder_html("social-feed-mockup.webp", "Instagram Feed Ad Creative", "1080x1080", "aspect-1-1", "social-media-advertising.html", "Feed Mockup",
                                "Minimalist luxury product advertisement with striking dramatic shadows and vibrant background",
                                "Commercial product photography of a modern luxury cosmetic bottle set upon dark wet slate with coral splash backlighting, razor sharp studio focus, 8k, no logos, no text.")}
              <div class="mockup-cta-bar">
                <span>Shop New Collection</span>
                <span>Learn More →</span>
              </div>
              <div class="mockup-footer">
                <div class="mockup-actions-bar">
                  <span style="color: var(--accent-main);">♥ 4,129 Likes</span>
                  <span>💬 128 comments</span>
                </div>
                <div class="mockup-caption">
                  <strong>advertising_agency_demo</strong> Experience the future of brand storytelling. Engineered to turn casual scrolling into brand loyalty. #CreativeAdvertising #DesignDemo
                </div>
              </div>
            </div>
            <div style="text-align: center; margin-top: 14px; font-size: 0.85rem; font-weight: 600;">Feed Square Format (1:1)</div>
          </div>

          <!-- Mockup 3: Instagram Reels Ad -->
          <div>
            <div class="mockup-vertical-frame">
              <div class="story-top-profile">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <div class="mockup-avatar">AA</div>
                  <div>
                    <div style="font-size: 0.75rem; font-weight: 700; color: #FFF;">reels_ad_campaign</div>
                    <div style="font-size: 0.65rem; color: #CCC;">Sponsored Reel • Demo</div>
                  </div>
                </div>
              </div>
              {placeholder_html("social-reels-mockup.webp", "Instagram Reels Ad Creative", "1080x1920", "aspect-9-16", "social-media-advertising.html", "Reels Mockup",
                                "Dynamic motion freeze of an urban runner with luminous neon light streaks",
                                "Dynamic vertical sports apparel commercial advertisement, athletic model moving through dusk city with glowing neon streaks, high shutter speed, cinematic visual depth, 8k, no logos, no text.")}
              <div style="position: absolute; right: 14px; bottom: 60px; display: flex; flex-direction: column; gap: 14px; align-items: center; z-index: 5;">
                <div style="font-size: 0.75rem; color: #FFF; text-align: center;">❤️<br>12.4k</div>
                <div style="font-size: 0.75rem; color: #FFF; text-align: center;">💬<br>382</div>
                <div style="font-size: 0.75rem; color: #FFF; text-align: center;">↗️<br>Share</div>
              </div>
              <div class="story-swipe-up" style="bottom: 16px;">
                <span>Tap to Learn More</span>
              </div>
            </div>
            <div style="text-align: center; margin-top: 14px; font-size: 0.85rem; font-weight: 600;">Reels Motion Format (9:16)</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Platforms Covered -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-violet">Omni-Channel Social Presence</span>
          <h2>Platforms We Plan & Produce For</h2>
          <p>Targeted creative strategies aligned with the unique consumer mindset of each social environment.</p>
        </div>

        <div class="grid-4">
          <div class="card">
            <h4>Instagram Advertising</h4>
            <p>Visual-first storytelling across Feed, Stories, Reels, and Explore with aesthetic brand alignment.</p>
          </div>
          <div class="card">
            <h4>Facebook Advertising</h4>
            <p>Deep audience reach, community engagement, carousel storytelling, and direct lead generation forms.</p>
          </div>
          <div class="card">
            <h4>YouTube Ads</h4>
            <p>Non-skippable, bumper, and discovery video campaigns engineered to hook viewers within the first three seconds.</p>
          </div>
          <div class="card">
            <h4>LinkedIn Ads</h4>
            <p>Precision B2B decision-maker targeting, sponsored content, and executive thought-leadership promotion.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_google_ads():
    content = f'''
    <!-- Google Ads Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Intent-Driven Search & Display</span>
            <h1 style="margin: 16px 0;">Capture High-Intent Customers with Google Ads</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              When potential buyers search for solutions, be their immediate answer. We engineer search advertising, display banners, Google Shopping feeds, and remarketing loops that drive measurable enquiries.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="faq.html" class="btn btn-secondary">Google Ads FAQ</a>
            </div>
          </div>
          <div>
            {placeholder_html("google-ads-hero.webp", "Google Ads Ecosystem Visualization", "1920x1080", "aspect-16-9", "google-ads.html", "Hero Section",
                              "Multi-device ecosystem showing Google search queries and display banner ads across laptop, tablet, and smartphone",
                              "Commercial advertising visualization showing sleek laptops and tablets rendering search and display ad frameworks, dark studio lighting, subtle acid lime glow, 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Fictional SERP Search Mockup -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Search Advertising Anatomy</span>
          <h2>Illustrative Google Search Result Ad Mockup</h2>
          <p>How we structure search ads with optimized headlines, descriptions, callouts, and sitelinks for maximum Quality Score.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Demo Preview — Not Connected to Google Live Servers</div>
        </div>

        <div class="container-narrow">
          <div class="mockup-google-serp">
            <div class="serp-sponsored-badge">
              <span style="font-weight: 800;">Sponsored</span> • https://www.example.com/demo-campaign
            </div>
            <div class="serp-title">Award-Winning Creative Advertising Solutions | Scale Your Brand Growth</div>
            <div class="serp-desc">
              Connect with audiences through bespoke advertising campaigns, social media ads, commercial video production, and multi-channel media strategy. Request a tailored proposal today.
            </div>
            <div class="serp-sitelinks">
              <div>
                <div class="serp-sitelink-title">Explore Campaign Portfolio</div>
                <div class="serp-sitelink-desc">Browse selected creative campaigns across fashion, tech & F&B.</div>
              </div>
              <div>
                <div class="serp-sitelink-title">Request Custom Proposal</div>
                <div class="serp-sitelink-desc">Get an illustrative breakdown of campaign scopes & timelines.</div>
              </div>
              <div>
                <div class="serp-sitelink-title">Advertising Capabilities</div>
                <div class="serp-sitelink-desc">Search, Display, Social, Video, Outdoor & Brand Strategy.</div>
              </div>
              <div>
                <div class="serp-sitelink-title">Client Enquiry Portal</div>
                <div class="serp-sitelink-desc">Direct communication line with our advertising strategic team.</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Google Ads Formats -->
    <section class="section">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-violet">Search & Network Capabilities</span>
          <h2>Comprehensive Google Campaign Formats</h2>
          <p>Reaching prospects across the entire Google Search and Display network.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Search Campaigns</h4>
            <p>Targeting exact-match and phrase-match user queries to capture immediate purchase intent with precision copy.</p>
          </div>
          <div class="card">
            <h4>Google Display Network</h4>
            <p>Engaging visual banner ads placed across millions of high-authority partner websites, blogs, and portals.</p>
          </div>
          <div class="card">
            <h4>YouTube Video Ads</h4>
            <p>In-stream and discovery video ads that capture viewer immersion on the world's second largest search engine.</p>
          </div>
          <div class="card">
            <h4>Shopping Ads</h4>
            <p>Product listing ads with imagery, pricing, and ratings designed for high-conversion e-commerce catalogs.</p>
          </div>
          <div class="card">
            <h4>Dynamic Remarketing</h4>
            <p>Re-engaging visitors who interacted with your website with tailored creative messages that drive them back.</p>
          </div>
          <div class="card">
            <h4>Conversion Architecture</h4>
            <p>Setting up conversion tags, tracking values, and offline conversion loops to verify true business impact.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_meta_ads():
    content = f'''
    <!-- Meta Ads Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Meta Advertising Precision</span>
            <h1 style="margin: 16px 0;">Scale Your Reach with Meta Ads Strategy</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Leverage Facebook and Instagram's audience graph. We craft high-converting ad creative sequences, test lookalike cohorts, and build automated retargeting funnels that maximize commercial return.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="lead-generation.html" class="btn btn-secondary">Lead Generation Strategy</a>
            </div>
          </div>
          <div>
            {placeholder_html("meta-ads-hero.webp", "Meta Ads Management Concept", "1920x1080", "aspect-16-9", "meta-ads.html", "Hero Section",
                              "Contemporary workspace featuring creative ad mockups on floating transparent glass panels",
                              "Editorial concept photography of modern ad mockups displayed on semi-translucent glass interfaces, moody dark studio atmosphere with coral orange and lavender lighting accents, 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Meta Formats & Testing -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Creative Testing Methodology</span>
          <h2>How We Engineer Meta Campaigns</h2>
          <p>Scientific ad testing combined with world-class creative art direction.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Methodology Demo</div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Audience Segmentation</h4>
            <p>Testing interest clusters, broad demographic sets, and custom behavioral audiences to discover responsive customer pockets.</p>
          </div>
          <div class="card">
            <h4>Creative Matrix Testing</h4>
            <p>Systematically varying hooks, visuals, ad angles, and calls-to-action to eliminate creative fatigue and identify winning combinations.</p>
          </div>
          <div class="card">
            <h4>Lead Generation Forms</h4>
            <p>Frictionless native in-app instant forms that capture verified leads without requiring external landing page redirects.</p>
          </div>
          <div class="card">
            <h4>Catalog & Carousel Ads</h4>
            <p>Interactive multi-card product showcases allowing users to swipe through curated items, collections, or service benefits.</p>
          </div>
          <div class="card">
            <h4>Dynamic Retargeting</h4>
            <p>Segmenting site visitors based on specific behaviors (product view, cart abandonment) and serving tailored reassurance messaging.</p>
          </div>
          <div class="card">
            <h4>CBO & Budget Scaling</h4>
            <p>Strategic Campaign Budget Optimization allocation that channels capital into top-performing creative sets without inflating CPA.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_video_advertising():
    content = f'''
    <!-- Video Advertising Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Motion & Visual Storytelling</span>
            <h1 style="margin: 16px 0;">Turn Your Brand Message Into Visual Stories</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              From high-octane commercial brand films and short-form social reels to product showcases, we script, storyboard, and direct video advertisements that command undivided audience attention.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Video Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Showreel</a>
            </div>
          </div>
          <div>
            <div class="video-player-container">
              {placeholder_html("video-advertising-hero-poster.webp", "Commercial Brand Film Showreel", "1920x1080", "aspect-16-9", "video-advertising.html", "Hero Video",
                                "Cinematic frame from a commercial film showing a luxury automobile speeding through wet neon-lit city streets",
                                "Cinematic commercial film frame showing an elegant sleek vehicle traveling along a rain-slicked boulevard at twilight, neon reflections in puddles, cinematic anamorphic lens flare, 8k resolution, no logos, no text.")}
              <button class="video-play-btn" aria-label="Play demo showreel">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              </button>
            </div>
            <div style="text-align: center; margin-top: 10px; font-size: 0.76rem; color: var(--text-muted);">
              Frontend Demo Video Player — Click to simulate play/pause state
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Video Production Capabilities -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Production Disciplines</span>
          <h2>Video Formats We Produce</h2>
          <p>Full-spectrum video production tailored for commercial broadcast and digital distribution.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Commercial Brand Films</h4>
            <p>Cinematic, emotionally resonant video productions that define brand identity and create lasting cultural memory.</p>
          </div>
          <div class="card">
            <h4>Product Showcases</h4>
            <p>Close-up macro cinematography, lighting effects, and motion choreography highlighting product craftsmanship.</p>
          </div>
          <div class="card">
            <h4>Social Media Reels & Shorts</h4>
            <p>Fast-paced, hook-driven short-form vertical videos engineered specifically for TikTok, Reels, and YouTube Shorts.</p>
          </div>
          <div class="card">
            <h4>Corporate Storytelling</h4>
            <p>Sophisticated corporate brand videos highlighting company vision, culture, innovation, and leadership.</p>
          </div>
          <div class="card">
            <h4>Explainer & Motion Graphics</h4>
            <p>Dynamic 2D/3D typography, vector animations, and interface simulations that clearly articulate complex products.</p>
          </div>
          <div class="card">
            <h4>AI-Assisted Video Concepts</h4>
            <p>Harnessing cutting-edge generative video pipelines for rapid concept exploration, pre-visualization, and storyboarding.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Video Gallery Previews -->
    <section class="section">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-violet">Selected Motion Previews</span>
          <h2>Illustrative Commercial Concepts</h2>
          <p>Explore concept frames from demo commercial video productions.</p>
        </div>

        <div class="grid-3">
          <div class="card" style="padding: 0; overflow: hidden;">
            {placeholder_html("video-thumb-fashion.webp", "Fashion Campaign Commercial", "1920x1080", "aspect-16-9", "video-advertising.html", "Video Gallery",
                              "Avant-garde fashion video still featuring silhouette lighting and textured fabric motion",
                              "Cinematic still from a luxury fashion commercial, model in motion against a stark sculptural backdrop, high contrast shadows, atmospheric haze, 8k, no logos, no text.")}
            <div style="padding: 20px;">
              <h4>Haute Couture Concept Reel</h4>
              <p style="font-size: 0.88rem; margin-top: 6px;">Editorial fashion motion concept designed for multi-platform seasonal launch.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden;">
            {placeholder_html("video-thumb-beverage.webp", "Beverage Brand Commercial", "1920x1080", "aspect-16-9", "video-advertising.html", "Video Gallery",
                              "High-speed liquid splash photography capturing iced citrus beverage in motion",
                              "Macro high-speed commercial still of iced sparkling citrus beverage with water droplets and flying ice cubes, dramatic studio rim light, 8k, no logos, no text.")}
            <div style="padding: 20px;">
              <h4>Artisanal Beverage Campaign</h4>
              <p style="font-size: 0.88rem; margin-top: 6px;">High-speed splash cinematography capturing sensory refreshment and craft.</p>
            </div>
          </div>

          <div class="card" style="padding: 0; overflow: hidden;">
            {placeholder_html("video-thumb-tech.webp", "Tech Hardware Commercial", "1920x1080", "aspect-16-9", "video-advertising.html", "Video Gallery",
                              "Futuristic audio hardware hovering in zero gravity with neon audio frequency waves",
                              "Commercial product video still of sleek matte black wireless headphones hovering in mid-air, surrounded by ethereal neon audio wave trails, 8k, no logos, no text.")}
            <div style="padding: 20px;">
              <h4>Acoustic Hardware Launch</h4>
              <p style="font-size: 0.88rem; margin-top: 6px;">Zero-gravity product reveal highlighting minimalist industrial design.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_creative_design():
    content = f'''
    <!-- Creative Design Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Visual Craft & Art Direction</span>
            <h1 style="margin: 16px 0;">Creative Advertising Design That Stops The World</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Exceptional design is not decoration; it is commercial persuasion. We architect bold key visuals, scroll-stopping social banners, campaign posters, and promotional graphics that establish unforgettable brand prestige.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Design Work</a>
            </div>
          </div>
          <div>
            {placeholder_html("creative-design-hero.webp", "Advertising Key Visual Masterpiece", "1920x1080", "aspect-16-9", "creative-design.html", "Hero Section",
                              "Sculptural 3D abstract composition combining organic forms with bold modern typography blocks",
                              "Art direction master visual showing bold abstract sculptural shapes floating in an obsidian studio space, vibrant coral orange and acid lime gradient lighting, razor sharp 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Creative Deliverables Grid -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Creative Formats</span>
          <h2>Design Assets Engineered for Commercial Impact</h2>
          <p>Every asset is crafted with strategic purpose, typographic hierarchy, and visual restraint.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Campaign Key Visuals (KV)</h4>
            <p>The anchor visual identity that governs all campaign collateral across billboards, digital banners, and packaging.</p>
          </div>
          <div class="card">
            <h4>Social Media Creatives</h4>
            <p>Dynamic Instagram feed assets, carousel graphics, and high-impact story layouts tuned for viral shareability.</p>
          </div>
          <div class="card">
            <h4>Digital Display Banners</h4>
            <p>HTML5, GIF, and static responsive display banners optimized for high CTR and pristine legibility at all scales.</p>
          </div>
          <div class="card">
            <h4>Promotional Posters & Collateral</h4>
            <p>Editorial-grade poster art combining striking typography and commercial photography for retail and events.</p>
          </div>
          <div class="card">
            <h4>Carousel Storyboard Ads</h4>
            <p>Multi-slide sequential visual journeys that educate, intrigue, and guide users step-by-step toward conversion.</p>
          </div>
          <div class="card">
            <h4>Festival & Seasonal Creatives</h4>
            <p>Timely holiday and seasonal campaign themes crafted with cultural sensitivity and celebratory visual elegance.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_brand_strategy():
    content = f'''
    <!-- Brand Strategy Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Strategic Foundation</span>
            <h1 style="margin: 16px 0;">Brand Strategy That Gives Advertising Meaning</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Great advertising without strategy is just expensive noise. We clarify your positioning, define your core messaging pillars, profile audience desires, and chart an authentic trajectory for market dominance.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Brand Strategy</a>
              <a href="process.html" class="btn btn-secondary">Explore Our Process</a>
            </div>
          </div>
          <div>
            {placeholder_html("brand-strategy-hero.webp", "Brand Strategy Framework Architecture", "1920x1080", "aspect-16-9", "brand-strategy.html", "Hero Section",
                              "Editorial style strategy presentation deck displayed on sleek minimalist mahogany table with warm ambient glow",
                              "Clean commercial flat-lay photography of open brand strategy brand books, color swatch fans, and typography specimen sheets arranged neatly on a dark basalt desk, warm soft lighting, 8k, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Strategy Presentation Mockup -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Strategic Framework</span>
          <h2>The 4 Pillars of Advertising Strategy</h2>
          <p>How we translate business ambition into a competitive market presence.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Strategy Framework — Generic Demo</div>
        </div>

        <div class="grid-4">
          <div class="card">
            <div style="font-size: 2rem; color: var(--accent-main); font-weight: 800; margin-bottom: 12px;">01</div>
            <h4>Market & Audience Positioning</h4>
            <p>Pinpointing the unique white space your brand can own in the minds of your highest-value customers.</p>
          </div>
          <div class="card">
            <div style="font-size: 2rem; color: var(--accent-secondary); font-weight: 800; margin-bottom: 12px;">02</div>
            <h4>Core Messaging Architecture</h4>
            <p>Defining taglines, brand narrative, tonal guidelines, and value propositions across every consumer touchpoint.</p>
          </div>
          <div class="card">
            <div style="font-size: 2rem; color: var(--accent-highlight); font-weight: 800; margin-bottom: 12px;">03</div>
            <h4>Competitive Moat Analysis</h4>
            <p>Benchmarking rivals to highlight distinct product differentiators and counter-position against industry clichés.</p>
          </div>
          <div class="card">
            <div style="font-size: 2rem; color: #FFF; font-weight: 800; margin-bottom: 12px;">04</div>
            <h4>Campaign Narrative Roadmap</h4>
            <p>Choreographing multi-quarter advertising arcs that nurture audience awareness into long-term brand equity.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_graphic_design():
    content = f'''
    <!-- Graphic Design Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Graphic Design & Identity</span>
            <h1 style="margin: 16px 0;">Graphic Design for Brands with High Ambition</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              From complete visual identity guidelines and bespoke typography to packaging, brochures, and promotional print collateral, we create graphic design that elevates perceived brand value.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Design Project</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Design Gallery</a>
            </div>
          </div>
          <div>
            {placeholder_html("graphic-design-hero.webp", "Brand Identity Stationery Mockup", "1920x1080", "aspect-16-9", "graphic-design.html", "Hero Section",
                              "Curated luxury stationery identity suite with embossed business cards, letterheads, and notebooks on dark concrete",
                              "High-end corporate identity stationery branding mockup on dark textured slate background, featuring embossed business cards, envelopes, and brand style manual, soft diffused lighting, 8k, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Graphic Design Portfolio Grid -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Design Disciplines</span>
          <h2>Graphic Design Capabilities</h2>
          <p>Crafting coherent visual languages across physical and digital surfaces.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Brand Identity Systems</h4>
            <p>Logo marks, symbol guidelines, typography pairings, color systems, and comprehensive style governance guides.</p>
          </div>
          <div class="card">
            <h4>Packaging & Box Design</h4>
            <p>Consumer packaging concepts, dieline design, label architecture, and tactile unboxing experience curation.</p>
          </div>
          <div class="card">
            <h4>Editorial Brochures & Lookbooks</h4>
            <p>Multi-page corporate brochures, fashion lookbooks, and annual reports designed with editorial precision.</p>
          </div>
          <div class="card">
            <h4>Marketing Collateral</h4>
            <p>Flyers, leaflets, exhibition booth banners, presentation decks, and business stationery sets.</p>
          </div>
          <div class="card">
            <h4>Social Media Asset Toolkits</h4>
            <p>Modular, reusable social templates designed in Figma and Adobe Creative Suite for in-house marketing velocity.</p>
          </div>
          <div class="card">
            <h4>Infographics & Data Art</h4>
            <p>Transforming complex corporate research and statistics into visually engaging, brand-aligned diagrams.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_content_marketing():
    content = f'''
    <!-- Content Marketing Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Editorial & Narrative Strategy</span>
            <h1 style="margin: 16px 0;">Content Marketing That Educates, Engages & Converts</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Publishing content without purpose is wasted effort. We build strategic editorial calendars, write magnetic ad copywriting, produce in-depth articles, and craft video scripts that build brand authority.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="blog.html" class="btn btn-secondary">Read Insights</a>
            </div>
          </div>
          <div>
            {placeholder_html("content-marketing-hero.webp", "Content Strategy & Editorial Calendar System", "1920x1080", "aspect-16-9", "content-marketing.html", "Hero Section",
                              "Editorial desk with open digital calendar interface, fountain pen, and creative article manuscripts",
                              "Overhead flat-lay photograph of a writer's workspace with a sleek tablet showing an editorial calendar planner, coffee cup, notebook, and warm task light, 8k resolution, no logos, no text.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Content Calendar Mockup Preview -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Strategic Content Rhythm</span>
          <h2>Illustrative Monthly Content Calendar Framework</h2>
          <p>How we organize brand storytelling across awareness, consideration, and conversion pillars.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Editorial Schedule Demo</div>
        </div>

        <div class="grid-4">
          <div class="card">
            <span class="badge badge-coral" style="margin-bottom: 12px;">Week 1 — Anchor</span>
            <h4>Authority & Thought Leadership</h4>
            <p>Deep-dive industry analysis, trend breakdown, and core educational articles establishing market expertise.</p>
          </div>
          <div class="card">
            <span class="badge badge-lime" style="margin-bottom: 12px;">Week 2 — Proof</span>
            <h4>Process & Behind-The-Scenes</h4>
            <p>Showcasing craftsmanship, production excellence, client problem-solving narratives, and methodology.</p>
          </div>
          <div class="card">
            <span class="badge badge-violet" style="margin-bottom: 12px;">Week 3 — Engagement</span>
            <h4>Interactive & Community Discourse</h4>
            <p>Polls, provocative discussion prompts, customer query answers, and dynamic short-form video hooks.</p>
          </div>
          <div class="card">
            <span class="badge" style="margin-bottom: 12px; background: rgba(255,255,255,0.1);">Week 4 — Action</span>
            <h4>Direct Conversion & Offers</h4>
            <p>Direct advertising copy, product feature highlights, seasonal incentives, and friction-free consultation calls.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_influencer_marketing():
    content = f'''
    <!-- Influencer Marketing Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Creator Partnerships</span>
            <h1 style="margin: 16px 0;">Influencer Collaborations That Command Real Trust</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Harness the authenticity of top digital creators. We manage end-to-end influencer campaigns—from creator discovery, vetting, and creative briefs to content coordination and performance verification.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Influencer Campaign</a>
              <a href="contact.html" class="btn btn-secondary">Request Creator Strategy</a>
            </div>
          </div>
          <div>
            {placeholder_html("influencer-marketing-hero.webp", "Creator Studio Collaboration Concept", "1920x1080", "aspect-16-9", "influencer-marketing.html", "Hero Section",
                              "Content creator in a modern minimalist studio with professional ring light and mirrorless camera setup",
                              "Commercial lifestyle photography of a creative lifestyle influencer producing content in a warm contemporary studio, professional camera on tripod, warm golden rim lighting, 8k, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Creator Tiers Mockup -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Creator Tiers</span>
          <h2>Strategic Creator Selection Framework</h2>
          <p>We match brands with creators based on audience affinity, engagement depth, and content authenticity.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Creator Profile Cards — Generic Demo</div>
        </div>

        <div class="grid-3">
          <div class="card">
            <span class="badge badge-coral" style="margin-bottom: 12px;">Micro-Creators (10K - 50K)</span>
            <h4>Hyper-Engaged Niche Champions</h4>
            <p>Exceptional community trust, high comment interaction rates, and ideal suitability for targeted local and specialist product launches.</p>
          </div>
          <div class="card">
            <span class="badge badge-lime" style="margin-bottom: 12px;">Mid-Tier Creators (50K - 250K)</span>
            <h4>High-Production Category Experts</h4>
            <p>Polished production capabilities, established category authority across lifestyle, fashion, tech, or business, with scalable reach.</p>
          </div>
          <div class="card">
            <span class="badge badge-violet" style="margin-bottom: 12px;">Macro Creators (250K+)</span>
            <h4>Mass Brand Awareness Amplifiers</h4>
            <p>Broad cultural footprint designed to drive massive top-of-funnel brand visibility and anchor nationwide promotional campaigns.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_outdoor_advertising():
    content = f'''
    <!-- Outdoor Advertising Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Out-Of-Home & Transit Media</span>
            <h1 style="margin: 16px 0;">Command Attention in The Physical World</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Digital noise makes real-world scale all the more powerful. We design impactful billboards, digital LED displays, bus wraps, and retail signage that make your brand unavoidable in metropolitan spaces.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Outdoor Campaign</a>
              <a href="portfolio.html" class="btn btn-secondary">Explore Outdoor Portfolio</a>
            </div>
          </div>
          <div>
            <div class="mockup-billboard">
              <div class="billboard-spotlight"></div>
              {placeholder_html("outdoor-billboard-mockup.webp", "Metropolitan LED Billboard Mockup", "1920x1080", "aspect-16-9", "outdoor-advertising.html", "Billboard Mockup",
                                "Monumental highway billboard showcasing an avant-garde fashion campaign at blue hour in a futuristic metropolis",
                                "Urban outdoor advertising photography showing a massive illuminated billboard mounted high on a modern steel structure overlooking a glowing metropolitan highway at dusk, cinematic blue hour lighting, 8k, no logos, no text.")}
            </div>
            <div class="billboard-structure"></div>
            <div style="text-align: center; margin-top: 10px; font-size: 0.76rem; color: var(--text-muted);">
              Illustrative Demo Billboard Mockup — Concept Placement
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Outdoor Formats -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Physical Reach</span>
          <h2>Outdoor Advertising Formats</h2>
          <p>High-visibility real-world placements engineered for instant visual recall.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Highway Billboards & Hoardings</h4>
            <p>Massive arterial road displays engineered with bold typography and high-contrast visuals for rapid 3-second comprehension.</p>
          </div>
          <div class="card">
            <h4>Digital Out-Of-Home (DOOH)</h4>
            <p>High-definition dynamic LED screens placed in luxury shopping malls, transit hubs, and commercial centers.</p>
          </div>
          <div class="card">
            <h4>Transit & Bus Advertisements</h4>
            <p>Moving city canvases including full bus wraps, metro train interiors, and station platform lightboxes.</p>
          </div>
          <div class="card">
            <h4>Building & Facade Signage</h4>
            <p>Architectural building graphics, 3D illuminated channel letters, and high-prestige flagship retail displays.</p>
          </div>
          <div class="card">
            <h4>Airport Concourse Displays</h4>
            <p>Premium displays situated in high-dwell international departures, lounges, and baggage claim terminals.</p>
          </div>
          <div class="card">
            <h4>Point-of-Sale (POS) Retail Graphics</h4>
            <p>Floor stands, window vinyls, and promotional shelf-talkers that convert foot traffic into store sales.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_print_advertising():
    content = f'''
    <!-- Print Advertising Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Editorial & Print Media</span>
            <h1 style="margin: 16px 0;">Tactile Prestige: Editorial Print Advertising</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Print commands a level of undivided attention that screens cannot match. We design high-end magazine spreads, newspaper placements, luxury catalogues, and direct marketing collateral with editorial sophistication.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Print Project</a>
              <a href="contact.html" class="btn btn-secondary">Request Print Spec</a>
            </div>
          </div>
          <div>
            <div class="mockup-print-spread">
              <div class="print-page" style="background: #111;">
                {placeholder_html("print-magazine-left.webp", "Magazine Editorial Ad Left", "1080x1350", "aspect-4-5", "print-advertising.html", "Magazine Spread",
                                  "High-fashion editorial portrait with dramatic split lighting and deep shadows",
                                  "Editorial magazine fashion portrait photograph, monochromatic tones with coral lips, sculptural posture, soft matte print paper texture, 8k, no text, no logos.")}
              </div>
              <div class="print-page" style="background: #161616; justify-content: center;">
                <span class="badge badge-coral" style="margin-bottom: 16px;">Editorial Spread</span>
                <h3 style="margin-bottom: 12px; font-family: var(--font-display);">THE NEW LUXURY PARADIGM</h3>
                <p style="font-size: 0.88rem; line-height: 1.6; margin-bottom: 20px;">
                  Crafted for high-circulation luxury publications. Engineered with rigorous typographic hierarchy, generous margins, and museum-grade color reproduction standards.
                </p>
                <div style="font-size: 0.76rem; color: var(--accent-secondary); font-family: var(--font-mono);">
                  DEMO ISSUE № 27 • FULL SPREAD BLEED
                </div>
              </div>
            </div>
            <div style="text-align: center; margin-top: 10px; font-size: 0.76rem; color: var(--text-muted);">
              Illustrative Demo Print Spread Mockup (Double-Page Spread)
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Print Formats -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Print Mediums</span>
          <h2>Print Advertising Solutions</h2>
          <p>Meticulously prepared print layouts with color-managed CMYK pre-press standards.</p>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Magazine Full-Page & Spreads</h4>
            <p>Flawlessly typeset advertisements designed to blend seamlessly into luxury editorial layouts.</p>
          </div>
          <div class="card">
            <h4>Newspaper Display Ads</h4>
            <p>High-contrast, high-impact layouts engineered to stand out sharply on newsprint paper stocks.</p>
          </div>
          <div class="card">
            <h4>Luxury Product Catalogues</h4>
            <p>Substantial multi-page product portfolios featuring foil stamping, emboss treatments, and premium stocks.</p>
          </div>
          <div class="card">
            <h4>Direct Mail & Lookbooks</h4>
            <p>Targeted physical mailers and invitations that engage high-net-worth customers through tactile intimacy.</p>
          </div>
          <div class="card">
            <h4>Event Programmes & Guides</h4>
            <p>Commemorative event booklets, sponsorship placements, and gala programmes with pristine typography.</p>
          </div>
          <div class="card">
            <h4>Pre-Press & Color Proofing</h4>
            <p>Rigorous pre-flight checks, ink density limits, spot color separations, and press-ready PDF delivery.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_seo_services():
    content = f'''
    <!-- SEO Services Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">Organic Search Engine Authority</span>
            <h1 style="margin: 16px 0;">Technical SEO & Search Discoverability</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Paid advertising buys attention; organic SEO earns sustainable market prominence. We optimize site architecture, technical crawlability, on-page content, and keyword relevance to fuel long-term inbound discovery.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start a Campaign</a>
              <a href="faq.html" class="btn btn-secondary">SEO FAQs</a>
            </div>
          </div>
          <div>
            {placeholder_html("seo-services-hero.webp", "SEO Analytics & Search Architecture", "1920x1080", "aspect-16-9", "seo-services.html", "Hero Section",
                              "3D isometric wireframe representation of a website architecture hierarchy with search crawl pathways",
                              "Futuristic 3D visualization of search engine crawl vectors navigating a multi-tiered website structure, luminous lime green nodes on obsidian grid, 8k resolution, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- SEO Pillars -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header">
          <span class="badge badge-lime">Search Optimization Pillars</span>
          <h2>Ethical, Sustainable Search Engineering</h2>
          <p>We build organic search equity through foundational web best practices.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Strategy — No Ranking Guarantees Implied</div>
        </div>

        <div class="grid-3">
          <div class="card">
            <h4>Technical SEO Foundations</h4>
            <p>Valid semantic HTML5, XML sitemaps, clean robots.txt directives, Canonical URLs, and schema structured data.</p>
          </div>
          <div class="card">
            <h4>Core Web Vitals & Speed</h4>
            <p>Aggressive image optimization, minimal CSS/JS payloads, zero layout shifts (CLS), and ultra-fast First Contentful Paint.</p>
          </div>
          <div class="card">
            <h4>Keyword & Intent Research</h4>
            <p>Identifying commercial, transactional, and informational search intent queries that your customers actually search for.</p>
          </div>
          <div class="card">
            <h4>On-Page Optimization</h4>
            <p>Optimizing heading hierarchies (H1-H6), meta titles, compelling meta descriptions, and descriptive image alt tags.</p>
          </div>
          <div class="card">
            <h4>Internal Linking Architecture</h4>
            <p>Structuring clean topical clusters and siloing related service offerings to distribute authority naturally.</p>
          </div>
          <div class="card">
            <h4>Landing Page Content Relevance</h4>
            <p>Drafting comprehensive, well-structured answers to customer questions that search engines recognize as authoritative.</p>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

def generate_lead_generation():
    content = f'''
    <!-- Lead Generation Hero -->
    <section class="section section-hero">
      <div class="container">
        <div class="grid-2" style="align-items: center;">
          <div>
            <span class="badge badge-coral">High-Intent Acquisition Funnels</span>
            <h1 style="margin: 16px 0;">Turn Advertising Attention Into Business Enquiries</h1>
            <p class="lead-text" style="margin-bottom: 28px;">
              Traffic without conversion is vanity. We construct full-funnel lead generation architectures—from hook-driven ad creatives and high-converting landing pages to automated lead validation and qualification.
            </p>
            <div class="btn-group">
              <a href="start-campaign.html" class="btn btn-primary">Start Lead Generation</a>
              <a href="pricing.html" class="btn btn-secondary">Explore Packages</a>
            </div>
          </div>
          <div>
            {placeholder_html("lead-generation-hero.webp", "Lead Generation Funnel Architecture", "1920x1080", "aspect-16-9", "lead-generation.html", "Hero Section",
                              "Sophisticated glass geometric funnel structure refracting light and illuminating customer pathways",
                              "Sculptural architectural render of a multi-tiered glass funnel structure glowing with coral and lime light, representing high-intent customer acquisition stages, dark background, 8k, no text, no logos.")}
          </div>
        </div>
      </div>
    </section>

    <!-- Marketing Funnel Visualization -->
    <section class="section section-bg-secondary">
      <div class="container">
        <div class="section-header text-center">
          <span class="badge badge-lime">Conversion Architecture</span>
          <h2>The 5-Stage Customer Journey Funnel</h2>
          <p>How we shepherd cold prospects from first impression into high-value sales conversations.</p>
          <div class="demo-disclaimer" style="margin-top: 10px;">Illustrative Acquisition Funnel Demo</div>
        </div>

        <div class="funnel-container">
          <div class="funnel-step" style="border-left: 6px solid var(--accent-main);">
            <div>
              <div class="funnel-step-name">1. Awareness (Top of Funnel)</div>
              <div class="funnel-step-desc">High-impact social reels, display banners, and search ads that introduce brand promise.</div>
            </div>
            <span class="badge badge-coral">Broad Reach</span>
          </div>

          <div class="funnel-step" style="border-left: 6px solid #FF8A65; margin-left: 20px;">
            <div>
              <div class="funnel-step-name">2. Interest (Mid Funnel)</div>
              <div class="funnel-step-desc">Engaging carousel ads, problem-solving video explainers, and educational content.</div>
            </div>
            <span class="badge">Engagement</span>
          </div>

          <div class="funnel-step" style="border-left: 6px solid var(--accent-highlight); margin-left: 40px;">
            <div>
              <div class="funnel-step-name">3. Consideration (Evaluation)</div>
              <div class="funnel-step-desc">Demonstration case studies, capability decks, and comparative product advantages.</div>
            </div>
            <span class="badge badge-violet">Intent Building</span>
          </div>

          <div class="funnel-step" style="border-left: 6px solid var(--accent-secondary); margin-left: 60px;">
            <div>
              <div class="funnel-step-name">4. Enquiry (Action Trigger)</div>
              <div class="funnel-step-desc">High-speed friction-free multi-step enquiry forms and direct consultation booking.</div>
            </div>
            <span class="badge badge-lime">Lead Capture</span>
          </div>

          <div class="funnel-step" style="border-left: 6px solid #FFF; margin-left: 80px;">
            <div>
              <div class="funnel-step-name">5. Conversion (Commercial Result)</div>
              <div class="funnel-step-desc">Qualified prospect engagement, proposal presentation, and commercial kickoff.</div>
            </div>
            <span class="badge" style="background: #FFF; color: #0A0A0A;">Client Onboarding</span>
          </div>
        </div>
      </div>
    </section>
    '''
    return content

print("Services generators loaded.")
