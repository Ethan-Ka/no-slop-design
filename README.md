# no-slop-design

An installable agent skill that keeps generated interfaces and copy from
reading as AI output.

Generated design fails in a specific, recognizable way. Not because the model
lacks skill, but because an underspecified prompt returns the statistical
center of the training data, and for web design that center is the median
Tailwind tutorial scraped between 2019 and 2024. The result looks correct and
has no author. Readers detect that absence in under sixty seconds, even when
they cannot name what they are detecting.

This skill is brand-agnostic. It constrains defaults without prescribing a
palette or a typeface, so it works on client projects, on someone else's brand,
and on work that has no design system at all.

## What is here

| Path | What it is |
|---|---|
| `SKILL.md` | The skill itself. Four decisions to make before building, the rules in brief, how to audit. |
| `references/visual.md` | Color, type, layout, and imagery, with the reason behind each rule |
| `references/copy.md` | The em dash rule, banned vocabulary, headline patterns, microcopy |
| `references/craft.md` | The seven states, component rules, WCAG 2.2 AA baseline |
| `references/audit-checklist.md` | The gate. Two failures means the work goes back. |
| `scripts/audit.py` | The mechanical half of the audit. No dependencies. |

## Using it

Point an agent at `SKILL.md`, or package the folder as a `.skill` file and
install it.

The load-bearing part is the four decisions in `SKILL.md`: where the palette
comes from, which two typefaces and why, what the content actually demands, and
what the one specific checkable claim is. An unanswered question becomes a
default, and a default is the failure this skill exists to prevent.

## Running the audit

```bash
python3 scripts/audit.py path/to/src
python3 scripts/audit.py index.html --json
```

Python 3.8 and up, no dependencies. Exit code 1 when anything hard fails.

It catches the mechanical tells: em dashes and spaced en dashes, banned
vocabulary, banned headline patterns and structures, AI-default hues computed
from hex values, purple and cyan gradients, glassmorphism, colored glows,
colored left borders, emoji standing in for icons, `outline: none` with no
replacement, images without alt text, placeholder testimonial names,
round-number stat banners.

It cannot see whether the layout is symmetric, whether the copy is specific, or
whether empty and error states exist. Those live in
`references/audit-checklist.md`, marked so it is clear which half the script
covers and which half needs someone to look at the rendered result.

## On typefaces

Three faces are out: Inter, Space Grotesk, and Roboto. Not because they are bad,
Inter in particular is excellent, but because they have become the signature of
a choice that was not made. Everything else is open, so long as you can say what
the face is doing.

## Related

A second skill, `standardized-design-system`, is this one plus a concrete token
set: a warm neutral ramp, two accents, a 4px space scale, and verified WCAG AA
pairs shipped as CSS custom properties and a Tailwind preset. Use that one
inside a project that follows the house system, and this one everywhere else.

## License

MIT. See LICENSE.
