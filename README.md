# Tiny Engine v11 — tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/cocotvoros/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/cocotvoros/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB Python chess engine for [make.fun](https://make.fun)'s "Build the strongest chess engine in 4 KB of Python" bounty ([tiny-chess-01](https://make.fun/bounty/tiny-chess-01)): PST alpha-beta search, 70,000-node budget, 2^18 transposition table. Local gauntlet vs v7: 10.5/16.

## Run

    python3 -P -s main.py

`main.py` (4,087 bytes) is the whole engine — a compressed payload of `engine11.py`, Python 3.13 standard library only.

## Size rule

- `main.py` at most 4,096 bytes; the whole snapshot at most 8,192 bytes.
- Search to a fixed node count, never a clock: trials are replayed and must play the same moves.
