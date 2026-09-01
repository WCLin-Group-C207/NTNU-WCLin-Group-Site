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
├── honors.html                 # Honors, conferences, and academic mobility
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
      <li><a href="honors.html">Honors</a></li>
      <li><a href="gallery.html">Gallery</a></li>
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

## 12. Honors page — `honors.html`

Page title: "Honors, Conferences, and Academic Mobility". Two tab panels, each a year-by-year timeline of `.tl-item` entries:

- **Honors & Awards** — scholarships, fellowships, and competition awards
- **Conferences & Mobility** — conference attendance, formal exchange programs, and short-term research visits/experiments abroad

Both tabs share the same base item markup:

```html
<div class="tl-item" data-category="...">
  <span class="tl-tag phd">Ph.D.</span>
  <p class="tl-text"><strong>Name</strong> · Content · Location</p>
</div>
```

Degree/position tag classes (shared by both tabs):

```html
<span class="tl-tag phd">Ph.D.</span>
<span class="tl-tag msc">M.S.</span>
<span class="tl-tag bsc">B.S.</span>
<span class="tl-tag postdoc">Postdoc</span>
```

### 12.1 Honors & Awards tab

Each `.tl-item` carries a `data-category` used by the filter bar above the timeline. A value can hold more than one category separated by a space (e.g. `data-category="national conference"`) if a single award genuinely belongs to two — the filter matches on "any selected category present."

| Category value | Filter label | Meaning |
|---|---|---|
| `internal` | Internal | Scholarships issued by the department or college (merit-based, alumni-association, thesis awards, etc.) |
| `national` | External Funding | Government (NSTC/MOST) or foundation (e.g. CTCI) grants and fellowships |
| `exchange` | Int'l Exchange | Alumni-association scholarships specifically funding international exchange |
| `conference` | Conference | Awards won through a conference/competition presentation |

The filter bar is **multi-select**: clicking a category toggles it independently; clicking "All" clears the others; deselecting every category falls back to "All" automatically.

**Routine "Internal" merit scholarships collapse.** A handful of `internal` awards repeat almost every year with no real distinguishing detail (e.g. plain "Alumni Scholarship, NTNU Physics"). To keep the timeline from being dominated by these, each year merges **all** of that year's routine entries into a single collapsible summary, always placed **last** within that year:

```html
<details class="tl-collapse" data-category="internal">
  <summary class="tl-collapse-summary">Alumni Scholarship (2)</summary>
  <div class="tl-items tl-items-collapsed">
    <div class="tl-item" data-category="internal">...</div>
    <div class="tl-item" data-category="internal">...</div>
  </div>
</details>
```

`(N)` is the count of merged entries for that year. The `.tl-collapse` element itself needs the same `data-category` as its contents so the filter can hide the whole block (not just the items inside it) when it doesn't match the active filter.

**Known Chinese award name.** When an award's official Chinese name is known, append it in a muted, non-italic span so it doesn't compete visually with the English name:

```html
<p class="tl-text"><strong>Name</strong> · Alumni Scholarship, NTNU Physics <span class="tl-zh">「獎學金中文全名」</span></p>
```

Apply the same Chinese subtitle to **every** occurrence of that exact award name across years — don't leave some instances without it.

### 12.2 Conferences & Mobility tab

Each `.tl-item` carries:

- `data-month=""` — used by the year/month sort script (see below); leave empty when the month is unknown, never guess a number.
- `data-type="conf" | "prog" | "mob"` — drives the Conference/Program/Mobility filter bar (also multi-select, same mechanics as 12.1).

```html
<div class="tl-item" data-month="" data-type="conf">
  <div class="tl-tags">
    <span class="tl-tag2 conf">Conference</span>
    <span class="tl-tag phd">Ph.D.</span>
  </div>
  <p class="tl-text"><strong>Name</strong> · <span class="tl-hl">Content</span> · <span class="tl-loc">Location</span></p>
</div>
```

The attribute (Conference/Program/Mobility) tag always comes **before** the degree tag inside `.tl-tags`.

**Classifying an entry:**

- **Conference** — attending/presenting at a named conference or symposium.
- **Program** — a formally named exchange program (e.g. "Overseas Dream-Build Program", "Japan-Taiwan Sakura Science Program").
- **Mobility** — everything else: short-term lab visits, beamtime/experiments abroad, research collaboration exchanges, or an international-exchange trip that happened to include a presentation.

If one trip covers **two separate named conferences**, split it into two `.tl-item` entries (same person/year/location) rather than joining the names with "&".

**Conference/program naming:**

- Recurring numbered conferences: `<Series Name> <Edition>th` (e.g. `ISSS 8th`, `ACSIN 14th`) — name first, then the ordinal edition number. Don't prepend the ordinal (not `8th ISSS`) and don't use a dash-number form (not `ISSS-8`).
- Don't repeat the year in the name when the entry is already grouped under that year in the timeline (`Intermag 2015` → `Intermag`, `MML-2013` → `MML`).
- A conference's own well-known short name doesn't need a generic suffix (`MMM Conference` → `MMM`).

**Content field — what goes in the middle segment:**

- **Conference**: `<Report Type> Presentation – <Conference Name>` if a report was given (e.g. `Oral Presentation – MMM`), otherwise just `<Conference Name>`. Highlight (`.tl-hl`) the conference name always; additionally highlight the report-type word (not the word "Presentation") only when the report is **oral or higher** (Oral, Subplenary, Invited, Keynote, Plenary — not Poster).
- **Program**: just the program's proper name, highlighted.
- **Mobility**: `<Report Type> Presentation – Short-term Visit` if a report was given, otherwise a duration-based label (highlight nothing in the content field for Mobility — see below):
  - days to about a month → `Short-term Research Visit`
  - about a month to about six months → `Research Visit`
  - six months or longer → `Long-term Research Visit`
  - a beamtime/instrument run at a facility (not a general lab visit) → `Short-term Research Visit` is still fine, but keep it distinct in your own notes if the visit and the experiment are genuinely different trips.

**Location field:** `<Institution(s)> · <Country>` — use `<span class="tl-loc">`. Keep commas only between an institution's own internal tiers (e.g. `Institute for Solid State Physics (ISSP), University of Tokyo`); always separate the trailing country with `" · "`, and always include the country even when the institution name seems to imply it.

**Highlighting (`.tl-hl`) — what's the "headline" of this entry:**

| Category | What gets `.tl-hl` |
|---|---|
| Program | The program name |
| Mobility | The institution name only (wrap it as `<span class="tl-loc tl-hl">`) — the trailing `, Country` stays a plain `<span class="tl-loc">` |
| Conference | The conference name, plus the report-type word if oral-or-higher (see above) |

**Year/month sort script.** The tab rebuilds its own timeline on load from each item's `data-month`: newest year first, and within a year, items with a known month sort newest-month-first, with unmonthed items always last for that year. Year headers render as "YYYY年M月" when a month is known, otherwise "YYYY年" — never invent a month to make sorting cleaner.

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

### Gallery photo naming convention

Photos under `assets/images/gallery/{year}/...` must follow this filename format:

```text
AAAABBB_CCCC_DDD_EE.jpg
```

The underscore `_` is the **primary field separator** (4 fields total); the hyphen `-` is only for separating multiple English words **inside a single field** — it must never be used as a field separator.

| Field | Meaning | Example |
|---|---|---|
| `AAAA` | 4-digit year | `2022` |
| `BBB`  | 3-letter month abbreviation (Jan/Feb/Mar/…/Dec) | `Jul` |
| `CCCC` | Conference / program / event name — prefer a known abbreviation, otherwise the full name; hyphenate multiple words | `TPS`, `TAMT`, `MMM`, `Lab-dinner` |
| `DDD`  | Country abbreviation | `TW`, `JP`, `KR`, `US` |
| `EE`   | 2-digit sequence number, increments for multiple photos from the same event | `01`, `02` |

Example: `2022Jul_TAMT_TW_01.jpg`, `2026Dec_Lab-dinner_TW_01.jpg`

**Use `XXX` for any unknown field** — never leave it blank, use a question mark, or guess a value. Example with unknown month:

```text
2016XXX_MMM_US_01.jpg
```

### Three category definitions (conference / program / event)

Photos in each year folder are split into three categories by activity type:

- **conference**: domestic and international academic conferences. Known abbreviations so far:
  - `MMM`
  - `ICMFs`
  - `TAMT` (usually July, Taiwan)
  - `TPS` (usually January, Taiwan)
- **program**: overseas programs, research visits, and off-site experiments — including short exchange visits tied to coursework, and domestic off-site experiments. Known programs so far:
  - 學海築夢 (Overseas Dream Build)
  - 千里馬 (Chien-Li-Ma Program)
- **event**: anything else — lab dinners, outings, and similar gatherings.

### Page layout: year-based "album" view

The Gallery page lists years in descending order (newest first). Each year is one block: the left side is a fixed-size frame showing a random photo from that year, rotating on a timer (the frame size never changes as the photo changes); the right side is a 2×2 grid of "album" tiles, always ordered **conference > program > event**. Clicking an album cover expands it into a viewer (one large photo plus a thumbnail strip below it — clicking a thumbnail swaps the large photo).

#### Album count allocation

First count how many albums exist for that year (each activity subfolder — e.g. `conference/tamt/` — counts as one album):

- **Total < 4**: show as many real albums as exist, in conference > program > event order; fill the rest with "coming soon" placeholders.
- **Total = 4**: use the priority table below to decide how many of the first 3 slots go to conference/program/event; the one album left over (not picked for the first 3) is shown normally in the 4th slot.
- **Total > 4**: use the same priority table for the first 3 slots; the 4th slot always becomes a "+N More albums" tile (N = total − albums shown in the first 3 slots). Clicking it lists every album for that year as thumbnails; clicking one of those opens the full album viewer.

Priority table (walk top to bottom, use the first combination where all three counts are ≤ what that year actually has):

```text
conference + program + event =
1+1+1 > 2+1+0 > 2+0+1 > 1+2+0 > 1+0+2 > 0+2+1 > 0+1+2 > 3+0+0 > 0+3+0 > 0+0+3
```

A category allocated 0 is skipped entirely — no placeholder tile is shown for it (placeholders are only used in the "total < 4" case).

#### Picking which subfolder represents a category

When a category has more subfolders than the slots it was allocated, pick in this order:

1. **Foreign (non-Taiwan) events first** — based on the conference/program's host country
2. For conference's domestic options, **TPS before TAMT**
3. Otherwise, pick at random

Example: 2022 has 4 conference subfolders (icmfs / tamt / tps / XXX). The priority table selects `2+0+1` (conference×2 + event×1), so only 2 conference albums can be shown — icmfs (Japan, foreign) is picked first, then TPS beats TAMT for the domestic slot, giving icmfs + tps. TAMT and XXX get no dedicated album that year (they still appear in the "+N" list and the left-side rotation).

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
<a href="gallery.html">Gallery</a>
```

requires:

```text
gallery.html
```

not:

```text
photots.html
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
honors.html
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
