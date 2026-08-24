# Copy: voice and tone

Copy is where generated work gives itself away fastest, and it is the part most
often shipped unedited. A visually careful page with default copy still reads as
machine output.

---

## The rule that matters most: no em dashes

Do not use em dashes. Not in body copy, not in headlines, not in UI strings,
not in documentation, not in commit messages, not in alt text.

The em dash has become the most reliable single-character signature of
generated text. Human writers reach for it occasionally. Language models reach
for it constantly, roughly four times per hundred words, and readers have
calibrated to that difference. The spaced en dash used as a connector (" - "
set with an en dash character) reads identically and is also out.

### Substitutions

| Instead of an em dash | Use |
|---|---|
| Interrupting an idea | A comma, or two sentences |
| Introducing a list or an explanation | A colon |
| Setting off an aside | Parentheses |
| Joining two related clauses | A semicolon, or a period |
| Emphatic pause before a punchline | A period. Then the punchline. |

### Examples

Before: `Ship faster [em dash] without the guesswork.`
After: `Ship faster, without the guesswork.`

Before: `The platform does three things [em dash] reporting, alerting, and analysis.`
After: `The platform does three things: reporting, alerting, and analysis.`

Before: `The team [em dash] all four of them [em dash] shipped it in a week.`
After: `The team (all four of them) shipped it in a week.`

### Related punctuation tells

Curly quotes and apostrophes where a person typing in a code editor would have
produced straight ones. Perfect Oxford comma consistency across every list on
the site. Sentence lengths that barely vary from one paragraph to the next.

---

## Banned headline patterns

- "Build the future of [X]"
- "Your all-in-one [X]"
- "[X], reimagined"
- "The [X] platform for modern teams"
- Any tricolon of imperatives: "Ship faster. Build better. Scale smarter."
- "Where [X] meets [Y]"
- "Say goodbye to [X]"
- "It's not just [X]. It's [Y]."
- "Take your [X] to the next level"
- "Powered by AI" used as the value proposition rather than a footnote

---

## Banned vocabulary

Delve, robust, seamless, seamlessly, elevate, unlock, harness, tapestry, realm,
empower, revolutionize, game-changing, cutting-edge, best-in-class,
world-class, industry-leading, state-of-the-art, next-generation, holistic,
synergy, curated, bespoke, meticulous, supercharge, effortlessly, testament to,
at the end of the day, in today's fast-paced world, more than ever before.

Figurative only, fine in their literal senses: leverage (as a verb), navigate,
landscape, journey (for anything that is not travel), ecosystem (for a product
line).

---

## Banned structures

- "It's not just X, it's Y." The negative-parallel construction.
- "Whether you're a X or a Y, ..." The false-inclusivity opener.
- "In a world where..." The movie-trailer opener.
- A rhetorical question used as a section header. "So what does this mean for you?"
- A closing paragraph that restates the opening paragraph in different words.
- Stacked hedging: "may potentially help to improve."
- Bulleted lists where every bullet is exactly one line and opens with a bolded
  two-word label.

---

## Banned specifics

Placeholder testimonial names: Sarah Johnson, John Smith, Michael Chen, Emily
Rodriguez, Alex Thompson, Jane Doe. If the testimonial is not real, do not ship
a testimonials section at all.

Round-number metrics nobody measured. Superlatives with no comparison and no
source ("the fastest", "the most powerful").

---

## Explanatory filler

The second-loudest tell after em dashes, and the one that survives every visual
fix. A model narrates the interface because narrating is cheap, and because
prose fills space that composition would otherwise have to fill. The result is
a page explaining itself to somebody who is already looking at it.

### Never ship

- **A subhead under every heading that restates the heading.** "Settings /
  Manage your account settings and preferences."
- **A page-intro paragraph** explaining what the page is for, to a person who
  navigated there on purpose.
- **"Here you can", "In this section", "Use this page to", "This dashboard
  allows you to".** The interface talking about itself in the third person.
- **A welcome banner.** "Welcome to Analytics! Here you can track metrics,
  monitor performance, and share reports with your team."
- **Helper text under a field that needs none.** "Email address / Enter your
  email address."
- **A description under every card title** that restates the title at greater
  length.
- **A tooltip on an obvious control.** A tooltip reading "Save" on the Save
  button.
- **Prose explaining an affordance.** "Click the button below to get started."
  If a control needs a sentence, the control's label is wrong.
- **The trailing reassurance.** "You can change this at any time." "Don't
  worry, we'll never share your email." Appended everywhere, carrying nothing.
- **Three sentences in an empty state where one works.**
- **A closing paragraph that summarizes the section directly above it.**

### The deletion test

Read the page with every paragraph removed that is not a heading, a label, or a
control. If a reader can still tell what the thing is and still complete the
task, those paragraphs were filler and they go.

Then take each sentence you kept and ask what a reader can do after reading it
that they could not do before. No answer means delete it.

### Instead

A heading plus its content is the explanation. Do not put a sentence between
them saying what the section is.

Helper text earns its place only when it carries something the label cannot: a
format constraint ("MM/YY"), a consequence ("Visible to everyone in the
workspace"), a non-obvious rule ("Minimum 12 characters"). Reassurance is not
information.

In an application interface, budget one sentence of body copy per view and
spend it on the thing the user cannot infer. Marketing pages get more room, but
every paragraph has to carry a fact rather than a mood.

Empty space is not a problem that text solves. An empty, confident section
beats a filled, generic one. If a region looks bare, the fix is composition:
change the proportions, cut the section, or find something real to put there.

Where an explanation genuinely is needed, put it where it is needed. Inline at
the point of confusion, or behind a "Why?" control. Not as a preamble everyone
reads and nobody needed.

---

## What to do instead

Write one specific, true, checkable sentence about what the thing does.

"Turns a Postgres query into a shareable dashboard in about a minute" beats
"Unlock the power of your data" every time, because specificity is the one
thing a model cannot fabricate. It does not know your specifics. Every page
needs at least one claim a reader could go and verify.

Vary sentence length. Short ones land. Then a longer one that carries the
qualification and the context and gives the reader somewhere to settle before
the next short one.

When you do not have the specifics, ask for them. If you have to proceed
without them, mark the copy as placeholder in your output rather than filling
the gap with something that sounds finished.

---

## UI microcopy

Buttons say what happens: "Create project", not "Submit". Never "Click here" or
a bare "Learn more" with no object.

Errors say what went wrong and what to do about it: "That email is already
registered. Sign in instead?" not "An error occurred."

Empty states explain what belongs there and how to put it there.

Loading states name what is loading when it will take more than a moment.

Confirmations name the thing and the consequence: "Delete 3 drafts? This cannot
be undone."

Say it once. If the button label, the field label, and the helper text are all
carrying the same sentence, two of them are filler. See the explanatory-filler
section above.
