#!/usr/bin/env python3
"""Recover the three-constant XOR result from The Disassembled Mind."""

from pathlib import Path
import marshal
import sys
import types


def find_check(module: types.CodeType) -> types.CodeType:
    for value in module.co_consts:
        if isinstance(value, types.CodeType) and value.co_name == "check":
            return value
    raise ValueError("check() code object not found")


def recover(pyc: bytes) -> str:
    if len(pyc) < 16:
        raise ValueError("truncated pyc")
    module = marshal.loads(pyc[16:])
    check = find_check(module)
    blobs = [value for value in check.co_consts if isinstance(value, bytes)]
    if len(blobs) != 5 or len({len(value) for value in blobs}) != 1:
        raise ValueError("unexpected constant layout")
    enc1, _a, enc2, key2, _b = blobs
    return bytes(a ^ b ^ key for a, b, key in zip(enc1, enc2, key2)).decode("ascii")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} program.pyc")
    print(recover(Path(sys.argv[1]).read_bytes()))

