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

---

## Component rules

### Buttons

Three variants, no more: primary (filled), secondary (bordered), quiet (text
only). If a fourth is needed, the page is doing too much. One primary per view;
two primaries means neither is primary. Minimum hit target 44 by 44 CSS pixels,
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

## Responsive

Check at 320px, 768px, 1440px, and 2560px. 320px is narrower than most
breakpoint sets go and is where layouts actually break. 2560px is where a
container with no max width turns body copy into a single 200-character line.
