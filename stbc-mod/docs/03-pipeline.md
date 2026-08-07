# 03 — The Per-Ship Pipeline

The repeatable checklist for taking **one ship** from a sourced 3D model to flying in
Bridge Commander. Copy this into each ship's `README.md` and tick it off.

Legend: 🖥️ = on your PC · 🤖 = Claude can drive it (Blender MCP or writing scripts)

---

## Phase A — Source the model 🖥️
1. [ ] Find a 3D model of the ship (see `05-cross-universe-guide.md` for where + licensing).
   Prefer `.obj`/`.fbx`/`.gltf`; mid-poly (BC is an old engine — tens of thousands of
   tris, not millions).
2. [ ] Note the license + author for credit (`06-legal-sourcing.md`).
3. [ ] Drop the raw model in the ship's `assets/` folder (gitignored — it's a binary).

## Phase B — Convert in Blender 🤖🖥️
With Blender open + MCP server running, have Claude:
4. [ ] Import the model into a clean scene.
5. [ ] **Recenter** to world origin (center of mass / geometric center).
6. [ ] **Scale** to BC conventions. BC ships are sized roughly to real scale; match the
   ship's canonical length against a known stock ship as reference (e.g. Galaxy ≈ 642 m).
7. [ ] **Orient** to BC axes: ship faces **+Y forward**, **+Z up** (verify against a stock
   import — axis conventions are the #1 cause of "ship flies backwards/sideways").
8. [ ] **Reduce/clean**: weld doubles, recalculate normals outward, decimate if too dense,
   remove hidden interior geometry.
9. [ ] Confirm the mesh is **unified/welded** (BC needs this for clean damage + to avoid
   graphical glitches).
10. [ ] **Apply** all transforms (location/rotation/scale → identity).
11. [ ] Assign materials/textures; export textures as **32-bit `.tga`**.
12. [ ] **Export `.nif`** via NifTools into `assets/<name>.nif`.

## Phase C — Repair the .nif 🖥️
13. [ ] Open `<name>.nif` in **NifSkope**.
14. [ ] Fix **texture paths** to be relative to `data/models/ships/`.
15. [ ] Check node/version flags; compare structure against a working stock BC `.nif`.
16. [ ] Save.

## Phase D — Hardpoints + subsystems 🖥️🤖
17. [ ] Copy a **stock ship's hardpoint script** as your API ground-truth (see `04`).
18. [ ] Have Claude adapt the ship's hardpoint `.py` from our template + the
    lore-accurate stats (`05`), reconciled against that stock file.
19. [ ] In the **Model Property Editor**, load the `.nif` and place weapon hardpoints
    (muzzle positions/arcs) and subsystem nodes; save.
20. [ ] Have Claude write/confirm the **ship script** (`scripts/ships/<Name>.py`).

## Phase E — Install 🖥️
21. [ ] Copy `<name>.nif` + `.tga` → `<BC>/data/models/ships/`.
22. [ ] Copy hardpoint `.py` → `<BC>/scripts/ships/Hardpoints/`.
23. [ ] Copy ship `.py` → `<BC>/scripts/ships/`.
24. [ ] Register the ship so it's selectable (QuickBattle list / your mod's ship registry).

## Phase F — Test in-game 🖥️ (the real validation)
25. [ ] Launch BC → **QuickBattle** → spawn the ship.
26. [ ] Verify: model loads, textures render, correct scale/orientation.
27. [ ] Verify weapons **fire from the right points** with correct **arcs**.
28. [ ] Verify subsystems + hull **take damage**; for UNSC confirm **no shields**.
29. [ ] Iterate on stats by editing the `.py` files (no remodeling needed) → re-test.

---

## Common failure modes & fixes
| Symptom | Likely cause | Fix |
|---|---|---|
| Ship invisible / CTD on spawn | bad `.nif` version / texture path | NifSkope: fix paths, re-version vs stock |
| Flies backwards/sideways | wrong axis orientation | re-orient to +Y forward / +Z up, re-export |
| Weapons fire from origin | hardpoints not placed in MPE | place muzzle nodes in MPE |
| Ship is a giant/ant | wrong scale | rescale vs known stock length, apply, re-export |
| No damage / indestructible | hull/subsystem props off | check hardpoint stats vs stock template |

→ Next: `04-hardpoint-scripting.md`
