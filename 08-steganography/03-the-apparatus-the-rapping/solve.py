#!/usr/bin/env python3
"""Decode the Morse-like knock timing in The Apparatus, The Rapping."""

from pathlib import Path
import struct
import sys
import wave


MORSE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "----.": "9", "---..": "8", "--...": "7",
    "-....": "6", "....-": "4",
}


def recover(path: str) -> str:
    with wave.open(str(Path(path)), "rb") as audio:
        if audio.getnchannels() != 1 or audio.getsampwidth() != 2:
            raise ValueError("expected mono 16-bit PCM")
        rate = audio.getframerate()
        samples = audio.readframes(audio.getnframes())

    values = struct.unpack(f"<{len(samples) // 2}h", samples)
    window = rate // 100  # 10 ms
    levels = []
    for start in range(0, len(values) - window + 1, window):
        chunk = values[start : start + window]
        levels.append((sum(sample * sample for sample in chunk) / window) ** 0.5)

    active = [level > 500 for level in levels]
    runs = []
    start = None
    for i, state in enumerate(active + [False]):
        if state and start is None:
            start = i
        elif not state and start is not None:
            runs.append((start, i))
            start = None

    letters = []
    current = ""
    for i, (begin, end) in enumerate(runs):
        if i and begin - runs[i - 1][1] >= 18:
            letters.append(current)
            current = ""
        current += "." if (end - begin) * 10 < 160 else "-"
    letters.append(current)
    return "".join(MORSE[letter] for letter in letters)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} recording.wav")
    print(recover(sys.argv[1]))
