#!/usr/bin/env python3
"""
The Apparatus, Ectograph — POCTF 2026 Forensics (Wave 6, 141 pts)

Recovers the unauthorized device ID from Elena's Threshold data directory.

The challenge: After Elena went silent at 2026-06-28 22:47, three messages were sent
from her account from a device that isn't one of her three registered devices.
Find the 16-char base32 device ID.
"""

import sqlite3
import json
from pathlib import Path

def solve(data_dir: str = ".") -> str:
    """Find the unauthorized device ID from Threshold data."""
    db_path = Path(data_dir) / "elena-threshold-data" / "threshold.db"
    if not db_path.exists():
        db_path = Path(data_dir) / "threshold.db"
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Elena's user ID
    elena_id = "u_elena"
    
    # Elena's registered devices (from challenge description: 3 devices)
    registered_devices = {
        '6XQDEDUHPWFMNMVE',  # Elena's MacBook Pro
        'GZSNOSIHIU62F773',  # Elena's iPhone 15 Pro
        'DWA2CYMFMTOEFMWK',  # Elena's iPad
    }
    print(f"Elena's registered devices: {registered_devices}")
    
    # Find messages from Elena after she went silent (2026-06-28 22:47 UTC)
    silence_timestamp = 1719610020  # 2026-06-28 22:47 UTC
    
    cursor.execute("""
        SELECT sender_device_id, sent_at, content 
        FROM messages 
        WHERE sender_id = ? AND sent_at > ?
        ORDER BY sent_at
    """, (elena_id, silence_timestamp))
    
    messages = cursor.fetchall()
    print(f"\nMessages from Elena after silence:")
    for device_id, sent_at, content in messages:
        print(f"  Device: {device_id}, Time: {sent_at}, Content: {content[:80]}...")
    
    # Find device IDs not in registered set
    unauthorized_devices = set()
    for device_id, sent_at, content in messages:
        if device_id not in registered_devices:
            unauthorized_devices.add(device_id)
    
    conn.close()
    
    if len(unauthorized_devices) == 1:
        return unauthorized_devices.pop()
    elif len(unauthorized_devices) > 1:
        print(f"Multiple unauthorized devices found: {unauthorized_devices}")
        return list(unauthorized_devices)[0]
    else:
        return None


if __name__ == "__main__":
    import sys
    data_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    device_id = solve(data_dir)
    if device_id:
        print(f"\nUnauthorized device ID (flag): {device_id}")
        print(f"Flag: POCTF{{{device_id}}}")
    else:
        print("No unauthorized device found")
        sys.exit(1)