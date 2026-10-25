#!/usr/bin/env python3
"""Extract a POCTF flag from the supplied Firefox profile archive."""

import argparse
import re
import zipfile


FLAG_RE = re.compile(rb"POCTF\{[^}\r\n]+\}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="downloaded left-open-profile.zip")
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as archive:
        for name in archive.namelist():
            matches = FLAG_RE.findall(archive.read(name))
            for match in matches:
                print(f"{name}: {match.decode()}")


if __name__ == "__main__":
    main()
