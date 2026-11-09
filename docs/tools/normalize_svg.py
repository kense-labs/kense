#!/usr/bin/env python3
"""Normalise diagram SVG tokens before publishing.

Usage:
    python3 docs/tools/normalize_svg.py <file-or-dir> [<file-or-dir> ...]

Converges the scattered numeric values that accumulated across generators into
four type sizes, two line weights plus the arrow weight, and four corner radii.
Also makes marker ids unique per SVG file so several diagrams can be embedded
in one HTML page without cross-referencing each other's arrow heads.

Idempotent: running twice produces no further changes.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Four type sizes: caption / body / node title / sheet title.
FONT_TOKENS = ('10.5', '11', '12.5', '16')
# Container hairline and structural line. Arrow heads are handled separately.
LINE_TOKENS = ('0.9', '1.2')
ARROW_WEIGHT = '1.5'
# Small marker / block / large block / canvas.
RADIUS_TOKENS = ('2', '6', '8', '14')


def font(v: str) -> str:
    f = float(v)
    if f <= 10.8:
        return FONT_TOKENS[0]
    if f <= 11.5:
        return FONT_TOKENS[1]
    if f <= 13:
        return FONT_TOKENS[2]
    return FONT_TOKENS[3]


def weight(v: str) -> str:
    return LINE_TOKENS[0] if float(v) < 1.0 else LINE_TOKENS[1]


def radius(v: str) -> str:
    f = float(v)
    if f <= 3:
        return RADIUS_TOKENS[0]
    if f <= 7:
        return RADIUS_TOKENS[1]
    if f <= 10:
        return RADIUS_TOKENS[2]
    return RADIUS_TOKENS[3]


def unique_markers(text: str, stem: str) -> str:
    ids = set(re.findall(r'<marker id="([^"]+)"', text))
    for old in ids:
        if old.startswith(stem + '-'):
            continue
        new = f'{stem}-{old}'
        text = text.replace(f'<marker id="{old}"', f'<marker id="{new}"')
        text = text.replace(f'url(#{old})', f'url(#{new})')
    return text


def normalise(text: str, stem: str | None = None) -> tuple[str, int]:
    before = text
    text = re.sub(r'font-size="([\d.]+)"', lambda m: f'font-size="{font(m.group(1))}"', text)
    text = re.sub(r'stroke-width="([\d.]+)"', lambda m: f'stroke-width="{weight(m.group(1))}"', text)
    text = re.sub(r'\brx="([\d.]+)"', lambda m: f'rx="{radius(m.group(1))}"', text)
    # Arrow heads keep a slightly heavier stroke than structural lines.
    text = re.sub(
        r'(<path d="M2 1L8 5L2 9"[^>]*?stroke-width=")[\d.]+(")',
        lambda m: m.group(1) + ARROW_WEIGHT + m.group(2),
        text,
    )
    if stem:
        text = unique_markers(text, stem)
    if 'role="img"' not in text and '<svg ' in text:
        text = re.sub(r'(<svg [^>]*?)(>)', r'\1 role="img"\2', text, count=1)
    return text, 0 if text == before else 1


def main(argv: list[str]) -> int:
    targets: list[Path] = []
    for arg in argv[1:]:
        p = Path(arg)
        if p.is_dir():
            targets += sorted(q for q in p.rglob('*') if q.suffix in ('.svg', '.html', '.py'))
        elif p.is_file():
            targets.append(p)

    changed = 0
    for p in targets:
        if 'node_modules' in str(p) or '/.git/' in str(p) or p.name == 'normalize_svg.py':
            continue
        try:
            original = p.read_text()
        except (UnicodeDecodeError, OSError):
            continue
        stem = p.stem if p.suffix == '.svg' else None
        out, hit = normalise(original, stem)
        if hit:
            p.write_text(out)
            changed += 1
            print(f'  normalised {p}')
    print(f'{changed}/{len(targets)} files changed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
