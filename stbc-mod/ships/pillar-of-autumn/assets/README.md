# assets/ — binary model + texture files (PC-side)

Gitignored (see `stbc-mod/.gitignore`). Don't commit large binaries / copyrighted assets.

## What goes here
- `pillar_of_autumn_raw.<obj|fbx|gltf>` — sourced community model (input)
- `pillar_of_autumn.blend` — Blender working file (optional)
- `pillar_of_autumn.nif` — exported model (→ `<BC>/data/models/ships/`)
- `pillar_of_autumn*.tga` — 32-bit textures (→ `<BC>/data/models/ships/`)

Record author + license in the ship `README.md`. Keep polycount sane. Repair the `.nif`
in NifSkope after NifTools export.
