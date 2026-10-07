# Craft: states, components, accessibility

These are not aesthetic items. They are the states nobody generated because
nobody asked for them, and they are the fastest way to tell that something was
produced in one pass. A design missing any of them is not finished, regardless
of how good the happy path looks.

---

## The seven states

Every interactive component ships all seven. Claiming a component is done
without them is the failure this list exists to catch.

1. **Default.**
2. **Hover**, distinct from default, and never the only affordance, since touch
   devices have no hover.
3. **Active / pressed**, distinct from hover.
4. **Focus visible.** A 2px outline at 2px offset, in a color that clears 3:1
   against both the component and its background. Visible with the keyboard
   alone. Never removed. `outline: none` without a replacement is a defect.
5. **Disabled**, visually distinct, communicated to assistive technology, with
   the reason available somewhere.
6. **Loading**, wherever an action can take longer than roughly 400ms.
7. **Error**, naming what went wrong and what to do about it.

Components that display data add two more: **empty** and **partial**.

In a repeated list, every item carries the same spacing. One card missing the
bottom margin its siblings have will touch the next card. An icon in a form
row is sized to the control beside it, not scaled down inside a larger box.

---

## Component rules

### Buttons

Three variants, no more: primary (filled), secondary (bordered), quiet (text
only). If a fourth is needed, the page is doing too much. One primary per view;
two primaries means neither is primary. The hero version of this failure has a
name: twin buttons, "Get started" beside "Learn more", same size, same weight,
same visual pull, so the page declines to say what it wants you to do. Pick the
one action and let the other be a text link. Minimum hit target 44 by 44 CSS pixels,
icon-only buttons included, and icon-only buttons need an accessible name.
Label with a verb phrase naming the outcome.

### Cards

The most abused component in generated design, so the constraints are tighter.

Banned: colored left borders, icon-on-top with a heading and exactly two lines
of body, three or six identical cards in a row, colored glow, uniform height
forced across content of different lengths.

Required: if a card is clickable, the whole card is the target and there is
exactly one link inside it, not a nested link plus a card link. Cards in a set
may differ in size when their content differs in importance. That variation is
the point.

### Forms

Every input has a visible, persistent label. Placeholder text is not a label,
and placeholder-as-label fails the moment someone starts typing. Mark required
fields in the label, not only with a red asterisk. Errors appear next to the
field, are announced to screen readers, and survive a failed submit without
clearing what was entered. Validate on blur, not on every keystroke. Use the
correct input `type` and `autocomplete` so browsers and password managers work.

### Navigation

Current location is indicated by more than color. Keyboard order follows visual
order. There is a skip link to main content. Mobile navigation is reachable and
closable by keyboard, and traps focus while open.

### Tables and data

Real `th` elements with a scope. Sort controls that announce their state.
Numeric columns right aligned with tabular figures. An empty state that explains
what would appear. A defined behavior at narrow widths, either horizontal
scroll with a visible affordance or a card reflow, chosen deliberately.
Categorical series in charts must be distinguishable without relying on hue
alone.

### Modals and overlays

Focus moves into the dialog on open and returns to the trigger on close. Escape
closes. Focus is trapped while open. The background is inert to screen readers.
There is a visible close control, not only a click on the backdrop.

### Feedback

Toasts and inline messages announce politely to assistive technology. They do
not vanish on a timer if the user needs to act on them. Errors are never
communicated by color alone.

### Motion that was never watched

Most tells are an absence of taste. These are an absence of looking, which is
worse, because anyone who ran the page for four seconds would have caught them.

**The wobbling spinner.** A loading ring that does not turn about its own
centre, so the arc traces a small circle as it spins. It happens when a rotate
keyframe replaces a `transform` that was also doing the centering
`translate(-50%, -50%)`, or when the arc is not centred in its own viewBox, or
when `transform-origin` was moved. Centre the artwork in its box, position with
a wrapper rather than inside the animated transform, and watch one full
revolution before you move on. It lands at the worst possible moment, when the
user has nothing to do but stare at it, and a limping spinner reads as broken.

**Dead states.** A button that does nothing on hover, snaps with no transition
on press, and shows no focus ring. The inverse of the springy hover, and just
as much a sign that nobody ran it.

**One fade-in on everything.** A single scroll-triggered animation applied
globally, so the page reveals itself in one undifferentiated wave.

Watch what you built. Hover it, tab through it, press the buttons, let the
loading state run. A model does not render its own output, so this is the class
of defect that only exists in generated work.

---

## Accessibility baseline

Target is WCAG 2.2 Level AA. Listed separately because these are the items most
often skipped in one-pass generation, and skipping them is both a quality
failure and, in many contexts, a legal one.

**Contrast.** Body text 4.5:1. Large text 3:1. Non-text UI (input borders,
meaningful icons, focus indicators) 3:1. Verify with a tool and record the
measured ratios. Color is never the sole carrier of meaning.

**Keyboard.** Everything reachable by mouse is reachable by keyboard. Tab order
follows visual order. Focus is always visible. No keyboard traps except the
intentional one in a modal, which releases on Escape.

**Structure.** One `h1` per page. Heading levels descend without skipping.
Landmarks: `header`, `nav`, `main`, `footer`. A skip link to main. Lists marked
up as lists. Buttons that do things are `button`. Links that go places are `a`
with an `href`.

**Names.** Every form control has a programmatically associated label. Every
meaningful image has alt text describing its purpose, not its appearance.
Decorative images get `alt=""`. Icon-only controls have accessible names.
Dynamic regions use `aria-live` at the right politeness level.

**Motion and timing.** All animation respects `prefers-reduced-motion`. Nothing
auto-plays with sound. Nothing flashes more than three times per second. Any
time limit is adjustable or removable.

**Zoom and reflow.** Usable at 200% zoom without horizontal scroll. Usable at
320px width. Text spacing can be overridden without clipping.

### Verifying

Automated tooling catches roughly a third of accessibility issues. Before
calling it done, also:

- Navigate the whole flow with keyboard only
- Run the primary path with a screen reader, at minimum VoiceOver or NVDA
- Check at 200% zoom and at 320px width
- Confirm every state above actually exists

An automated pass alone is not verification. Say which of these you actually
did and which you did not.

---

## Reaching for real tools

Two failures sit at opposite ends, and this skill is only about one of them.
Shipping a framework's factory settings is the default failure. Hand-rolling
something a mature library already does correctly is the other, and generated
work does it constantly: a spinner that wobbles, a dropdown with no focus trap
and no `aria-activedescendant`, a bar chart built from divs with a hardcoded
max, a hand-drawn SVG icon with two dots for eyes, an easing curve invented on
the spot. That is not craft. It is a worse version of solved work, missing the
accessibility and the edge cases the library spent years on.

So reach for the good tools when the work calls for them. Where the surface
should feel considered rather than merely functional, the difference is usually
that somebody used a real library and then made decisions on top of it.

**Components and primitives.** [shadcn/ui](https://ui.shadcn.com/) is the
strong default: Radix primitives underneath, which means the focus management,
keyboard behavior, and ARIA are already right, and the styles land in your repo
as code you own rather than as a dependency you fight. Radix UI, React Aria, or
Base UI directly are equally good when you want to bring your own styling
layer.

**Motion.** [Motion](https://motion.dev/examples) for anything past a CSS
transition: layout animation, shared-element transitions, gesture-driven
movement, orchestrated sequences, spring physics for things that genuinely move
through space. Its examples page is the fastest way to see what a state change
should look like when it is doing a job.

**Data.** [D3](https://d3js.org/) when the chart has a form no chart library
ships: a custom scale, a force layout, an arbitrary projection, an annotation
layer that has to sit exactly there. Observable Plot or Vega-Lite for the
ordinary cases, where reaching for raw D3 is over-engineering. Visx if you want
D3's math with React's rendering.

**The catch, and it is the whole point.** A library is a starting point you
decide on top of, never the decision itself. shadcn shipped with its default
tokens, default radius, default Inter, and the default `zinc` neutral is
precisely the generated look this skill exists to stop; it is one of the most
recognizable surfaces on the web right now. The same components with your
palette, your radius, your type scale, and your spacing are the opposite. So
when you install one of these:

- Replace the token file first, before you build a single screen. Palette,
  radius, type scale, spacing. If you skipped this, you shipped the default.
- Delete the variants you are not using, rather than keeping all of them
  because they came in the box.
- Keep the accessibility behavior exactly as it came. That is what you came
  for.
- Be able to say what the library is doing for this project in one sentence,
  the same test the typeface has to pass.

The rule is not "avoid popular tools". It is "do not let a tool make the
decisions that were yours to make". Using D3 to draw exactly the chart the data
needs is a decision. Using a library's demo palette because it was already
there is not.

---

## Responsive

Check at 320px, 768px, 1440px, and 2560px. 320px is narrower than most
breakpoint sets go and is where layouts actually break. 2560px is where a
container with no max width turns body copy into a single 200-character line.
