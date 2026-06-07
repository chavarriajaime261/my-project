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


PILLAR_OF_AUTUMN = {
    "name": "UNSC Pillar of Autumn (Halcyon-class)",
    "hull": 26000,
    "shields": {"front": 0, "rear": 0, "top": 0, "bottom": 0,
                "left": 0, "right": 0, "recharge": 0},
    "weapons": [
        {"name": "MAC_Gun", "type": "pulse", "damage": 13000, "recharge": 16.0,
         "arc_h": 15, "arc_v": 15, "range": 1.7, "muzzles": ["hp_MAC"]},
        {"name": "Archer_Pods", "type": "torpedo", "damage": 400, "ammo": 260,
         "reload": 0.30, "arc_h": 120, "arc_v": 80,
         "muzzles": ["hp_Archer_L", "hp_Archer_R", "hp_Archer_D"]},
        {"name": "Shiva", "type": "torpedo", "damage": 30000, "ammo": 3,
         "reload": 45.0, "arc_h": 30, "arc_v": 30, "muzzles": ["hp_Shiva"]},
        {"name": "PD_50mm", "type": "pulse", "damage": 55, "recharge": 0.16,
         "arc_h": 220, "arc_v": 160, "range": 0.45,
         "muzzles": ["hp_PD_1", "hp_PD_2", "hp_PD_3",
                     "hp_PD_4", "hp_PD_5", "hp_PD_6"]},
    ],
}

COVENANT_CRUISER = {
    "name": "Covenant Battlecruiser (CCS-class)",
    "hull": 11000,
    "shields": {"front": 9000, "rear": 9000, "top": 9000, "bottom": 9000,
                "left": 9000, "right": 9000, "recharge": 450},
    "weapons": [
        {"name": "Energy_Projector", "type": "beam", "damage": 1300,
         "recharge": 24.0, "arc_h": 12, "arc_v": 12, "range": 1.8,
         "muzzles": ["hp_Projector"]},
        {"name": "Plasma_Torpedo", "type": "torpedo", "damage": 1600, "ammo": 40,
         "reload": 5.5, "arc_h": 140, "arc_v": 100,
         "muzzles": ["hp_Plasma_L", "hp_Plasma_R"]},
        {"name": "Pulse_Lasers", "type": "pulse", "damage": 210, "recharge": 0.30,
         "arc_h": 200, "arc_v": 150, "range": 0.7,
         "muzzles": ["hp_Pulse_1", "hp_Pulse_2", "hp_Pulse_3", "hp_Pulse_4"]},
    ],
}

ALL_SHIPS = [UNSC_FRIGATE, PILLAR_OF_AUTUMN, COVENANT_CRUISER]


def main() -> int:
    total_issues = 0
    for ship in ALL_SHIPS:
        warns = check_ship(ship)
        print(f"Checking: {ship['name']}")
        if not warns:
            print("  OK — no issues.")
            continue
        issues = [x for x in warns if "INFO:" not in x]
        total_issues += len(issues)
        for x in warns:
            print(f"  - {x}")
        print(f"  -> {len(issues)} issue(s), {len(warns) - len(issues)} info note(s).")
    return 1 if total_issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
