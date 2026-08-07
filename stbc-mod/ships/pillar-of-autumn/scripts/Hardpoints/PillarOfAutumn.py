# =============================================================================
# UNSC PILLAR OF AUTUMN (Halcyon-class cruiser) -- HARDPOINT SCRIPT
# -> copy to <BC>/scripts/ships/Hardpoints/PillarOfAutumn.py
# =============================================================================
#
#  Lore-accurate UNSC capital profile (see ../../../docs/05-cross-universe-guide.md):
#    * NO energy shields -- but EXCEPTIONAL hull. The Halcyon-class is famous for a
#      reinforced honeycomb internal structure (cross-bracing) making it absurdly
#      durable for its size -- the toughest ship class in the UNSC.
#    * Heavily refitted: upgraded MAC, expanded Archer batteries, Shiva nukes,
#      dense 50mm point-defense.
#    * Plays as a slow, armored brawler that soaks punishment and answers with one
#      huge MAC slug + missile storms.
#
#  !!! API CAVEAT: App.* calls are REPRESENTATIVE. Reconcile against a stock
#      capital-ship hardpoint (STOCK_REFERENCE.py) on your PC -- see docs/04.
# =============================================================================

import App

g_ShipName = "PillarOfAutumn"


def LoadPropertySet():
    # ---- Hull: enormous. The Halcyon's signature trait. ---------------------
    HULL_HP            = 26000

    # ---- Power: 3 fusion reactors (refit). ----------------------------------
    MAIN_POWER         = 12000
    BACKUP_POWER       = 2500

    # ---- Shields: ZERO. -----------------------------------------------------
    SHIELD_MAX_FRONT   = 0
    SHIELD_MAX_REAR    = 0
    SHIELD_MAX_TOP     = 0
    SHIELD_MAX_BOTTOM  = 0
    SHIELD_MAX_LEFT    = 0
    SHIELD_MAX_RIGHT   = 0
    SHIELD_RECHARGE    = 0

    # ---- Propulsion: a cruiser -- slower + less nimble than the frigate. -----
    IMPULSE_SPEED      = 0.95
    TURN_RATE          = 0.80

    # ---- Sensors / repair ---------------------------------------------------
    SENSOR_RANGE       = 1.1
    REPAIR_RATE        = 1.1
    REPAIR_TEAMS       = 5

    # ---- Weapons ------------------------------------------------------------
    WEAPONS = [
        # Upgraded MAC: heavier slug than the frigate's -- bigger hit, still slow.
        {
            "name":     "MAC_Gun",
            "type":     "pulse",
            "damage":   13000,
            "recharge": 16.0,
            "arc_h":    15,
            "arc_v":    15,
            "range":    1.7,
            "muzzles":  ["hp_MAC"],
        },
        # Expanded Archer batteries: more launchers, bigger magazine.
        {
            "name":     "Archer_Pods",
            "type":     "torpedo",
            "damage":   400,
            "ammo":     260,
            "reload":   0.30,
            "tracking": 1.0,
            "arc_h":    120,
            "arc_v":    80,
            "muzzles":  ["hp_Archer_L", "hp_Archer_R", "hp_Archer_D"],
        },
        # Shiva nuclear missiles: rare, fight-ending warheads.
        {
            "name":     "Shiva",
            "type":     "torpedo",
            "damage":   30000,
            "ammo":     3,
            "reload":   45.0,
            "tracking": 0.55,
            "arc_h":    30,
            "arc_v":    30,
            "muzzles":  ["hp_Shiva"],
        },
        # Dense 50mm point-defense grid.
        {
            "name":     "PD_50mm",
            "type":     "pulse",
            "damage":   55,
            "recharge": 0.16,
            "arc_h":    220,
            "arc_v":    160,
            "range":    0.45,
            "muzzles":  ["hp_PD_1", "hp_PD_2", "hp_PD_3",
                         "hp_PD_4", "hp_PD_5", "hp_PD_6"],
        },
    ]

    # ---- Subsystems (targetable). No shield generator. ----------------------
    SUBSYSTEMS = {
        "PowerPlant":   4000,
        "Impulse":      3200,
        "SensorArray":  2200,
        "WeaponSystem": 3500,
    }

    # ---- TODO (PC): emit App.* property-set calls using STOCK_REFERENCE.py. --
    pass


# LoadPropertySet()   # VERIFY: auto-run at import vs called by ship script.
