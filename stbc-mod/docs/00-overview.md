# 00 — Overview

## What we're building

Custom ships for **Star Trek: Bridge Commander** that you can fly/fight in QuickBattle and
missions — including ships from other universes (Halo, Star Wars, …), built with a
**lore-accurate** balance philosophy.

## How a STBC ship is assembled

Every ship in STBC is the sum of a few files spread across the game install:

| File | Location (under the BC install) | What it does |
|------|--------------------------------|--------------|
| Mesh | `Data/Models/Ship/<name>.nif` | The 3D model |
| Textures | `Data/Models/Ship/<name>*.tga` | 32-bit TGA skins |
| **Hardpoint script** | `scripts/ships/Hardpoints/<Name>.py` | Subsystems, weapons, shields, hull, arcs |
| **Ship script** | `scripts/ships/<Name>.py` | Ties model ↔ hardpoint, registers the ship, sets name/class |
| Menu/registry entry | varies (e.g. a ship list / mutator) | Makes the ship pickable in QuickBattle |

The two `.py` files are plain text — **this is the half we build here**. The `.nif`/`.tga`
are binary art produced on your PC.

## Cloud vs. PC: who does what

This toolkit was scaffolded in an ephemeral **Linux cloud session** with **no Blender, no
GPU, and no game**. So the division of labor is:

### Done here (text/code — already in this repo)
- Project scaffold + documentation (this `docs/` set)
- Reusable hardpoint/ship **script templates**
- The first ship's scripts (`ships/unsc-frigate/`)
- The cross-universe **balance reference**
- Blender MCP config + optional helper tools

### Done on your PC (art + integration + testing)
- Drive **Blender via Blender MCP** to import a sourced model, scale/orient it, and export
  `.nif` with the **NifTools** addon
- Clean up the `.nif` in **NifSkope**
- Place weapon/subsystem hardpoints in the **Model Property Editor (MPE)**
- Copy the scripts into the game, drop in the `.nif`/`.tga`
- **Launch the game and test** — the only real validation

## The mental model for cross-universe ships

Bridge Commander only understands *its own* combat vocabulary: phasers (beam/pulse),
torpedoes (guided/dumb-fire projectiles), shields (6 facings), hull, and subsystems
(power, engines, sensors, repair, weapons). Bringing in a Halo or Star Wars ship is an
exercise in **mapping that universe's tech onto BC's vocabulary**:

- Halo MAC gun → a single, very high-damage, slow-recharge pulse weapon
- Halo Archer missile pods → salvos of guided torpedoes
- UNSC armor, no shields → very high hull, shield strength ≈ 0
- Star Wars turbolasers → rapid-fire pulse banks; strong regenerating shields

`docs/05-cross-universe-guide.md` has the full mapping + lore-accurate stat tables.

## Next

→ `01-toolchain-setup.md`
