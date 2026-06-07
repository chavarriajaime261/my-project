# STBC Cross-Universe Ship Modding Toolkit

A foundation for building custom ships for **Star Trek: Bridge Commander (STBC)** using
**Claude Code + Blender MCP** — including cross-universe ships (Halo, Star Wars, etc.).

This folder was scaffolded in a cloud session to give you a fast, repeatable workflow
*before* you start the hands-on work on your Windows PC where the game is installed.

> This project lives alongside the unrelated IPC band website in this repo. Nothing here
> touches the website.

---

## The big idea: code vs. art

A STBC ship is really two different jobs:

| Part | What it is | Where it's done |
|------|-----------|-----------------|
| **Hardpoint + ship scripts** (weapons, shields, hull, subsystems, arcs) | Python `.py` text | ✅ Here / Claude Code — Claude's strength |
| **3D mesh** (`.nif`) + **textures** (`.tga`) | Binary art | 🖥️ Your PC — Blender (via Blender MCP) + NifSkope |
| **In-game testing** | The actual game | 🖥️ Your PC — Windows only |

The scripting half is ~50% of "ship design" and is fully buildable as text. That's what
this toolkit front-loads.

---

## What's in here

```
stbc-mod/
├── docs/        ← read these in order (00 → 06)
├── templates/   ← reusable annotated hardpoint + ship script templates
├── ships/       ← per-ship projects (first: ships/unsc-frigate/)
├── mcp/         ← Blender MCP config for Claude Code
└── tools/       ← optional helper scripts
```

## Start here

1. **`docs/00-overview.md`** — the concept and the cloud-vs-PC split.
2. **`docs/01-toolchain-setup.md`** — install the BC SDK, Blender, NifTools, NifSkope, MPE.
3. **`docs/02-mcp-setup.md`** — wire Blender MCP into Claude Code in VS Code.
4. **`docs/03-pipeline.md`** — the repeatable per-ship checklist (sourced model → in-game).
5. **`docs/04-hardpoint-scripting.md`** — how the hardpoint `.py` format works.
6. **`docs/05-cross-universe-guide.md`** — sourcing models + lore-accurate balance tables.
7. **`docs/06-legal-sourcing.md`** — keep it personal/non-commercial; respect model licenses.

Then look at **`ships/unsc-frigate/`** for the first worked example.

---

## Confirmed project decisions

- **Meshes:** import/convert existing community 3D models (don't model from scratch).
- **Balance:** **lore-accurate** power scaling across universes.
- **First ship:** a Halo **UNSC Charon-class frigate** (simple mesh) → then the
  **Pillar of Autumn** (Halcyon-class cruiser) as the iconic stretch goal.

## Important caveats (read before trusting any script)

- STBC runs an **ancient embedded Python** (~1.5.2/2.0). The `.py` scripts here use the
  `App.*` SDK API and **cannot be validated with modern Python**. The templates are based
  on the documented format and **must be reconciled against a real stock ship's hardpoint
  file** on your PC before relying on them (see `docs/04`).
- The **Blender NifTools addon** has no stable 1.0 release and STBC uses an older `.nif`
  version, so expect a **manual NifSkope cleanup pass** after export.
