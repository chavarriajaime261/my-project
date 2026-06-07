#!/usr/bin/env python3
"""Hardpoint stat sanity-checker (modern Python 3 — runs anywhere).

This does NOT validate Bridge Commander's `App.*` API (that's only possible in-game
against your install — see docs/04). It lints the *numbers* for a ship: catches
out-of-range arcs, missing ammo on projectile weapons, nonsensical recharge, and
flags design intent (e.g. shields == 0 for a UNSC-style armor tank) so balance
mistakes surface before you copy files onto your PC.

Usage:
    python check_stats.py            # checks the built-in UNSC frigate example
    (or import `check_ship` and pass your own dict)

Keep ship stat dicts here (or import them) so balance stays documented + testable.
"""

from __future__ import annotations

# --- Sane ranges (tune to taste; these are guard-rails, not hard rules) -------
HULL_RANGE      = (500, 200_000)
SHIELD_RANGE    = (0, 100_000)
ARC_RANGE       = (0, 360)
RANGE_MULT      = (0.05, 5.0)
WEAPON_TYPES    = {"beam", "pulse", "torpedo"}


def check_ship(ship: dict) -> list[str]:
    """Return a list of warning strings. Empty list == all checks passed."""
    warns: list[str] = []
    name = ship.get("name", "<unnamed>")

    def w(msg: str) -> None:
        warns.append(f"[{name}] {msg}")

    # Hull
    hull = ship.get("hull")
    if hull is None:
        w("missing 'hull'")
    elif not (HULL_RANGE[0] <= hull <= HULL_RANGE[1]):
        w(f"hull {hull} outside sane range {HULL_RANGE}")

    # Shields
    shields = ship.get("shields", {})
    facings = ("front", "rear", "top", "bottom", "left", "right")
    total_shield = sum(shields.get(f, 0) for f in facings)
    if total_shield == 0:
        # Not an error — intentional for UNSC-style. Just announce it.
        w("INFO: shields total 0 — armor-tank profile (intended for UNSC).")
    for f in facings:
        v = shields.get(f, 0)
        if not (SHIELD_RANGE[0] <= v <= SHIELD_RANGE[1]):
            w(f"shield facing '{f}'={v} outside {SHIELD_RANGE}")
    if total_shield > 0 and shields.get("recharge", 0) == 0:
        w("has shields but recharge is 0 — they'll never regenerate.")

    # Weapons
    weapons = ship.get("weapons", [])
    if not weapons:
        w("no weapons defined.")
    for wp in weapons:
        wn = wp.get("name", "<weapon>")
        wt = wp.get("type")
        if wt not in WEAPON_TYPES:
            w(f"weapon '{wn}' has bad type {wt!r} (expected {WEAPON_TYPES})")
        for a in ("arc_h", "arc_v"):
            if a in wp and not (ARC_RANGE[0] <= wp[a] <= ARC_RANGE[1]):
                w(f"weapon '{wn}' {a}={wp[a]} outside {ARC_RANGE}")
        if "range" in wp and not (RANGE_MULT[0] <= wp["range"] <= RANGE_MULT[1]):
            w(f"weapon '{wn}' range x{wp['range']} outside {RANGE_MULT}")
        if wp.get("damage", 0) <= 0:
            w(f"weapon '{wn}' has non-positive damage.")
        if wt == "torpedo" and wp.get("ammo", 0) <= 0:
            w(f"torpedo '{wn}' has no ammo (>0 required).")
        if wt in ("pulse", "beam") and wp.get("recharge", 0) <= 0:
            w(f"{wt} '{wn}' has non-positive recharge.")
        if not wp.get("muzzles"):
            w(f"weapon '{wn}' has no muzzle hardpoints listed.")

    return warns


# --- Built-in example: the UNSC Charon-class frigate --------------------------
UNSC_FRIGATE = {
    "name": "UNSC Frigate (Charon-class)",
    "hull": 14000,
    "shields": {"front": 0, "rear": 0, "top": 0, "bottom": 0,
                "left": 0, "right": 0, "recharge": 0},
    "weapons": [
        {"name": "MAC_Gun", "type": "pulse", "damage": 9500, "recharge": 15.0,
         "arc_h": 15, "arc_v": 15, "range": 1.6, "muzzles": ["hp_MAC"]},
        {"name": "Archer_Pods", "type": "torpedo", "damage": 320, "ammo": 160,
         "reload": 0.35, "arc_h": 100, "arc_v": 70,
         "muzzles": ["hp_Archer_L", "hp_Archer_R"]},
        {"name": "PD_50mm", "type": "pulse", "damage": 55, "recharge": 0.18,
         "arc_h": 200, "arc_v": 140, "range": 0.4,
         "muzzles": ["hp_PD_1", "hp_PD_2", "hp_PD_3", "hp_PD_4"]},
    ],
}


def main() -> int:
    warns = check_ship(UNSC_FRIGATE)
    print(f"Checking: {UNSC_FRIGATE['name']}")
    if not warns:
        print("  OK — no issues.")
        return 0
    issues = [x for x in warns if "INFO:" not in x]
    for x in warns:
        print(f"  - {x}")
    print(f"\n{len(issues)} issue(s), {len(warns) - len(issues)} info note(s).")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
