# =============================================================================
# COVENANT CCS-class BATTLECRUISER -- SHIP SCRIPT
# -> copy to <BC>/scripts/ships/CovenantCruiser.py
# =============================================================================
#  API is REPRESENTATIVE -- reconcile against a stock ship script. See docs/04.
# =============================================================================

import App

g_ShipName      = "CovenantCruiser"
g_ModelName     = "covenant_cruiser"     # -> data/models/ships/covenant_cruiser.nif
g_HardpointName = "CovenantCruiser"      # -> scripts/ships/Hardpoints/CovenantCruiser.py

g_DisplayName   = "Covenant Battlecruiser (CCS-class)"
g_Abbreviation  = "COV-CCS"
g_ShipClass     = "Battlecruiser"


def LoadModel(pModelManager, bQuickReload):
    """Load mesh + apply hardpoint property set. Reconcile vs stock (docs/04).
    Sketch:
        pModel = App.g_kModelManager.LoadModel("ships", g_ModelName)
        import Hardpoints.CovenantCruiser as HP
        HP.LoadPropertySet()
        ... set name / class metadata ...
        return pModel
    """
    pass


def GetDescription():
    return g_DisplayName + " -- strong regenerating shields; plasma torpedoes + energy projector."


# Register with your base's ship list / QuickBattle config.
