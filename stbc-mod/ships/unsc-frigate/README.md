# UNSC Frigate (Charon-class) — first proof-of-concept ship

The first end-to-end ship for the toolkit. Goal: prove the whole pipeline
(source → convert → .nif → scripts → in-game) on a **simple mesh** before tackling the
iconic **Pillar of Autumn** (Halcyon-class cruiser).

Lore-accurate UNSC: **no shields, heavy armor, one big MAC gun, Archer missile swarms.**

## Files here
```
unsc-frigate/
├── scripts/
│   ├── ships/UNSCFrigate.py          ← ship script (copy to <BC>/scripts/ships/)
│   └── Hardpoints/UNSCFrigate.py     ← hardpoint script (copy to <BC>/scripts/ships/Hardpoints/)
└── assets/                           ← put the raw model + exported .nif/.tga here (gitignored)
```

## Balance worksheet (vs Galaxy baseline = 1.0×)
| Stat | Value | Notes |
|---|---|---|
| Hull | 14000 | high — armor tank |
| Shields (each facing) | 0 | UNSC has no energy shields |
| MAC gun | 9500 dmg / 15s recharge / 15° arc / 1.6× range | one huge slow punch |
| Archer pods | 320 dmg × 160 ammo / 0.35s cadence | missile swarm |
| 50mm PD | 55 dmg / 0.18s / 200° arc / 0.4× range | anti-missile |
| Impulse / turn | 1.15× / 1.10× | nimble frigate |

Tweak these in `scripts/Hardpoints/UNSCFrigate.py` and re-test — no remodeling needed.

## Build checklist (from docs/03-pipeline.md)
### A — Source 🖥️
- [ ] Find a Charon-class (or generic UNSC) frigate model; record license + author
- [ ] Drop raw model in `assets/` (gitignored)

### B — Convert in Blender 🤖🖥️
- [ ] Import → recenter → scale (frigate ≈ 490 m; reference vs a stock ship)
- [ ] Orient to +Y forward / +Z up
- [ ] Weld/clean, recalc normals, decimate if dense, apply transforms
- [ ] Export textures as 32-bit .tga
- [ ] Export `assets/unsc_frigate.nif` via NifTools

### C — Repair 🖥️
- [ ] NifSkope: fix texture paths, check version vs a stock .nif, save

### D — Hardpoints + subsystems 🖥️🤖
- [ ] Copy a stock frigate-ish `Hardpoints/*.py` → `STOCK_REFERENCE.py` (API ground truth)
- [ ] Reconcile `UNSCFrigate.py` (hardpoint) against it; keep our stats
- [ ] In Model Property Editor: place `hp_MAC`, `hp_Archer_L/R`, `hp_PD_1..4` muzzles
- [ ] Confirm ship script `scripts/ships/UNSCFrigate.py`

### E — Install 🖥️
- [ ] `.nif` + `.tga` → `<BC>/data/models/ships/`
- [ ] hardpoint `.py` → `<BC>/scripts/ships/Hardpoints/`
- [ ] ship `.py` → `<BC>/scripts/ships/`
- [ ] Register in QuickBattle / ship list

### F — Test 🖥️
- [ ] Spawns; model + textures load; correct scale/orientation
- [ ] MAC fires forward from `hp_MAC`; Archers salvo; PD tracks
- [ ] Hull takes damage; **confirm no shields**
- [ ] Iterate stats → re-test

## Credits (fill in once a model is chosen)
```
Model: "<title>" by <author> — <url>
License: <e.g. CC-BY 4.0>
Mods: imported, rescaled, re-textured, exported to .nif for STBC
Franchise: Halo © Microsoft / 343 Industries (fan, non-commercial use)
```
