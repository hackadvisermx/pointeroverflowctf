#!/usr/bin/env python3
"""Reproduce the Leap of Faith game-client API flow."""

import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen


BASE_URL = "https://pointeroverflowctf.com/api/challenges/47"


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

    game_token = (args.credentials_dir / "game.token").read_text().strip()
    team_key = (args.credentials_dir / "team.key").read_text().strip()
    headers = {
        "X-POCTF-GAME-TOKEN": game_token,
        "X-POCTF-TEAM-KEY": team_key,
        "User-Agent": "POCTF2026-client",
    }

    instance = request_json(f"{BASE_URL}/instance", headers)
    nonce = instance["nonce"]
    complete_headers = {**headers, "X-POCTF-CHALLENGE-NONCE": nonce}
    result = request_json(f"{BASE_URL}/complete", complete_headers, method="POST")
    print(result["marker"])


if __name__ == "__main__":
    main()
