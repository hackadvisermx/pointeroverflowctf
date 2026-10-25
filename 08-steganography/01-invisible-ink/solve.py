#!/usr/bin/env python3
"""Extract Invisible Ink's 7-bit trailing-whitespace carrier."""

from __future__ import annotations

import argparse
from pathlib import Path


def extract(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    chars: list[str] = []

    for index in range(0, 46, 2):
        if index >= len(lines):
            raise ValueError("the artifact has fewer than 46 lines")
        line = lines[index]
        trailer = line[len(line.rstrip(" \t")) :]
        bits = trailer[-7:]
        if len(bits) != 7 or any(char not in " \t" for char in bits):
            raise ValueError(f"line {index + 1} has no 7-bit carrier")
        value = int("".join("0" if char == " " else "1" for char in bits), 2)
        chars.append(chr(value))

    flag = "".join(chars)
    if not (flag.startswith("POCTF{") and flag.endswith("}")):
        raise ValueError(f"unexpected decoded value: {flag!r}")
    return flag


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    print(extract(args.artifact))


if __name__ == "__main__":
    main()
