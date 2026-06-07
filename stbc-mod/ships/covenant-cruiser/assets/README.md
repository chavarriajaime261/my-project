# assets/ — binary model + texture files (PC-side)

Gitignored (see `stbc-mod/.gitignore`). Don't commit large binaries / copyrighted assets.

## What goes here
- `covenant_cruiser_raw.<obj|fbx|gltf>` — sourced community model (input)
- `covenant_cruiser.blend` — Blender working file (optional)
- `covenant_cruiser.nif` — exported model (→ `<BC>/data/models/ships/`)
- `covenant_cruiser*.tga` — 32-bit textures (→ `<BC>/data/models/ships/`)

Record author + license in the ship `README.md`. Keep polycount sane. Repair the `.nif`
in NifSkope after NifTools export.
