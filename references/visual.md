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

Three faces are out: **Inter, Space Grotesk, and Roboto.** Not because they are
bad (Inter in particular is excellent) but because they have become the
signature of a choice that was not made. Everything else is open.

### Never ship

- **Inter, Space Grotesk, or Roboto.** Inter as the default for everything,
  chosen because it was not chosen, is the most common version of this.
- **A typeface you did not choose.** If you cannot say in one sentence what the
  face is doing for this design, it was inherited from a starter template or
  from habit, and that is what readers pick up on.
- **A single italic serif word dropped into a sans headline.** "Build *better*
  software."
- **All-caps eyebrow labels** above section headings, especially with a
  decorative dot or a trailing rule.
- **Monospace body copy** on a page that is not about code.
- **Type hierarchy that is only size.** If the only difference between a
  heading and body text is that one is bigger, there is no hierarchy.

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

## Imagery

### Never ship

- Stock photography of a diverse team laughing in a sunlit office.
- Abstract 3D blobs, spheres, or ribbons floating in space with a plastic sheen.
- AI-generated people. The uncanny smoothness is now the point people notice.
- Nothing at all, where every section became a text card because sourcing images
  was skipped.

### Instead

Real product screenshots, real photographs of the real thing, or honest
diagrams that show a mechanism. If there is nothing real to show, say less
rather than filling the space. An empty, confident section beats a filled,
generic one.
