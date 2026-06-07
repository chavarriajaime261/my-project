# 01 — Toolchain Setup (your PC)

Everything in this file is installed/configured **on your Windows PC** where Bridge
Commander lives. Do it once.

## 0. Prerequisites
- Star Trek: Bridge Commander installed. The patched **1.1** version is recommended.
- Strongly recommended community base: the **Kobayashi Maru** mod or **Bridge Commander
  Remastered** — they modernize the engine, fix bugs, and make adding ships far easier.
  (You can also mod a clean stock install; ships are forward-compatible with care.)

## 1. Bridge Commander SDK
The official **STBC SDK** contains the core modding assets, sample files, and the
`.nif` exporter, plus tutorials.
- Source: ModDB — "Star Trek: Bridge Commander SDK v1.1".
- After install you'll have the **Model Property Editor (MPE)** in the `Tools/`
  subdirectory of the game (or the SDK). This is the GUI you use to place weapon
  hardpoints and edit subsystems on a model.

### Model Property Editor quick config
Launch the MPE and set:
- **Default model directory** → `<BC>/data/models/ships`
- **Default script directory** → `<BC>/scripts/ships/Hardpoints`

so it reads/writes in the right places.

## 2. Blender + NifTools addon
We import/convert sourced models in Blender, then export `.nif`.
- Install **Blender** (a current LTS is fine; if you hit NifTools incompatibility, fall
  back to the Blender version the addon's release notes target).
- Install the **Blender NifTools Addon**: https://github.com/niftools/blender_niftools_addon
  - Download the release `.zip`, then in Blender: *Edit → Preferences → Add-ons → Install…*
    → pick the zip → enable "Import-Export: NetImmerse/Gamebryo nif format".
  - You now get **File → Import → NetImmerse/Gamebryo (.nif)** and the matching Export.
- ⚠️ No stable 1.0 exists and STBC uses an older `.nif` version than the Skyrim-era games
  the addon is tuned for — expect to fix things in NifSkope afterward (next step).

## 3. NifSkope
The `.nif` inspector/repair tool. Used after export to fix node names, texture paths,
flags, and version issues so BC loads the model.
- Source: https://github.com/niftools/nifskope (releases).

## 4. (Optional) 3ds Max 3 path
The original BC ships were made in **3ds Max 3**, and the SDK's exporter targets it. If you
ever hit a wall with the Blender path, the Max 3 + SDK exporter route is the "blessed" one.
Most people get by with Blender + NifSkope now.

## 5. Folder map you'll be touching
```
<BC install>/
├── data/models/ships/           ← .nif + .tga go here
├── scripts/ships/               ← ship scripts (<Name>.py)
│   └── Hardpoints/              ← hardpoint scripts (<Name>.py)
└── Tools/                       ← Model Property Editor
```

## Sanity check before moving on
- [ ] MPE launches and its model/script dirs point into the BC install
- [ ] Blender shows NetImmerse/Gamebryo in Import **and** Export menus
- [ ] NifSkope opens a stock ship `.nif` (e.g. `galaxy.nif`) without errors

→ Next: `02-mcp-setup.md`
