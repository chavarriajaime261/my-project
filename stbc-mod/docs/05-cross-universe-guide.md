# 05 — Cross-Universe Guide: Sourcing + Lore-Accurate Balance

How to bring Halo, Star Wars, and other ships into BC, and how to stat them with
**lore-accurate power scaling** (our chosen philosophy).

---

## Part 1 — Sourcing models

We **import existing community models** rather than modeling from scratch. Good sources:
- **Sketchfab** — filter by **downloadable** + check each model's license (many are
  CC-BY = free to use *with credit*; some are non-commercial; some are editorial-only).
- **3D model repos** — TurboSquid/CGTrader (free + paid), Free3D, etc.
- **Existing BC ship packs** — GameFront, ModDB, Nexus Mods already have many cross-universe
  ships converted; sometimes it's faster to build on/learn from those.
- **Game asset rips** — possible but the muddiest legally; see `06-legal-sourcing.md`.

Model selection tips:
- Prefer **mid-poly** (BC is old — aim for tens of thousands of tris).
- Closed, **watertight** hulls convert/damage better than loose kit-bashed shells.
- Separate, named parts help if you want destructible subsystems.
- Always record **author + license** for `06`.

---

## Part 2 — The mapping principle

BC only understands: **beams, pulses, torpedoes, shields (×6), hull, subsystems.** Every
foreign weapon must become one of those. Lore-accurate scaling means tuning the *numbers*
so each universe *feels* canon — even though the fights are deliberately lopsided.

> ⚠️ **Lore-accurate ≠ balanced.** You chose lore-accuracy, so expect a Star Destroyer or
> Covenant cruiser to wreck a Trek ship. That's intended. (If a particular fight is *no
> fun*, you can always fork a "balanced" stat block later.)

### Reference anchor
Use a **Galaxy-class** as the Trek baseline ("1.0×") and scale others relative to it. Pick
real numbers by copying a stock ship's stats and multiplying.

---

## Part 3 — Universe profiles

### 🔵 Trek (baseline)
- Balanced shields + hull, phasers (beam) + photon/quantum torpedoes.
- This is BC's native tuning — use stock ships as the literal reference values.

### 🟢 Halo — UNSC (our first ship)
**Identity: no shields, heavy armor, one huge gun, missile spam.**

| System | Lore | BC mapping | Relative tuning |
|---|---|---|---|
| Shields | None | 6 facings ≈ 0 | ~0 (token at most) |
| Hull/armor | Thick Titanium-A | Hull | High (survivability lives here) |
| **MAC gun** | Hypervelocity slug, one big hit, slow reload | **Pulse**, narrow fwd arc, long range | Very high per-shot dmg, **long recharge** |
| **Archer pods** | Missile swarms | **Torpedo** salvos | Modest dmg each, **big ammo/salvo**, tracking |
| 50mm PD | Autocannon point-defense | short-range rapid **pulse** turrets | Low dmg, fast, anti-missile |
| Shiva nuke | Tactical nuke, rare | special **torpedo** | Huge dmg, **very low ammo** |

Weakness by design: glass-cannon-ish — hits hard, but with no shields a shielded enemy that
survives the MAC alpha can grind the hull down.

### 🟢 Halo — Covenant
**Identity: strong energy shields, plasma, devastating energy projector.**

| System | Lore | BC mapping | Relative tuning |
|---|---|---|---|
| Shields | Strong regenerating | Shields ×6 | High max + **fast recharge** |
| Hull | Moderate under shields | Hull | Medium |
| Plasma torpedoes | Tracking plasma | **Torpedo** (beam-ish dmg) | High dmg, homing |
| Pulse lasers | Point defense / mid | **Pulse** | Medium, fast |
| **Energy projector** | Glassing beam, catastrophic | **Beam**, very long recharge | Extreme dmg, very narrow arc, slow |

### 🔴 Star Wars — Imperial
**Identity: layered turbolasers, strong shields, big hull.**

| System | Lore | BC mapping | Relative tuning |
|---|---|---|---|
| Shields | Strong, regenerating | Shields ×6 | High + steady recharge |
| Hull | Massive on capital ships | Hull | Very high (Star Destroyer) |
| Turbolasers | Heavy energy batteries | **Pulse/Beam** banks | High dmg, many emitters, broad arcs |
| Ion cannons | Disable systems | **Pulse** tuned to hit subsystems | Med dmg, subsystem-focused |
| Proton torpedoes | Heavy ordnance | **Torpedo** | High dmg, limited ammo |

Scale by hull class: CR90 Corvette (small, light) ≪ Nebulon-B (frigate) ≪ Imperial-II Star
Destroyer (capital, very high everything).

### 🟡 Other universes (pattern)
For anything else, answer three questions, then borrow the closest profile above:
1. **Does it have energy shields?** → set shield max/recharge accordingly (0 for UNSC-likes).
2. **What's its signature weapon?** → one standout beam/pulse/torpedo, dialed up.
3. **What's its tankiness from?** → shields vs. hull.

---

## Part 4 — A simple scaling worksheet
For a new ship, fill in multipliers vs. the Galaxy baseline, then apply to stock numbers:

```
Ship: ____________________   Class/role: ____________
Hull        ×____    Shields(each)  ×____   Shield regen ×____
Main weapon ×____ dmg, ×____ recharge, arc ___°, range ×____
Secondary   ×____ dmg, ammo ____, reload ×____
Special     ×____ dmg, ammo ____
Impulse spd ×____    Turn rate ×____
```

Keep these worksheets in each ship's `README.md` so the balance is documented + tweakable.

→ Next: `06-legal-sourcing.md`
