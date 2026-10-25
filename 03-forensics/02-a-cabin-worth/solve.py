#!/usr/bin/env python3
"""Recover and decrypt the deleted Joplin note from a SQLite WAL frame."""

import argparse
import base64
import hashlib
import re
import zipfile

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


FLAG_RE = re.compile(rb"POCTF\{[^}\r\n]+\}")
BLOB_RE = re.compile(rb"[A-Za-z0-9+/=]{1000,}")


def find_deleted_blob(wal):
    page_size = int.from_bytes(wal[8:12], "big")
    frame_size = 24 + page_size
    for offset in range(32, len(wal) - frame_size + 1, frame_size):
        page_number = int.from_bytes(wal[offset : offset + 4], "big")
        page = wal[offset + 24 : offset + frame_size]
        if page_number == 4 and b"Delacroix" in page:
            match = BLOB_RE.search(page)
            if match:
                return base64.b64decode(match.group())
    raise ValueError("deleted note ciphertext not found in WAL")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", help="downloaded Joplin ZIP")
    parser.add_argument("--password", default="horatio")
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as archive:
        wal_name = next(
            name for name in archive.namelist() if name.endswith("database.sqlite-wal")
        )
        blob = find_deleted_blob(archive.read(wal_name))

    salt, nonce, ciphertext = blob[:16], blob[16:28], blob[28:]
    key = hashlib.pbkdf2_hmac(
        "sha256", args.password.encode(), salt, 200_000, dklen=32
    )
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
    print(plaintext.decode())
    for flag in FLAG_RE.findall(plaintext):
        print(flag.decode())


if __name__ == "__main__":
    main()
