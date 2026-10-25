#!/usr/bin/env python3
"""Padding-oracle solver for The Consulting Room.

The team token and ciphertext are intentionally supplied through environment
variables and are never written to the repository:

    POCTF_CONSULTING_TOKEN=... \
    POCTF_CONSULTING_RECORD=... \
    python3 solve.py

The endpoint documents a limit of 1,000 requests/minute.  The default pacing
uses 14 requests/second, with small concurrent batches.
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor


ORACLE_URL = "https://pointeroverflowctf.com/challenges/consulting-room/oracle"
BLOCK_SIZE = 16
REQUESTS_PER_SECOND = 5
WORKERS = 5
RETRIES = 6
BATCH_RETRIES = 10
CHECKPOINT_PATH = os.environ.get(
    "POCTF_CONSULTING_CHECKPOINT", "/tmp/poctf-consulting-progress.json"
)


def oracle(token: str, record: bytes) -> bool:
    request = urllib.request.Request(
        ORACLE_URL,
        data=json.dumps({"record": record.hex()}).encode(),
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read()) == {"padding": "valid"}
        except urllib.error.HTTPError as error:
            if error.code == 429 or error.code >= 500:
                time.sleep(2 + attempt)
                continue
            return False
        except urllib.error.URLError:
            time.sleep(2 + attempt)

    raise RuntimeError("Oracle unavailable after retries")


def query_batch(token: str, records: list[bytes]) -> list[bool]:
    for attempt in range(BATCH_RETRIES):
        try:
            with ThreadPoolExecutor(max_workers=WORKERS) as executor:
                return list(executor.map(lambda record: oracle(token, record), records))
        except RuntimeError:
            time.sleep(3 + attempt)
    raise RuntimeError("Oracle batch unavailable after retries")


def load_checkpoint() -> dict:
    try:
        with open(CHECKPOINT_PATH, encoding="utf-8") as checkpoint_file:
            return json.load(checkpoint_file)
    except FileNotFoundError:
        return {}


def save_checkpoint(checkpoint: dict) -> None:
    temporary_path = f"{CHECKPOINT_PATH}.tmp"
    with open(temporary_path, "w", encoding="utf-8") as checkpoint_file:
        json.dump(checkpoint, checkpoint_file)
    os.replace(temporary_path, CHECKPOINT_PATH)


def decrypt_block(
    token: str,
    blocks: list[bytes],
    block_index: int,
    checkpoint: dict,
) -> bytes:
    """Recover plaintext for one block using the preceding block as IV."""
    original_previous = blocks[block_index - 1]
    target = blocks[block_index]
    saved = checkpoint.get(str(block_index), {})
    intermediate = saved.get("intermediate", [None] * BLOCK_SIZE)
    plaintext = saved.get("plaintext", [None] * BLOCK_SIZE)

    for position in range(BLOCK_SIZE - 1, -1, -1):
        if intermediate[position] is not None:
            continue

        padding = BLOCK_SIZE - position
        prefix = blocks[: block_index - 1]
        candidates = []

        for guess in range(256):
            forged_previous = bytearray(original_previous)
            for suffix in range(position + 1, BLOCK_SIZE):
                forged_previous[suffix] = intermediate[suffix] ^ padding
            forged_previous[position] = guess
            candidates.append(b"".join(prefix + [bytes(forged_previous), target]))

        found = None
        for start in range(0, len(candidates), REQUESTS_PER_SECOND):
            batch = candidates[start : start + REQUESTS_PER_SECOND]
            results = query_batch(token, batch)

            for offset, valid in enumerate(results):
                if not valid:
                    continue

                guess = start + offset
                # Disambiguate the common last-byte false positive where the
                # untouched original ciphertext already has valid padding.
                if position == BLOCK_SIZE - 1:
                    check = bytearray(batch[offset])
                    check[-BLOCK_SIZE - 2] ^= 1
                    if not oracle(token, bytes(check)):
                        continue

                found = guess
                break

            if found is not None:
                break
            time.sleep(1 / REQUESTS_PER_SECOND)

        if found is None:
            raise RuntimeError(f"No padding candidate for block {block_index}, byte {position}")

        intermediate[position] = found ^ padding
        plaintext[position] = intermediate[position] ^ original_previous[position]
        checkpoint[str(block_index)] = {
            "intermediate": intermediate,
            "plaintext": plaintext,
        }
        save_checkpoint(checkpoint)
        print(
            f"block {block_index}/{len(blocks) - 1}, byte {position:02d}: "
            f"{plaintext[position]:02x} {chr(plaintext[position])!r}",
            flush=True,
        )

    return bytes(plaintext)


def main() -> int:
    token = os.environ.get("POCTF_CONSULTING_TOKEN")
    record_hex = os.environ.get("POCTF_CONSULTING_RECORD")
    if not token or not record_hex:
        print("Set POCTF_CONSULTING_TOKEN and POCTF_CONSULTING_RECORD", file=sys.stderr)
        return 2

    record = bytes.fromhex(record_hex)
    if len(record) % BLOCK_SIZE or len(record) < 2 * BLOCK_SIZE:
        raise ValueError("The record must contain at least two AES blocks")

    blocks = [record[index : index + BLOCK_SIZE] for index in range(0, len(record), BLOCK_SIZE)]
    checkpoint = load_checkpoint()
    recovered = []
    for block_index in range(len(blocks) - 1, 0, -1):
        recovered.append(decrypt_block(token, blocks, block_index, checkpoint))

    plaintext = b"".join(reversed(recovered))
    print("plaintext:", plaintext)
    print("plaintext (utf-8):", plaintext.rstrip(bytes([plaintext[-1]])).decode(errors="replace"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
