#!/usr/bin/env python3
"""Recover Velocity's 16-hex-digit nonce from the MIDI note velocities."""

from pathlib import Path
import struct
import sys


def read_vlq(data: bytes, pos: int) -> tuple[int, int]:
    value = 0
    while True:
        byte = data[pos]
        pos += 1
        value = (value << 7) | (byte & 0x7F)
        if not byte & 0x80:
            return value, pos


def track_data(midi: bytes) -> bytes:
    if midi[:4] != b"MThd":
        raise ValueError("not a MIDI file")
    header_len = struct.unpack(">I", midi[4:8])[0]
    pos = 8 + header_len
    if midi[pos : pos + 4] != b"MTrk":
        raise ValueError("expected a MIDI track")
    length = struct.unpack(">I", midi[pos + 4 : pos + 8])[0]
    return midi[pos + 8 : pos + 8 + length]


def recover(path: str) -> str:
    data = track_data(Path(path).read_bytes())
    pos = 0
    running_status = None
    bits = []

    while pos < len(data):
        _, pos = read_vlq(data, pos)
        status = data[pos]
        if status < 0x80:
            if running_status is None:
                raise ValueError("running status without a previous event")
            status = running_status
        else:
            pos += 1
            if status < 0xF0:
                running_status = status

        if status == 0xFF:
            pos += 1
            length, pos = read_vlq(data, pos)
            pos += length
        elif status in (0xF0, 0xF7):
            length, pos = read_vlq(data, pos)
            pos += length
        else:
            event = status & 0xF0
            size = 1 if event in (0xC0, 0xD0) else 2
            if status >= 0x80:
                first = data[pos]
                pos += 1
            else:
                first = status
            if size == 2:
                second = data[pos]
                pos += 1
            else:
                second = None
            if event == 0x90 and size == 2 and second:
                bits.append("1" if second >= 0x60 else "0")

    if len(bits) != 64:
        raise ValueError(f"expected 64 note-on events, got {len(bits)}")
    return "".join(f"{int(''.join(bits[i:i+4]), 2):X}" for i in range(0, 64, 4))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} etude.mid")
    print(recover(sys.argv[1]))
