#!/usr/bin/env python3
"""Reproduce the unchecked completion flow for challenge 48."""

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen


BASE_URL = "https://pointeroverflowctf.com/api/challenges/48"


def request_json(url, headers, method="GET"):
    request = Request(url, headers=headers, method=method)
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--credentials-dir",
        type=Path,
        default=Path("."),
        help="directory containing game.token and team.key",
    )
    args = parser.parse_args()

    headers = {
        "X-POCTF-GAME-TOKEN": (args.credentials_dir / "game.token").read_text().strip(),
        "X-POCTF-TEAM-KEY": (args.credentials_dir / "team.key").read_text().strip(),
        "User-Agent": "POCTF2026-client",
    }
    instance = request_json(f"{BASE_URL}/instance", headers)
    headers["X-POCTF-CHALLENGE-NONCE"] = instance["nonce"]
    result = request_json(f"{BASE_URL}/complete", headers, method="POST")
    print(result["marker"])


if __name__ == "__main__":
    main()
