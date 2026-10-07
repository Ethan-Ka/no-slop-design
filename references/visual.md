# Visual: color, type, layout, imagery

The banned list, with the reason for each. Nothing here is a claim that the
banned thing is ugly. Each one is banned because it is what you get when
nobody decides.

---

## Color

### Never ship

- **Indigo or violet as the primary accent**, especially the Tailwind defaults
  (`indigo-500`, `violet-500`, roughly #615FFF through #8E51FF). This is the
  single most recognized tell. It is everywhere because it was Tailwind's
  default five years ago and then saturated every tutorial in the training data.
- **Purple-to-blue or purple-to-cyan gradients**, in hero backgrounds, button
  fills, headline text, or card borders.
- **Glassmorphism**, particularly a frosted panel with a colored neon glow
  behind it.
- **Large colored glows or drop shadows** behind hero cards, buttons, or
  floating UI mockups.
- **Amber-and-cream** as the tasteful escape hatch. It is the second-order
  default and just as recognizable now.
- **Emerald green** as the escape hatch from the escape hatch.
- **Dark mode chosen by default** rather than by decision, especially paired
  with mid-grey body text on near-black.
- **The framework's stock semantic set.** Info in blue, tip in amber, success
  in green, error in red, always at the `-50` background with `-600` text. Four
  unrelated candy colors that match neither the brand nor each other. Grow the
  semantic colors out of the one palette instead: tints of a single hue plus
  neutrals, and color only the few states that genuinely differ. Most notes
  need no color at all.
- **The one-hue status box.** Border, text, and background all the same hue at
  three opacities: `border-red-500`, `text-red-500`, `bg-red-500/10`. Red on
  red, amber on amber, green on green, every time. Red, amber, and green are a
  traffic light, not a palette. Carry the state in the word and the weight
  first, since a bold "Error" is read before any color is.
- **Gradient used as atmosphere.** A near-black navy page with a soft spotlight
  glow at the top, card surfaces that are themselves gradients (lighter above,
  darker below), each card washed in a tint of its own accent so the green card
  gets a green gradient and the blue card a blue one, or repeating-linear
  stripes laid on as texture. None of it answers a design question. Pick one
  flat background and hold it, and build depth with a hairline and a restrained
  shadow.

### Instead

Source the palette from something real: a brand asset, a physical material, a
photograph, a printed reference. Build a neutral ramp with enough steps that
you never need to invent a value mid-build (ten or twelve is right), and give
it a temperature, warm or cool, on purpose. Pick one accent that carries
action. If you need a second, it is for emphasis and data, not for buttons.

Then verify. Every text and background pair needs a measured contrast ratio:
4.5:1 for body, 3:1 for large text (18.66px bold or 24px regular and up) and
for non-text UI like input borders, meaningful icons, and focus rings. State
the numbers. A pair you did not measure has not been checked.

Color is never the only signal for a state. Pair it with an icon, a label, or
a shape change. Shadows stay neutral; a shadow on a near-black surface reads as
dirt, so on dark surfaces use borders for separation instead.

---

## Typography

Six faces are out: **Inter, Space Grotesk, Roboto, Geist, Manrope, and Plus
Jakarta Sans.** Not because they are bad (Inter in particular is excellent) but
because they have become the signature of a choice that was not made. Nearly
every generated page draws from those six, usually as Space Grotesk for display
over Inter for body. Everything else is open.

### Never ship

- **Inter, Space Grotesk, Roboto, Geist, Manrope, or Plus Jakarta Sans.** Inter
  as the default for everything, chosen because it was not chosen, is the most
  common version of this. A system stack picked for a reason is a choice; the
  `next/font/google` Inter boilerplate is not.
- **A typeface you did not choose.** If you cannot say in one sentence what the
  face is doing for this design, it was inherited from a starter template or
  from habit, and that is what readers pick up on.
- **A single italic serif word dropped into a sans headline.** "Build *better*
  software."
- **Eyebrow labels above section headings.** Banned by default; the full
  treatment is below.
- **Monospace body copy** on a page that is not about code.
- **Type hierarchy that is only size.** If the only difference between a
  heading and body text is that one is bigger, there is no hierarchy.
- **A whole sentence set at display size.** Fourteen words at 72px in
  extrabold with the tracking crushed, wrapping to three or four lines and
  eating the first screen. Display sizes are for the two or three words that
  can carry them. Setting the entire pitch huge is the size standing in for the
  decision about what matters, and it reads as less sure, not more. Tighten
  tracking only as far as the face was drawn to go, never past about -0.03em.
- **The flat scale.** Every size on the page crammed between 14 and 18px, steps
  under 1.25x apart, hierarchy left entirely to shades of grey. The opposite
  failure from the display sentence and the same absence behind it. If two
  sizes are within a pixel or two of each other, merge them.
- **Drawing on the words.** Strikethrough on a word that is not being deleted,
  an underline that is not a link, a highlighter swipe, a colored or bolded
  word every other line in a paragraph. When every word is emphasised, none is.
  Keep strikethrough for real edits, underline for links, and `mark` for real
  annotation. At most one accent per paragraph, and usually none. Emphasis is
  the job of sentence structure, weight, and the line break.

### Instead

Two families maximum, each with a stated reason. Pick for the job: what the
face has to do at 13px in a table cell, at 48px in a headline, in the language
the content is actually in.

Open-licensed options worth knowing, if you want somewhere to start: IBM Plex
Sans, Public Sans, Source Sans 3, Libre Franklin, Atkinson Hyperlegible for
sans; Source Serif 4, Libre Baskerville, Newsreader, Literata for serif; IBM
Plex Mono, JetBrains Mono for mono.

Build hierarchy in this order of preference: position, weight, color, spacing,
then size. A heading that sits alone above whitespace in full ink while the
body sits a step down in grey is a clearer heading than one that is merely
larger.

Consider a base size other than 16px. 16px is a browser default, not a
decision. Cap body measure around 65 to 70 characters; longer lines lose the
reader on the return sweep.


### Eyebrows

The small label above a heading. Banned by default, and worth its own entry
because it is the most common piece of pure decoration in generated design.

The recipe, which is worth learning to spot: 11 or 12px, all caps, wide
letter-spacing, semibold, in the accent color, usually with a leading dot, a
trailing hairline rule, or a pill border. It sits above the heading of every
section, and it almost always says the thing the heading is about to say.

Banned outright:

- **A monospace, all-caps eyebrow.** `font-mono uppercase tracking-widest` over a
  heading is the single most recognizable form of the pattern, and it is wrong
  even when the page is about code. If an eyebrow earns its place, it is set in
  the body face, in sentence case.
- **An eyebrow that restates its heading.** "FEATURES" above "Everything you
  need".
- **An eyebrow naming the category the page is already about.** "PRICING" above
  "Simple, transparent pricing".
- **The pill badge above an H1.** The same pattern wearing a border.
- **Decorative chrome on an eyebrow:** leading dot, trailing rule, gradient
  text, sparkle icon, a border on three sides. The dot and the rule are the
  loudest of these; see the dots section under Decoration.
- **Section-number eyebrows.** `00 / INDEX`, `001 · Capabilities`,
  `06 · how it works`, and the oversized `01 / 02 / 03` ordinals set above
  features that are not a sequence. Numbering implies order. If the reader can
  read them in any order, do not number them.
- **The poetic label.** "Field notes", "From the field", "Loose plates",
  "Selected work" on three items. It is atmosphere standing where a category
  should be.
- **A second line under the eyebrow.** A micro-sentence between the eyebrow and
  the heading, or floated to the top right of the section, explaining what the
  heading is about to say. Two pieces of decoration stacked is not better than
  one.
- **An eyebrow on every section**, which is the giveaway that none of them was
  a decision.

An eyebrow is legitimate only when it carries information the heading does not
and the reader needs right then: a category in a list of genuinely mixed
categories, a date on an article, a step number in a sequence the reader is
actually moving through. When it is doing that job, it does not need to be
all-caps, letter-spaced, and accent-colored to do it.

The default is none. Write the page without eyebrows and add one only if you can
name what the reader would lose without it.

If you keep any at all, cap them: no more than one per three sections, and
never two in a row. That ceiling is a fallback, not a target. Count them before
you present. A page with an eyebrow on every section has, in effect, none.

If you want a heading to feel anchored, anchor it with position, spacing, or a
rule that belongs to the layout. Not with a word that repeats the heading.

---

## Layout

### Never ship

- **A centered hero with a small pill badge directly above the H1.** The most
  reproduced layout on the web.
- **Three or six feature cards in a row**, each icon on top, heading, two lines
  of text, all forced to the same height.
- **Colored left borders on cards.** Nearly as reliable a signal as the purple.
- **A numbered 1-2-3 step sequence** used as the explanation of how the product
  works.
- **A horizontal band of round-number statistics.** 10,000+ Users. 99.9%
  Uptime. 24/7 Support.
- **Emoji standing in for icons.** Rocket, lightbulb, sparkles, chart-increasing.
- **Perfect symmetry.** Identical text lengths, identical card heights, nothing
  breaking the grid.
- **Whitespace so uniform and so generous** that the page reads as unfinished
  rather than composed.
- **Text used to fill space that composition should fill.** A paragraph added
  under a heading because the area looked empty, a description under every card
  because the cards were short. It reads as a copy problem and it is a layout
  problem. See the explanatory-filler section in `references/copy.md`.
- **One global fade-in on scroll** applied to every element, or bounce-on-hover
  applied to everything clickable.

### Instead

Let content decide structure. Count the real things and show that many. If one
matters more, make it bigger and put it first.

Spacing is how grouping is communicated. Pick a small set of steps from a 4px
base and use only those. The gap inside a related group must be visibly smaller
than the gap to the next group, by a full step or more, not by a few pixels.
When everything is separated by the same amount, nothing is grouped, and that
flatness is one of the tells.

Radius: pick one value and hold it across the interface. Heavy rounding applied
uniformly to every card, button, input, and image is a recognized signature.
Anything above 8px on everything reads as generated.

Motion: three durations at most, none longer than about 220ms, and every one of
them explaining a state change. Something appeared, something moved, something
is loading. Motion that is decoration is on the banned list. Respect
`prefers-reduced-motion` globally.

Something in every composition must be deliberately asymmetric: different card
sizes, an offset image, a section that breaks the container, a headline that is
not centered. Asymmetry is evidence a human made a judgment call, and perfect
symmetry across every section is the strongest cue that nobody did.

---

## Decoration

Everything in this section is ornament a model reaches for because ornament is
cheap and photographs as "designed" in a thumbnail. None of it carries
information. This is the layer that survives after the palette and the typeface
have been fixed, which is why work that passes every other check can still read
as generated.

One test covers the whole section. Delete the thing. If nothing became harder
to understand, it was decoration, and decoration nobody decided on is the tell.

---

### The dots

Dots are the cheapest ornament available, so generated design is full of them.
Six habits, all banned by default.

**The status dot.** A saturated dot, almost always green, sitting in a pale
halo, usually pulsing, next to a word like Live, Online, Available, Shipping
now, or Accepting clients. It shows up on pages with no status to report,
because it reads as a real product. A status indicator is legitimate when there
is genuine state behind it and the reader needs it right there. Then it is one
small flat dot and a word: no halo, no pulse, and never the only carrier of the
meaning, since color alone is not a signal.

**The leading dot on an eyebrow.** A dot before a small all-caps label, usually
with a hairline rule trailing after it. This is the most reproduced single
piece of chrome in generated design, to the point that the dot and the rule
identify the output faster than the color does. Covered in the eyebrow section
above; repeated here because it is where most people meet it.

**The middle dot as the default separator.** `Brand · No. 01`,
`001 · Capabilities`, `Lisbon 14:23 · 18°C`, `Design · Build · Ship`. The
interpunct is a good separator used once, where two facts genuinely belong on
one line. It becomes a tell when it turns into the connective tissue of the
entire page, joining things that were never a series. One per line at most. A
line that wants three of them wants a line break, a hairline, or a column
instead. Where you do use one, set it with a pseudo-element or mark it
`aria-hidden`, so it is not read aloud between every item.

**A colored dot on every row.** Before every nav link, every list item, every
badge, every spec. When each dot is a different hue and none of them maps to a
state, they are confetti. One dot that means something beats twelve that mean
nothing.

**The dot grid.** A repeating radial-gradient dot field behind a hero, plus its
relatives: crosshair marks in the corners of a section, a faint hairline grid
laid over nothing, a dotted rule used as a divider. All of it drawn to make an
empty area look considered. Rules and grids are fine when they organize real
content and separate things that need separating.

**Traffic-light dots on fake chrome.** Three dots in a rounded bar above a
div-built mock of a product interface. It is a fake screenshot of a thing that
does not exist, and the dots are the giveaway. Show the real screenshot, or
show nothing. The window frame is not the product.

Two more that are dot-shaped and just as empty: carousel dots under something
that does not scroll, and a three-dot overflow button with no overflow menu
behind it.

---

**Text glyphs standing in for icons.** `✓ ✗ → ← ↑ ↓ ×` set as characters in
buttons, rows and result lists. They render at different weights and baselines
in every font and look unfinished beside real icons. Use inline SVG drawn in
the same stroke as the rest of the UI.

**Status that duplicates a control.** A dot and the word "Learning" on a page
whose on/off toggle lives elsewhere, or a "Virtual" pill on a card whose label
already says so. If another control already shows the state, delete the
indicator.

### Badges, pills, and micro-labels

**Never ship**

- **A version or status pill in the hero.** `V0.6`, `BETA`, `EARLY ACCESS`,
  `INVITE-ONLY PREVIEW`, `ALPHA`. Ship one only when the launch state is
  actually the news.
- **Badge spam.** `New` with a sparkle, `Popular` with a flame, `Beta`, `Pro`,
  `AI-powered`, scattered across cards and nav. If everything is flagged,
  nothing is.
- **Pills laid over images.** `Brand · 02`, `PLATE · BRAND`, `Field notes` as
  an absolutely positioned span on a photo. Let the image carry itself, or put
  a real caption underneath it.
- **A bordered, tinted, uppercase-tracked pill for a plain fact.** "BETA" in
  accent blue becomes plain muted "Beta" text. A pill needs a reason to be a
  pill.
- **A pill that duplicates its container.** A `Pricing` chip inside the pricing
  section.

A badge earns its place when it changes what the reader does: a real state
change, a real constraint, a real difference between two otherwise identical
items. Then it is one badge, in one style, and it says the specific thing.

---

### Decorative micro-text

Small text placed for texture rather than for a reader. It is the copy version
of the dot, and it fails the deletion test every time.

**Never ship**

- **Scroll cues.** `Scroll`, `↓ Scroll to explore`, `Keep going`. The page
  scrolls; people know.
- **Locale, time, and weather strips.** `Lisbon 14:23 · 18°C`. Only where the
  place is genuinely the subject.
- **Manufactured scarcity.** `Reservation 412 of 800`, `2 spots left this
  quarter`, a live counter with no live data behind it. If the number is not
  real and not measured, it is a lie with a dot next to it.
- **Fake archival captions.** `Plate 03 · House archive`,
  `Field study no. 12`, `Frame XII · 35mm` under an image nobody shot. Credit
  real photographers; skip it otherwise.
- **A word strip under the hero.** `BRAND. MOTION. SPATIAL.` Three nouns in
  wide letter-spacing, standing in for a value proposition.
- **A micro-sentence hung off a heading**, floated top-right or set under an
  eyebrow, explaining the section the heading already named.
- **False modesty in social proof.** `Quietly trusted by`, `Quietly in use at`.
  Say `Used at`, or name the customers, or cut the section.

---

### Decorative surfaces

- **Rules on every row.** A top border and a bottom border on each item of a
  long list or spec table, so the page becomes a ledger. Pick one edge, or
  group with spacing instead.
- **Cards inside cards.** A bordered box inside a bordered box, each with its
  own padding and radius. Two nested surfaces is usually one too many.
- **Corners that do not nest.** The same radius on a parent and its child.
  Inner radius equals outer radius minus the gap between them, or the curves
  visibly disagree.
- **The icon in a tint of itself.** A rounded square filled with 10% of the
  icon's own color, repeated down a feature list. It is the icon-on-top card
  wearing a smaller box.
- **A grid of rounded-square icon tiles**, all the same size, all the same
  radius, each holding one line-art glyph.
- **The border that dies at the corner.** A hairline on the straight edges and
  nothing along the arcs, because the radius lives on a wrapper with
  `overflow-hidden` while the border lives on the child inside it. Every line
  is locally correct and the composition is broken, which is the fingerprint of
  code nobody ever rendered. Put the radius and the border on the same box.
- **The oversized drop shadow.** A 40px or wider blur at low opacity with
  almost no offset, so a button and a hero card float in the same fog. A shadow
  models height, so it needs a small elevation scale: tight blur, small offset,
  low opacity, never larger than the thing casting it, and never both a
  hairline and a wide soft shadow on the same element. Often the hairline alone
  does the separating.
- **Uniform component metrics.** The same radius, the same padding, and the
  same forced height on every card, button, input, and image, so nothing has a
  size that means anything.

---

## Evolved defaults

The bans above describe the first-order default. A model scolded out of the
indigo gradient does not start deciding; it moves to the next safest template.
Those templates are now common enough to be tells in their own right, and they
are harder to catch because they are not ugly. That is the trap. Polish is not
evidence of a decision.

**The tasteful terminal.** Monospace as the interface chrome rather than as
code, a near-black ground, one warm accent, ASCII art in the hero, lowercase
everything, a fake shell prompt in front of the buttons. It reads as taste in
isolation and as a template in aggregate. Keep monospace for code. Use a
terminal metaphor only where the product is one.

**The editorial dashboard.** An operational screen dressed as a magazine: a
large serif "Good evening, Mara", oldstyle serif numerals in the stat cards,
cream paper, a tracked-caps label over every block. A magazine is read once,
top to bottom. A console is scanned all day. Display serifs carry proportional
oldstyle figures, which are exactly the numerals you cannot scan down a column,
so a scanned interface wants a legible sans with tabular lining figures. If you
want warmth, make one material decision, not the whole costume.

**Amber and cream.** Covered under Color, and it belongs here too. It is what
"warm and human" becomes when the model translates it laziest.

The test is the same for all three: name the decision. If the answer is that
this is what a good product looks like right now, that is the training-data
average talking, and it will date the same way indigo did.

---

## Imagery

### Never ship

- Stock photography of a diverse team laughing in a sunlit office.
- Abstract 3D blobs, spheres, or ribbons floating in space with a plastic sheen.
- AI-generated people. The uncanny smoothness is now the point people notice.
- **A product screenshot built out of divs.** A fake window, fake sidebar, fake
  rows, usually topped with three traffic-light dots. It claims a product exists
  and shows a drawing instead.
- **Hand-rolled SVG icons.** Blobby shapes with two dots for eyes, a mascot
  assembled from circles, a set where the stroke weights disagree. Use a real
  icon family and use one.
- **Gradient-mesh backgrounds and blurred color blobs.** The soft multicolor
  wash behind a hero, usually purple into cyan, usually blurred to 200px.
- **Isometric blob-people illustrations.** Corporate Memphis: flat figures with
  no faces and long bendy limbs, in two brand tints.
- **Garbled text inside a generated image.** The single fastest giveaway that
  an image was generated, and it survives every other fix, so read every
  string in every image before shipping it.
- Nothing at all, where every section became a text card because sourcing images
  was skipped.

### Instead

Real product screenshots, real photographs of the real thing, or honest
diagrams that show a mechanism. If there is nothing real to show, say less
rather than filling the space. An empty, confident section beats a filled,
generic one.
