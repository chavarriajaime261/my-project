# tools/

Optional helper scripts. These run under **modern Python 3** (your dev machine) — they do
**not** touch Bridge Commander's `App.*` API (that only validates in-game).

## check_stats.py
A balance/sanity linter for ship stats. Catches out-of-range firing arcs, missing ammo on
projectile weapons, non-positive damage/recharge, shields-without-recharge, and announces
design intent (e.g. shields == 0 for a UNSC armor tank).

```bash
python check_stats.py        # lints the built-in UNSC frigate example
```

To check your own ship, import `check_ship(dict)` or add your stat dict alongside
`UNSC_FRIGATE` and call it from `main()`.
