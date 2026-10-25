#!/usr/bin/env python3
"""Solve the team-specific 7x7 Lights Out board."""

import argparse
import ast
import json
import re
from pathlib import Path


SIZE = 7


def toggle(board, row, col):
    for drow, dcol in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        new_row, new_col = row + drow, col + dcol
        if 0 <= new_row < SIZE and 0 <= new_col < SIZE:
            board[new_row * SIZE + new_col] ^= 1


def solve(bits, first_row):
    board = bits[:]
    clicks = []
    for col in range(SIZE):
        if (first_row >> col) & 1:
            toggle(board, 0, col)
            clicks.append({"r": 0, "c": col})
    for row in range(1, SIZE):
        for col in range(SIZE):
            if board[(row - 1) * SIZE + col]:
                toggle(board, row, col)
                clicks.append({"r": row, "c": col})
    if any(board[SIZE * (SIZE - 1) + col] for col in range(SIZE)):
        return None
    return clicks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path, help="saved authenticated challenge HTML")
    args = parser.parse_args()
    html = args.html.read_text()
    match = re.search(r"const initialBits = (\[[^;]+\]);", html)
    if not match:
        raise SystemExit("initialBits not found")
    bits = ast.literal_eval(match.group(1))
    clicks = next(
        (candidate for first in range(1 << SIZE) if (candidate := solve(bits, first))),
        None,
    )
    if clicks is None:
        raise SystemExit("no solution")
    print(json.dumps({"clicks": clicks}, separators=(",", ":")))
    print(f"presses: {len(clicks)}")


if __name__ == "__main__":
    main()
