# The House Always Misses
Flag: `POCTF{49.1522.d76707fec9a8266cb860b2a8456347a6.DQMNRBAWBH22NEQRBR5O6DOZVN}`

## Key findings
- Earlier notes were wrong: the PCK is NOT encrypted. `28b52ffd` is the zstd magic; Godot 4 stores GDScript bytecode (GDSC v101) zstd-compressed. No PCK entry has the encrypted flag.
- The PCK is embedded in the ELF (offset 73675128 in `game`), format v4, Godot 4.7.1.
- GDRE Tools v2.7.4 (`--recover`) decompiles all 16 scripts losslessly.
- Hit detection (`gallery.gd::_click_at`), scoring and the win check (`_score >= 1200`) are all client-side; the server only sees `/tick` heartbeats and `/complete`.
- The `team.key` embedded in the PCK belongs to another team; use the one shipped with your own credentials zip.

## Solve
Recover the project, import it with a native Godot 4.7.1 (`--headless --import`), apply the two patches
(auto-continue past the auth screen; each frame call `on_hit()` on every positive-point target and print the marker),
copy your own `game.token` / `team.key` next to `project.godot`, run `godot --headless --path .`.
Server calls (/instance, /tick, /complete) are left unmodified.
