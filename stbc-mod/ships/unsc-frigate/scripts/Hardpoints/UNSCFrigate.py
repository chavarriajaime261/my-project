# =============================================================================
# UNSC FRIGATE (Charon-class) -- HARDPOINT SCRIPT
# -> copy to <BC>/scripts/ships/Hardpoints/UNSCFrigate.py
# =============================================================================
#
#  Lore-accurate UNSC profile (see ../../../docs/05-cross-universe-guide.md):
#    * NO energy shields -- survivability comes from thick Titanium-A armor (Hull).
#    * One devastating MAC gun: a single huge-damage, slow-recharge forward pulse.
#    * Archer missile pods: large salvos of guided torpedoes.
#    * 50mm point-defense: fast, weak pulse turrets vs incoming missiles.
#    * Glass-cannon feel: hits like a truck, but a shielded foe that survives the
#      MAC alpha strike can grind the unshielded hull down.
#
#  !!! API CAVEAT: the App.* calls are REPRESENTATIVE. Reconcile against a stock
#      hardpoint file (STOCK_REFERENCE.py) on your PC -- see docs/04 + the template.
# =============================================================================

import App

g_ShipName = "UNSCFrigate"


def LoadPropertySet():
    # ---- Hull: tough. UNSC tanks with armor, not shields. -------------------
    HULL_HP            = 14000

    # ---- Power --------------------------------------------------------------
    MAIN_POWER         = 7000
    BACKUP_POWER       = 1200

    # ---- Shields: ZERO (no energy shields). ---------------------------------
    SHIELD_MAX_FRONT   = 0
    SHIELD_MAX_REAR    = 0
    SHIELD_MAX_TOP     = 0
    SHIELD_MAX_BOTTOM  = 0
    SHIELD_MAX_LEFT    = 0
    SHIELD_MAX_RIGHT   = 0
    SHIELD_RECHARGE    = 0

    # ---- Propulsion: frigates are fairly quick + maneuverable. ---------------
    IMPULSE_SPEED      = 1.15
    TURN_RATE          = 1.10

    # ---- Sensors / repair ---------------------------------------------------
    SENSOR_RANGE       = 1.0
    REPAIR_RATE        = 1.0
    REPAIR_TEAMS       = 3

    # ---- Weapons ------------------------------------------------------------
    WEAPONS = [
        # MAC GUN: the signature one-big-punch weapon. Narrow forward arc, long
        # range, enormous per-shot damage, long recharge between shots.
        {
            "name":     "MAC_Gun",
            "type":     "pulse",
            "damage":   9500,
            "recharge": 15.0,        # ~one shot every 15s
            "arc_h":    15,          # tight forward cone
            "arc_v":    15,
            "range":    1.6,
            "muzzles":  ["hp_MAC"],
        },
        # ARCHER MISSILE PODS: swarms. Modest each, big magazine, fast cadence.
        {
            "name":     "Archer_Pods",
            "type":     "torpedo",
            "damage":   320,
            "ammo":     160,
            "reload":   0.35,        # rapid salvo
            "tracking": 1.0,
            "arc_h":    100,
            "arc_v":    70,
            "muzzles":  ["hp_Archer_L", "hp_Archer_R"],
        },
        # 50mm POINT DEFENSE: weak/fast pulse turrets, short range, wide arcs.
        {
            "name":     "PD_50mm",
            "type":     "pulse",
            "damage":   55,
            "recharge": 0.18,
            "arc_h":    200,
            "arc_v":    140,
            "range":    0.4,
            "muzzles":  ["hp_PD_1", "hp_PD_2", "hp_PD_3", "hp_PD_4"],
        },
        # OPTIONAL -- Shiva nuke. Uncomment for a rare, fight-ending warhead.
        # {
        #     "name": "Shiva", "type": "torpedo", "damage": 28000,
        #     "ammo": 1, "reload": 60.0, "tracking": 0.5,
        #     "arc_h": 25, "arc_v": 25, "muzzles": ["hp_Shiva"],
        # },
    ]

    # ---- Subsystems (targetable). No shield generator (no shields). ----------
    SUBSYSTEMS = {
        "PowerPlant":   2600,
        "Impulse":      2100,
        "SensorArray":  1500,
        "WeaponSystem": 2200,
    }

    # ---- TODO (PC): emit the App.* property-set calls using STOCK_REFERENCE.py
    #      as the structural pattern; feed in the numbers above. ---------------
    pass


# VERIFY whether the loader auto-runs at import or is called by the ship script.
# LoadPropertySet()
