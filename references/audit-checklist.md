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
      rhetorical-question header, restating close
- [ ] Testimonials are real or absent (auto, partial)
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
- [ ] All text pairs clear WCAG AA, with measured ratios recorded

## Typography

- [ ] Body typeface is not Inter, Space Grotesk, or Roboto (auto)
- [ ] Two families maximum, each with a stated reason for this design
- [ ] No single italic serif word inside a sans headline
- [ ] No eyebrow above a heading, unless it carries information the heading
      does not (auto, partial)
- [ ] No eyebrow chrome: leading dot, trailing rule, gradient text
- [ ] Body copy is not monospace (auto, partial)
- [ ] Hierarchy uses more than size

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

## Imagery

- [ ] No generic stock office photography
- [ ] No floating 3D blobs
- [ ] No AI-generated people
- [ ] Every meaningful image has purposeful alt text (auto, partial)

## States

- [ ] Every interactive element has a visible keyboard focus state (auto, partial)
- [ ] Hover, active, and disabled states exist and are distinct
- [ ] Empty states exist and explain what belongs there
- [ ] Loading states exist where actions exceed roughly 400ms
- [ ] Error states name what went wrong and what to do

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
