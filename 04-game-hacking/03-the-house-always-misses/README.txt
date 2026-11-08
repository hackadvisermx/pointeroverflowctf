The House Always Misses — POCTF 2026
======================================

Install:
  1. Download the game binary for your OS from the challenge page.
  2. Extract this ZIP alongside the binary. The game reads
     game.token and team.key from the same directory as the
     executable at startup.

Layout:
  <folder>/
    POCTF2026-GH03.exe           (or POCTF2026-GH03.x86_64)
    game.token
    team.key
    README.txt   (this file)

Run the game. Auth screen should say 'Access granted.'

The game as shipped is harder than it looks. Winning requires
the player's shots to connect more often than the game's own
logic intends. Everything that decides whether a shot hits runs
on your machine, in a process you own.

When you win, an overlay will show the POCTF{...} flag. Copy it
back to the challenge page and submit.
