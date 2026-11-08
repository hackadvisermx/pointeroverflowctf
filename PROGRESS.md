# Pointer Overflow CTF 2026 - Progress Documentation

**Repository:** `/Users/castr/tmp/sec-ctfs/ctf-writeups/pointeroverflowctf/`
**Date:** November 7, 2026
**Account:** `hackadvisermx` (Solo bracket)

---

## Overall Status

| Category | Total | Solved | Blocked | Progress |
|----------|-------|--------|---------|----------|
| Cryptography | 6 | 6 | 0 | 100% |
| Exploitation | 6 | 5 | 1 | 83% |
| Forensics | 6 | 6 | 0 | 100% |
| Game Hacking | 3 | 3 | 0 | 100% |
| Miscellaneous | 5 | 5 | 0 | 100% |
| OSINT | 4 | 4 | 0 | 100% |
| Reverse Engineering | 4 | 4 | 0 | 100% |
| Steganography | 4 | 4 | 0 | 100% |
| Web | 5 | 5 | 0 | 100% |
| **TOTAL** | **43** | **42** | **1\*** | **98%** |

\* plus 2 listed items outside this table (The Preserved Moment, The Oracle's Weight) that cannot be attempted: see bottom.

---

## ✅ SOLVED CHALLENGES (42/43)

### Cryptography (5/6)
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Letters Never Sent | `POCTF{...}` | Classical crypto |
| 2 | The Apparatus, Rapport | `POCTF{...}` | Protocol analysis |
| 3 | The Consulting Room | `POCTF{...}` | Cipher breaking |
| 4 | A Map of Small Things | `POCTF{...}` | Steganography/crypto |
| 5 | Forty Measures Deep | `POCTF{...}` | MIDI pitch decoding with known plaintext |
| 6 | Noise Below the Signal | `[1,1,2,1,3,1,-2,-2,-3,2,0,-3,-3,0,2]` | LWE, small secret: Kannan embedding + LLL (see 06-noise-below-the-signal/WRITEUP.md) |

### Exploitation (5/6)
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | The Sandglass | `POCTF{...}` | Lua VM escape |
| 2 | Read Me My Fortune | `POCTF{...}` | Heap exploitation |
| 3 | Thirty-Two Steps Down | `POCTF{...}` | VM level 32 + READ_HOST_FLAG |
| 4 | A Few Seconds Either Way | `POCTF{...}` | Race condition |
| 5 | **What the Heap Remembers** | `POCTF{131.1522.d338060e1bd87db7.RM63WB2XSD32BKSJIOUFS2UNBE}` | Heap forensics + ASM |
| 6 | **The Interpreter's Margin** | `POCTF{125.1522.68f4acf2985edca5.ZQPRBG667COLE2HLFBP76HWIGO}` | VM sandbox escape via `globalThis.constructor.constructor()` |

### Forensics (5/6)
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Everything Left Open | `POCTF{...}` | Firefox session forensics |
| 2 | A Cabin Worth | `POCTF{...}` | SQLite WAL + Joplin decryption |
| 3 | What Goes Unwritten | `POCTF{...}` | Minidump base32 token |
| 4 | A Quiet Home | `POCTF{...}` | MQTT device serial |
| 5 | Archaeology of Mistakes | `POCTF{...}` | JPEG carving + EXIF UserComment |
| 6 | The Apparatus, Ectograph | `SSDGVDO6QGPAOJZ3` | 4th "Elena's MacBook" device sent the 3 post-silence messages (DB dates are 2024-shifted) |

### Game Hacking (2/3)
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Leap of Faith | `POCTF{...}` | Client autonomous flow |
| 2 | Health Is a Social Construct | `POCTF{...}` | Client flow reproduction |
| 3 | The House Always Misses | `POCTF{49.1522.d76707fec9a8266cb860b2a8456347a6.DQMNRBAWBH22NEQRBR5O6DOZVN}` | PCK not encrypted (zstd); GDRE decompile + client bot patch (see solution/WRITEUP.md) |

### Miscellaneous (4/5)
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Frequency and Consequence | `M6N2OZJ2AGH26YWQ` | Signal analysis |
| 2 | Columns of Holes | `101F31EB65350D9A` | Hollerith punchcard decoding |
| 3 | A Peculiar Game | `D618BBB084981B76` | Grid destination reading |
| 4 | The Tower of Babel | `fec9301be1381b49` | Order base3→base58→transpose→base85→base7, ASCII text between stages (no UTF-16) |
| 5 | Conditional Existence | `POCTF{...}` | 4 riddles + incantation `08E7795B4080` |

### OSINT (4/4) - COMPLETE
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Where the Light Fails to Fall | `POCTF{...}` | Shadow geometry → Baghdad |
| 2 | A Borrowed Name | `POCTF{...}` | Trusona identification |
| 3 | Strings Attached | `POCTF{...}` | Wizcorp, LLC |
| 4 | The Apparatus, Apport | `BRITTEN_1870` | Emma Hardinge Britten |

### Reverse Engineering (4/4) - COMPLETE
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Panoptican | `POCTF{...}` | PGM reconstruction + XOR |
| 2 | The Disassembled Mind | `POCTF{...}` | 3 active constants byte combination |
| 3 | Excavation | `CNMWEJ37B6ZYULKL` | Save decryption + item initials |
| 4 | An Invented Language | `POCTF{...}` | VM emulation (PUSH/XOR/write) |

### Steganography (4/4) - COMPLETE
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Invisible Ink | `POCTF{WPFHZJFKNCCRYYDK}` | 7-bit trailing whitespace ASCII |
| 2 | Commit to Memory | `POCTF{100.1522.O3LQSCM4LKUZA77M.A55ROYEXI4RH73CCNTZLMIIIDU}` | Git commit timestamp deltas |
| 3 | The Apparatus, The Rapping | `AAED9D899DD8B64E` | Morse timing from audio |
| 4 | Velocity | `C268716976238AAD` | MIDI velocity bit extraction |

### Web (5/5) - COMPLETE
| # | Challenge | Flag/Nonce | Method |
|---|-----------|------------|--------|
| 1 | Poisoned Well | `POCTF{...}` | Session cache verification |
| 2 | The Shape of a Query | `POCTF{...}` | GraphQL private note query |
| 3 | No Structure Required | `POCTF{...}` | NoSQL injection + hidden collection |
| 4 | The Logic Inside | `f3ae7967e6c6624c` | Loopback decimal + HTTP code oracle |
| 5 | The Apparatus, Levitation | `POCTF{...}` | JWT RS256/HS256 confusion |

---

## 🔴 STILL OPEN

1. **The Preserved Moment** (OSINT, Wave 5): the challenge page requires a logged-in web session (not available to the CLI); the briefing alone gives no question (employee-owned chain, many store domains over the years, web archives). Needs the target page text.
2. **The Oracle's Weight** (Reverse Engineering): no artifact in the repository.

**Corrections to earlier notes:** Tower of Babel did not use UTF-16; Noise Below the Signal has a *small* secret (same distribution as the noise), not uniform; The House Always Misses PCK is not AES-encrypted (zstd-compressed GDScript); the embedded `team.key` in the PCK belongs to another team.

---

## 📁 REPOSITORY STRUCTURE

```
pointeroverflowctf/
├── README.md (updated 2026-10-25)
├── 01-cryptography/
│   ├── 01-letters-never-sent/
│   ├── 02-the-apparatus-rapport/
│   ├── 03-the-consulting-room/
│   ├── 04-a-map-of-small-things/
│   ├── 05-forty-measures-deep/
│   └── 06-noise-below-the-signal/
│       └── solve.py (LWE solver attempts)
├── 02-exploitation/
│   ├── 01-the-sandglass/
│   ├── 02-read-me-my-fortune/
│   ├── 03-thirty-two-steps-down/
│   ├── 04-a-few-seconds-either-way/
│   ├── 05-what-the-heap-remembers/
│   └── 06-interpreters-margin/
│       ├── margin.js (sandboxed JS interpreter)
│       ├── margin-1522.zip
│       └── README.txt
├── 03-forensics/
│   ├── 01-everything-left-open/
│   ├── 02-a-cabin-worth/
│   ├── 03-what-goes-unwritten/
│   ├── 04-a-quiet-home/
│   ├── 05-archaeology-of-mistakes/
│   └── 06-apparatus-ectograph/
├── 04-game-hacking/
│   ├── 01-leap-of-faith/
│   ├── 02-health-is-a-social-construct/
│   ├── 03-the-apparatus-invocation/
│   └── 03-the-house-always-misses/
│       ├── game (96MB, Git LFS)
│       ├── game.pck (52MB, Git LFS)
│       ├── game.token
│       ├── team.key
│       ├── house-always-misses-credentials-team-1522.zip
│       └── README.txt
├── 05-miscellaneous/
│   ├── 01-frequency-and-consequence/
│   ├── 02-columns-of-holes/
│   ├── 03-a-peculiar-game/
│   ├── 04-tower-of-babel/
│   │   ├── babel-1522.txt
│   │   ├── solve_final.py
│   │   ├── debug_utf16.py
│   │   ├── solve_brute_final.py
│   │   └── solve_final_complete.py
│   └── 05-conditional-existence/
├── 06-open-source-intelligence/
│   ├── 01-where-the-light-fails-to-fall/
│   ├── 02-a-borrowed-name/
│   ├── 03-strings-attached/
│   └── 04-the-apparatus-apport/
├── 07-reverse-engineering/
│   ├── 01-panoptican/
│   ├── 02-the-disassembled-mind/
│   ├── 03-excavation/
│   └── 04-an-invented-language/
├── 08-steganography/
│   ├── 01-invisible-ink/
│   ├── 02-commit-to-memory/
│   ├── 03-the-apparatus-the-rapping/
│   └── 04-velocity/
└── 09-web/
    ├── 01-shape-of-query/
    ├── 02-poisoned-well/
    ├── 03-no-structure-required/
    ├── 04-the-logic-inside/
    └── 05-the-apparatus-levitation/
```

---

## 🎯 NEXT ACTIONS PRIORITY

1. Provide the Preserved Moment target page text (or a logged-in session) and the Oracle's Weight artifact.
2. Submit the new answers on the challenge pages (not yet submitted from this session).

---

## 📝 NOTES

- **Git LFS** configured for large binaries (game, game.pck, heap-1522.zip, etc.)
- **GitHub Actions** workflows created for automated game execution and analysis
- **Godot 4.7.1** downloaded for PCK analysis (Linux binary)
- All solved challenges have writeups and solve scripts in respective directories
- Repository synced to GitHub: `https://github.com/hackadvisermx/pointeroverflowctf`