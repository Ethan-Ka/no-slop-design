# Audit checklist

Run against finished work, before presenting it. Two or more failures means it
goes back.

`scripts/audit.py` covers the items marked (auto). Everything else needs a
human or a model actually looking at the rendered result. When you report,
record which checks were run by tool and which by hand. An unverified check is
a failure, not a pass.

## Copy

- [ ] Zero em dashes and zero spaced en dashes (auto)
- [ ] No banned vocabulary (auto)
- [ ] No banned headline pattern (auto)
- [ ] No banned structure: negative-parallel, false-inclusivity opener,
      rhetorical-question header, restating close, "not only X but also Y",
      colon reveal, triad (auto, partial)
- [ ] Zero chatbot residue: "I hope this helps", "as an AI language model" (auto)
- [ ] No unsolicited reassurance, no fake-profound closer, no sign-off (auto)
- [ ] Connectives are not overproduced: moreover, furthermore, additionally,
      notably (auto)
- [ ] Heading case is consistent and matches the house style
- [ ] Testimonials are real or absent (auto, partial)
- [ ] No placeholder company names on a logo wall (auto)
- [ ] No fake-precise metrics (99.99%, 3.2x) on an unmeasured product (auto, partial)
- [ ] At least one specific, checkable claim appears
- [ ] Sentence lengths vary
- [ ] Button labels name outcomes, errors say what to do
- [ ] No explanatory filler: no "Here you can", no page-intro paragraph, no
      subhead restating its heading, no welcome banner (auto, partial)
- [ ] Deletion test run: every paragraph that is not a heading, a label, or a
      control was checked for what it lets the reader do
- [ ] Helper text carries a constraint, a consequence, or a rule, never
      reassurance or a restatement of the field label

## Color

- [ ] Primary accent is not indigo, violet, or purple (auto)
- [ ] Palette came from a stated real source
- [ ] No gradient in the hero (auto, partial)
- [ ] No colored glow behind any card or button (auto)
- [ ] No glassmorphism (auto)
- [ ] Dark mode is a choice, not a silent default
- [ ] Semantic colors grow out of the one palette, not the framework's stock
      blue / amber / green / red set (auto, partial)
- [ ] No one-hue status box: border, text, and tint are not the same hue at
      three opacities (auto)
- [ ] No gradient on a card surface, no top spotlight glow, no card washed in
      a tint of its own accent (auto, partial)
- [ ] All text pairs clear WCAG AA, with measured ratios recorded

## Typography

- [ ] Body typeface is not Inter, Space Grotesk, Roboto, Geist, Manrope, or
      Plus Jakarta Sans (auto)
- [ ] Two families maximum, each with a stated reason for this design
- [ ] No single italic serif word inside a sans headline
- [ ] No eyebrow above a heading, unless it carries information the heading
      does not (auto, partial)
- [ ] No monospace or all-caps eyebrow, ever; zero eyebrows is the default
      (auto, partial)
- [ ] No eyebrow chrome: leading dot, trailing rule, gradient text, sparkle
      (auto, partial)
- [ ] No section-number eyebrow ("001 / Capabilities", "01 / 02 / 03") and no
      poetic label ("Field notes") (auto, partial)
- [ ] Eyebrows counted: at most one per three sections, never two in a row
      (auto, partial)
- [ ] Body copy is not monospace (auto, partial)
- [ ] No text glyphs (check, cross, arrows) standing in for icons (auto, partial)
- [ ] No status indicator duplicating a control that already shows the state
- [ ] No stock sentence repeated across empty states
- [ ] After an automated sweep: diffs reviewed for facts made false or invented,
      counts verified against git, tests run (see cleanup-pass.md)
- [ ] Hierarchy uses more than size
- [ ] No gradient-filled headline text (auto)
- [ ] The display headline is a few words, not a whole sentence; tracking is
      not crushed past the face (auto, partial)
- [ ] The scale has real contrast between steps, not everything at 14 to 18px
- [ ] No strikethrough, underline, highlighter, or scattered colored words used
      as emphasis (auto, partial)
- [ ] No display serif carrying body copy or UI text (auto, partial)

## Layout

- [ ] Hero is not centered with a pill badge above the H1
- [ ] Feature cards are not three or six identical icon-on-top boxes
- [ ] No colored left borders on cards (auto, partial)
- [ ] No numbered 1-2-3 explanation sequence
- [ ] No stat banner of round numbers (auto, partial)
- [ ] No emoji used as icons (auto)
- [ ] Something is deliberately asymmetric
- [ ] Grouping is communicated by uneven spacing
- [ ] One radius value, held across the interface
- [ ] Motion explains state changes and is not decoration

## Decoration

- [ ] No pulsing or haloed status dot; any status dot maps to real state and is
      paired with a word (auto, partial)
- [ ] Middle dot used at most once per line, never as the page's default
      separator, and hidden from screen readers where used (auto, partial)
- [ ] No colored dot on every nav link, list row, or badge (auto, partial)
- [ ] No dot-grid, crosshair, or hairline-grid background drawn as texture
      (auto, partial)
- [ ] No traffic-light dots or fake browser chrome around a mock screenshot
      (auto, partial)
- [ ] No carousel dots without a carousel, no three-dot menu without a menu
- [ ] No version or status pill in the hero, no badge spam, no pill laid over
      an image (auto, partial)
- [ ] No decorative micro-text: scroll cue, locale or weather strip, invented
      scarcity counter, fake archival photo credit, hero-bottom word strip
      (auto, partial)
- [ ] No top and bottom border on every row of a list, no card inside a card,
      no icon tile tinted in its own color
- [ ] Inner radius equals outer radius minus the gap, so corners nest
- [ ] Borders do not die at the corner: radius and border sit on the same box
      (auto, partial)
- [ ] Shadows model elevation: tight blur, small offset, never larger than the
      element, never both a hairline and a wide shadow (auto, partial)
- [ ] Radius, padding, and height are not one uniform value across every
      component
- [ ] Deletion test run on ornament: every dot, rule, badge, and micro-label
      removed in turn, and only the ones a reader would miss put back

## Imagery

- [ ] No generic stock office photography
- [ ] No floating 3D blobs
- [ ] No AI-generated people
- [ ] No gradient-mesh background, blurred color blobs, or isometric
      blob-people illustrations
- [ ] Every string inside every generated image read for garbled text
- [ ] No product screenshot built out of divs
- [ ] No hand-rolled blob icons; one real icon family used consistently
- [ ] Every meaningful image has purposeful alt text (auto, partial)

## Evolved defaults

- [ ] Not the tasteful terminal: mono chrome, near-black, one warm accent,
      ASCII art
- [ ] Not the editorial dashboard: serif greeting, oldstyle serif numerals,
      cream paper, tracked-caps label on every block (auto, partial)
- [ ] Whichever aesthetic it landed on, the decision behind it is stated

## Tooling

- [ ] Nothing hand-rolled that a mature library already does correctly
      (dropdowns, focus traps, spinners, charts, easing, icons)
- [ ] Any library in use had its tokens replaced before the first screen was
      built: palette, radius, type scale, spacing
- [ ] Each library has a one-sentence reason for being in this project
- [ ] The library's accessibility behavior was kept, not reimplemented

## States

- [ ] Every interactive element has a visible keyboard focus state (auto, partial)
- [ ] Hover, active, and disabled states exist and are distinct
- [ ] Empty states exist and explain what belongs there
- [ ] Loading states exist where actions exceed roughly 400ms
- [ ] Error states name what went wrong and what to do
- [ ] Hover, press, and focus were actually exercised, not assumed
- [ ] A spinner was watched through a full revolution and does not wobble
      (auto, partial)
- [ ] Scroll animation is not one global fade applied to everything

## Structure

- [ ] One h1, ordered headings, landmarks, skip link
- [ ] Real buttons for actions, real links for navigation, labeled inputs
- [ ] Keyboard navigable end to end, tested
- [ ] Checked at 320px, 768px, 1440px, and 2560px
- [ ] Motion respects prefers-reduced-motion

## Sign-off

Write two lines in your output:

1. What passed, what failed, and what you changed as a result.
2. Which checks you could not verify, and why.
