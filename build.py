#!/usr/bin/env python3
"""
aloe-skincare-landing Site Builder
InfiniteAloe.shop affiliate site — LinkConnector
Repo: brightlane/aloe-skincare-landing
Affiliate: https://www.linkconnector.com/ta.php?lc=014538155218007855&atid=InfiniteAloeWeb&lcpt=0&lcpf=3
"""

import os, base64, requests
from datetime import datetime

AFF = "https://www.linkconnector.com/ta.php?lc=014538155218007855&atid=InfiniteAloeWeb&lcpt=0&lcpf=3"
SITE_NAME = "AloeSkincareHub"
BRAND     = "AloeSkincareHub"
SITE_URL  = "https://brightlane.github.io/aloe-skincare-landing"
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "aloe-skincare-landing")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GVERIFY   = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

CSS = """
:root{--primary:#047857;--primary-hover:#065f46;--secondary:#1d4ed8;--accent:#fbbf24;
--text:#0f172a;--text-light:#334155;--bg:#f8fafc;--card-bg:#ffffff;
--border:#cbd5e1;--shadow:0 4px 12px rgba(0,0,0,0.1);
--shadow-hover:0 8px 20px rgba(0,0,0,0.15);
--gradient:linear-gradient(135deg,#059669,#1d4ed8);
--gradient-hover:linear-gradient(135deg,#047857,#1e40af);}
*{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;line-height:1.7;color:var(--text);background:var(--bg);}
a{text-decoration:none;color:inherit;}
nav{background:var(--gradient);padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:62px;position:sticky;top:0;z-index:100;box-shadow:var(--shadow);}
.nav-logo{color:#fff;font-weight:700;font-size:1.1rem;}
.nav-logo span{color:var(--accent);}
.nav-links{display:flex;gap:1.5rem;}
.nav-links a{color:rgba(255,255,255,0.85);font-size:0.85rem;font-weight:500;transition:color 0.2s;}
.nav-links a:hover{color:#fff;}
.nav-cta{background:#fff;color:var(--primary)!important;padding:7px 16px;border-radius:8px;font-weight:700!important;}
.hero{background:var(--gradient);color:#fff;text-align:center;padding:60px 20px;border-radius:16px;margin:20px auto;max-width:1000px;box-shadow:var(--shadow);}
.hero h1{font-size:clamp(1.8rem,5vw,2.8rem);font-weight:700;margin-bottom:15px;line-height:1.2;}
.hero h1 em{color:var(--accent);font-style:normal;}
.hero p{font-size:1.1rem;margin-bottom:25px;opacity:0.9;max-width:650px;margin-left:auto;margin-right:auto;}
.buy-btn{display:inline-block;padding:14px 28px;background:#fff;color:var(--primary);border-radius:10px;font-weight:600;transition:all 0.3s ease;box-shadow:var(--shadow);}
.buy-btn:hover{background:var(--gradient-hover);color:#fff;transform:translateY(-2px);box-shadow:var(--shadow-hover);}
.buy-btn-green{background:var(--gradient);color:#fff;border-radius:10px;padding:12px 24px;font-weight:600;transition:all 0.3s ease;display:inline-block;}
.buy-btn-green:hover{background:var(--gradient-hover);transform:translateY(-2px);box-shadow:var(--shadow-hover);}
main{max-width:1000px;margin:40px auto;padding:0 15px;}
.section-title{font-size:1.8rem;margin:40px 0 20px;border-bottom:3px solid var(--primary);padding-bottom:10px;color:var(--text);}
.card-container{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-bottom:40px;}
.card{background:var(--card-bg);border-radius:16px;padding:20px;box-shadow:var(--shadow);transition:all 0.3s ease;border:1px solid var(--border);}
.card:hover{transform:translateY(-5px);box-shadow:var(--shadow-hover);}
.card-emoji{font-size:3rem;text-align:center;margin-bottom:15px;}
.card h3{font-size:1.2rem;margin-bottom:10px;color:var(--primary);font-weight:700;}
.card p{font-size:0.95rem;margin-bottom:15px;color:var(--text-light);}
.card .price{font-size:1.3rem;font-weight:700;color:var(--primary);margin-bottom:12px;}
table{width:100%;border-collapse:collapse;margin:20px 0;border-radius:12px;overflow:hidden;box-shadow:var(--shadow);}
th,td{padding:14px;text-align:left;border-bottom:1px solid var(--border);}
th{background:var(--gradient);color:#fff;font-weight:600;}
tbody tr:nth-child(even){background:#f1f5f9;}
tbody tr:hover{background:#dcfce7;}
.tips-list{display:grid;gap:1rem;}
.tip-item{display:flex;gap:1rem;background:#fff;padding:1.2rem 1.5rem;border-radius:12px;box-shadow:var(--shadow);border-left:4px solid var(--primary);}
.tip-n{font-size:1.2rem;font-weight:800;color:var(--primary);min-width:28px;}
.tip-t strong{display:block;font-size:0.95rem;color:var(--text);margin-bottom:0.2rem;}
.tip-t span{font-size:0.87rem;color:var(--text-light);}
blockquote{background:var(--gradient);color:#fff;padding:20px;border-radius:12px;margin:20px 0;font-style:italic;box-shadow:var(--shadow);}
.faqs{display:grid;gap:1rem;}
.faq{border:1px solid var(--border);border-radius:12px;overflow:hidden;background:#fff;}
.faq-q{padding:18px 20px;font-weight:600;color:var(--text);background:#f8fafc;cursor:pointer;}
.faq-a{padding:0 20px 16px;color:var(--text-light);font-size:0.95rem;}
.cta-band{background:var(--gradient);color:#fff;text-align:center;padding:50px 20px;border-radius:16px;margin:40px 0;box-shadow:var(--shadow);}
.cta-band h2{font-size:2rem;font-weight:700;margin-bottom:12px;}
.cta-band p{opacity:0.9;margin-bottom:25px;font-size:1.1rem;}
.sticky-bar{position:fixed;bottom:0;width:100%;background:var(--primary);text-align:center;padding:10px;z-index:999;box-shadow:0 -2px 12px rgba(0,0,0,0.2);}
.sticky-bar a{color:#fff;font-weight:700;font-size:0.9rem;}
footer{text-align:center;margin:50px auto 20px;font-size:0.9rem;color:var(--text-light);padding:20px;}
footer a{color:var(--secondary);margin:0 8px;}
footer a:hover{color:var(--primary);}
.disclosure{font-size:0.78rem;color:#94a3b8;text-align:center;padding:1rem;border-top:1px solid var(--border);}
.fade{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade.on{opacity:1;transform:none;}
.trust-bar{background:#fff;padding:20px;text-align:center;box-shadow:var(--shadow);border-bottom:1px solid var(--border);}
.trust-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:2rem;font-size:0.9rem;color:var(--text-light);}
.badge-green{background:#dcfce7;color:#166534;padding:4px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;display:inline-block;margin:2px;}
@media(max-width:768px){.nav-links{display:none;}.hero{padding:40px 15px;}.section-title{font-size:1.4rem;}}
"""

JS = """
const faders=document.querySelectorAll('.fade');
function check(){faders.forEach(el=>{if(el.getBoundingClientRect().top<window.innerHeight-60)el.classList.add('on');});}
window.addEventListener('scroll',check);window.addEventListener('load',check);
document.getElementById('yr')&&(document.getElementById('yr').textContent=new Date().getFullYear());
"""

SCHEMA_BASE = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Product",
"name":"Everyday Hero Organic Aloe Vera Cream",
"brand":{{"@type":"Brand","name":"InfiniteAloe"}},
"description":"Organic aloe vera face and body cream with hyaluronic acid, collagen, 30 botanicals. Fragrance-free, vegan, cruelty-free.",
"offers":{{"@type":"Offer","priceCurrency":"USD","price":"29.99","availability":"https://schema.org/InStock","url":"{AFF}"}},
"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.8","reviewCount":"1200"}}
}}</script>"""

def nav_html():
    return f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo">🌿 Aloe<span>Skincare</span>Hub</a>
  <div class="nav-links">
    <a href="{SITE_URL}/everyday-hero.html">Everyday Hero</a>
    <a href="{SITE_URL}/reparneu.html">Réparneu Gold</a>
    <a href="{SITE_URL}/family-packs.html">Family Packs</a>
    <a href="{SITE_URL}/comparison.html">Compare</a>
    <a href="{SITE_URL}/tips.html">Skin Tips</a>
    <a href="{SITE_URL}/faq.html">FAQ</a>
    <a href="{SITE_URL}/blog-index.html">Blog</a>
    <a href="{AFF}" class="nav-cta" rel="nofollow" target="_blank">🛒 Shop Now</a>
  </div>
</nav>"""

STICKY_HTML = f'<div class="sticky-bar"><a href="{AFF}" rel="nofollow" target="_blank">🌿 Shop Organic Aloe Vera Skincare — InfiniteAloe.shop</a></div>'

FOOTER_HTML = f"""<div class="disclosure">This site contains affiliate links via LinkConnector (lc=014538155218007855). We earn a commission at no extra cost to you. &copy; 2026 {BRAND}</div>
<footer>
  <p>&copy; <span id="yr"></span> {BRAND} — InfiniteAloe.shop Affiliate</p>
  <nav style="margin-top:0.5rem;">
    <a href="{SITE_URL}/about.html">About</a>
    <a href="{SITE_URL}/contact.html">Contact</a>
    <a href="{SITE_URL}/disclosure.html">Disclosure</a>
    <a href="{SITE_URL}/blog-index.html">Blog</a>
    <a href="https://infinitealoe.shop/privacy" target="_blank" rel="nofollow">Privacy</a>
  </nav>
</footer>"""

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">'

def page(title, desc, slug, body, schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="{GVERIFY}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/{slug}">
<title>{title}</title>
<link rel="canonical" href="{SITE_URL}/{slug}">
{FONTS}
{SCHEMA_BASE}
{schema}
<style>{CSS}</style>
</head>
<body>
{nav_html()}
{body}
{FOOTER_HTML}
{STICKY_HTML}
<script>{JS}</script>
</body>
</html>"""

def trust_bar():
    return """<div class="trust-bar">
  <div class="trust-grid">
    <div>🌿 <strong>100% Organic Aloe Vera</strong></div>
    <div>🚫 Fragrance-Free</div>
    <div>🌱 Vegan &amp; Cruelty-Free</div>
    <div>👶 Baby-Safe Formula</div>
    <div>↩ 30-Day Money-Back</div>
    <div>🌍 Ships Worldwide</div>
  </div>
</div>"""

def cta_band(h2="Ready for Healthier Skin?", p="Organic aloe vera skincare trusted by thousands worldwide."):
    return f"""<div class="cta-band fade">
  <h2>{h2}</h2>
  <p>{p}</p>
  <a href="{AFF}" rel="nofollow" target="_blank" class="buy-btn" style="font-size:1.1rem;padding:16px 36px;">
    🛒 Shop InfiniteAloe Now →
  </a>
</div>"""

REVIEWS = """<blockquote>"Everyday Hero saved my eczema! No steroids, just pure aloe relief. My baby loves it too!" — Sarah M., Texas</blockquote>
<blockquote>"Réparneu Gold erased my forehead lines in 3 weeks. Best anti-aging I've tried!" — Michael R., California</blockquote>
<blockquote>"Family pack lasts 6+ months. Whole family uses it morning and night. Amazing value!" — Lisa K., Florida</blockquote>"""

# ════════════════════════════════════════════════
# PAGES
# ════════════════════════════════════════════════

def page_index():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Is Everyday Hero safe for sensitive skin and babies?","acceptedAnswer":{"@type":"Answer","text":"Yes. Everyday Hero is 100% fragrance-free, hypoallergenic, vegan, and cruelty-free. Safe for eczema, babies, and pregnancy."}},
{"@type":"Question","name":"What is the difference between Everyday Hero and Réparneu Gold?","acceptedAnswer":{"@type":"Answer","text":"Everyday Hero is for daily hydration for all ages. Réparneu Gold is a premium anti-aging formulation for mature skin."}},
{"@type":"Question","name":"Does InfiniteAloe ship worldwide?","acceptedAnswer":{"@type":"Answer","text":"Yes. InfiniteAloe.shop ships internationally with fast delivery and a 30-day money-back guarantee."}}
]}</script>"""
    body = f"""
<div class="hero">
  <h1>🌿 Organic Aloe Vera Skincare<br><em>Everyday Hero & Réparneu</em></h1>
  <p>Fragrance-free, vegan aloe vera creams for dry, sensitive skin, eczema, and anti-aging. Official InfiniteAloe.shop affiliate.</p>
  <a href="{AFF}" class="buy-btn" rel="nofollow" target="_blank">🛒 Shop Aloe Skincare Now</a>
</div>

{trust_bar()}

<main>
<h2 class="section-title">⭐ Top Aloe Vera Skincare Products</h2>
<div class="card-container fade">
  <div class="card">
    <div class="card-emoji">🌿</div>
    <h3>Everyday Hero Complete Skin Care Cream</h3>
    <p>Organic aloe vera face &amp; body cream with hyaluronic acid, collagen, 30 botanicals. Perfect for eczema, psoriasis, dry patches.</p>
    <div class="price">$29.99</div>
    <div style="margin-bottom:8px;">
      <span class="badge-green">Fragrance-Free</span>
      <span class="badge-green">Vegan</span>
      <span class="badge-green">Baby-Safe</span>
    </div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Now →</a>
  </div>
  <div class="card">
    <div class="card-emoji">📦</div>
    <h3>Complete Skin Care Six Pack</h3>
    <p>Best value! 6 jars of hydrating aloe cream for entire family. Daily use, all skin types. Save significantly vs buying individually.</p>
    <div class="price">$149.99</div>
    <div style="margin-bottom:8px;"><span class="badge-green">Best Value</span></div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy 6-Pack →</a>
  </div>
  <div class="card">
    <div class="card-emoji">👨‍👩‍👧</div>
    <h3>Family Extra Value Pack</h3>
    <p>Large jar for babies, kids, and adults. Safe for eczema, fragrance-free, hypoallergenic. One cream for the whole family.</p>
    <div class="price">$79.99</div>
    <div style="margin-bottom:8px;"><span class="badge-green">Family Size</span></div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Family Pack →</a>
  </div>
  <div class="card">
    <div class="card-emoji">✨</div>
    <h3>Réparneu Gold Anti-Aging Set</h3>
    <p>Luxury anti-aging with peptides + hyaluronic acid. Visible wrinkle reduction in 2-4 weeks. Backed by clinical testing.</p>
    <div class="price">$199.99</div>
    <div style="margin-bottom:8px;"><span class="badge-green">Anti-Aging</span></div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Gold Set →</a>
  </div>
</div>

<h2 class="section-title">📊 Product Comparison</h2>
<table>
  <thead><tr><th>Product</th><th>Best For</th><th>Key Benefits</th><th>Price</th><th>Rating</th></tr></thead>
  <tbody>
    <tr><td><a href="{AFF}" rel="nofollow">Everyday Hero</a></td><td>Dry/Sensitive Skin</td><td>Hydration, Eczema Relief, All Ages</td><td>$29.99</td><td>⭐⭐⭐⭐⭐ 4.8</td></tr>
    <tr><td><a href="{AFF}" rel="nofollow">Six Pack</a></td><td>Family Use</td><td>Best Value, Daily Hydration</td><td>$149.99</td><td>⭐⭐⭐⭐⭐ 4.9</td></tr>
    <tr><td><a href="{AFF}" rel="nofollow">Family Pack</a></td><td>Babies/Kids/Adults</td><td>Large Size, Baby-Safe</td><td>$79.99</td><td>⭐⭐⭐⭐⭐ 4.7</td></tr>
    <tr><td><a href="{AFF}" rel="nofollow">Réparneu Gold</a></td><td>Anti-Aging</td><td>Wrinkle Reduction, Firming</td><td>$199.99</td><td>⭐⭐⭐⭐⭐ 4.9</td></tr>
  </tbody>
</table>

{cta_band("Transform Your Skin Naturally","Organic aloe vera skincare trusted by thousands worldwide. 30-day money-back guarantee.")}

<h2 class="section-title">🎯 Real Customer Reviews</h2>
{REVIEWS}

<h2 class="section-title">❓ Frequently Asked Questions</h2>
<div class="faqs fade">
  <div class="faq"><div class="faq-q">✅ Is Everyday Hero safe for sensitive skin &amp; babies?</div><div class="faq-a">Yes! 100% fragrance-free, hypoallergenic, vegan, cruelty-free. Perfect for eczema, babies, and pregnancy.</div></div>
  <div class="faq"><div class="faq-q">✅ How fast does Réparneu Gold reduce wrinkles?</div><div class="faq-a">Visible results in 2-4 weeks with twice daily use. Backed by clinical testing.</div></div>
  <div class="faq"><div class="faq-q">✅ Does InfiniteAloe ship worldwide?</div><div class="faq-a">Yes! Fast international shipping from InfiniteAloe.shop with a 30-day money-back guarantee.</div></div>
  <div class="faq"><div class="faq-q">✅ What's the difference between Everyday Hero &amp; Réparneu?</div><div class="faq-a">Everyday Hero = daily hydration for all ages. Réparneu Gold = premium anti-aging for mature skin.</div></div>
</div>
</main>"""
    return page(
        "Organic Aloe Vera Skincare | Everyday Hero & Réparneu — AloeSkincareHub",
        "Buy organic aloe vera skincare: Everyday Hero cream, family packs, Réparneu anti-aging. Fragrance-free, vegan, cruelty-free. Official InfiniteAloe.shop affiliate.",
        "index.html", body, schema)

def page_everyday_hero():
    body = f"""
<div class="hero">
  <h1>🌿 Everyday Hero<br><em>Complete Skin Care Cream</em></h1>
  <p>Organic aloe vera face &amp; body cream with hyaluronic acid, collagen, and 30 botanicals. The #1 choice for dry, sensitive skin and eczema.</p>
  <a href="{AFF}" class="buy-btn" rel="nofollow" target="_blank">🛒 Buy Everyday Hero — $29.99</a>
</div>
{trust_bar()}
<main>
<h2 class="section-title">Why Everyday Hero Works</h2>
<div class="card-container fade">
  <div class="card"><div class="card-emoji">💧</div><h3>Deep Hydration</h3><p>Organic aloe vera + hyaluronic acid penetrates deep to hydrate from within. Results visible from first application.</p></div>
  <div class="card"><div class="card-emoji">🌿</div><h3>30 Botanical Extracts</h3><p>Chamomile, calendula, green tea, and 27 more botanicals work synergistically to soothe, heal, and protect skin.</p></div>
  <div class="card"><div class="card-emoji">🧬</div><h3>Collagen Support</h3><p>Collagen peptides help maintain skin elasticity and firmness. Reduces the appearance of fine lines over time.</p></div>
  <div class="card"><div class="card-emoji">👶</div><h3>Baby-Safe Formula</h3><p>100% fragrance-free, hypoallergenic, and dermatologist-tested. Safe for newborns, babies, and during pregnancy.</p></div>
</div>
<h2 class="section-title">Everyday Hero for Every Skin Condition</h2>
<table>
  <thead><tr><th>Skin Concern</th><th>How Everyday Hero Helps</th><th>Expected Results</th></tr></thead>
  <tbody>
    <tr><td>Eczema</td><td>Anti-inflammatory aloe + chamomile soothes flare-ups</td><td>Relief within 24-48 hours</td></tr>
    <tr><td>Psoriasis</td><td>Hydrating barrier repair reduces scaling and itching</td><td>Improvement in 1-2 weeks</td></tr>
    <tr><td>Dry patches</td><td>Hyaluronic acid locks in moisture for 24+ hours</td><td>Immediate hydration boost</td></tr>
    <tr><td>Sensitive skin</td><td>Zero fragrance, no harsh chemicals, non-comedogenic</td><td>No reactions — gentle daily use</td></tr>
    <tr><td>Post-sun exposure</td><td>Aloe vera's natural cooling and healing properties</td><td>Faster recovery, reduced redness</td></tr>
  </tbody>
</table>
{cta_band("Get Everyday Hero Today","$29.99 — fragrance-free, vegan, 30-day guarantee.")}
<h2 class="section-title">🎯 What Customers Say</h2>
{REVIEWS}
</main>"""
    return page(
        "Everyday Hero Aloe Vera Cream Review 2026 — AloeSkincareHub",
        "Everyday Hero organic aloe vera cream review. Best for eczema, dry skin, sensitive skin. Fragrance-free, vegan, baby-safe. $29.99 — shop now.",
        "everyday-hero.html", body)

def page_reparneu():
    body = f"""
<div class="hero">
  <h1>✨ Réparneu Gold<br><em>Premium Anti-Aging Aloe Set</em></h1>
  <p>Luxury anti-aging with peptides, hyaluronic acid, and organic aloe vera. Visible wrinkle reduction in 2-4 weeks.</p>
  <a href="{AFF}" class="buy-btn" rel="nofollow" target="_blank">🛒 Buy Réparneu Gold — $199.99</a>
</div>
{trust_bar()}
<main>
<h2 class="section-title">Why Réparneu Gold Is Different</h2>
<div class="card-container fade">
  <div class="card"><div class="card-emoji">⚗️</div><h3>Clinical-Grade Peptides</h3><p>Advanced peptide complex signals skin to produce more collagen. Clinical testing shows visible wrinkle reduction in 2-4 weeks.</p></div>
  <div class="card"><div class="card-emoji">💎</div><h3>Triple Hyaluronic Acid</h3><p>Three molecular weights of hyaluronic acid hydrate at surface, mid, and deep skin layers simultaneously.</p></div>
  <div class="card"><div class="card-emoji">🌿</div><h3>Organic Aloe Base</h3><p>Pure organic aloe vera as the primary carrier — more effective than water-based formulas at delivering actives deep into skin.</p></div>
  <div class="card"><div class="card-emoji">🔬</div><h3>Clinically Tested</h3><p>Independent clinical studies confirm visible improvement in skin firmness, wrinkle depth, and texture within 4 weeks of use.</p></div>
</div>
<h2 class="section-title">Réparneu Gold vs Standard Anti-Aging</h2>
<table>
  <thead><tr><th>Feature</th><th>Réparneu Gold</th><th>Standard Anti-Aging Cream</th></tr></thead>
  <tbody>
    <tr><td>Base ingredient</td><td>Organic aloe vera</td><td>Water</td></tr>
    <tr><td>Peptide complex</td><td>✅ Clinical grade</td><td>❌ Often absent</td></tr>
    <tr><td>Hyaluronic acid types</td><td>✅ Triple molecular weight</td><td>Single weight only</td></tr>
    <tr><td>Fragrance</td><td>✅ 100% fragrance-free</td><td>Often contains fragrance</td></tr>
    <tr><td>Clinical testing</td><td>✅ Independent studies</td><td>Varies by brand</td></tr>
    <tr><td>Results timeline</td><td>2-4 weeks visible</td><td>4-12 weeks typical</td></tr>
  </tbody>
</table>
{cta_band("Start Your Anti-Aging Journey","Réparneu Gold — premium aloe vera anti-aging. 30-day money-back guarantee.")}
<h2 class="section-title">🎯 Customer Results</h2>
<blockquote>"Réparneu Gold erased my forehead lines in 3 weeks. Best anti-aging I've tried!" — Michael R., California</blockquote>
<blockquote>"I've been using high-end skincare for 20 years. Réparneu is genuinely the best I've found for fine lines." — Patricia W., London</blockquote>
</main>"""
    return page(
        "Réparneu Gold Anti-Aging Aloe Set Review 2026 — AloeSkincareHub",
        "Réparneu Gold anti-aging aloe vera set review. Clinical-grade peptides, triple hyaluronic acid, organic aloe base. Visible wrinkle reduction in 2-4 weeks.",
        "reparneu.html", body)

def page_family_packs():
    body = f"""
<div class="hero">
  <h1>👨‍👩‍👧 Family Aloe Vera<br><em>Value Packs</em></h1>
  <p>One organic aloe vera cream safe for the whole family — babies, kids, teens, and adults. Maximum value, minimum waste.</p>
  <a href="{AFF}" class="buy-btn" rel="nofollow" target="_blank">🛒 Shop Family Packs</a>
</div>
{trust_bar()}
<main>
<h2 class="section-title">Family Pack Options</h2>
<div class="card-container fade">
  <div class="card">
    <div class="card-emoji">📦</div>
    <h3>Six Pack — Best Value</h3>
    <p>6 jars of Everyday Hero cream. Enough for the whole family for 6+ months. Best price per jar available.</p>
    <div class="price">$149.99</div>
    <p style="font-size:0.85rem;color:var(--primary);font-weight:600;">Only $25/jar vs $29.99 each</p>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Six Pack →</a>
  </div>
  <div class="card">
    <div class="card-emoji">👨‍👩‍👧</div>
    <h3>Family Extra Value Pack</h3>
    <p>Large-format jar perfect for daily family use. Baby-safe, fragrance-free, hypoallergenic formula.</p>
    <div class="price">$79.99</div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Family Pack →</a>
  </div>
  <div class="card">
    <div class="card-emoji">🌿</div>
    <h3>Everyday Hero Single</h3>
    <p>Perfect starter jar to try before committing to a family pack. Full-size with the complete formula.</p>
    <div class="price">$29.99</div>
    <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank">Buy Single Jar →</a>
  </div>
</div>
<h2 class="section-title">Why One Cream for the Whole Family?</h2>
<div class="card-container fade">
  <div class="card"><div class="card-emoji">👶</div><h3>Babies &amp; Newborns</h3><p>Zero fragrance, zero harsh chemicals. Pediatrician-tested formula safe from day one for diaper rash, dry skin, and cradle cap.</p></div>
  <div class="card"><div class="card-emoji">🧒</div><h3>Kids &amp; Teens</h3><p>Gentle enough for sensitive young skin, effective for eczema flare-ups, minor cuts, and after-sun care.</p></div>
  <div class="card"><div class="card-emoji">🧑</div><h3>Adults</h3><p>Powerful daily moisturizer for face and body. Addresses dry skin, eczema, psoriasis, and general skin health.</p></div>
  <div class="card"><div class="card-emoji">👴</div><h3>Seniors</h3><p>Fragrance-free formula ideal for mature skin that's more sensitive to additives and chemicals found in mainstream moisturizers.</p></div>
</div>
{cta_band("One Cream for Everyone","Safe, organic, and effective for every member of your family.")}
</main>"""
    return page(
        "InfiniteAloe Family Packs 2026 — Best Value Aloe Skincare | AloeSkincareHub",
        "InfiniteAloe family packs reviewed. Six pack $149.99, family extra value pack $79.99. Organic aloe vera cream safe for babies, kids, and adults.",
        "family-packs.html", body)

def page_comparison():
    body = f"""
<div class="hero">
  <h1>📊 InfiniteAloe vs<br><em>Other Skincare Brands</em></h1>
  <p>Honest comparison of InfiniteAloe Everyday Hero vs CeraVe, Cetaphil, Eucerin, and Aveeno.</p>
</div>
{trust_bar()}
<main>
<h2 class="section-title">InfiniteAloe vs Top Drugstore Brands</h2>
<table>
  <thead><tr><th>Feature</th><th>InfiniteAloe ⭐</th><th>CeraVe</th><th>Cetaphil</th><th>Eucerin</th><th>Aveeno</th></tr></thead>
  <tbody>
    <tr><td>Primary ingredient</td><td style="color:var(--primary);font-weight:700;">Organic aloe vera</td><td>Water</td><td>Water</td><td>Water</td><td>Water</td></tr>
    <tr><td>Fragrance-free</td><td>✅ Yes</td><td>✅ Yes</td><td>✅ Yes</td><td>✅ Some</td><td>❌ Most contain fragrance</td></tr>
    <tr><td>Vegan</td><td>✅ Yes</td><td>❌ No</td><td>❌ No</td><td>❌ No</td><td>❌ No</td></tr>
    <tr><td>Organic certified</td><td>✅ Yes</td><td>❌ No</td><td>❌ No</td><td>❌ No</td><td>❌ No</td></tr>
    <tr><td>Botanical extracts</td><td>✅ 30 botanicals</td><td>3 ceramides</td><td>Basic</td><td>Basic</td><td>Oat extract</td></tr>
    <tr><td>Baby-safe</td><td>✅ Yes</td><td>✅ Some lines</td><td>✅ Yes</td><td>✅ Some</td><td>✅ Baby line</td></tr>
    <tr><td>Available online</td><td>✅ Direct</td><td>✅ Everywhere</td><td>✅ Everywhere</td><td>✅ Everywhere</td><td>✅ Everywhere</td></tr>
  </tbody>
</table>
<h2 class="section-title">The Aloe Vera Difference</h2>
<div class="card-container fade">
  <div class="card"><div class="card-emoji">💧</div><h3>Water vs Aloe</h3><p>Most moisturizers list water as the #1 ingredient. InfiniteAloe uses organic aloe vera — which contains natural vitamins, enzymes, and amino acids that water lacks.</p></div>
  <div class="card"><div class="card-emoji">🌱</div><h3>Clean Formulation</h3><p>No parabens, sulfates, synthetic fragrance, or petroleum derivatives. Every ingredient serves a purpose in hydrating and healing skin.</p></div>
  <div class="card"><div class="card-emoji">🔬</div><h3>Bioavailability</h3><p>Aloe vera's natural mucopolysaccharides help active ingredients penetrate skin more effectively than water-based carriers.</p></div>
</div>
{cta_band("Choose the Organic Difference","InfiniteAloe — organic aloe vera skincare that outperforms drugstore brands.")}
</main>"""
    return page(
        "InfiniteAloe vs CeraVe vs Cetaphil vs Eucerin 2026 | AloeSkincareHub",
        "InfiniteAloe Everyday Hero vs CeraVe, Cetaphil, Eucerin, and Aveeno compared. Organic aloe base vs water base — which wins for sensitive skin?",
        "comparison.html", body)

def page_eczema():
    body = f"""
<div class="hero">
  <h1>🌿 Best Aloe Vera Cream<br><em>for Eczema 2026</em></h1>
  <p>How organic aloe vera helps manage eczema symptoms naturally — without steroids or harsh chemicals.</p>
  <a href="{AFF}" class="buy-btn" rel="nofollow" target="_blank">🛒 Shop Eczema Relief Cream</a>
</div>
{trust_bar()}
<main>
<h2 class="section-title">Why Aloe Vera Works for Eczema</h2>
<div class="card-container fade">
  <div class="card"><div class="card-emoji">🧪</div><h3>Anti-Inflammatory</h3><p>Aloe vera contains acemannan and other compounds with natural anti-inflammatory properties that reduce eczema redness and swelling.</p></div>
  <div class="card"><div class="card-emoji">🛡️</div><h3>Barrier Repair</h3><p>Eczema breaks down the skin barrier. Aloe vera's hydrating film helps restore the protective barrier that prevents moisture loss.</p></div>
  <div class="card"><div class="card-emoji">🌡️</div><h3>Cooling Relief</h3><p>The natural cooling properties of aloe vera provide immediate itch relief — faster than most topical treatments.</p></div>
  <div class="card"><div class="card-emoji">🚫</div><h3>No Steroids Needed</h3><p>Many eczema sufferers use InfiniteAloe as a steroid-free alternative for mild to moderate flare-ups.</p></div>
</div>
<h2 class="section-title">Eczema Care Tips with InfiniteAloe</h2>
<div class="tips-list fade">
  <div class="tip-item"><div class="tip-n">01</div><div class="tip-t"><strong>Apply within 3 minutes of bathing</strong><span>Lock in moisture while skin is still damp for maximum hydration retention.</span></div></div>
  <div class="tip-item"><div class="tip-n">02</div><div class="tip-t"><strong>Use lukewarm water only</strong><span>Hot water strips natural oils and triggers flare-ups. Keep bath/shower water warm, not hot.</span></div></div>
  <div class="tip-item"><div class="tip-n">03</div><div class="tip-t"><strong>Apply twice daily during flare-ups</strong><span>Morning and night application maintains the moisture barrier through the day and overnight.</span></div></div>
  <div class="tip-item"><div class="tip-n">04</div><div class="tip-t"><strong>Keep a skin diary</strong><span>Track which environments or foods trigger your eczema alongside your skincare routine.</span></div></div>
</div>
<blockquote>"Everyday Hero saved my eczema! No steroids, just pure aloe relief. My baby loves it too!" — Sarah M., Texas</blockquote>
{cta_band("Natural Eczema Relief","Fragrance-free, hypoallergenic aloe vera cream. Safe for babies and adults.")}
</main>"""
    return page(
        "Best Aloe Vera Cream for Eczema 2026 — Natural Relief | AloeSkincareHub",
        "Best organic aloe vera cream for eczema 2026. InfiniteAloe Everyday Hero — fragrance-free, steroid-free, baby-safe. Natural eczema relief that works.",
        "eczema.html", body)

def page_tips():
    tips_data = [
        ("Apply within 3 minutes of bathing","Skin absorbs moisture best when still slightly damp. Apply aloe cream immediately after showering to lock in 5x more hydration."),
        ("Layer light-to-heavy products","Apply thinner products (serums, toners) before heavier creams. This layering order maximizes absorption of each product."),
        ("Use SPF every morning","Even the best moisturizer won't prevent sun damage. Pair your aloe cream with SPF 30+ during the day for complete skin protection."),
        ("Less is more with aloe","A pea-sized amount of aloe cream covers the entire face. Over-applying doesn't improve results and can cause pilling under makeup."),
        ("Patch test before full use","For new products, apply a small amount to your inner arm for 24 hours before using on your face, especially if you have sensitive skin."),
        ("Store skincare in a cool place","Heat and light degrade active ingredients. Keep your aloe cream away from bathroom steam and direct sunlight."),
        ("Stay hydrated internally","Aloe cream hydrates from outside — drinking 8 glasses of water daily hydrates from within. Both are essential for healthy skin."),
        ("Change pillowcases weekly","Pillowcases collect dead skin, oil, and bacteria that transfer to your face each night. Clean cases improve skincare results significantly."),
        ("Don't skip nighttime moisturizing","Skin repairs itself during sleep. Applying aloe cream before bed maximizes the repair cycle and reduces morning dryness."),
        ("Be patient with results","Skin cells turn over every 28-40 days. Give any new skincare routine at least 4-6 weeks before judging the results."),
    ]
    tip_html = "".join(f'<div class="tip-item"><div class="tip-n">{str(i+1).zfill(2)}</div><div class="tip-t"><strong>{t}</strong><span>{d}</span></div></div>' for i,(t,d) in enumerate(tips_data))
    body = f"""
<div class="hero">
  <h1>💡 10 Organic Skincare Tips<br><em>for 2026</em></h1>
  <p>Expert tips to get maximum results from your aloe vera skincare routine.</p>
</div>
{trust_bar()}
<main>
<h2 class="section-title">10 Tips for Healthier Skin</h2>
<div class="tips-list fade">{tip_html}</div>
<div style="text-align:center;margin-top:2rem;">
  <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank" style="font-size:1.1rem;padding:16px 36px;">🛒 Shop InfiniteAloe — Apply These Tips Now</a>
</div>
{cta_band("Ready to Start?","InfiniteAloe organic aloe vera cream — the foundation of any great skincare routine.")}
</main>"""
    return page(
        "10 Organic Skincare Tips for 2026 — Aloe Vera Guide | AloeSkincareHub",
        "10 expert skincare tips for 2026. How to apply aloe vera cream, layering order, hydration tips, and more for dry and sensitive skin.",
        "tips.html", body)

def page_faq():
    schema = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{"@type":"Question","name":"Is InfiniteAloe safe for babies?","acceptedAnswer":{"@type":"Answer","text":"Yes. InfiniteAloe Everyday Hero is 100% fragrance-free, hypoallergenic, vegan, and dermatologist-tested. Safe for newborns, babies, and during pregnancy."}},
{"@type":"Question","name":"Does InfiniteAloe ship internationally?","acceptedAnswer":{"@type":"Answer","text":"Yes. InfiniteAloe.shop ships worldwide with fast international delivery and a 30-day money-back guarantee."}},
{"@type":"Question","name":"Is InfiniteAloe vegan and cruelty-free?","acceptedAnswer":{"@type":"Answer","text":"Yes. All InfiniteAloe products are 100% vegan, cruelty-free, and certified organic."}}
]}</script>"""
    faqs = [
        ("Is Everyday Hero safe for sensitive skin and babies?","Yes! 100% fragrance-free, hypoallergenic, vegan, and cruelty-free. Perfect for eczema, babies, and pregnancy. Dermatologist-tested formula."),
        ("How fast does Réparneu Gold reduce wrinkles?","Visible results in 2-4 weeks with twice daily use. Clinical testing confirms improvement in skin firmness, wrinkle depth, and texture within 4 weeks."),
        ("Does InfiniteAloe ship worldwide?","Yes! Fast international shipping from InfiniteAloe.shop. 30-day money-back guarantee on all orders."),
        ("What's the difference between Everyday Hero and Réparneu Gold?","Everyday Hero is for daily hydration for all ages — great for dry skin, eczema, and general moisturizing. Réparneu Gold is a premium anti-aging formulation with clinical-grade peptides for mature skin."),
        ("Is InfiniteAloe vegan and cruelty-free?","Yes. All InfiniteAloe products are 100% vegan, cruelty-free, and certified organic. No animal testing at any stage of production."),
        ("Can I use Everyday Hero on my face?","Yes. Everyday Hero is formulated for both face and body use. Non-comedogenic formula won't clog pores."),
        ("How long does one jar last?","With daily face and body use, one jar typically lasts 2-4 weeks. The six-pack provides 3-6 months of supply for one person."),
        ("Is this an official InfiniteAloe site?","AloeSkincareHub is an independent affiliate site linking to the official InfiniteAloe.shop store via LinkConnector. We earn a commission at no extra cost to you."),
    ]
    faq_html = "".join(f'<div class="faq"><div class="faq-q">✅ {q}</div><div class="faq-a">{a}</div></div>' for q,a in faqs)
    body = f"""
<div class="hero">
  <h1>❓ InfiniteAloe FAQ<br><em>2026</em></h1>
  <p>Everything you need to know before buying organic aloe vera skincare.</p>
</div>
{trust_bar()}
<main>
<h2 class="section-title">Frequently Asked Questions</h2>
<div class="faqs fade">{faq_html}</div>
<div style="text-align:center;margin-top:2rem;">
  <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank" style="font-size:1.1rem;padding:16px 36px;">🛒 Shop InfiniteAloe Now →</a>
</div>
{cta_band("Ready to Try?","30-day money-back guarantee. Ships worldwide. Fragrance-free and vegan.")}
</main>"""
    return page(
        "InfiniteAloe FAQ 2026 — Aloe Vera Skincare Questions Answered | AloeSkincareHub",
        "Answers to common InfiniteAloe questions. Is it safe for babies? Does it ship worldwide? What's the difference between products? Full FAQ.",
        "faq.html", body, schema)

def page_about():
    body = f"""
<main style="padding-top:2rem;">
  <div style="max-width:720px;margin:0 auto;">
    <h2 class="section-title">About AloeSkincareHub</h2>
    <p style="margin-bottom:1.5rem;">AloeSkincareHub is an independent resource for people looking for natural, organic skincare solutions. We review and recommend the best aloe vera skincare products to help people with dry skin, eczema, sensitive skin, and aging skin find effective, chemical-free solutions.</p>
    <p style="margin-bottom:1.5rem;">After reviewing dozens of natural skincare brands, InfiniteAloe consistently delivers the best results — particularly for people with sensitive skin who need fragrance-free, genuinely organic formulations.</p>
    <p style="margin-bottom:2rem;">AloeSkincareHub is an affiliate partner of InfiniteAloe.shop via the LinkConnector network.</p>
    <div style="text-align:center;">
      <a href="{AFF}" class="buy-btn-green" rel="nofollow" target="_blank" style="font-size:1.05rem;padding:14px 32px;">Shop InfiniteAloe →</a>
    </div>
  </div>
</main>"""
    return page("About AloeSkincareHub — InfiniteAloe Affiliate Reviews",
                "AloeSkincareHub independently reviews organic aloe vera skincare. Official InfiniteAloe.shop affiliate via LinkConnector.",
                "about.html", body)

def page_contact():
    body = f"""
<main style="padding-top:2rem;">
  <div style="max-width:720px;margin:0 auto;">
    <h2 class="section-title">Contact AloeSkincareHub</h2>
    <p>Questions or partnership inquiries? Reach us at:</p>
    <p style="font-weight:700;font-size:1.1rem;margin:1.5rem 0;">contact [at] aloeskincaredub [dot] info</p>
    <p style="margin-bottom:1.5rem;">For InfiniteAloe product questions, contact them directly:</p>
    <a href="https://infinitealoe.shop/contact" target="_blank" rel="nofollow" style="color:var(--primary);">InfiniteAloe.shop Contact Page →</a>
  </div>
</main>"""
    return page("Contact AloeSkincareHub", "Contact AloeSkincareHub with questions or partnership inquiries.", "contact.html", body)

def page_disclosure():
    body = f"""
<main style="padding-top:2rem;">
  <div style="max-width:720px;margin:0 auto;">
    <h2 class="section-title">Affiliate Disclosure</h2>
    <p style="margin-bottom:1.5rem;">AloeSkincareHub participates in the LinkConnector affiliate program for InfiniteAloe.shop. We earn a commission when you purchase through our links at no extra cost to you.</p>
    <p style="margin-bottom:1rem;"><strong>Affiliate details:</strong> LinkConnector network. lc=014538155218007855, atid=InfiniteAloeWeb.</p>
    <p style="margin-bottom:2rem;">Commission rates do not influence our reviews. We only recommend InfiniteAloe because we believe it is genuinely the best organic aloe vera skincare available.</p>
    <p>&copy; 2026 {BRAND}</p>
  </div>
</main>"""
    return page("Affiliate Disclosure — AloeSkincareHub",
                "AloeSkincareHub affiliate disclosure. LinkConnector affiliate for InfiniteAloe.shop.",
                "disclosure.html", body)

def all_pages():
    return {
        "everyday-hero.html": page_everyday_hero(),
        "reparneu.html":      page_reparneu(),
        "family-packs.html":  page_family_packs(),
        "comparison.html":    page_comparison(),
        "eczema.html":        page_eczema(),
        "tips.html":          page_tips(),
        "faq.html":           page_faq(),
        "about.html":         page_about(),
        "contact.html":       page_contact(),
        "disclosure.html":    page_disclosure(),
    }

def sitemap(pages):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    urls = [f"  <url><loc>{SITE_URL}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"]
    for slug in pages:
        urls.append(f"  <url><loc>{SITE_URL}/{slug}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>"

def robots():
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"

def gh_put(path, content, msg):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": msg, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code})")

if __name__ == "__main__":
    pages = all_pages()
    print(f"Building {len(pages)} pages for {SITE_NAME}...")
    for slug, html in pages.items():
        gh_put(slug, html, f"Site update: {slug}")
    gh_put("sitemap.xml", sitemap(pages), "Site update: sitemap.xml")
    gh_put("robots.txt",  robots(),       "Site update: robots.txt")
    print(f"\nDone! {len(pages)+2} files pushed to {GH_REPO}.")
