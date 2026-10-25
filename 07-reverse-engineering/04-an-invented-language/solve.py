#!/usr/bin/env python3
"""Emulate the relevant PUSH/XOR/store subset of prog.bin."""

from pathlib import Path
import sys


def recover(program: bytes) -> str:
    memory = bytearray(256)
    stack = []
    pc = 0
    while pc < len(program):
        op = program[pc]
        pc += 1
        if op == 0x01:
            stack.append(int.from_bytes(program[pc : pc + 4], "little"))
            pc += 4
        elif op == 0x07:
            right = stack.pop()
            left = stack.pop()
            stack.append(left ^ right)
        elif op == 0x0B:
            address = stack.pop() & 0xFF
            memory[address] = stack.pop() & 0xFF
        elif op == 0x0D:
            break
        else:
            raise ValueError(f"unexpected opcode 0x{op:02x} at {pc - 1}")
    return bytes(memory).split(b"\0", 1)[0].decode("ascii")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} prog.bin")
    print(recover(Path(sys.argv[1]).read_bytes()))

