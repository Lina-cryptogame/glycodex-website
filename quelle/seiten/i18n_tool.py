"""Textsegmente aus den erzeugten Seiten herausziehen und Übersetzungen einsetzen.

Ein Segment ist das innere HTML des obersten Elements, das direkten Text enthält.
SVG-Teile darin werden durch Platzhalter ⟦n⟧ ersetzt, damit Übersetzungen sie nicht anfassen.
Die nachgebaute App-Oberfläche (.phone-live) bleibt deutsch, wie die Screenshots.
"""
import json
import re
from html.parser import HTMLParser

VOID = {"br", "img", "input", "meta", "link", "hr", "source", "wbr"}
SKIP_TAGS = {"style", "script", "svg", "helmet", "title"}
ATTRS = ("alt", "aria-label", "title", "placeholder")
SVG_RE = re.compile(r"<svg\b.*?</svg>", re.S)


class Node:
    __slots__ = ("tag", "attrs", "start", "inner_start", "inner_end", "end", "children", "texts")

    def __init__(self, tag, attrs, start, inner_start):
        self.tag, self.attrs, self.start, self.inner_start = tag, attrs, start, inner_start
        self.inner_end = self.end = None
        self.children, self.texts = [], []


class P(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.src = src
        self.lines = [0]
        for m in re.finditer("\n", src):
            self.lines.append(m.end())
        self.root = Node("#root", [], 0, 0)
        self.stack = [self.root]

    def pos(self):
        ln, col = self.getpos()
        return self.lines[ln - 1] + col

    def handle_starttag(self, tag, attrs):
        s = self.pos()
        raw = self.get_starttag_text()
        n = Node(tag, attrs, s, s + len(raw))
        self.stack[-1].children.append(n)
        if tag in VOID:
            n.inner_end = n.end = s + len(raw)
        else:
            self.stack.append(n)

    def handle_startendtag(self, tag, attrs):
        s = self.pos()
        raw = self.get_starttag_text()
        n = Node(tag, attrs, s, s + len(raw))
        n.inner_end = n.end = s + len(raw)
        self.stack[-1].children.append(n)

    def handle_endtag(self, tag):
        s = self.pos()
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                for n in self.stack[i:]:
                    n.inner_end = s
                    n.end = self.src.index(">", s) + 1
                del self.stack[i:]
                return

    def handle_data(self, data):
        if data.strip():
            self.stack[-1].texts.append(data)

    handle_entityref = lambda self, name: self.stack[-1].texts.append("&" + name + ";")
    handle_charref = lambda self, name: self.stack[-1].texts.append("&#" + name + ";")


def body_range(src):
    a = src.index("</helmet>")
    b = src.index("</x-dc>")
    return a, b


def is_live(n):
    for k, v in n.attrs:
        if k == "class" and v and ("phone-live" in v.split()):
            return True
    return False


def collect(src, skip=None):
    """Liefert (spans, attrs): spans = [(start, end, text)], attrs = [(start, end, text)]."""
    a, b = body_range(src)
    p = P(src)
    p.feed(src)
    spans, attrs = [], []

    def has_text(n):
        return any(t.strip() for t in n.texts)

    def walk(n):
        if n.tag in SKIP_TAGS or is_live(n):
            return
        if n.start < a or (n.end or 0) > b:
            if n.tag != "#root":
                for c in n.children:
                    walk(c)
                return
        if skip and skip[0] <= n.start < skip[1]:
            return
        # Attribute
        if n.tag != "#root":
            raw = src[n.start:n.inner_start]
            for at in ATTRS:
                m = re.search(r'\s' + at + r'="([^"]*)"', raw)
                if m and m.group(1).strip() and "{{" not in m.group(1):
                    attrs.append((n.start + m.start(1), n.start + m.end(1), m.group(1)))
        if n.tag != "#root" and has_text(n) and n.inner_end is not None:
            spans.append((n.inner_start, n.inner_end, src[n.inner_start:n.inner_end]))
            return
        for c in n.children:
            walk(c)

    walk(p.root)
    return spans, attrs


def mask(text):
    """SVG durch ⟦n⟧ ersetzen. Gibt (maskiert, liste) zurück."""
    svgs = []

    def rep(m):
        svgs.append(m.group(0))
        return "⟦%d⟧" % (len(svgs) - 1)

    return SVG_RE.sub(rep, text), svgs


def unmask(text, svgs):
    for i, s in enumerate(svgs):
        text = text.replace("⟦%d⟧" % i, s)
    return text


def norm(t):
    return re.sub(r"\s+", " ", t).strip()


def segments(src, skip=None):
    spans, attrs = collect(src, skip)
    out = []
    for s, e, t in spans:
        m, _ = mask(t)
        out.append(norm(m))
    for s, e, t in attrs:
        out.append(norm(t))
    return out


def apply(src, table, skip=None, missing=None):
    spans, attrs = collect(src, skip)
    edits = []
    for s, e, t in spans:
        m, svgs = mask(t)
        key = norm(m)
        if key in table:
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            edits.append((s, e, lead + unmask(table[key], svgs) + trail))
        elif missing is not None:
            missing.append(key)
    for s, e, t in attrs:
        key = norm(t)
        if key in table:
            edits.append((s, e, table[key].replace('"', "&quot;")))
        elif missing is not None:
            missing.append(key)
    edits.sort(key=lambda x: x[0], reverse=True)
    last = None
    for s, e, t in edits:
        if last is not None and e > last:
            continue  # verschachtelt: äußeres hat Vorrang (kommt in Sortierung später)
        src = src[:s] + t + src[e:]
        last = s
    return src
