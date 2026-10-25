#!/usr/bin/env python3
"""Recover Panoptican's authorization string from the stripped ELF."""

from pathlib import Path
import sys


MASK_OFFSET = 0x2070
REFERENCE_OFFSET = 0x20F0
REFERENCE_SIZE = 0x400
AUTH_SIZE = 0x80


def recover(binary: bytes) -> str:
    reference = binary[REFERENCE_OFFSET : REFERENCE_OFFSET + REFERENCE_SIZE]
    mask = binary[MASK_OFFSET : MASK_OFFSET + AUTH_SIZE]
    if len(reference) != REFERENCE_SIZE or len(mask) != AUTH_SIZE:
        raise ValueError("unexpected Panoptican artifact size/layout")
    authorization = bytes(
        pixel ^ key for pixel, key in zip(reference[:AUTH_SIZE], mask)
    )
    return authorization.split(b"\0", 1)[0].decode("ascii")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} panoptican")
    print(recover(Path(sys.argv[1]).read_bytes()))

