#!/usr/bin/env python3
"""Recover the split UTF-16 session token from a Windows minidump."""

import argparse
import re
import zipfile


UTF16_RUN_RE = re.compile(rb"(?:(?:[\x20-\x7e])\x00){4,}")
TOKEN_RE = re.compile(r"^[A-Z2-7]{8}$")


def utf16_runs(data):
    for match in UTF16_RUN_RE.finditer(data):
        yield match.group().decode("utf-16le")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="downloaded minidump ZIP")
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as archive:
        dump_name = next(name for name in archive.namelist() if name.endswith(".dmp"))
        runs = list(utf16_runs(archive.read(dump_name)))

    first = next(
        run.split("sessionRestoreToken:", 1)[1]
        for run in runs
        if "sessionRestoreToken:" in run
    )
    second = next(
        run.split("|expires:", 1)[0] for run in runs if "|expires:" in run
    )
    if not TOKEN_RE.fullmatch(first) or not TOKEN_RE.fullmatch(second):
        raise ValueError("unexpected token fragments")
    print(first + second)


if __name__ == "__main__":
    main()
