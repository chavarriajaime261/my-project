# =============================================================================
# SHIP SCRIPT TEMPLATE  ->  copy to <BC>/scripts/ships/<Name>.py
# =============================================================================
#
#  The lightweight wrapper that ties everything together and registers the ship.
#  Like the hardpoint template, the exact App.* API is REPRESENTATIVE -- reconcile
#  against a stock ship script (e.g. scripts/ships/Galaxy.py) on your PC.
#
#  Responsibilities of this file:
#    1. Point at the .nif model in data/models/ships/
#    2. Point at the hardpoint script in scripts/ships/Hardpoints/
#    3. Set display name / abbreviation / class
#    4. Register the ship so the game can instantiate it (and it shows in menus)
# =============================================================================

import App

# --- What to load -----------------------------------------------------------
# Internal name -- MUST match g_ShipName in the hardpoint script.
g_ShipName        = "TEMPLATE_SHIP"     # TODO e.g. "UNSCFrigate"

# Model file (without path/extension by convention; VERIFY vs stock).
g_ModelName       = "template_ship"     # -> data/models/ships/template_ship.nif

# Hardpoint module name (file in scripts/ships/Hardpoints/, no .py).
g_HardpointName   = "TEMPLATE_SHIP"     # TODO match hardpoint filename

# --- How it presents --------------------------------------------------------
g_DisplayName     = "Template Ship"     # TODO e.g. "UNSC Frigate (Charon-class)"
g_Abbreviation    = "TMPL"              # short tag
g_ShipClass       = "Frigate"           # role/class label


def LoadModel(pModelManager, bQuickReload):
    """Load the mesh + attach the hardpoint property set.

    Reconcile the body against a stock ship script. The shape is roughly:

        # load the .nif
        pModel = App.g_kModelManager.LoadModel("ships", g_ModelName)
        # apply the hardpoint property set (loaded from the Hardpoints module)
        import Hardpoints.<g_HardpointName> as HP
        HP.LoadPropertySet()
        # set name / class metadata
        ...
        return pModel
    """
    # TODO (PC): implement using stock reference. Placeholder:
    pass


def GetDescription():
    """Optional: text shown in ship selection."""
    return g_DisplayName + " (" + g_ShipClass + ")"


# Stock ships typically register themselves with a ship-list / loader here, OR are
# registered by a mutator / QuickBattle config. VERIFY how your base (stock vs
# Kobayashi Maru vs Remastered) expects ships to be registered, and add that call.
