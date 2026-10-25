#!/usr/bin/env python3
"""Sign in to Poisoned Well and ask its verification endpoint for the nonce."""

import json
import sys
import requests


def main(token: str) -> None:
    base = "https://poisoned-well.pointeroverflowctf.com"
    session = requests.Session()
    result = session.post(f"{base}/login", data={"token": token})
    result.raise_for_status()
    result = session.get(f"{base}/")
    result.raise_for_status()
    result = session.get(f"{base}/verify")
    result.raise_for_status()
    print(json.dumps(result.json(), indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} POISON1-token")
    main(sys.argv[1])
