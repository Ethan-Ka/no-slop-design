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
| `references/visual.md` | Color, type, layout, decoration, and imagery, with the reason behind each rule |
| `references/copy.md` | The em dash rule, banned vocabulary, headline patterns, microcopy |
| `references/craft.md` | The seven states, component rules, motion nobody watched, when to reach for a real library, WCAG 2.2 AA baseline |
| `references/cleanup-pass.md` | Removing slop from existing work: worked before/after cases, what to leave alone, how automated sweeps go wrong |
| `references/audit-checklist.md` | The gate. Two failures means the work goes back. |
| `scripts/audit.py` | The mechanical half of the audit. No dependencies. |

## Install

The skill is the folder: `SKILL.md`, `references/`, and `scripts/`.

### Claude Code

As a plugin, from inside Claude Code:

```
/plugin marketplace add Ethan-Ka/no-slop-design
/plugin install no-slop-design@no-slop-design
```

Update later with `/plugin marketplace update no-slop-design`.

Or as a plain skill, one line in the shell, available in every project:

```bash
git clone https://github.com/Ethan-Ka/no-slop-design.git ~/.claude/skills/no-slop-design
```

Per-project install: clone into `<your-project>/.claude/skills/no-slop-design`
instead. Update with `git -C ~/.claude/skills/no-slop-design pull`.

Restart Claude Code, or start a new session. The skill loads on its own when you
ask for UI or copy work, and you can call it directly with `/no-slop-design`.

### Claude.ai and other agents

Upload `dist/no-slop-design.skill` under Settings, Capabilities, Skills. For
agents without skill support, point them at `SKILL.md`.

Rebuild the package after any change to the skill:

```bash
mkdir -p /tmp/pkg/no-slop-design
cp -R SKILL.md references scripts /tmp/pkg/no-slop-design/
rm -f dist/no-slop-design.skill
(cd /tmp/pkg && zip -qr "$OLDPWD/dist/no-slop-design.skill" no-slop-design)
```

### Check it worked

In Claude Code, ask "what skills do you have?" and look for `no-slop-design`, or
run the audit directly:

```bash
python3 ~/.claude/skills/no-slop-design/scripts/audit.py path/to/src
```

## Using it

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
vocabulary, banned headline patterns and structures, explanatory filler,
eyebrow labels with their chrome and the one-per-three-sections budget, the dot
family (pulsing status dots, middle-dot separator runs, dot-grid backgrounds,
traffic-light dots on fake browser chrome, a dot on every row), badge and
version-pill spam, decorative micro-text, AI-default hues computed from hex
values, purple and cyan gradients, glassmorphism, colored glows, colored left
borders, emoji standing in for icons, `outline: none` with no replacement,
images without alt text, placeholder testimonial and company names,
round-number stat banners and fake precision, chatbot residue, unsolicited
reassurance, gradient-clipped headline text, the one-hue status box, the
framework's stock semantic palette, oversized drop shadows, and spinners likely
to wobble.

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
