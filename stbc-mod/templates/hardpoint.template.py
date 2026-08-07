# =============================================================================
# HARDPOINT SCRIPT TEMPLATE  ->  copy to <BC>/scripts/ships/Hardpoints/<Name>.py
# =============================================================================
#
#  !!!! READ BEFORE USING !!!!
#
#  Bridge Commander runs an ANCIENT embedded Python (~1.5.2/2.0) and a proprietary
#  `App.*` SDK. The exact API names below are REPRESENTATIVE of the documented
#  hardpoint format -- they are NOT guaranteed to match your install byte-for-byte.
#
#  GROUND-TRUTH STEP (do this once, on your PC):
#    1. Copy a stock ship's hardpoint file (e.g. scripts/ships/Hardpoints/Galaxy.py)
#       next to your new ship as STOCK_REFERENCE.py.
#    2. Keep that file's STRUCTURE / function + constructor names.
#    3. Paste in the STATS from this template (and from docs/05 balance tables).
#    4. Open the result in the Model Property Editor to confirm it parses, then
#       place the weapon/subsystem hardpoints on the mesh and save.
#
#  In other words: trust the stock file for the API, trust this template for the
#  CONCEPTS, COMMENTS, and NUMBERS.
# =============================================================================

import App

# --- Identification ---------------------------------------------------------
# Unique internal name. Must match what the ship script references.
g_ShipName = "TEMPLATE_SHIP"          # TODO: rename, e.g. "UNSCFrigate"


def LoadPropertySet():
    """Build and register this ship's subsystem/weapon property set.

    NOTE: the precise constructor calls (App.*_Create, AddProperty, etc.) MUST be
    reconciled against your STOCK_REFERENCE.py. The blocks below describe WHAT to
    define and WITH WHICH NUMBERS, in the order a stock file defines them.
    """

    # =====================================================================
    # 1) HULL  -- physical structure HP. For armor-tanks (UNSC) this is high.
    # =====================================================================
    HULL_HP            = 12000        # TODO: scale vs stock (Galaxy ~ baseline)

    # =====================================================================
    # 2) POWER  -- main power feeds weapons/shields/engines.
    # =====================================================================
    MAIN_POWER         = 8000
    BACKUP_POWER       = 1500

    # =====================================================================
    # 3) SHIELDS  -- 6 facings: front, rear, top, bottom, left, right.
    #    Set to ~0 for UNSC-style armor tanks (no shields).
    # =====================================================================
    SHIELD_MAX_FRONT   = 0
    SHIELD_MAX_REAR    = 0
    SHIELD_MAX_TOP     = 0
    SHIELD_MAX_BOTTOM  = 0
    SHIELD_MAX_LEFT    = 0
    SHIELD_MAX_RIGHT   = 0
    SHIELD_RECHARGE    = 0            # per-second regen; 0 = no shields

    # =====================================================================
    # 4) PROPULSION  -- impulse (sublight) + turn rate. Warp is cosmetic for combat.
    # =====================================================================
    IMPULSE_SPEED      = 1.0          # multiplier vs stock baseline
    TURN_RATE          = 1.0          # higher = nimbler

    # =====================================================================
    # 5) SENSORS / REPAIR
    # =====================================================================
    SENSOR_RANGE       = 1.0
    REPAIR_RATE        = 1.0
    REPAIR_TEAMS       = 3

    # =====================================================================
    # 6) WEAPONS
    #    Each weapon = a TYPE + stats + a named MUZZLE hardpoint. The 3D
    #    position/orientation of each muzzle is placed in the Model Property
    #    Editor; the NAME here links script <-> mesh.
    #
    #    Types you will use (see docs/04):
    #      - "beam"    continuous energy (phaser / sustained turbolaser)
    #      - "pulse"   discrete bolts   (MAC slug / plasma bolt / PD turret)
    #      - "torpedo" projectiles      (missiles / Archer pods / nukes)
    # =====================================================================
    WEAPONS = [
        # --- Example primary: a single heavy "MAC" pulse (one big slow punch) ---
        {
            "name":        "MAC_Gun",
            "type":        "pulse",
            "damage":      9000,      # very high per-shot
            "recharge":    14.0,      # seconds between shots (slow!)
            "arc_h":       20,        # narrow forward horizontal arc (deg)
            "arc_v":       20,
            "range":       1.5,       # x baseline range (long)
            "muzzles":     ["hp_MAC"],          # name(s) placed in MPE
        },
        # --- Example secondary: Archer missile pods (torpedo salvos) ---
        {
            "name":        "Archer_Pods",
            "type":        "torpedo",
            "damage":      350,       # modest per-missile
            "ammo":        120,       # large magazine
            "reload":      0.4,       # fast salvo cadence
            "tracking":    1.0,       # homing strength
            "arc_h":       90,
            "arc_v":       60,
            "muzzles":     ["hp_Archer_L", "hp_Archer_R"],
        },
        # --- Optional special: Shiva nuke (rare, devastating) ---
        # {
        #     "name": "Shiva", "type": "torpedo", "damage": 25000,
        #     "ammo": 2, "reload": 30.0, "tracking": 0.6,
        #     "arc_h": 30, "arc_v": 30, "muzzles": ["hp_Shiva"],
        # },
        # --- Optional point-defense (50mm) pulse turrets vs incoming ---
        # {
        #     "name": "PD_50mm", "type": "pulse", "damage": 60, "recharge": 0.2,
        #     "arc_h": 180, "arc_v": 120, "range": 0.4,
        #     "muzzles": ["hp_PD_1", "hp_PD_2", "hp_PD_3", "hp_PD_4"],
        # },
    ]

    # =====================================================================
    # 7) SUBSYSTEMS (targetable parts) -- give each HP; disabling has effects.
    #    Typical: WeaponSystem, ShieldGenerator (skip if no shields),
    #    Impulse, Warp, SensorArray, PowerPlant. Names should match mesh nodes
    #    you place in the MPE if you want them individually targetable.
    # =====================================================================
    SUBSYSTEMS = {
        "PowerPlant":   2500,
        "Impulse":      2000,
        "SensorArray":  1500,
        "WeaponSystem": 2000,
        # "ShieldGen":  0,   # omit for UNSC (no shields)
    }

    # -------------------------------------------------------------------------
    # TODO (PC): translate the dictionaries above into the actual App.* calls,
    # using STOCK_REFERENCE.py as the pattern. Pseudocode of the shape:
    #
    #   pSet = App.ShipProperty_Create(g_ShipName)
    #   pSet.SetHullValue(HULL_HP)
    #   ... add power, shields(=0), propulsion, sensors, repair ...
    #   for w in WEAPONS:  <create weapon property of w["type"], set stats, attach muzzles>
    #   for name, hp in SUBSYSTEMS.items():  <create subsystem property with hp>
    #   App.g_kModelPropertyManager.AddPropertySet(pSet)   # name varies -- VERIFY
    #
    # -------------------------------------------------------------------------
    pass


# Most stock hardpoint files call their loader at import time. VERIFY against the
# stock reference whether it's auto-invoked or called by the ship script.
# LoadPropertySet()
