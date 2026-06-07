# Covenant Battlecruiser (CCS-class) — lore-accurate UNSC sparring partner

The natural enemy for the UNSC ships. Designed as the **mirror image** of the UNSC profile:
where the UNSC has no shields + huge armor + one big slug, the Covenant has **strong
regenerating shields + moderate hull + plasma + a glassing energy projector**. This is the
classic Halo matchup.

## Files here
```
covenant-cruiser/
├── scripts/
│   ├── ships/CovenantCruiser.py          ← copy to <BC>/scripts/ships/
│   └── Hardpoints/CovenantCruiser.py     ← copy to <BC>/scripts/ships/Hardpoints/
└── assets/                               ← raw model + exported .nif/.tga (gitignored)
```

## Balance worksheet (vs Galaxy baseline = 1.0×)
| Stat | Value | Notes |
|---|---|---|
| Hull | 11000 | moderate — shields do the tanking |
| Shields (each facing) | 9000 / 450 regen | strong + fast recharge |
| Energy projector | 1300 dmg/s beam / 24s / 12° arc / 1.8× range | glassing beam |
| Plasma torpedoes | 1600 dmg × 40 ammo / 5.5s, homing | slow heavy homing |
| Pulse lasers | 210 dmg / 0.3s / 4 emitters | mid + point defense |
| Impulse / turn | 1.05× / 0.90× | — |
| ShieldGen subsystem | 3000 HP | **disable to drop the shields** |

## The intended fight (UNSC vs Covenant)
- **Covenant should usually win 1v1** (canon ~3:1) — that's lore-accurate by design.
- **UNSC win condition:** land the **MAC alpha strike** + Archer storm before the
  projector charges, and target the **ShieldGen** to strip the shields, then grind the
  moderate hull.
- **Covenant win condition:** keep shields up, soak the MAC, and connect with the energy
  projector / plasma torpedoes.

Tune `SHIELD_RECHARGE`, `Energy_Projector` damage, and the UNSC `MAC_Gun` damage to dial
how lopsided the matchup feels.

## Build checklist (see docs/03-pipeline.md)
- [ ] Source a CCS-class battlecruiser model; record license + author
- [ ] Blender (via MCP): import → recenter → scale (CCS ≈ 1780 m) → orient +Y/+Z
- [ ] Weld/clean/decimate → apply transforms → export .tga (32-bit)
- [ ] NifTools export `assets/covenant_cruiser.nif`; repair in NifSkope
- [ ] Copy a stock hardpoint as `STOCK_REFERENCE.py`; reconcile the API
- [ ] MPE: place `hp_Projector`, `hp_Plasma_L/R`, `hp_Pulse_1..4`
- [ ] Install scripts + model; register in QuickBattle
- [ ] Test: shields hold + regen, projector fires, hull takes damage once shields down

## Credits (fill in once a model is chosen)
```
Model: "<title>" by <author> — <url>
License: <e.g. CC-BY 4.0>
Mods: imported, rescaled, re-textured, exported to .nif for STBC
Franchise: Halo © Microsoft / 343 Industries (fan, non-commercial use)
```
