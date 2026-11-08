# The Apparatus, Ectograph (Forensics, 141 pts, Wave 6)

## Challenge Description

Elena Marchetti used Threshold, a privacy-focused messenger, for her research communications. Her data directory (SQLite + attachments + config) was recovered from her laptop. Ten conversations from the last two weeks are attached.

After Elena went silent at 2026-06-28 22:47, three messages were sent from her account — from a device that isn't one of her three registered devices. That device's id is a 16-char base32 token that this challenge treats as the team's nonce.

## Analysis

### Data Structure

The Threshold data directory contains:
- `threshold.db` — SQLite database with users, devices, threads, messages, etc.
- `config.json` — Client configuration
- `attachments/` — Voice memo transcript, images, PDFs
- `unaccounted_transmission.txt` — Anomalous binary blob with a cryptic message

### Database Analysis

The SQLite database contains:
- **users** — 13 users including Elena (`u_elena`) and her contacts
- **devices** — 28 devices including Elena's 3 registered devices:
  - `6XQDEDUHPWFMNMVE` — Elena's MacBook Pro
  - `GZSNOSIHIU62F773` — Elena's iPhone 15 Pro
  - `DWA2CYMFMTOEFMWK` — Elena's iPad
- **messages** — All messages from the last two weeks

### Key Finding

Querying messages from Elena's account after she went silent (2026-06-28 22:47 ≈ Unix timestamp 1719610020):

```sql
SELECT sender_device_id, sent_at, content FROM messages 
WHERE sender_id = 'u_elena' AND sent_at > 1719610020;
```

Three messages were sent from device `SSDGVDO6QGPAOJZ3` (not one of Elena's 3 registered devices):

1. `m_3iop2dsttood` (1719948000) — "You're right. Deleting. Please stop contacting me. I'm dropping the research. Delete everything I sent you."
2. `m_6uvmzfhhppen` (1719951600) — "Aldous, I've thought about it. I'm withdrawing from the program effective immediately..."
3. `m_4ziab7mxlikg` (1719962400) — "Ren I'm going up to Marion's for the weekend. Research overnight, phone off. Don't worry."

The device ID `SSDGVDO6QGPAOJZ3` is a 16-character base32 token, not matching any of Elena's three registered devices (`6XQDEDUHPWFMNMVE`, `GZSNOSIHIU62F773`, `DWA2CYMFMTOEFMWK`).

The `unaccounted_transmission.txt` contains a fragment: "The offering is placed and cannot be reclaimed. What is taken is taken in full."

The voice memo transcript from 2026-06-28 22:41 UTC (6 minutes before Elena went silent) states: "The hand is not the medium's. The signal comes from behind the wall. The pen has never left the drawer. The words were spoken in another room."

## Solution

The device ID `SSDGVDO6QGPAOJZ3` is the 16-character base32 token of the unauthorized device that sent messages after Elena went silent. This is the team's nonce/flag.

## Flag

`SSDGVDO6QGPAOJZ3` (or `POCTF{SSDGVDO6QGPAOJZ3}`)