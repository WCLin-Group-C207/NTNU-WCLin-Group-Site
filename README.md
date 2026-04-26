# NTNU WCLin Group Site — Editing README

This repository contains the static website for the **NanoMaterials & Spintronics Laboratory / WCLin Group** at NTNU.

Live site:

```text
https://wclin-group-c207.github.io/NTNU-WCLin-Group-Site/
```

The website is built with plain **HTML + CSS + small JavaScript snippets**. There is no external build system, no React/Vue framework, and no server-side backend. Each page is an independent HTML file that can be edited directly.

---

## 1. Website structure

Current intended site structure:

```text
NTNU-WCLin-Group-Site/
├── index.html                 # Home page
├── group-leader.html          # Principal Investigator / group leader page
├── members.html               # Current members + alumni
├── research.html              # Research directions
├── publications.html          # Searchable publication list
├── facilities.html            # Instruments / facilities
├── exchange-awards.html       # Awards, exchange, scholarships, visits
├── gallery.html                # Gallery page; see filename note below
├── assets/
│   └── images/
│       ├── skyrmion-hero.png  # Home hero background
│       ├── Prof-Lin-photo.jpg
│       ├── Po-Wei.jpg
│       ├── Ko-Fan.jpeg
│       ├── AFM.jpg
│       ├── VSM.jpg
│       └── ...
└── README.md

---

## 2. Basic editing workflow on GitHub

### Option A — Edit directly on GitHub

1. Open the repository on GitHub.
2. Click the file you want to edit, for example `members.html`.
3. Click the pencil icon.
4. Modify the code.
5. Scroll down to **Commit changes**.
6. Add a short commit message, for example:

```text
Update member profile
```

7. Click **Commit changes**.
8. Wait 1–5 minutes.
9. Refresh the website.

If the page does not update immediately, try:

```text
Ctrl + F5
```

or open the site in a private/incognito browser window.

### Option B — Upload a replaced file

1. Edit the HTML file locally.
2. On GitHub, open the repository.
3. Click **Add file → Upload files**.
4. Upload the edited file.
5. Make sure the uploaded filename is exactly the same as the file being replaced.
6. Commit changes.

---

## 3. Design system

Each HTML file contains its own `<style>` block. The website does **not** currently use a shared external CSS file.

Most pages begin with the same CSS variables:

```css
:root {
  --color-ink:       #1a2238;
  --color-accent:    #a82740;
  --color-cream:     #faf7f0;
  --color-paper:     #ffffff;
  --color-rule:      #e4dfd0;
  --color-muted:     #6b7280;
  --color-soft:      #f0ebdc;

  --font-display: 'Fraunces', 'Noto Serif TC', Georgia, serif;
  --font-body:    Arial, 'Noto Sans TC', -apple-system, BlinkMacSystemFont, sans-serif;

  --max-width: 1240px;
  --gutter: clamp(20px, 4vw, 48px);
}
```

### Main visual identity

| Item | Current choice |
|---|---|
| Main ink color | `#1a2238` |
| Accent color | `#a82740` |
| Background | `#faf7f0` |
| Display font | Fraunces |
| Body font | Arial + Noto Sans TC |
| Style direction | editorial academic / journal-like |

### What to avoid

Avoid adding:

- bright purple AI-style gradients
- emoji icons in formal sections
- large rounded SaaS-style cards
- heavy drop shadows
- too many different colors
- inconsistent fonts

The design goal is closer to a **Nature / MIT / academic editorial** style, not a startup landing page.

---

## 4. Shared navigation bar

Each page has a navigation block similar to:

```html
<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand">WCLin Group</a>
    <button class="nav-toggle" aria-label="Menu" onclick="document.getElementById('navLinks').classList.toggle('open')">☰</button>
    <ul class="nav-links" id="navLinks">
      <li><a href="index.html">Home</a></li>
      <li><a href="group-leader.html">Group Leader</a></li>
      <li><a href="members.html">Members</a></li>
      <li><a href="research.html">Research</a></li>
      <li><a href="publications.html">Publications</a></li>
      <li><a href="facilities.html">Facilities</a></li>
      <li><a href="exchange-awards.html">Awards</a></li>
      <li><a href="photos.html">Gallery</a></li>
    </ul>
  </div>
</nav>
```

### When editing navigation

If you add, remove, rename, or reorder navigation items, update the navigation block in **all HTML files**.

Also make sure the active page has:

```html
class="active"
```

Example for the Publications page:

```html
<a href="publications.html" class="active">Publications</a>
```

Only one navigation item should be active per page.

---

## 5. Shared footer

Most pages use a common footer block:

```html
<footer class="footer">
  ...
</footer>
```

If you update:

- lab address
- phone number
- Prof. Lin email
- copyright year
- designer credit
- external links

then update the footer in all HTML files.

Current designer credit format:

```html
Designed by Ko-Fan Chen &amp; Po-Wei Chen · Rebuilt 2026
```

---

## 6. Home page editing guide — `index.html`

The home page contains:

1. navigation bar
2. hero section
3. research focus cards
4. lab news
5. join-us CTA
6. footer

---

### 6.1 Hero background image

The hero background uses:

```text
assets/images/skyrmion-hero.png
```

Typical CSS location:

```css
.hero {
  background-image:
    linear-gradient(...),
    radial-gradient(...),
    radial-gradient(...),
    linear-gradient(...),
    url("assets/images/skyrmion-hero.png");
}
```

#### What the background layers mean

The hero background is built from several layers:

1. horizontal mist gradient
2. right-top radial mist
3. left-bottom radial mist
4. vertical top/bottom mist
5. actual background image

The order matters. In CSS, the first background layer is displayed on top.

#### Adding another mist layer

Add another `radial-gradient(...)` as a separate background layer:

```css
background-image:
  linear-gradient(...),
  radial-gradient(circle at 88% 12%, ...),
  radial-gradient(circle at 12% 88%, ...),
  radial-gradient(circle at 50% 50%, ...), /* new layer */
  linear-gradient(...),
  url("assets/images/skyrmion-hero.png");
```

If you add one more background layer, also add one more value in:

```css
background-size
background-position
background-repeat
```

Example with six layers:

```css
background-size:
  100% 100%,
  100% 100%,
  100% 100%,
  100% 100%,
  100% 100%,
  cover;

background-position:
  center center,
  center center,
  center center,
  center center,
  center center,
  center center;

background-repeat:
  no-repeat,
  no-repeat,
  no-repeat,
  no-repeat,
  no-repeat,
  no-repeat;
```

### 6.2 Hero title and text

Edit this HTML block:

```html
<header class="hero">
  <div class="hero-mark">
    <strong>EST. 2007</strong><br>
    Department of Physics<br>
    National Taiwan Normal University<br>
    Taipei · Taiwan
  </div>

  <div class="hero-label"> Magnetic thin films, 2D materials, and spin transport</div>

  <h1 class="hero-title">
    NanoMaterials &amp;<br>
    <em>Spintronics Laboratory</em>
  </h1>

  <p class="hero-lead">
    ...
  </p>

  <a class="hero-cta" href="research.html">Explore our research <span aria-hidden="true">→</span></a>
</header>
```

### 6.3 Hero font weights

To adjust hero text thickness:

```css
.hero-label {
  font-weight: 600;
}
```

```css
.hero-title {
  font-weight: 400;
}
```

```css
.hero-title em {
  font-weight: 300;
}
```

```css
.hero-lead {
  font-weight: 500;
}
```

Recommended values:

| Section | Suggested range |
|---|---|
| `.hero-label` | `600–700` |
| `.hero-title` | `400–500` |
| `.hero-title em` | `300–400` |
| `.hero-lead` | `400–500` |

Avoid making the title too heavy; Fraunces can become visually bulky.

---

### 6.4 Mobile hero

The mobile version is controlled inside:

```css
@media (max-width: 720px) {
  ...
}
```

If the mobile background looks too busy, do not keep increasing `.hero::after` indefinitely. Instead, redefine the mobile `.hero` background directly:

```css
@media (max-width: 720px) {
  .hero {
    background-image:
      linear-gradient(...),
      linear-gradient(...),
      url("assets/images/skyrmion-hero.png");
  }

  .hero::after {
    display: none;
  }
}
```

This prevents mobile from inheriting the desktop multi-layer hero background.

---

### 6.5 Research focus cards on home page

Edit this block:

```html
<div class="research-grid">

  <article class="research-card">
    <div class="research-num">01</div>
    <h3>Hydrogen-Tunable Magnetism</h3>
    <p>...</p>
  </article>

  ...
</div>
```

To add a new card:

1. Copy one full `<article class="research-card">...</article>`.
2. Change the number.
3. Change the title.
4. Change the description.
5. Check mobile layout.

---

### 6.6 Lab News on home page

The news block is grouped by year:

```html
<div class="news-year">
  <div class="news-year-label">2026</div>
  <div class="news-items">

    <div class="news-item">
      <span class="news-tag admission">ADMISSION</span>
      <p class="news-text">...</p>
    </div>

  </div>
</div>
```

To add a news item:

1. Find the correct year.
2. Copy one `.news-item`.
3. Change the tag and text.

Available tag styles include:

```html
<span class="news-tag admission">ADMISSION</span>
<span class="news-tag intl">EXCHANGE</span>
<span class="news-tag award">AWARD</span>
<span class="news-tag paper">PAPER</span>
```

If adding a new tag category, also add a matching CSS rule:

```css
.news-tag.newtype { color: #xxxxxx; }
```

---

## 7. Group leader page — `group-leader.html`

The group leader page contains:

- page header
- profile photo
- profile information
- education / experience / research interests
- footer

Typical editable sections include:

```html
<header class="page-header">
  ...
</header>
```

and:

```html
<section class="profile">
  ...
</section>
```

### Updating the group leader photo

Use:

```html
<img src="assets/images/Prof-Lin-photo.jpg" alt="Prof. Wen-Chin Lin">
```

To replace the photo:

1. Upload a new image to `assets/images/`.
2. Use a simple filename, for example:

```text
Prof-Lin-photo.jpg
```

3. Update the `src` path if needed.

Avoid spaces and special symbols in filenames.

---

## 8. Members page — `members.html`

The members page uses repeating member cards.

Typical structure:

```html
<article class="member">
  <div class="member-photo">
    <img src="assets/images/Po-Wei.jpg" alt="Po-Wei Chen">
    <span class="member-badge">D3</span>
  </div>

  <div>
    <h3 class="member-name">
      陳柏維<span class="member-name-en">Po-Wei Chen</span>
    </h3>

    <ul class="member-edu">
      <li>B.S. Physics, NTNU (2023)</li>
      <li>Ph.D. Physics (Dual-Degree), UOsaka &amp; NTNU (2024 – Present)</li>
    </ul>

    <p class="member-contact">
      <span class="contact-label">Contact</span><br>
      <a href="mailto:example@email.edu">example@email.edu</a>
    </p>
  </div>
</article>
```

### Adding a new member

1. Copy an entire `<article class="member">...</article>`.
2. Update:
   - image file
   - alt text
   - badge
   - Chinese name
   - English name
   - education list
   - contact email, if needed
3. Upload the photo into:

```text
assets/images/
```

### Member photo requirements

Recommended:

```text
Portrait ratio: 4:5
Width: 800–1200 px
Format: jpg, jpeg, or png
Filename: English letters, numbers, hyphens only
```

Good examples:

```text
Po-Wei.jpg
Ko-Fan.jpeg
Ming-Hsien.png
```

Avoid:

```text
Po Wei photo final copy.png
陳柏維照片.jpg
IMG_1234 (1).jpeg
```

### Contact label

If you want:

```text
Contact
email@example.edu
```

use:

```html
<p class="member-contact">
  <span class="contact-label">Contact</span><br>
  <a href="mailto:email@example.edu">email@example.edu</a>
</p>
```

Corresponding CSS:

```css
.contact-label {
  color: var(--color-ink);
  font-weight: 600;
}

.member-contact a {
  color: var(--color-accent);
  font-weight: 400;
}
```

### Common members page spacing controls

Member English-name spacing:

```css
.member-name-en {
  margin-bottom: 6px;
}
```

Education/contact spacing:

```css
.member-edu {
  min-height: 0;
}
```

Contact spacing:

```css
.member-contact {
  margin-top: 0;
}
```

If contact is too far from education, check whether `.member-edu` has an unwanted `min-height`.

---

## 9. Research page — `research.html`

The research page contains:

- page header
- table of contents / anchor buttons
- research topic blocks

Typical topic block:

```html
<section class="topic" id="hydrogen">
  <div class="topic-head">
    <div class="topic-num">01</div>
    <div>
      <div class="topic-kicker">Hydrogen-Tunable Magnetism</div>
      <h2 class="topic-title">...</h2>
    </div>
  </div>

  <div class="topic-body">
    ...
  </div>
</section>
```

### Adding a new research topic

1. Copy one full `<section class="topic">...</section>`.
2. Give it a new `id`.
3. Add a link to the `.toc` section.
4. Update topic number, title, summary, keywords, and details.

Example TOC link:

```html
<a href="#new-topic">New Topic</a>
```

Example section ID:

```html
<section class="topic" id="new-topic">
```

The `href` and `id` must match.

---

## 10. Publications page — `publications.html`

The Publications page is the most data-heavy page. It includes:

- statistics cards
- search box
- year filter
- sort filter
- publication list generated from JavaScript data

### Key sections

Stats:

```html
<div class="stats">
  ...
</div>
```

Controls:

```html
<div class="controls">
  ...
</div>
```

Publication list container:

```html
<ul class="pub-list" id="pubList"></ul>
```

Publication data is typically stored in a JavaScript array such as:

```js
const publications = [
  {
    year: 2026,
    title: "...",
    authors: "...",
    journal: "...",
    volume: "...",
    url: "...",
    thumbnail: "",
    roles: ["CORRESP."]
  },
  ...
];
```

### Adding a publication

Add one object to the publication array:

```js
{
  year: 2026,
  title: "Full paper title here",
  authors: "Author A, Author B, Author C, W. C. Lin",
  journal: "Journal Name",
  volume: "12, 123–130",
  url: "https://doi.org/...",
  thumbnail: "",
  roles: ["CORRESP."]
}
```

### Nature-like citation style

Recommended display style:

```text
Author A, Author B & Author C. Paper title. Journal Name volume, pages (year).
```

For this site, the publication object separates fields. Keep author names complete and consistent.

### Thumbnail behavior

If:

```js
thumbnail: ""
```

the page can display a year-based thumbnail.

If:

```js
thumbnail: "assets/images/p001.jpg"
```

the page displays that image.

### Updating publication statistics

The statistics area may include manually written numbers such as total publication count or year range. If the page does not automatically calculate a number, update the stat manually when publications change.

---

## 11. Facilities page — `facilities.html`

Facilities are displayed as repeated cards.

Typical structure:

```html
<article class="facility">
  <div class="facility-photo">
    <img src="assets/images/AFM.jpg" alt="AFM">
  </div>
  <div class="facility-body">
    <div class="facility-num">01</div>
    <h3>Atomic Force Microscope</h3>
    <p>...</p>
  </div>
</article>
```

### Adding a facility

1. Upload equipment photo to `assets/images/`.
2. Copy an existing `.facility` block.
3. Update:
   - image path
   - alt text
   - number
   - equipment name
   - description

Recommended image aspect ratio:

```text
4:3
```

---

## 12. Awards & Exchange page — `exchange-awards.html`

This page uses tab panels and timeline entries.

Typical timeline item:

```html
<div class="tl-item">
  <span class="tl-tag phd">PHD</span>
  <p class="tl-text">...</p>
</div>
```

### Adding an award or exchange record

1. Find the correct tab panel.
2. Find the correct year.
3. Copy one `.tl-item`.
4. Update the tag and text.

Common tag classes:

```html
<span class="tl-tag phd">PHD</span>
<span class="tl-tag msc">MSC</span>
<span class="tl-tag bsc">BSC</span>
<span class="tl-tag postdoc">POSTDOC</span>
```

If you create a new tag class, add CSS:

```css
.tl-tag.newtag { color: #xxxxxx; }
```

---

## 13. Gallery page — `gallery.html`

The Gallery page uses photo sections and photo grids.

Typical structure:

```html
<section class="gallery-section" id="2026">
  <div class="section-head">
    <span class="section-num">01</span>
    <h2 class="section-title">2026</h2>
    <span class="section-meta">...</span>
  </div>

  <div class="photo-grid">
    <article class="photo-card">
      <img src="assets/images/photo-name.jpg" alt="Description">
    </article>
  </div>
</section>
```

### Adding photos

1. Upload images to `assets/images/`.
2. Add a new `.photo-card`.
3. Use descriptive `alt` text.
4. Keep filenames simple and case-consistent.

Recommended filenames:

```text
lab-meeting-2026-01.jpg
conference-osaka-2026.jpg
```

---

## 14. Image path and filename rules

Use relative paths:

```html
<img src="assets/images/Po-Wei.jpg" alt="Po-Wei Chen">
```

or in CSS:

```css
background-image: url("assets/images/skyrmion-hero.png");
```

### GitHub Pages filename rules

GitHub Pages is case-sensitive:

```text
Po-Wei.jpg
po-wei.jpg
Po-Wei.JPG
```

These are all different filenames.

If an image does not display:

1. Check the exact filename in GitHub.
2. Check uppercase/lowercase letters.
3. Check file extension: `.jpg`, `.jpeg`, `.png`.
4. Check that the image is committed.
5. Open the image directly in browser:

```text
https://wclin-group-c207.github.io/NTNU-WCLin-Group-Site/assets/images/IMAGE_NAME
```

If the direct image URL opens but the page does not show it, the HTML/CSS path is wrong.

---

## 15. Mobile editing rules

The website uses media queries such as:

```css
@media (max-width: 960px) {
  ...
}
```

and:

```css
@media (max-width: 720px) {
  ...
}
```

### Common breakpoints

| Breakpoint | Purpose |
|---|---|
| `960px` | Navigation switches to hamburger menu |
| `720px` | Main mobile layout |
| `600px` | Smaller content grids |
| `420px` | Very narrow phone layout |

### Before committing, test these widths

Use browser developer tools and test:

```text
390px
430px
768px
1024px
1440px
```

---

## 16. Common problems and fixes

### Problem: image does not display

Check:

```text
filename
file extension
uppercase/lowercase
folder path
commit status
browser cache
```

### Problem: navigation link gives 404

Check whether the filename matches the link exactly.

Example:

```html
<a href="photos.html">Gallery</a>
```

requires:

```text
photos.html
```

not:

```text
gallery.html
```

### Problem: mobile menu does not open

Check the button:

```html
<button class="nav-toggle" onclick="document.getElementById('navLinks').classList.toggle('open')">☰</button>
```

and the menu ID:

```html
<ul class="nav-links" id="navLinks">
```

The ID must be exactly:

```text
navLinks
```

### Problem: CSS changes do nothing

Possible causes:

1. Browser cache.
2. The same CSS selector appears later and overrides the earlier one.
3. The rule is inside a media query and only applies on certain screen widths.
4. Missing or extra braces `{ }`.

### Problem: layout suddenly breaks

Check for:

```css
missing }
extra }
unclosed comment /* ... 
missing comma in background-image
wrong number of background-size layers
wrong number of background-position layers
```

For multi-layer backgrounds, the number of layers should match:

```css
background-image:
  layer1,
  layer2,
  layer3,
  url(...);

background-size:
  size1,
  size2,
  size3,
  size4;

background-position:
  position1,
  position2,
  position3,
  position4;
```

---

## 17. Recommended editing principles

### Do

- Edit one section at a time.
- Save and test after each change.
- Keep filenames simple.
- Keep colors within the design system.
- Keep nav and footer consistent across all pages.
- Use comments to mark editable blocks.

### Do not

- Rename files without updating all links.
- Add spaces or Chinese characters to image filenames.
- Mix many unrelated font styles.
- Add large shadows or saturated gradients.
- Edit both desktop and mobile CSS at the same time unless necessary.
- Leave invalid CSS fragments after deleting a block.

---

## 18. Pre-publish checklist

Before pushing changes:

```text
[ ] Open index.html locally or on GitHub Pages
[ ] Check Home page desktop
[ ] Check Home page mobile
[ ] Check navigation links
[ ] Check hamburger menu
[ ] Check all images
[ ] Check Members page
[ ] Check Publications search/filter
[ ] Check Gallery filename/link consistency
[ ] Check footer information
[ ] Commit changes with clear message
```

Recommended commit messages:

```text
Update member profiles
Add 2026 publications
Fix mobile hero layout
Update facilities photos
Revise gallery page
```

---

## 19. Maintenance recommendation

The current site keeps CSS inside each HTML file. This is easy for direct editing, but repeated CSS means global style updates must be copied across files.

For future maintenance, consider moving shared CSS into:

```text
assets/css/style.css
```

Then each HTML file can use:

```html
<link rel="stylesheet" href="assets/css/style.css">
```

This would make global design updates easier, but it requires one larger cleanup. Until then, remember:

```text
Navbar changes → update every page
Footer changes → update every page
Global color/font changes → update every page
```

---

## 20. Quick reference

### Main files

```text
index.html
group-leader.html
members.html
research.html
publications.html
facilities.html
exchange-awards.html
gallery.html
```

### Main image folder

```text
assets/images/
```

### Main colors

```css
--color-ink:    #1a2238;
--color-accent: #a82740;
--color-cream:  #faf7f0;
```

### Main fonts

```css
--font-display: Fraunces;
--font-body: Arial, Noto Sans TC;
```

### Live website

```text
https://wclin-group-c207.github.io/NTNU-WCLin-Group-Site/
```
