# =============================================================================
# COVENANT CCS-class BATTLECRUISER -- HARDPOINT SCRIPT
# -> copy to <BC>/scripts/ships/Hardpoints/CovenantCruiser.py
# =============================================================================
#
#  Lore-accurate Covenant profile (see ../../../docs/05-cross-universe-guide.md):
#    * STRONG, fast-regenerating energy shields -- the opposite of UNSC. Survivability
#      lives in the shields; the hull underneath is only moderate.
#    * Plasma torpedoes: slow, homing, very high damage.
#    * Pulse lasers: fast medium/point-defense energy bolts.
#    * Energy projector: a glassing beam -- catastrophic damage, very narrow arc,
#      very long recharge (the signature "do not get hit by this" weapon).
#    * Canonically outmatches UNSC ships roughly 3-to-1 -- intended to win the
#      straight-up fight unless the UNSC lands its MAC alpha + missile storm first.
#
#  !!! API CAVEAT: App.* calls are REPRESENTATIVE. Reconcile against a stock
#      hardpoint (STOCK_REFERENCE.py) on your PC -- see docs/04.
# =============================================================================

import App

g_ShipName = "CovenantCruiser"


def LoadPropertySet():
    # ---- Hull: only moderate -- it relies on shields. -----------------------
    HULL_HP            = 11000

    # ---- Power: abundant (plasma reactors). ---------------------------------
    MAIN_POWER         = 14000
    BACKUP_POWER       = 3000

    # ---- Shields: STRONG + FAST recharge. The whole identity. ---------------
    SHIELD_MAX_FRONT   = 9000
    SHIELD_MAX_REAR    = 9000
    SHIELD_MAX_TOP     = 9000
    SHIELD_MAX_BOTTOM  = 9000
    SHIELD_MAX_LEFT    = 9000
    SHIELD_MAX_RIGHT   = 9000
    SHIELD_RECHARGE    = 450          # per-second; regenerates aggressively

    # ---- Propulsion ---------------------------------------------------------
    IMPULSE_SPEED      = 1.05
    TURN_RATE          = 0.90

    # ---- Sensors / repair ---------------------------------------------------
    SENSOR_RANGE       = 1.2
    REPAIR_RATE        = 1.2
    REPAIR_TEAMS       = 4

    # ---- Weapons ------------------------------------------------------------
    WEAPONS = [
        # Energy projector: glassing beam. Extreme damage, narrow arc, slow charge.
        {
            "name":     "Energy_Projector",
            "type":     "beam",
            "damage":   1300,         # per-second of beam contact -- adds up fast
            "recharge": 24.0,         # long cooldown between firings
            "arc_h":    12,           # very narrow forward cone
            "arc_v":    12,
            "range":    1.8,
            "muzzles":  ["hp_Projector"],
        },
        # Plasma torpedoes: slow homing balls of plasma, very high damage.
        {
            "name":     "Plasma_Torpedo",
            "type":     "torpedo",
            "damage":   1600,
            "ammo":     40,
            "reload":   5.5,
            "tracking": 0.9,
            "arc_h":    140,
            "arc_v":    100,
            "muzzles":  ["hp_Plasma_L", "hp_Plasma_R"],
        },
        # Pulse lasers: fast medium energy bolts + point defense.
        {
            "name":     "Pulse_Lasers",
            "type":     "pulse",
            "damage":   210,
            "recharge": 0.30,
            "arc_h":    200,
            "arc_v":    150,
            "range":    0.7,
            "muzzles":  ["hp_Pulse_1", "hp_Pulse_2", "hp_Pulse_3", "hp_Pulse_4"],
        },
    ]

    # ---- Subsystems (targetable). Includes a shield generator. --------------
    SUBSYSTEMS = {
        "PowerPlant":     3500,
        "Impulse":        2800,
        "SensorArray":    2000,
        "WeaponSystem":   3000,
        "ShieldGen":      3000,        # disable this to drop the shields!
    }

    # ---- TODO (PC): emit App.* property-set calls using STOCK_REFERENCE.py. --
    pass


# LoadPropertySet()   # VERIFY: auto-run at import vs called by ship script.
