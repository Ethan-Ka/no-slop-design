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

**3. What does the content actually demand?** Count the real things. If there are four features, show four, not three padded or six invented. If one matters more than the others, make it bigger and put it first. Let the content set the structure instead of pouring it into a hero-then-three-cards template.

**4. What is the one specific, checkable claim?** Write one true sentence about what the thing does, with a number or a mechanism in it. "Turns a Postgres query into a shareable dashboard in about a minute" beats "Unlock the power of your data" every time, because specificity is what a model cannot fabricate. If you do not know the specifics, ask, or say plainly that the copy is placeholder.

## The rules, in brief

Full reasoning and the complete lists live in the reference files. Read the relevant one when you are working in that area.

**Color** (`references/visual.md`): no indigo or violet accent, no purple-to-blue or purple-to-cyan gradient anywhere, no glassmorphism, no colored glow behind cards or buttons, no dark mode as a silent default. Shadows stay neutral.

**Typography** (`references/visual.md`): no single italic serif word inside a sans headline, no all-caps eyebrow label above a heading, no monospace body copy on a page that is not about code. Build hierarchy from position, weight, color, and spacing before you reach for size. Hierarchy that is only size is not hierarchy.

**Layout** (`references/visual.md`): no centered hero with a pill badge above the H1, no row of three or six identical icon-on-top cards, no colored left borders, no numbered 1-2-3 explainer, no stat banner of round numbers, no emoji as icons. Something in the composition must be deliberately asymmetric. Uniform spacing communicates no grouping; the gap inside a group has to be visibly smaller than the gap to the next group, by a full step.

**Imagery** (`references/visual.md`): no laughing-team stock photos, no floating 3D blobs, no AI-generated people. Real screenshots, real photographs, or honest diagrams. If there is nothing real to show, say less rather than filling the space.

**Copy** (`references/copy.md`): this is where the tell is loudest and the part most often shipped unedited. No em dashes, anywhere, including UI strings and docs. No spaced en dashes either. The banned vocabulary and headline patterns are in the reference file; read it before writing any user-facing text. Vary sentence length.

**Craft** (`references/craft.md`): the states nobody generated because nobody asked. Focus, hover, active, disabled, empty, loading, error. Semantic markup. Verified contrast. Behavior at 320, 768, 1440, 2560. A design missing any of these is not finished no matter how good the happy path looks.

## Running the audit

```bash
python3 scripts/audit.py path/to/src            # whole tree
python3 scripts/audit.py index.html --json      # machine-readable
```

No dependencies, Python 3.8 and up. It catches the mechanical tells: em dashes, banned vocabulary, banned headline patterns, AI-default hues in hex values, banned typefaces, colored glows, glassmorphism, emoji icons, suppressed focus outlines, placeholder testimonial names, missing alt text. Exit code 1 when anything hard fails.

It cannot see whether the layout is symmetric, whether the copy is specific, or whether empty and error states exist. Those are in `references/audit-checklist.md` and you have to actually look. When you report the result, say which checks you ran by tool and which by hand. An unverified check is a failure, not a pass.

## When a rule blocks you

The rules ban specific defaults, not whole categories. If purple is genuinely the brand color, use purple and say why. An exception with a stated reason is a decision. An exception without one is exactly the thing this skill exists to stop.

## Reference files

| File | Read it when |
|---|---|
| `references/visual.md` | Choosing color, type, layout, or imagery |
| `references/copy.md` | Writing any user-facing text, including microcopy |
| `references/craft.md` | Building components, or checking accessibility and states |
| `references/audit-checklist.md` | Reviewing finished work |
