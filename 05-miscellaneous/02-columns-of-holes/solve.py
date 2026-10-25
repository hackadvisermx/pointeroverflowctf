#!/usr/bin/env python3
"""Decode the two Hollerith punchcards from Columns of Holes."""

import argparse
from pathlib import Path

from PIL import Image


ROW_CODES = (12, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
ROW_Y = (111, 153.5, 196.5, 239, 281, 323.5, 366.5, 409, 451, 493.5, 536.5, 579)


def hollerith_table():
    table = {(row,): str(row) for row in range(10)}
    for row, letter in enumerate("ABCDEFGHI", 1):
        table[tuple(sorted((12, row)))] = letter
    for row, letter in enumerate("JKLMNOPQR", 1):
        table[tuple(sorted((11, row)))] = letter
    for row, letter in enumerate("STUVWXYZ", 2):
        table[tuple(sorted((0, row)))] = letter
    table[(3, 8)] = "#"
    table[(2, 8)] = "?"
    return table


def decode_card(path: Path):
    image = Image.open(path).convert("L")
    table = hollerith_table()
    values = []

    for column in range(1, 81):
        x = 40.5 + 19 * column
        punched = []
        for row, y in zip(ROW_CODES, ROW_Y):
            crop = image.crop((round(x - 5), round(y - 10), round(x + 6), round(y + 11)))
            dark = sum(pixel < 80 for pixel in crop.getdata())
            if dark > 100:
                punched.append(row)
        key = tuple(sorted(punched))
        values.append(table.get(key, "?" if punched else " "))

    decoded = "".join(values)
    marker = decoded[40:42]
    start, stride = (int(marker[0]), int(marker[1]))
    payload = decoded[44:]
    fragment = payload[start::stride][:8]
    if len(fragment) != 8:
        raise ValueError(f"{path}: marker {marker!r} did not yield eight characters")
    return decoded, marker, payload, fragment


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("card_a", type=Path)
    parser.add_argument("card_b", type=Path)
    args = parser.parse_args()

    cards = [decode_card(args.card_a), decode_card(args.card_b)]
    for label, (_, marker, payload, fragment) in zip(("A", "B"), cards):
        print(f"{label}: PAT#{marker} payload={payload} fragment={fragment}")
    print(cards[0][3] + cards[1][3])


if __name__ == "__main__":
    main()
