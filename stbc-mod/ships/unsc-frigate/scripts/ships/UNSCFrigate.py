# =============================================================================
# UNSC FRIGATE (Charon-class) -- SHIP SCRIPT
# -> copy to <BC>/scripts/ships/UNSCFrigate.py
# =============================================================================
#  Ties the model + hardpoint together and registers the ship.
#  API is REPRESENTATIVE -- reconcile against a stock ship script on your PC.
# =============================================================================

import App

g_ShipName      = "UNSCFrigate"          # matches the hardpoint g_ShipName
g_ModelName     = "unsc_frigate"         # -> data/models/ships/unsc_frigate.nif
g_HardpointName = "UNSCFrigate"          # -> scripts/ships/Hardpoints/UNSCFrigate.py

g_DisplayName   = "UNSC Frigate (Charon-class)"
g_Abbreviation  = "UNSC-F"
g_ShipClass     = "Frigate"


def LoadModel(pModelManager, bQuickReload):
    """Load mesh + apply the UNSC hardpoint property set.
    Reconcile the body against a stock ship script (see docs/04)."""
    # TODO (PC): implement using stock reference. Sketch:
    #   pModel = App.g_kModelManager.LoadModel("ships", g_ModelName)
    #   import Hardpoints.UNSCFrigate as HP
    #   HP.LoadPropertySet()
    #   ... set display name / class metadata ...
    #   return pModel
    pass


def GetDescription():
    return g_DisplayName + " -- armored, shieldless; MAC gun + Archer pods."


# Register with your base's ship list / QuickBattle config (varies by base mod).
