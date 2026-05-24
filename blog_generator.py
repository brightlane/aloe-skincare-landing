#!/usr/bin/env python3
"""
aloe-skincare-landing Daily Blog Generator
30 posts: aloe vera skincare, eczema, anti-aging, organic skincare guides
No API key — cycles daily
"""

import os, json, base64, requests
from datetime import datetime, timezone

AFF        = "https://www.linkconnector.com/ta.php?lc=014538155218007855&atid=InfiniteAloeWeb&lcpt=0&lcpf=3"
SITE_URL   = "https://brightlane.github.io/aloe-skincare-landing"
GH_USER    = os.environ.get("GH_USER", "brightlane")
GH_REPO    = os.environ.get("GH_REPO", "aloe-skincare-landing")
GH_TOKEN   = os.environ.get("GITHUB_TOKEN", "")
BLOG_INDEX = "blog-index.json"
BRAND      = "AloeSkincareHub"

HEADERS = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f8fafc;color:#0f172a;line-height:1.7;}
a{color:#047857;text-decoration:none;}a:hover{text-decoration:underline;}
nav{background:linear-gradient(135deg,#059669,#1d4ed8);padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:58px;}
.nav-logo{color:#fff;font-weight:700;font-size:1.05rem;text-decoration:none;}
.nav-cta{background:#fff;color:#047857!important;padding:6px 14px;border-radius:8px;font-weight:700;font-size:0.85rem;text-decoration:none;}
.container{max-width:820px;margin:0 auto;padding:2rem 1.5rem;background:#fff;min-height:60vh;}
.meta{color:#64748b;font-size:0.85rem;margin-bottom:1.5rem;}
h1{font-size:clamp(1.6rem,4vw,2.3rem);font-weight:700;color:#0f172a;margin-bottom:0.75rem;line-height:1.2;}
h2{font-size:1.25rem;font-weight:700;color:#047857;margin:2rem 0 0.75rem;}
p{margin-bottom:1rem;color:#334155;font-size:0.97rem;}
.btn{display:inline-block;padding:13px 28px;background:linear-gradient(135deg,#059669,#1d4ed8);color:#fff;border-radius:10px;font-weight:700;font-size:0.95rem;margin:1rem 0;text-decoration:none;}
.btn:hover{background:linear-gradient(135deg,#047857,#1e40af);text-decoration:none;}
.tip-box{background:#f0fdf4;border-left:4px solid #047857;padding:1rem 1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;}
.sticky{position:fixed;bottom:0;width:100%;background:#047857;text-align:center;padding:9px;z-index:999;}
.sticky a{color:#fff;font-weight:700;font-size:0.85rem;text-decoration:none;}
footer{background:#0f172a;color:rgba(255,255,255,0.5);text-align:center;padding:1.5rem;font-size:0.8rem;margin-top:3rem;}
footer a{color:#34d399;text-decoration:none;}
"""

POSTS = [
  {
    "title": "Aloe Vera Cream vs Regular Moisturizer — What's the Real Difference?",
    "keywords": "aloe vera cream vs moisturizer, organic aloe vera benefits, why aloe vera better than regular lotion",
    "body": f"""<p>Most moisturizers use water as their primary ingredient. Aloe vera creams use something far more powerful. Here is why the difference matters for your skin.</p>
<h2>What Standard Moisturizers Are Made Of</h2>
<p>Turn over almost any drugstore moisturizer and you will find water listed first. Water is cheap, safe, and effective at providing temporary hydration — but it has no intrinsic skin benefit beyond this. The active ingredients are typically present in small amounts at the bottom of the list.</p>
<h2>What Aloe Vera Brings Instead</h2>
<p>Organic aloe vera gel contains over 200 biologically active compounds including vitamins A, C, and E, amino acids, enzymes, and mucopolysaccharides. These compounds work together to hydrate, heal, and protect skin in ways that water cannot replicate.</p>
<h2>Penetration Advantage</h2>
<p>Aloe vera's natural acemannan polysaccharides act as a carrier that helps other active ingredients penetrate the skin more effectively. This means the botanicals, peptides, and hyaluronic acid in an aloe-based formula reach deeper skin layers than they would in a water-based formula.</p>
<h2>Anti-Inflammatory Properties</h2>
<p>Water has no anti-inflammatory effect. Aloe vera contains several compounds with demonstrated anti-inflammatory activity, making it particularly beneficial for eczema, rosacea, and post-sun skin.</p>
<div class="tip-box">Apply aloe vera cream within 3 minutes of bathing while skin is still slightly damp. This locks in 5x more moisture than applying to completely dry skin.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Shop InfiniteAloe Organic Aloe Cream →</a></p>"""},
  {
    "title": "How to Use Everyday Hero Cream for Eczema — Complete Guide",
    "keywords": "everyday hero eczema guide, aloe vera eczema treatment, InfiniteAloe eczema",
    "body": f"""<p>Everyday Hero organic aloe vera cream is one of the most effective fragrance-free options for eczema management. Here is exactly how to use it for best results.</p>
<h2>Understanding Your Eczema Triggers</h2>
<p>Before using any cream, identify your triggers. Common eczema triggers include fragranced products, harsh detergents, temperature extremes, stress, and certain fabrics. Everyday Hero eliminates the fragrance trigger entirely with its 100% fragrance-free formula.</p>
<h2>The Eczema Routine with Everyday Hero</h2>
<p><strong>Morning:</strong> Cleanse with a fragrance-free gentle cleanser. Pat (don't rub) skin dry. Apply Everyday Hero within 3 minutes while skin is still slightly damp. The aloe base absorbs quickly without a greasy residue.</p>
<p><strong>Evening:</strong> Repeat the same routine. For active flare-ups, apply a slightly thicker layer at night and cover with a soft cotton layer to enhance absorption.</p>
<p><strong>During flare-ups:</strong> Apply Everyday Hero up to 3 times daily. The anti-inflammatory botanicals — chamomile and calendula — help calm redness and reduce itch.</p>
<h2>What to Expect</h2>
<p>Most users report reduced itching within 24-48 hours. Significant improvement in skin texture and redness typically appears within 1-2 weeks of consistent twice-daily use.</p>
<div class="tip-box">For babies with eczema, apply Everyday Hero after every diaper change and bath. The fragrance-free, hypoallergenic formula is safe for newborns from day one.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Get Everyday Hero for Eczema →</a></p>"""},
  {
    "title": "Réparneu Gold Review — Does It Really Reduce Wrinkles?",
    "keywords": "Réparneu Gold review, does Réparneu work, aloe vera anti-aging cream review",
    "body": f"""<p>Réparneu Gold costs $199.99 — premium pricing for a skincare product. Is it justified? Here is an honest breakdown of what it contains and whether it delivers on its anti-aging claims.</p>
<h2>What Makes Réparneu Gold Different</h2>
<p>Most anti-aging creams use water as their base. Réparneu Gold uses organic aloe vera as the primary carrier — which provides better penetration of actives into deeper skin layers. This is not just marketing; the bioavailability of peptides and hyaluronic acid is genuinely higher in an aloe-based formula.</p>
<h2>The Peptide Complex</h2>
<p>Réparneu Gold contains clinical-grade peptides that signal fibroblasts to produce more collagen. Unlike retinol (which can cause irritation), peptides work without side effects. The results are slower but more suitable for sensitive skin.</p>
<h2>Triple Hyaluronic Acid</h2>
<p>Most hyaluronic acid products use one molecular weight. Réparneu Gold uses three — which hydrate at the surface, mid-skin, and deeper dermal layers simultaneously. This explains why the plumping effect feels more substantial than single-weight alternatives.</p>
<h2>Realistic Results Timeline</h2>
<p>Visible wrinkle reduction in 2-4 weeks is achievable with consistent twice-daily use. Significant improvement in skin firmness and texture requires 8-12 weeks. This timeline aligns with how long collagen synthesis takes to produce visible results.</p>
<h2>Verdict: Yes, Worth It for Mature Skin</h2>
<p>For women over 40 with fine lines and loss of firmness, Réparneu Gold's combination of organic aloe base, clinical peptides, and triple hyaluronic acid justifies the price point.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">✨ Shop Réparneu Gold →</a></p>"""},
  {
    "title": "Best Fragrance-Free Moisturizer for Sensitive Skin 2026",
    "keywords": "best fragrance free moisturizer sensitive skin 2026, fragrance free cream review, organic fragrance free lotion",
    "body": f"""<p>Fragrance is the #1 cause of allergic contact dermatitis from skincare products. Here is why fragrance-free matters and which aloe vera cream leads in 2026.</p>
<h2>Why Fragrance Damages Sensitive Skin</h2>
<p>Synthetic and even natural fragrances contain dozens of individual chemical compounds, any of which can trigger reactions in sensitive individuals. Reactions range from mild redness and itching to severe contact dermatitis requiring medical treatment.</p>
<h2>The "Unscented" vs "Fragrance-Free" Confusion</h2>
<p>Unscented products often contain masking fragrances — chemicals added to cover up the smell of other ingredients. These still cause reactions. True fragrance-free products contain zero fragrance compounds. Always look for "fragrance-free," not "unscented."</p>
<h2>InfiniteAloe Everyday Hero — True Fragrance-Free</h2>
<p>Everyday Hero is certified fragrance-free — no masking agents, no essential oils, no natural or synthetic fragrance compounds. This makes it appropriate for even the most reactive sensitive skin types.</p>
<h2>What to Look for in a Fragrance-Free Moisturizer</h2>
<p>Beyond fragrance-free, the best sensitive skin moisturizers also avoid: parabens, sulfates, alcohol (the drying kind), dyes, and formaldehyde-releasing preservatives. Everyday Hero avoids all of these.</p>
<div class="tip-box">Always patch test new products on your inner arm for 24 hours before applying to your face, even products labeled fragrance-free.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Get Fragrance-Free Aloe Cream →</a></p>"""},
  {
    "title": "Organic Aloe Vera Skincare for Babies — What Parents Need to Know",
    "keywords": "aloe vera cream babies safe, organic baby skincare, InfiniteAloe baby eczema",
    "body": f"""<p>Choosing skincare for babies is one of the most important decisions new parents make. Here is what you need to know about using organic aloe vera cream on infants and young children.</p>
<h2>Why Baby Skin Needs Special Care</h2>
<p>Baby skin is 20-30% thinner than adult skin and absorbs substances at a higher rate. Chemicals applied to baby skin enter the bloodstream more readily than the same chemicals applied to adults. This makes ingredient quality critical.</p>
<h2>What to Avoid in Baby Skincare</h2>
<p>Avoid products containing: synthetic fragrance, parabens, sulfates, PEG compounds, artificial dyes, and formaldehyde-releasing preservatives. Many mainstream baby products contain one or more of these.</p>
<h2>Why InfiniteAloe Everyday Hero Works for Babies</h2>
<p>Everyday Hero contains zero synthetic fragrance, zero parabens, zero sulfates, and is certified vegan and cruelty-free. The organic aloe vera base is soothing for baby eczema, diaper rash, and general dry skin without any harsh chemicals.</p>
<h2>Safe Applications for Babies</h2>
<p>Everyday Hero is safe for: baby eczema, cradle cap (when moisturizing is appropriate), general dry patches, post-bath moisturizing, and diaper area moisture barrier (not for active rash — consult pediatrician).</p>
<div class="tip-box">For babies under 6 months, always consult your pediatrician before introducing new skincare products, even gentle organic options.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">👶 Shop Baby-Safe Aloe Cream →</a></p>"""},
  {
    "title": "Aloe Vera vs Hyaluronic Acid — Which Is Better for Dry Skin?",
    "keywords": "aloe vera vs hyaluronic acid dry skin, aloe vera hydration comparison, best hydrating ingredient",
    "body": f"""<p>Both aloe vera and hyaluronic acid are celebrated for hydration. Here is how they work differently and why the best products combine both.</p>
<h2>How Hyaluronic Acid Works</h2>
<p>Hyaluronic acid is a humectant — it attracts and holds water molecules. A single gram of hyaluronic acid can hold up to 6 liters of water. Applied to skin, it draws moisture from the air and from deeper skin layers to the surface.</p>
<h2>How Aloe Vera Works</h2>
<p>Aloe vera hydrates through a different mechanism. Its mucopolysaccharides form a thin film on skin that locks in moisture, while its active compounds — vitamins, amino acids, enzymes — actively support skin cell health and repair.</p>
<h2>Why They Work Better Together</h2>
<p>Hyaluronic acid attracts moisture. Aloe vera locks it in and provides the biological environment for skin healing. Together, they address both sides of hydration — delivery and retention — more effectively than either alone.</p>
<h2>InfiniteAloe's Combined Formula</h2>
<p>InfiniteAloe Everyday Hero combines organic aloe vera base with hyaluronic acid alongside 30 botanical extracts. This formulation strategy explains why users consistently report longer-lasting hydration than from either ingredient used alone.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Get Aloe + Hyaluronic Acid Cream →</a></p>"""},
  {
    "title": "How Long Does InfiniteAloe Everyday Hero Last? Usage Guide",
    "keywords": "how long does InfiniteAloe last, everyday hero usage guide, aloe cream jar size",
    "body": f"""<p>Before buying any skincare product, knowing how long it will last helps you calculate true cost per day. Here is a complete usage guide for Everyday Hero.</p>
<h2>Jar Size and Application Amount</h2>
<p>Everyday Hero comes in a 4oz (113g) jar. For face-only use, a pea-sized amount (approximately 0.5g) is sufficient per application. For full face and neck, use a slightly larger amount (1-1.5g).</p>
<h2>How Long Each Jar Lasts</h2>
<p><strong>Face only, twice daily:</strong> Approximately 75-90 days (2.5-3 months) per jar.</p>
<p><strong>Face and neck, twice daily:</strong> Approximately 45-60 days (1.5-2 months) per jar.</p>
<p><strong>Face, neck, and hands, twice daily:</strong> Approximately 30-45 days per jar.</p>
<h2>Six Pack Value Calculation</h2>
<p>The six pack at $149.99 works out to $25/jar — vs $29.99 for a single jar. For face and neck use twice daily, that is 9-12 months of supply for one person at $25/jar, or enough for a family of 2-3 for 3-4 months.</p>
<h2>Maximizing Value</h2>
<p>A little goes a long way with aloe-based creams because the formula spreads easily. Using the correct amount (pea-size for face) prevents waste and extends the jar life significantly.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🛒 Buy the Six Pack — Best Value →</a></p>"""},
  {
    "title": "Organic Skincare for Psoriasis — Can Aloe Vera Help?",
    "keywords": "aloe vera psoriasis relief, organic cream psoriasis, natural psoriasis treatment",
    "body": f"""<p>Psoriasis is a chronic skin condition that causes red, scaly patches. While aloe vera is not a cure, clinical evidence supports its use as a complementary treatment. Here is what you need to know.</p>
<h2>What Research Shows</h2>
<p>Several peer-reviewed studies have examined aloe vera for psoriasis. A notable double-blind trial published in Tropical Medicine and International Health found that an aloe vera extract cream reduced psoriasis plaques more effectively than placebo. The anti-inflammatory and skin-barrier-repair properties of aloe are the likely mechanisms.</p>
<h2>How Aloe Helps with Psoriasis Symptoms</h2>
<p><strong>Scaling:</strong> The hydrating film aloe forms on skin helps soften and reduce the scaling associated with psoriasis plaques.</p>
<p><strong>Itching:</strong> Aloe vera's cooling properties and anti-inflammatory compounds reduce itch intensity, one of the most disruptive psoriasis symptoms.</p>
<p><strong>Redness:</strong> Regular application may help reduce the erythema (redness) associated with active plaques over time.</p>
<h2>Important Notes</h2>
<p>Aloe vera is a complementary approach, not a replacement for prescribed psoriasis treatments. Always consult your dermatologist before modifying your treatment plan. Everyday Hero's fragrance-free formula is appropriate for sensitive psoriasis-affected skin.</p>
<div class="tip-box">For psoriasis on the scalp, look for aloe vera in a gel form rather than a cream. For body psoriasis, the Everyday Hero cream format works well.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Get Organic Aloe Cream for Skin Conditions →</a></p>"""},
  {
    "title": "Morning vs Night Skincare Routine — When to Use Aloe Vera Cream",
    "keywords": "morning vs night skincare routine, when to apply aloe vera cream, aloe vera skincare timing",
    "body": f"""<p>Timing matters in skincare. Knowing when to apply your aloe vera cream maximizes its benefits. Here is the complete morning and night routine guide.</p>
<h2>Morning Routine with Aloe Vera</h2>
<p><strong>Step 1:</strong> Gentle fragrance-free cleanser.</p>
<p><strong>Step 2:</strong> Apply any water-based serum or vitamin C (thinnest layer first).</p>
<p><strong>Step 3:</strong> Apply Everyday Hero aloe vera cream while skin is still slightly damp from previous steps.</p>
<p><strong>Step 4:</strong> Finish with SPF 30+ sunscreen. This is non-negotiable — no moisturizer substitutes for sun protection.</p>
<h2>Night Routine with Aloe Vera</h2>
<p><strong>Step 1:</strong> Double cleanse — oil cleanser first to remove SPF and makeup, then gentle cleanser.</p>
<p><strong>Step 2:</strong> Apply any actives (retinol, niacinamide) if you use them. Note: if using Réparneu Gold, skip retinol.</p>
<p><strong>Step 3:</strong> Apply Everyday Hero or Réparneu Gold as your final step. The occlusive properties help lock in everything applied before.</p>
<h2>Why Night Application Matters Most</h2>
<p>Skin enters repair mode during sleep, increasing cell turnover and collagen production. Applying aloe vera cream before bed provides the ingredients your skin needs during its active repair window.</p>
<div class="tip-box">For maximum overnight hydration, apply aloe cream to slightly damp skin (mist your face lightly first) and let it absorb for 2 minutes before bed.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Start Your Aloe Skincare Routine →</a></p>"""},
  {
    "title": "InfiniteAloe Family Pack vs Six Pack — Which Is the Better Deal?",
    "keywords": "InfiniteAloe six pack vs family pack, best value aloe vera pack, InfiniteAloe bulk buy",
    "body": f"""<p>InfiniteAloe offers multiple bulk options. Here is exactly how the Family Pack and Six Pack compare so you can choose the right value for your household.</p>
<h2>The Six Pack ($149.99)</h2>
<p>Six standard jars of Everyday Hero cream. At $149.99, you pay $25 per jar compared to $29.99 individually — a saving of $30 total. Best for: single person or couple who use Everyday Hero consistently and want to stock up.</p>
<h2>The Family Extra Value Pack ($79.99)</h2>
<p>One large-format jar designed for family use. The larger jar reduces packaging waste and provides a single shared supply for multiple family members. Best for: families with 2-4 people sharing one cream who prefer simplicity over having individual jars.</p>
<h2>Cost Per Day Comparison</h2>
<p>Six Pack for one person (face and neck, twice daily): approximately $0.28/day. Family Pack shared between two people (same usage): approximately $0.44/day each. The Six Pack wins on per-person cost.</p>
<h2>Which to Choose</h2>
<p>Choose the <strong>Six Pack</strong> if you want the lowest cost per jar and don't mind having multiple jars. Choose the <strong>Family Pack</strong> if you prefer one large shared jar for household simplicity and don't need 6 months of supply at once.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">🛒 Shop InfiniteAloe Value Packs →</a></p>"""},
]

while len(POSTS) < 30:
    POSTS.append(POSTS[len(POSTS) % 10])

NAV = f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">🌿 AloeSkincareHub</a>
  <a href="{AFF}" class="nav-cta" rel="nofollow" target="_blank">🛒 Shop Now</a>
</nav>"""

STICKY = f'<div class="sticky"><a href="{AFF}" rel="nofollow" target="_blank">🌿 Shop InfiniteAloe Organic Aloe Vera Skincare</a></div>'

def build_post_html(post, slug, date_str):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{post['title']} | AloeSkincareHub</title>
<meta name="description" content="{post['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/blog/{slug}">
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="container">
  <p class="meta">Published {date_str} &mdash; <a href="{SITE_URL}/blog-index.html">← All Posts</a> &mdash; by {BRAND}</p>
  <h1>{post['title']}</h1>
  {post['body']}
  <div style="border:1px solid #bbf7d0;padding:1.2rem;margin-top:2rem;border-radius:8px;background:#f0fdf4;">
    <strong>About AloeSkincareHub</strong><br>
    AloeSkincareHub independently reviews organic aloe vera skincare products. Our recommended brand is InfiniteAloe.shop — affiliate via LinkConnector (lc=014538155218007855).
  </div>
  <p style="text-align:center;margin-top:2rem;">
    <a href="{AFF}" class="btn" rel="nofollow" target="_blank">🌿 Shop InfiniteAloe — Our Top Pick →</a>
  </p>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Affiliate Disclosure</a> | lc=014538155218007855</p></footer>
{STICKY}
</body>
</html>"""

def gh_put(path, content, message):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code})")

def load_blog_index():
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return json.loads(base64.b64decode(r.json()["content"]).decode())
    return []

def save_blog_index(data):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": f"Blog index {datetime.utcnow().strftime('%Y-%m-%d')}",
               "content": base64.b64encode(json.dumps(data, indent=2).encode()).decode()}
    if sha:
        payload["sha"] = sha
    requests.put(url, headers=HEADERS, json=payload)

def build_blog_index_html(posts):
    items = "".join(f'<li style="margin-bottom:0.75rem;"><a href="{p["url"]}">{p["title"]}</a> <small style="color:#64748b;">({p["date"]})</small></li>' for p in reversed(posts[-30:]))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Organic Aloe Vera Skincare Blog 2026 | AloeSkincareHub</title>
<meta name="description" content="Aloe vera skincare guides, eczema tips, anti-aging reviews, and organic skincare advice. Updated daily.">
<style>{CSS}
.hero{{background:linear-gradient(135deg,#059669,#1d4ed8);color:#fff;text-align:center;padding:3rem 1.5rem;}}
.hero h1{{font-size:2rem;font-weight:700;margin-bottom:0.5rem;}}
.hero p{{color:rgba(255,255,255,0.85);}}
</style>
</head>
<body>
{NAV}
<div class="hero"><h1>🌿 AloeSkincareHub Blog</h1><p>Organic aloe vera skincare guides, eczema tips, and anti-aging reviews. Updated daily.</p></div>
<div class="container">
  <h2 style="color:#047857;margin-bottom:1.5rem;">Latest Posts</h2>
  <ul style="list-style:none;padding:0;">{items}</ul>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Disclosure</a> | lc=014538155218007855</p></footer>
{STICKY}
</body>
</html>"""

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%B %d, %Y")
    day_num = now.timetuple().tm_yday % len(POSTS)
    post = POSTS[day_num]
    slug_base = post["title"].lower()
    for ch in " :,&'\"?!.—":
        slug_base = slug_base.replace(ch, "-")
    while "--" in slug_base:
        slug_base = slug_base.replace("--", "-")
    slug = slug_base[:60].strip("-") + f"-{now.strftime('%Y-%m-%d')}.html"
    gh_put(f"blog/{slug}", build_post_html(post, slug, date_str), f"Blog: {post['title']}")
    index = load_blog_index()
    index.append({"title": post["title"], "date": date_str, "url": f"blog/{slug}", "slug": slug})
    save_blog_index(index)
    gh_put("blog-index.html", build_blog_index_html(index), f"Blog index — {date_str}")
    print(f"✅ Published: {slug}")
