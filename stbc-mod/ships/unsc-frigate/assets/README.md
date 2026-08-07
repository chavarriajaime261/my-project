# assets/ — binary model + texture files (PC-side)

This folder holds the **binary** art for the ship. These are produced/handled on your PC
and are **gitignored** (see `stbc-mod/.gitignore`) — don't commit large binaries or
copyrighted assets to the repo.

## What goes here
- `unsc_frigate_raw.<obj|fbx|gltf>` — the sourced community model (input)
- `unsc_frigate.blend` — your Blender working file (optional)
- `unsc_frigate.nif` — the exported model (output → goes to `<BC>/data/models/ships/`)
- `unsc_frigate*.tga` — 32-bit textures (→ `<BC>/data/models/ships/`)

## Reminders
- Record the model's **author + license** in the ship `README.md` credits block.
- Keep polycount sane (BC is old — tens of thousands of tris).
- After NifTools export, **repair in NifSkope** (texture paths, version) before installing.
