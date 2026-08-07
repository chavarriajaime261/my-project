# UNSC Pillar of Autumn (Halcyon-class cruiser) — iconic UNSC capital ship

The flagship target after the frigate proves the pipeline. Same lore identity (no shields,
heavy armor, MAC + missiles) scaled to a **capital ship** with the Halcyon-class's
legendary durability, plus Shiva nukes.

## Files here
```
pillar-of-autumn/
├── scripts/
│   ├── ships/PillarOfAutumn.py          ← copy to <BC>/scripts/ships/
│   └── Hardpoints/PillarOfAutumn.py     ← copy to <BC>/scripts/ships/Hardpoints/
└── assets/                              ← raw model + exported .nif/.tga (gitignored)
```

## Balance worksheet (vs Galaxy baseline = 1.0×)
| Stat | Value | Notes |
|---|---|---|
| Hull | 26000 | Halcyon honeycomb bracing — toughest UNSC hull |
| Shields (each) | 0 | no energy shields |
| MAC gun | 13000 dmg / 16s / 15° arc / 1.7× range | upgraded heavy slug |
| Archer pods | 400 dmg × 260 ammo / 0.30s, 3 launchers | missile storm |
| Shiva nukes | 30000 dmg × 3 ammo / 45s reload | fight-ender |
| 50mm PD | 55 dmg / 0.16s / 6 turrets | dense anti-missile grid |
| Impulse / turn | 0.95× / 0.80× | slow, ponderous cruiser |

Profile: a brawler that soaks damage and trades MAC slugs + missile storms. Vulnerable to
fast shielded attackers that dodge the MAC and whittle the unshielded hull.

## Build checklist (see docs/03-pipeline.md)
- [ ] Source a Pillar of Autumn / Halcyon-class model; record license + author
- [ ] Blender (via MCP): import → recenter → scale (PoA ≈ 1170 m) → orient +Y/+Z
- [ ] Weld/clean/decimate → apply transforms → export .tga (32-bit)
- [ ] NifTools export `assets/pillar_of_autumn.nif`; repair in NifSkope
- [ ] Copy a stock capital hardpoint as `STOCK_REFERENCE.py`; reconcile the API
- [ ] MPE: place `hp_MAC`, `hp_Archer_L/R/D`, `hp_Shiva`, `hp_PD_1..6`
- [ ] Install scripts + model; register in QuickBattle
- [ ] Test: spawns, fires, takes hull damage, no shields → iterate stats

## Credits (fill in once a model is chosen)
```
Model: "<title>" by <author> — <url>
License: <e.g. CC-BY 4.0>
Mods: imported, rescaled, re-textured, exported to .nif for STBC
Franchise: Halo © Microsoft / 343 Industries (fan, non-commercial use)
```
