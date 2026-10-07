---
name: no-slop-design
description: 'Keeps generated interfaces and copy from reading as AI output. Use this skill whenever you are about to design, build, restyle, or write copy for any user-facing thing: a landing page, a web app, a dashboard, a marketing site, a slide deck, a README, a UI component, an email. Also use it when the user says the work looks "generic", "AI-generated", "vibe coded", "like every other AI site", "soulless", or asks you to make something "look designed", "look human", "not look like ChatGPT made it". Applies before you write the first line, and again as a pass over finished work. Brand-agnostic: it constrains defaults without prescribing a palette.'
---

# No-slop design

Generated design fails in a specific, recognizable way. Not because the model lacks skill, but because an underspecified prompt returns the statistical center of the training data, and for web design that center is the median Tailwind tutorial scraped between 2019 and 2024. The result looks correct and has no author. Readers detect that absence in under sixty seconds, even when they cannot name what they are detecting.

Every item in this skill is a place where a default gets accepted instead of a decision getting made. The fix is constraint, not taste.

## How to use this

Two moments, both required.

**Before building.** Run the four decisions below. Write the answers into your output or your plan. An unanswered question becomes a default, and a default is the failure.

**After building.** Run `scripts/audit.py` for the mechanical checks, then walk `references/audit-checklist.md` for the judgment ones. Report the result honestly, including what you did not check. Two or more failures means the work goes back before you present it.

If the user gave you a brand, a palette, or an existing system, that wins. This skill fills the vacuum where no direction was given; it does not override direction that exists.

## The four decisions

Make these first, in this order, and state each one with its reason.

**1. Where does the palette come from?** Pick from something real: a brand asset, a physical material, a photograph, a printed reference, the subject matter itself. Then verify every text and background pair clears WCAG AA (4.5:1 body, 3:1 large text and non-text UI) and state the measured ratios. Do not use indigo, violet, or purple as the accent. Amber-cream and emerald are the second-order defaults and are just as recognized now, so treat them the same way.

**2. Which two typefaces, and why each?** Two maximum. Not Inter, not Space Grotesk, not Roboto. Not because they are bad (Inter is excellent) but because they have become the signature of a choice that was not made. Everything else is open, so long as you can say in one sentence what each face is doing here, at the sizes it actually has to work at.

**3. What does the content actually demand?** Count the real things. If there are four features, show four, not three padded or six invented. If one matters more than the others, make it bigger and put it first. Let the content set the structure instead of pouring it into a hero-then-three-cards template. Padding a thin section with explanatory prose is the same failure as inventing a sixth feature, so if there is not much to say, build a smaller thing.

**4. What is the one specific, checkable claim?** Write one true sentence about what the thing does, with a number or a mechanism in it. "Turns a Postgres query into a shareable dashboard in about a minute" beats "Unlock the power of your data" every time, because specificity is what a model cannot fabricate. If you do not know the specifics, ask, or say plainly that the copy is placeholder.

## The rules, in brief

Full reasoning and the complete lists live in the reference files. Read the relevant one when you are working in that area.

**Color** (`references/visual.md`): no indigo or violet accent, no purple-to-blue or purple-to-cyan gradient anywhere, no glassmorphism, no colored glow behind cards or buttons, no dark mode as a silent default. Not the framework's stock semantic set either (blue, amber, green, red at -50 over -600), and not the one-hue status box where border, text, and tint are the same color at three opacities. Gradient is not atmosphere: no card-surface gradients, no top spotlight, no card washed in a tint of its own accent. Shadows stay neutral, and they model height, so never wider than the thing casting them.

**Typography** (`references/visual.md`): no single italic serif word inside a sans headline, no eyebrow label above a heading unless it carries information the heading does not (the default is none, and a monospace all-caps eyebrow is never acceptable), and none of the newer eyebrow variants either: no section numbers ("001 / Capabilities"), no poetic label ("Field notes"), no micro-sentence stacked under it. If any survive, cap them at one per three sections and never two in a row. No monospace body copy on a page that is not about code, and no display serif carrying UI text. Also out: a whole sentence set at display size with the tracking crushed, a scale with everything between 14 and 18px, and drawing on the words with strikethrough, underline, highlighter, or a colored word every other line. Six typefaces are banned now, not three: Inter, Space Grotesk, Roboto, Geist, Manrope, Plus Jakarta Sans. Build hierarchy from position, weight, color, and spacing before you reach for size. Hierarchy that is only size is not hierarchy.

**Layout** (`references/visual.md`): no centered hero with a pill badge above the H1, no row of three or six identical icon-on-top cards, no colored left borders, no numbered 1-2-3 explainer, no stat banner of round numbers, no emoji as icons. Something in the composition must be deliberately asymmetric. Uniform spacing communicates no grouping; the gap inside a group has to be visibly smaller than the gap to the next group, by a full step.

**Decoration** (`references/visual.md`): the ornament layer, and the one that survives after the color and the typeface are fixed. Dots first, because there are six of them and they are the cheapest tell on the page: the pulsing haloed status dot next to "Live", the leading dot on an eyebrow, the middle dot used as the separator for everything, a colored dot on every row, the radial dot-grid background, and the three traffic-light dots on a fake browser frame. Then badge and version-pill spam, decorative micro-text (scroll cues, locale strips, invented scarcity counters, fake photo credits), rules on every row, cards inside cards, and icon tiles tinted in their own color. One test for all of it: delete it, and if nothing got harder to understand, it was never a decision.

**Imagery** (`references/visual.md`): no laughing-team stock photos, no floating 3D blobs, no AI-generated people, no gradient-mesh or blurred-blob backgrounds, no isometric blob-people, no product screenshot built out of divs, no hand-rolled blob icons. Read every string inside any generated image, since garbled text is the fastest giveaway there is. Real screenshots, real photographs, or honest diagrams. If there is nothing real to show, say less rather than filling the space.

**Evolved defaults** (`references/visual.md`): a model scolded out of the indigo gradient moves to the next safest template rather than starting to decide. Two are common enough to be tells: the tasteful terminal (mono chrome, near-black, one warm accent, ASCII art) and the editorial dashboard (serif greeting, oldstyle serif numerals, cream paper, tracked-caps label on every block). Neither is ugly, which is the trap. Polish is not evidence of a decision.

**Tooling** (`references/craft.md`): hand-rolling something a mature library already does correctly is its own failure, and generated work does it constantly. Reach for the real tools where the surface should feel considered: shadcn/ui or Radix for components, Motion for anything past a CSS transition, D3 when the chart has a form no chart library ships. Then replace the token file before you build the first screen, because a library shipped on its defaults is the generated look, not the fix for it.

**Copy** (`references/copy.md`): this is where the tell is loudest and the part most often shipped unedited. No em dashes, anywhere, including UI strings and docs. No spaced en dashes either. The banned vocabulary and headline patterns are in the reference file; read it before writing any user-facing text. Vary sentence length.

**Restraint** (`references/copy.md`): the interface does not explain itself. No paragraph under a heading that restates the heading, no page-intro telling people what page they are on, no "Here you can", no welcome banner, no helper text repeating the field label, no prose explaining what a button does, no trailing "you can change this at any time". Run the deletion test before you present: strip every paragraph that is not a heading, a label, or a control, and keep back only the ones whose absence a reader would feel. Text is not the fix for a section that looks empty; composition is.

**Craft** (`references/craft.md`): the states nobody generated because nobody asked. Focus, hover, active, disabled, empty, loading, error. Semantic markup. Verified contrast. Behavior at 320, 768, 1440, 2560. One primary action per view, never twin buttons of equal weight. Then actually run it: a wobbling spinner, a dead hover, and a border that dies at the corner are not failures of taste but of nobody ever looking at the rendered result, which is the one defect class unique to generated work.

## Running the audit

```bash
python3 scripts/audit.py path/to/src            # whole tree
python3 scripts/audit.py index.html --json      # machine-readable
```

No dependencies, Python 3.8 and up. It catches the mechanical tells: em dashes, banned vocabulary, banned headline patterns, explanatory filler, eyebrow labels and the uppercase-plus-letter-spacing recipe, the eyebrow budget of one per three sections, the dot family (pulsing status dots, eyebrow dots, middle-dot separator runs, dot-grid backgrounds, traffic-light window dots), badge and version-pill spam, decorative micro-text, AI-default hues in hex values, banned typefaces, colored glows, glassmorphism, emoji icons, suppressed focus outlines, placeholder testimonial and company names, chatbot residue, unsolicited reassurance, gradient-clipped headlines, the one-hue status box, the stock semantic palette, oversized shadows, wobble-prone spinners, missing alt text. Exit code 1 when anything hard fails.

It cannot see whether the layout is symmetric, whether the copy is specific, whether a given paragraph earns its place, or whether empty and error states exist. Those are in `references/audit-checklist.md` and you have to actually look. When you report the result, say which checks you ran by tool and which by hand. An unverified check is a failure, not a pass.

## When a rule blocks you

The rules ban specific defaults, not whole categories. If purple is genuinely the brand color, use purple and say why. An exception with a stated reason is a decision. An exception without one is exactly the thing this skill exists to stop.

## Reference files

| File | Read it when |
|---|---|
| `references/visual.md` | Choosing color, type, layout, or imagery |
| `references/copy.md` | Writing any user-facing text, including microcopy |
| `references/craft.md` | Building components, or checking accessibility and states |
| `references/audit-checklist.md` | Reviewing finished work |
