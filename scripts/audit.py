#!/usr/bin/env python3
"""Automated pass of the anti-slop audit.

Catches the mechanical tells: em dashes, banned vocabulary, banned headline
patterns, explanatory filler, eyebrow labels and their chrome, the eyebrow
budget, the dot family (status dots, middle-dot separator runs, dot grids,
traffic-light window dots, dot-on-every-row), badge and version-pill spam,
decorative micro-text, AI-default hues, banned typefaces, glows, glassmorphism,
emoji icons, suppressed focus outlines, placeholder names, round-number stat
banners, missing alt text.

It does not catch the judgment items (is the layout symmetric, is the copy
specific, do empty and error states exist). Those stay on the human checklist
in references/audit-checklist.md. A clean run here means the mechanical half
passed, not that the work is done.

Usage:
    python3 audit.py <file-or-dir> [more paths...]
    python3 audit.py src/ --tokens tokens.json    # also check token conformance
    python3 audit.py src/ --json

Exit code 0 when nothing was found, 1 when anything was.
"""

import argparse
import colorsys
import json
import os
import re
import sys

TEXT_EXT = {
    ".html", ".htm", ".jsx", ".tsx", ".js", ".ts", ".vue", ".svelte",
    ".md", ".mdx", ".css", ".scss", ".astro", ".txt", ".json",
}
SKIP_DIRS = {"node_modules", ".git", "dist", "build", ".next", "vendor", "__pycache__"}

BANNED_WORDS = [
    "delve", "robust", "seamless", "seamlessly", "elevate", "unlock",
    "harness", "tapestry", "realm", "empower", "revolutionize",
    "game-changing", "cutting-edge", "best-in-class", "world-class",
    "industry-leading", "state-of-the-art", "next-generation", "holistic",
    "synergy", "curated", "bespoke", "meticulous", "testament to",
    "at the end of the day", "in today's fast-paced world",
    "more than ever before", "supercharge", "effortlessly",
    "utilize", "facilitate", "foster", "streamline", "synergize",
    "frictionless", "bleeding-edge", "disruptive", "paradigm shift",
    "thought leader", "ever-evolving", "move the needle", "circle back",
    "low-hanging fruit", "deep dive", "showcase", "unveil", "garner",
    "boast", "underscore", "myriad", "plethora", "nestled", "reimagine",
    "nuanced", "multifaceted", "intricate", "pivotal", "beacon",
    "it's worth noting", "it is worth noting", "it's no secret that",
    "gone are the days", "sheds light on", "navigating the complexities of",
    "aligns with", "in today's digital age",
]
# Model-overproduced connectives and study-flagged words. Common enough in
# ordinary writing that they report as warnings, not failures.
SOFT_WORDS_EXTRA = [
    "moreover", "furthermore", "additionally", "notably", "comprehensive",
    "crucial", "enhance", "vibrant", "captivating", "interplay", "symphony",
    "treasure trove", "kaleidoscope",
]
# These are only tells in figurative use, so they are reported separately as
# soft hits rather than hard failures.
SOFT_WORDS = ["leverage", "navigate", "landscape", "journey", "ecosystem"]

BANNED_PATTERNS = [
    (r"\bbuild the future of\b", "headline: 'Build the future of X'"),
    (r"\byour all[- ]in[- ]one\b", "headline: 'Your all-in-one X'"),
    (r"[,\s—\-]\s*reimagined\b", "headline: 'X, reimagined'"),
    (r"\bthe .{2,24} platform for modern teams\b", "headline: 'The X platform for modern teams'"),
    (r"\bwhere .{2,20} meets .{2,20}\b", "headline: 'Where X meets Y'"),
    (r"\bsay goodbye to\b", "headline: 'Say goodbye to X'"),
    (r"it'?s not just .{2,40}[.,] it'?s\b", "structure: 'It's not just X, it's Y'"),
    (r"\bwhether you'?re an? \w+ or an? \w+", "structure: 'Whether you're an X or a Y'"),
    (r"\bin a world where\b", "structure: 'In a world where'"),
    (r"\bpowered by ai\b", "'Powered by AI' as the value proposition"),
    (r"\bmay potentially\b|\bcould possibly help to\b", "stacked hedging"),
    (r"\btake your .{2,30} to the next level\b", "cliche: 'to the next level'"),
    (r"\bnot only .{2,40}[,]? but also\b", "structure: 'Not only X but also Y'"),
    (r"\byou'?re not (alone|imagining it|broken|crazy)\b",
     "structure: unsolicited reassurance"),
    (r"\bas an ai language model\b|\bi hope this helps\b|"
     r"\blet me know if you need anything else\b|"
     r"\bbased on the information provided\b|\bhere'?s a draft\b",
     "chatbot residue: direct evidence of paste"),
    (r"\blet'?s dive in\b|\bready to get started\?|\bthe future is bright\b",
     "structure: sign-off"),
]

# Text where the interface explains itself to somebody already looking at it.
# The single most common filler in generated UI, and the one that survives
# every visual fix.
FILLER_PATTERNS = [
    (r"\bhere you can\b", "filler: 'Here you can'", "fail"),
    (r"\bin this section\b", "filler: 'In this section'", "fail"),
    (r"\bthis (page|section|dashboard|view|panel|screen|tab) (lets|allows|helps|enables) you\b",
     "filler: the interface narrating itself", "fail"),
    (r"\buse this (page|section|form|tool|dashboard|view) to\b",
     "filler: 'Use this page to'", "fail"),
    (r"\bwelcome to (your |the |our )?[\w' ]{2,30}[!.]", "filler: welcome banner", "fail"),
    (r"\bclick (the )?(button |link )?below\b", "filler: affordance explained in prose", "fail"),
    (r"\bget started by\b", "filler: 'Get started by'", "fail"),
    (r"\byou can (change|update|edit|adjust) (this|these|it) at any time\b",
     "filler: trailing reassurance", "fail"),
    (r"\bwe'?ll never (share|sell|spam)\b|\bdon'?t worry\b",
     "filler: trailing reassurance", "fail"),
    (r"\bmanage your \w+ (settings|preferences|account|profile)\b",
     "filler: subhead restating its heading", "fail"),
    (r"\beverything you need to\b", "filler: catch-all subhead", "fail"),
    (r"\blearn more about how\b", "filler: 'Learn more about how'", "warn"),
    (r"\benter your (email|name|password|address|phone)\b",
     "filler: helper text restating the field label", "warn"),
    (r"\bsimply\b|\bjust\b(?= click| enter| add| select)",
     "filler: 'simply' / 'just' minimising a step", "warn"),
]

# Eyebrows: the small all-caps label above a heading. Structural guesses, so
# these report as warnings and need eyes on the rendered page to confirm.
EYEBROW_CLASS = re.compile(
    r"\b(eyebrow|kicker|overline|pre-?title|supertitle|section-label)\b", re.I)
EYEBROW_MARKUP = re.compile(
    r"<(p|span|div)\b[^>]*>\s*([A-Z][A-Z0-9 &/'\-]{2,28})\s*</\1>\s*<h[1-3]\b")

MONO_CAPS = re.compile(
    r"(?=.*(?:font-mono|monospace|\bmono\b))(?=.*uppercase)", re.I)

# Eyebrow chrome and the newer eyebrow variants.
EYEBROW_NUMBER = re.compile(
    r"^\s*(?:0\d\d?|\d{1,2})\s*[/·•]\s*[A-Za-z]{3,}", re.M)
POETIC_LABELS = [
    "field notes", "from the field", "loose plates", "selected work",
    "the archive", "in the wild", "notes from", "quietly trusted by",
    "quietly in use at",
]

# The dot family. Each entry is (regex, label, severity).
# Structural guesses for the most part, so most report as warnings and need
# eyes on the rendered page.
DOT_PATTERNS = [
    (r"animate-pulse[^\"\']*rounded-full|rounded-full[^\"\']*animate-pulse",
     "dot: pulsing status dot", "fail"),
    (r"\b(status|live|pulse|online|availability)[-_]?dot\b",
     "dot: status dot element", "warn"),
    (r"rounded-full[^\"\']*\bbg-(green|emerald|lime)-\d00\b|"
     r"\bbg-(green|emerald|lime)-\d00[^\"\']*rounded-full",
     "dot: green status dot", "warn"),
    (r"box-shadow[^;]*0\s+0\s+0\s+\d+px\s+rgba?\([^)]*\)[^;]*;?\s*.{0,40}border-radius\s*:\s*(50%|9999px|999px)",
     "dot: haloed status dot", "warn"),
    (r"radial-gradient\([^)]*circle[^)]*\)[^;]*;?[^}]{0,120}background-size|"
     r"bg-\[radial-gradient\([^\]]*circle",
     "dot: dot-grid background", "warn"),
    (r"#ff5f56|#ffbd2e|#27c9?3f|#28c840|#febc2e|#ff5f57",
     "dot: macOS traffic-light dots on fake browser chrome", "fail"),
    (r"\bcarousel-dots?\b|\bslider-dots?\b|\bdot-nav\b",
     "dot: carousel dots", "warn"),
]

# Decoration that is text by character count and ornament by function.
DECOR_TEXT = [
    (r"\bscroll to explore\b|\bscroll down\b|>\s*↓?\s*scroll\s*<",
     "decoration: scroll cue", "fail"),
    (r"\b(invite[- ]only preview|early access|coming soon)\b",
     "decoration: version or status pill", "warn"),
    (r">\s*(BETA|ALPHA|V\d+(\.\d+)*|v\d+\.\d+)\s*<",
     "decoration: version pill", "warn"),
    (r"\b\d{1,3} (spots?|seats?|slots?|places?) (left|remaining|open)\b|"
     r"\breservation \d+ of \d+\b|\bonly \d+ (spots?|seats?) \b",
     "decoration: manufactured scarcity", "fail"),
    (r"\d{1,2}:\d{2}\s*[·•]\s*-?\d{1,2}\s*°",
     "decoration: locale / time / weather strip", "fail"),
    (r"\b(plate|frame|field study|study) (no\.? ?)?\s*[IVX0-9]{1,4}\s*[·•]",
     "decoration: fake archival photo credit", "warn"),
    (r"\b(new|hot|popular|pro|beta)\b\s*(badge|pill|chip)\b|"
     r"(badge|pill|chip)[^\"\']*>\s*(✨|🔥|⚡)\s*(New|Hot|Popular)",
     "decoration: badge spam", "warn"),
]

# Surface and type failures that show up as recognizable code shapes.
SURFACE_PATTERNS = [
    (r"\bbg-(red|amber|yellow|green|blue|indigo)-\d00/\d{1,2}\b",
     "one-hue status box: same hue as border, text, and tint", "check-hue"),
    (r"(box-shadow|drop-shadow)\s*:[^;]*\b(4\d|[5-9]\d|\d{3,})px\b|"
     r"shadow-\[[^\]]*\b(4\d|[5-9]\d|\d{3,})px",
     "oversized drop shadow: blur 40px or wider", "warn"),
    (r"overflow-hidden[^\"\']*rounded-|rounded-[^\"\']*overflow-hidden",
     "border may die at the corner: radius on a clipping wrapper", "warn"),
    (r"bg-clip-text|background-clip\s*:\s*text|"
     r"-webkit-text-fill-color\s*:\s*transparent",
     "gradient headline text", "fail"),
    (r"repeating-linear-gradient", "gradient used as texture", "warn"),
    (r"letter-spacing\s*:\s*-0\.0[3-9]|tracking-tighter",
     "tracking crushed past the face", "warn"),
    (r"<(mark|u|s)\b(?![^>]*\bhref)", "drawing on the words for emphasis", "warn"),
    (r"transform-origin\s*:\s*(?!center|50%)",
     "spinner may wobble: transform-origin moved off centre", "warn"),
    (r"animate-spin[^\"\']*translate-|translate-[^\"\']*animate-spin",
     "spinner may wobble: centering inside the animated transform", "warn"),
    (r"font-family[^;]*\b(Playfair|Lora|Cormorant|Fraunces|Instrument Serif)\b",
     "display serif used where a text face belongs", "warn"),
    (r"\bgood (morning|afternoon|evening),?\s*\{",
     "editorial dashboard: a greeting used as an app headline", "warn"),
]

# Tailwind's stock semantic set, only a tell when several appear together.
SEMANTIC_SET = re.compile(r"\bbg-(blue|amber|yellow|green|red)-50\b")

PLACEHOLDER_BRANDS = [
    "Acme", "Acme Corp", "Nexus", "Vertex", "Lumina", "Cloudly",
    "SmartFlow", "Zenith Labs", "Globex", "Initech",
]

FAKE_PRECISION = [
    (r"\b99\.9[89]\s?%", "fake precision: 99.99%"),
    (r"\b\d\.\dx (faster|better|more|cheaper)\b", "fake precision: N.Nx faster"),
]

BANNED_FONTS = ["Inter", "Space Grotesk", "Roboto", "Geist", "Manrope",
                "Plus Jakarta Sans"]

PLACEHOLDER_NAMES = [
    "Sarah Johnson", "John Smith", "Michael Chen", "Emily Rodriguez",
    "Alex Thompson", "Jane Doe", "Sarah Chen", "David Kim",
]

ROUND_STATS = [
    (r"\b99\.9\s?%", "round-number stat: 99.9%"),
    (r"\b24/7\b", "round-number stat: 24/7"),
    (r"\b\d{1,3},000\+", "round-number stat: N,000+"),
    (r"\b\d0[MK]\+ (users|customers|downloads|developers)", "round-number stat"),
    (r"\b10x\b", "round-number stat: 10x"),
]

# Hue windows for the six recognized AI defaults. Only flagged when the color
# is saturated enough to read as an accent.
HUE_BANDS = [
    (238, 300, "indigo / violet / purple"),
    (180, 200, "cyan"),
    (35, 50, "amber"),
    (145, 165, "emerald"),
]

EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF✨⭐]"
)
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")


def hex_to_hsl(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    return hue * 360, sat, light


def iter_files(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
            for f in files:
                if os.path.splitext(f)[1].lower() in TEXT_EXT:
                    yield os.path.join(root, f)


def scan(path, approved=None):
    hits = []

    def add(line_no, category, detail, line, severity="fail"):
        hits.append({
            "file": path, "line": line_no, "category": category,
            "detail": detail, "severity": severity,
            "text": line.strip()[:110],
        })

    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
    except OSError as err:
        return [{"file": path, "line": 0, "category": "io", "detail": str(err),
                 "severity": "fail", "text": ""}]

    for i, line in enumerate(lines, 1):
        low = line.lower()

        if "—" in line or "&mdash;" in low or "&#8212;" in low:
            add(i, "copy", "em dash", line)
        if re.search(r"\s–\s", line) or "&ndash;" in low:
            add(i, "copy", "spaced en dash", line)

        for w in BANNED_WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                add(i, "copy", "banned word: " + w, line)
        for w in SOFT_WORDS:
            if re.search(r"\b" + re.escape(w) + r"(s|d|ing)?\b", low):
                add(i, "copy", "check figurative use: " + w, line, "warn")
        for w in SOFT_WORDS_EXTRA:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                add(i, "copy", "model-overproduced word: " + w, line, "warn")

        for rx, label in BANNED_PATTERNS:
            if re.search(rx, low):
                add(i, "copy", label, line)
        for rx, label, sev in FILLER_PATTERNS:
            if re.search(rx, low):
                add(i, "copy", label, line, sev)

        if EYEBROW_CLASS.search(line):
            add(i, "type", "eyebrow / kicker element", line, "warn")
            if MONO_CAPS.search(line):
                add(i, "type", "monospace all-caps eyebrow", line)
            if "·" in line or "•" in line or "&middot;" in low:
                add(i, "type", "eyebrow chrome: leading or separating dot", line)
        if "uppercase" in low and ("letter-spacing" in low or "tracking-" in low):
            add(i, "type", "eyebrow recipe: uppercase plus letter-spacing", line, "warn")
        if EYEBROW_NUMBER.search(re.sub(r"<[^>]+>", "", line)):
            add(i, "type", "section-number eyebrow: '01 / Capabilities'", line, "warn")
        for label in POETIC_LABELS:
            if label in low:
                add(i, "type", "poetic section label: " + label, line, "warn")

        # The dot family, plus the ornament that travels with it.
        dots = line.count("·") + line.count("•") + low.count("&middot;")
        if dots >= 2:
            add(i, "decoration",
                "middle dot as the default separator (%d on one line)" % dots, line)
        for rx, label, sev in DOT_PATTERNS:
            if re.search(rx, line, re.I):
                add(i, "decoration", label, line, sev)
        for rx, label, sev in DECOR_TEXT:
            if re.search(rx, line, re.I):
                add(i, "decoration", label, line, sev)

        for brand in PLACEHOLDER_BRANDS:
            if re.search(r"\b" + re.escape(brand) + r"\b", line):
                add(i, "copy", "placeholder company name: " + brand, line)
        for rx, label in FAKE_PRECISION:
            if re.search(rx, low):
                add(i, "copy", label, line, "warn")

        for rx, label, sev in SURFACE_PATTERNS:
            m = re.search(rx, line, re.I)
            if not m:
                continue
            if sev == "check-hue":
                # Only a tell when the tint, the text, and the border share a hue.
                hue = re.search(r"bg-([a-z]+)-\d00/", low)
                if hue and re.search(r"\btext-" + hue.group(1) + r"-\d00\b", low) \
                        and re.search(r"\bborder-" + hue.group(1) + r"-\d00\b", low):
                    add(i, "color", label, line)
                continue
            add(i, "color" if "gradient" in label or "hue" in label else "craft",
                label, line, sev)

        if "border-t" in low and "border-b" in low:
            add(i, "decoration", "top and bottom border on the same row", line, "warn")
        if re.search(r"hover:scale-1\d", low) and "transition-all" in low:
            add(i, "layout", "springy hover: scale plus transition-all", line, "warn")
        if re.search(r"cursor\s*:\s*url\(", low):
            add(i, "layout", "custom mouse cursor", line, "warn")
        m = re.search(r"\bbg-([a-z]+)-\d00/\d{1,2}\b", low)
        if m and re.search(r"\btext-" + m.group(1) + r"-\d00\b", low):
            add(i, "decoration", "icon tinted in a wash of its own color", line, "warn")
        for rx, label in ROUND_STATS:
            if re.search(rx, line):
                add(i, "copy", label, line, "warn")
        for name in PLACEHOLDER_NAMES:
            if name.lower() in low:
                add(i, "copy", "placeholder testimonial name: " + name, line)

        for f in BANNED_FONTS:
            if re.search(r"\b" + re.escape(f) + r"\b", line):
                add(i, "type", "banned typeface: " + f, line)
        if re.search(r"font-family[^;]*monospace", low) and re.search(
                r"\bbody\b|\bp\s*{|prose", low):
            add(i, "type", "monospace on body copy", line, "warn")

        for m in HEX.finditer(line):
            hexv = "#" + m.group(1)
            hue, sat, light = hex_to_hsl(hexv)
            if sat > 0.25 and 0.15 < light < 0.85:
                for lo, hi, label in HUE_BANDS:
                    if lo <= hue <= hi:
                        add(i, "color", "AI-default hue (%s): %s" % (label, hexv),
                            line, "fail" if label.startswith("indigo") else "warn")
            if approved is not None and hexv.upper() not in approved:
                add(i, "tokens", "raw hex outside the token set: " + hexv, line)

        if re.search(r"\b(indigo|violet|purple|fuchsia)-\d00\b", low):
            add(i, "color", "banned Tailwind color class", line)
        if "gradient" in low and re.search(
                r"purple|violet|indigo|fuchsia|cyan|#8[0-9a-f]{2}f|#6[0-9a-f]{2}f", low):
            add(i, "color", "purple or cyan gradient", line)
        if re.search(r"backdrop-filter\s*:\s*blur|backdrop-blur", low):
            add(i, "color", "glassmorphism", line)
        if re.search(r"(box-shadow|drop-shadow)\s*:", low) or "shadow-[" in low:
            for m in HEX.finditer(line):
                hue, sat, light = hex_to_hsl("#" + m.group(1))
                if sat > 0.3:
                    add(i, "color", "colored glow behind an element", line)
                    break
            if re.search(r"rgba?\(\s*\d+\s*,\s*\d+\s*,\s*\d+", low):
                nums = re.search(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", low)
                r, g, b = (int(x) for x in nums.groups())
                if max(r, g, b) - min(r, g, b) > 40:
                    add(i, "color", "colored glow behind an element", line)

        if re.search(r"border-l(eft)?(-\d)?\s*:\s*\d+px", low) or re.search(
                r'"[^"]*\bborder-l-\d', low):
            add(i, "layout", "colored left border on a card", line, "warn")
        if EMOJI.search(line) and re.search(r"<(span|div|li|p|h\d)|icon|className", line):
            add(i, "layout", "emoji standing in for an icon", line)
        if re.search(r"outline\s*:\s*(none|0)", low) and "focus-visible" not in low:
            add(i, "craft", "focus outline removed without replacement", line)
        if re.search(r"<img\b", low) and "alt=" not in low:
            add(i, "craft", "img without alt", line)

    # Markup-level: a short all-caps element immediately before a heading.
    # Spans lines, so it runs over the whole document rather than per line.
    doc = "\n".join(lines)
    eyebrow_lines = []
    for m in EYEBROW_MARKUP.finditer(doc):
        line_no = doc.count("\n", 0, m.start()) + 1
        eyebrow_lines.append(line_no)
        add(line_no, "type",
            "eyebrow label above a heading: " + m.group(2).strip(),
            lines[line_no - 1] if line_no <= len(lines) else "", "warn")

    # The eyebrow budget: at most one per three sections. A page with an
    # eyebrow on every section has, in effect, none.
    seen = set(eyebrow_lines)
    for m in EYEBROW_CLASS.finditer(doc):
        seen.add(doc.count("\n", 0, m.start()) + 1)
    eyebrows = len(seen)
    sections = len(re.findall(r"<section\b", doc, re.I)) or len(
        re.findall(r"<h2\b", doc, re.I))
    if sections >= 3 and eyebrows > -(-sections // 3):
        add(eyebrow_lines[0] if eyebrow_lines else 1, "type",
            "eyebrow budget: %d eyebrows across %d sections (cap is %d)"
            % (eyebrows, sections, -(-sections // 3)), "", "warn")

    # Three or more of the stock -50 semantic backgrounds together is the
    # framework's factory palette, which nobody picked.
    stock = set(SEMANTIC_SET.findall(doc))
    if len(stock) >= 3:
        add(1, "color",
            "framework's stock semantic palette: " + ", ".join(sorted(stock)),
            "", "warn")

    # A colored dot repeated down every row is confetti, not a signal.
    empty_dots = re.findall(
        r"<(?:span|div|i)\b[^>]*rounded-full[^>]*>\s*</(?:span|div|i)>", doc)
    if len(empty_dots) >= 3:
        add(1, "decoration",
            "a decorative dot on every row (%d empty round elements)"
            % len(empty_dots), "", "warn")

    # Three round elements carrying red, amber, and green within a short span
    # is a fake browser title bar.
    for m in re.finditer(r"rounded-full", doc):
        window = doc[m.start():m.start() + 320].lower()
        if (re.search(r"bg-red-\d00", window)
                and re.search(r"bg-(yellow|amber)-\d00", window)
                and re.search(r"bg-green-\d00", window)):
            line_no = doc.count("\n", 0, m.start()) + 1
            add(line_no, "decoration",
                "traffic-light dots on fake browser chrome",
                lines[line_no - 1] if line_no <= len(lines) else "")
            break

    return hits


def main():
    ap = argparse.ArgumentParser(description="Anti-slop audit, mechanical checks.")
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--tokens", help="tokens.json to check raw hex values against")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--strict", action="store_true", help="treat warnings as failures")
    args = ap.parse_args()

    approved = None
    if args.tokens:
        with open(args.tokens, encoding="utf-8") as fh:
            blob = fh.read()
        approved = {("#" + m.group(1)).upper() for m in HEX.finditer(blob)}

    hits = []
    for path in iter_files(args.paths):
        hits.extend(scan(path, approved))

    if args.as_json:
        print(json.dumps(hits, indent=2))
    else:
        fails = [h for h in hits if h["severity"] == "fail"]
        warns = [h for h in hits if h["severity"] == "warn"]
        for label, group in (("FAIL", fails), ("WARN", warns)):
            if not group:
                continue
            print("\n%s (%d)" % (label, len(group)))
            print("-" * 60)
            for h in group:
                print("%s:%s  [%s] %s" % (h["file"], h["line"], h["category"], h["detail"]))
                if h["text"]:
                    print("    %s" % h["text"])
        if not hits:
            print("No mechanical failures found.")
        print(
            "\nMechanical checks only. The judgment items (asymmetry, specific claims,"
            "\nempty / loading / error states, verified contrast) still need a human pass."
            "\nThe deletion test is one of them: strip every paragraph that is not a"
            "\nheading, a label, or a control, and see what the reader actually loses."
        )

    hard = [h for h in hits if h["severity"] == "fail" or args.strict]
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
