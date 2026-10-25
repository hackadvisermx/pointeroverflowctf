#!/usr/bin/env python3
"""Extract the 16-bit candidate from The Hidden Path's specimen SVG.

The artifact contains sixteen house outlines.  In each outline the final
vertical endpoint is deliberately above or below the roof apex.  Treating an
endpoint above the apex as 0 and one below it as 1, in row-major order, gives
four hexadecimal digits.  The script prints both the raw hexadecimal value
and its Unicode code point representation; the target page accepts a raw
nonce, so validation must be done against the official challenge endpoint.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


PATH_RE = re.compile(
    r'<path\s+fill="none"[^>]*\sd="M\s*[-.0-9]+\s+[-.0-9]+'
    r'\s+L\s*[-.0-9]+\s+[-.0-9]+'
    r'\s+L\s*[-.0-9]+\s+(?P<right>[-.0-9]+)'
    r'\s+L\s*[-.0-9]+\s+(?P<apex>[-.0-9]+)',
)


def recover(svg: str) -> tuple[str, str, list[tuple[float, float]]]:
    measurements = [
        (float(m.group("right")), float(m.group("apex")))
        for m in PATH_RE.finditer(svg)
    ]
    if len(measurements) != 16:
        raise ValueError(f"expected 16 glyph paths, found {len(measurements)}")

    # The SVG/PDF coordinate system is inverted vertically, so a numerically
    # smaller endpoint is visually higher.  0 = higher, 1 = lower.
    bits = "".join("0" if right < apex else "1" for right, apex in measurements)
    value = int(bits, 2)
    return bits, f"{value:04X}", measurements


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("specimen.svg")
    bits, nonce, measurements = recover(path.read_text(encoding="utf-8"))
    print(f"right/apex pairs: {measurements}")
    print(f"bits: {bits}")
    print(f"nonce: {nonce}")
    print(f"unicode: U+{nonce} ({chr(int(nonce, 16))})")


if __name__ == "__main__":
    main()
