#!/usr/bin/env python3
"""Recover the flag encoded by adjacent commit timestamp deltas."""

from pathlib import Path
import subprocess
import sys
import tempfile


def recover(bundle: str) -> str:
    with tempfile.TemporaryDirectory(prefix="commit-to-memory-") as work:
        subprocess.run(
            ["git", "clone", "--quiet", str(Path(bundle).resolve()), work],
            check=True,
        )
        raw = subprocess.check_output(
            ["git", "-C", work, "log", "origin/main", "--reverse", "--format=%ct"],
            text=True,
        )
    timestamps = [int(line) for line in raw.splitlines()]
    deltas = [b - a for a, b in zip(timestamps, timestamps[1:])]
    flag = bytes(deltas).decode("ascii")
    if not flag.startswith("POCTF{") or not flag.endswith("}"):
        raise ValueError("timestamp deltas did not produce a POCTF flag")
    return flag


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} commits.bundle")
    print(recover(sys.argv[1]))
