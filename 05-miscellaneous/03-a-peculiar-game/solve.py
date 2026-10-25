#!/usr/bin/env python3
"""Decode the non-chess board encoding from A Peculiar Game."""

MOVES = (
    "g4", "d3", "a4", "e3", "f4", "f4", "f4", "a3",
    "e3", "c3", "e4", "e3", "a4", "f4", "d4", "d3",
)


def decode(moves):
    values = []
    for move in moves:
        file_index = ord(move[0].lower()) - ord("a")
        rank_bit = int(move[1]) - 3
        if not 0 <= file_index < 7 or rank_bit not in (0, 1):
            raise ValueError(f"unexpected destination: {move}")
        values.append(file_index * 2 + rank_bit)
    return "".join(f"{value:X}" for value in values)


if __name__ == "__main__":
    print(decode(MOVES))
