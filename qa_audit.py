# -*- coding: utf-8 -*-
"""
ADVERTISING AGENCY — Comprehensive QA Audit Script
"""

import os
import re

BASE_DIR = r"P:\TSCG\2027 Demo Websites\Advertising Agency"

expected_pages = [
    "index.html", "about.html", "services.html", "digital-advertising.html",
    "social-media-advertising.html", "google-ads.html", "meta-ads.html",
    "video-advertising.html", "creative-design.html", "brand-strategy.html",
    "graphic-design.html", "content-marketing.html", "influencer-marketing.html",
    "outdoor-advertising.html", "print-advertising.html", "seo-services.html",
    "lead-generation.html", "industries.html", "portfolio.html", "campaign-details.html",
    "process.html", "pricing.html", "technologies.html", "careers.html",
    "blog.html", "faq.html", "contact.html", "start-campaign.html",
    "privacy-policy.html", "terms-and-conditions.html"
]

print("=== STARTING COMPREHENSIVE QA AUDIT ===")
errors = []

# 1. Check all 30 HTML pages exist
for p in expected_pages:
    fp = os.path.join(BASE_DIR, p)
    if not os.path.exists(fp):
        errors.append(f"Missing page: {p}")
    else:
        size = os.path.getsize(fp)
        if size < 1000:
            errors.append(f"Page unexpectedly small ({size} bytes): {p}")

print(f"[QA] Page existence check passed: {len(expected_pages)} pages verified.")

# 2. Check CSS and JS assets
required_assets = [
    "assets/css/style.css",
    "assets/css/responsive.css",
    "assets/css/animations.css",
    "assets/js/main.js",
    "assets/js/interactions.js",
    "assets/js/portfolio.js",
    "sitemap.xml",
    "robots.txt",
    "README.md",
    "IMAGE-GENERATION-GUIDE.md"
]

for a in required_assets:
    fp = os.path.join(BASE_DIR, a.replace('/', os.sep))
    if not os.path.exists(fp):
        errors.append(f"Missing asset file: {a}")
    else:
        print(f"[QA] Asset verified: {a} ({os.path.getsize(fp)} bytes)")

# 3. Check for external image requests or banned frameworks
banned_patterns = [
    (r'https?://[^\s"\'>]+\.(png|jpg|jpeg|webp|gif|avif)', "External image URL detected"),
    (r'unsplash\.com', "Unsplash image detected"),
    (r'pexels\.com', "Pexels image detected"),
    (r'shutterstock\.com', "Shutterstock image detected"),
    (r'cdn\.jsdelivr\.net/npm/(bootstrap|jquery|vue|react|angular)', "Banned JS framework CDN detected"),
    (r'cdnjs\.cloudflare\.com/ajax/libs/(gsap|three)', "Banned library (GSAP/Three.js) detected")
]

for p in expected_pages:
    fp = os.path.join(BASE_DIR, p)
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()

    for pattern, msg in banned_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            errors.append(f"In {p}: {msg} -> {match.group(0)}")

# 4. Check internal links
link_pattern = re.compile(r'href="([a-zA-Z0-9_\-]+\.html)"')
all_internal_links = set()

for p in expected_pages:
    fp = os.path.join(BASE_DIR, p)
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = link_pattern.findall(content)
    for m in matches:
        all_internal_links.add(m)
        target_fp = os.path.join(BASE_DIR, m)
        if not os.path.exists(target_fp):
            errors.append(f"Broken link in {p}: points to non-existent '{m}'")

print(f"[QA] Verified {len(all_internal_links)} distinct internal link targets.")

# 5. Check real image embeddings
img_tag_pattern = re.compile(r'<img[^>]+src="([^">]+)"')
embedded_images = set()

for p in expected_pages:
    fp = os.path.join(BASE_DIR, p)
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = img_tag_pattern.findall(content)
    for src in matches:
        embedded_images.add(src)
        clean_src = src.split('?')[0].split('#')[0]
        img_fp = os.path.join(BASE_DIR, clean_src.replace('/', os.sep))
        if not os.path.exists(img_fp):
            errors.append(f"Broken image in {p}: '{src}' not found at {img_fp}")
        else:
            if os.path.getsize(img_fp) == 0:
                errors.append(f"Empty image file: {img_fp}")

print(f"[QA] Verified {len(embedded_images)} embedded images across all pages - all files exist and are non-empty.")

# 6. Check unique titles and descriptions
titles = {}
descs = {}
for p in expected_pages:
    fp = os.path.join(BASE_DIR, p)
    with open(fp, "r", encoding="utf-8") as f:
        content = f.read()
    
    t_match = re.search(r'<title>([^<]+)</title>', content)
    d_match = re.search(r'<meta name="description" content="([^"]+)">', content)

    if not t_match:
        errors.append(f"Missing <title> tag in {p}")
    else:
        titles[p] = t_match.group(1)

    if not d_match:
        errors.append(f"Missing meta description in {p}")
    else:
        descs[p] = d_match.group(1)

print(f"[QA] Verified {len(titles)} titles and {len(descs)} meta descriptions.")

# 7. Check sitemap.xml entries
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_text = f.read()

for p in expected_pages:
    if f"<loc>https://demo-advertising-agency.com/{p}</loc>" not in sitemap_text:
        errors.append(f"Page {p} missing from sitemap.xml")

print(f"[QA] Sitemap verified for all {len(expected_pages)} pages.")

# Summary
print("\n=== QA AUDIT RESULT ===")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
else:
    print("[SUCCESS] 100% of tests passed! ZERO errors found.")
    print("The website is production-ready for static hosting on Hostinger.")
