# =============================================================================
# UNSC PILLAR OF AUTUMN (Halcyon-class cruiser) -- SHIP SCRIPT
# -> copy to <BC>/scripts/ships/PillarOfAutumn.py
# =============================================================================
#  API is REPRESENTATIVE -- reconcile against a stock ship script. See docs/04.
# =============================================================================

import App

g_ShipName      = "PillarOfAutumn"
g_ModelName     = "pillar_of_autumn"     # -> data/models/ships/pillar_of_autumn.nif
g_HardpointName = "PillarOfAutumn"       # -> scripts/ships/Hardpoints/PillarOfAutumn.py

g_DisplayName   = "UNSC Pillar of Autumn (Halcyon-class)"
g_Abbreviation  = "UNSC-PoA"
g_ShipClass     = "Cruiser"


def LoadModel(pModelManager, bQuickReload):
    """Load mesh + apply hardpoint property set. Reconcile vs stock (docs/04).
    Sketch:
        pModel = App.g_kModelManager.LoadModel("ships", g_ModelName)
        import Hardpoints.PillarOfAutumn as HP
        HP.LoadPropertySet()
        ... set name / class metadata ...
        return pModel
    """
    pass


def GetDescription():
    return g_DisplayName + " -- ultra-durable hull; upgraded MAC, Archers, Shiva nukes."


# Register with your base's ship list / QuickBattle config.
