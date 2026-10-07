# Cleanup pass: removing slop from existing work

Real before/after cases from a pass over a shipped app, marketing site and
prototype (about 210 files). Use this when the job is to strip slop from
something that already exists, rather than to build something new. Each section
is a category to look for, with the rule behind it.

Read `copy.md` first. This file is the worked examples and the process.

---

## 1. Em dashes

Remove everywhere: UI, comments, docs, test names, package.json. Replace with a
period, colon, semicolon, comma, or parentheses, whichever fits the sentence.
In the source pass this was most of roughly 1,300 changed lines.

- `The first real (non-virtual) physical prototype for Noma [em] an ESP32 sketch`
  becomes `... for Noma. An ESP32 sketch`
- `USB cable (serial + power [em] skip Bluetooth for v1)` becomes
  `USB cable (serial and power; skip Bluetooth for v1)`
- `Noma Device Firmware [em] reference implementation` becomes
  `Noma Device Firmware: reference implementation`
- `${APP_DISPLAY_NAME} [em] TEST PROFILE` becomes `${APP_DISPLAY_NAME}, TEST PROFILE`

An em dash used as an empty-cell placeholder in a table is not punctuation. Use
"n/a" or leave it blank. Never fill it with content (see section 11).

## 2. Page intros and subtitles that restate the title

A subtitle under a page heading that lists what the page contains, or repeats
the nav label, goes.

- `Settings` / "Glide, Flow learning, your data, updates, and getting help." becomes `Settings`
- `Controls` / "Your interface right now, and every action Noma has learned..." becomes `Controls`
- `Activity` / "What Noma has noticed and done, most recent first" is removed
- "Real patterns, counted from real activity" is removed. It is reassurance, not information.

## 3. Paragraphs that explain a control or restate what the UI shows

- A paragraph on how Flow learns, sitting directly above two lists titled
  "Flow sees" and "Flow never sees": removed. The lists carry it.
- "Every app has its own four. Click a zone to change it": removed.
- "Click to change them" under zone labels: removed. The affordance is the control.
- "Max 12 characters: this has to fit on a small physical display." under an
  input that already has `maxLength={12}`: removed.
- A three-sentence settings description becomes one line:
  "Adds the device simulator, Demo Mode and the device log to the sidebar."
- "This is exactly the kind of signal this prototype exists to collect." after
  a feedback submit: removed.

## 4. Trailing "you can change this at any time"

- "Everything Flow has observed and suggested is stored locally, never sent
  anywhere. You can clear it at any time." becomes
  "Stored on this computer. Never sent anywhere."
- A banner reading "On, watching your trackpad · Switch it off here or from the
  tray icon at any time" is removed entirely when the feature is on or off,
  because the toggle already shows state. Keep it only for "Starting..." and
  for problems.

## 5. Status elements that duplicate another control

- A dot plus the word "Learning" on Home, when the on/off toggle lives in
  Settings: remove the component and its only usage.
- A "Virtual Noma" pill with a dot in the corner of a card whose own label
  already says so: removed.
- A bordered, tinted, uppercase-tracked "BETA" pill in the accent color becomes
  plain muted "Beta" text. A pill needs a reason to be a pill.

## 6. Empty states

Rules: no stock phrase repeated across states, no title that restates the
section heading above it, no title at all when the hint is enough.

- Title "Noma hasn't noticed a pattern yet." under a heading "Noma noticed"
  becomes the hint alone: "A workflow appears here once Noma sees one repeat."
- "Keep working normally. Noma will surface a workflow here as soon as it sees
  one repeat." becomes "A workflow appears here once Noma sees one repeat."
- "Noma will build your interface as it learns." / "Keep working normally.
  Controls appear here once..." becomes "No controls yet." / "They appear once
  Noma has something to put on them."
- "Nothing here yet." / "Keep working normally. Noma will log..." becomes
  "No activity yet." / "Noma logs what it notices and creates here."
- "Once you've repeated the same shortcut sequence about three times, it shows
  up here for you to review." becomes "Repeat the same shortcut sequence about
  three times and it shows up here."

"Keep working normally." appeared in six empty states. One phrase repeated
across a product is a tell. Grep for repeated sentences before you finish.

## 7. Banned vocabulary and filler words

Also out: "simply", and "just" used to minimise a step.

| Before | After |
|---|---|
| seamless | unified, or drop the word |
| curated | selected |
| journey (metaphorical) | workflow |
| "Welcome to Noma" as a Home heading | "Noma" |
| "Noma now shows what changed, like this note." | "Noma shows what changed." |
| "Something not working? Describe what you did and what happened." beside a button that says the same | phrase removed, privacy note kept |

## 8. Glyph "icons"

Text characters used as icons render inconsistently and look unfinished beside
the rest of the UI. Replace with inline SVG matching the app's stroke style:
checks and crosses (onboarding, test results), arrows (back, workflow chain,
"Review →"), up, down and delete on list rows, and per-type marks drawn from
six unrelated geometric glyphs.

Side effect: tests that matched the text ("Review →") have to switch to
`getByRole('button', { name: /Review/ })`.

## 9. Separator dots in labels

`Visual Studio Code · Lower right zone` becomes
`Visual Studio Code, lower right zone`. Sweep for the rest; a single pass
usually leaves some.

## 10. Spacing bugs found along the way

- One card in a stack was missing the bottom margin every sibling had, so it
  touched the next card. Check that every item in a repeated list carries the
  same spacing class.
- An app icon in a form row was drawn at 68% of an 18px box, about 12px. Size
  the box to the control it sits beside (24px) and use the component's fill mode.

## 11. What the pass gets wrong

Cheap model passes make confident factual edits. Diff-review every change for:

- **A true statement made false.** A README said fonts were "Sora (display),
  Inter (body)". An agent rewrote it to "Sora (display and body)" while the
  site still loads Inter.
- **A blank filled with an invented fact.** A table cell that was an em dash
  became "~$3". Placeholder dashes need "n/a", not content.
- **Reports that overstate or miscount.** "138 files changed" when git showed 91.
- **Strings asserted by tests.** Change the string and the test together, then
  run the suite.
- **Dev-only pages.** Decide separately whether the same cleanup applies.

## 12. What to leave alone

- Warnings and errors the user needs, including "not available on this computer".
- Privacy facts a control depends on.
- Literal uses of banned words that are configuration keys (a "navigate" editor setting).
- Pure styling findings (glass panels, glows), unless the user asked for a visual pass.

---

## Process

- Split the work by directory so agents never share files, and keep each
  agent's token use small.
- Give every agent `copy.md` to read first and `scripts/audit.py` to run before
  and after.
- When agents finish: grep tracked files for any remaining banned pattern,
  typecheck, run the tests, then spot-check diffs for the failures in section 11.
