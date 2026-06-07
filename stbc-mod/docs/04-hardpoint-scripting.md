# 04 — Hardpoint & Ship Scripting

This is the half Claude builds best: the **Python that defines a ship's combat behavior**.

> ⚠️ **The single most important rule:** STBC runs an *ancient embedded Python* and a
> proprietary `App.*` SDK. The exact API names below are **representative**, modeled on the
> documented format — they are **not guaranteed** to match your install's SDK byte-for-byte.
> **Before trusting any script, copy a stock ship's hardpoint file and diff against it.**
> See "Ground-truth workflow" at the bottom.

## The two files

### 1. Hardpoint script — `scripts/ships/Hardpoints/<Name>.py`
Defines the ship's *systems*: hull strength, power, shields (6 facings), weapons (type,
damage, recharge, position, firing arc), engines, sensors, repair, and which subsystems
exist + their hit points. This is what the Model Property Editor reads/writes — the file
is partly machine-generated, but you (and Claude) hand-tune the numbers.

### 2. Ship script — `scripts/ships/<Name>.py`
The lightweight wrapper that:
- points at the `.nif` model,
- points at the hardpoint script,
- sets the display name, abbreviation, and class,
- registers the ship with the game so it can be instantiated.

## Anatomy of a hardpoint (conceptual)

A hardpoint file builds up a **property set** describing subsystems. Conceptually:

```
Property Set "<Name>"
├── Hull         → total hull HP, condition thresholds
├── Power        → main power output, battery/backup
├── Shields      → per-facing max + recharge   (UNSC: set to ~0)
├── Impulse      → sublight speed/accel
├── Warp         → (cosmetic for combat)
├── Sensors      → detection range
├── Repair       → repair rate, number of repair teams
└── Weapons[]    → each: kind (beam/pulse/torpedo), damage, recharge,
                    arc (h/v degrees), max range, muzzle hardpoint name
```

Each **weapon hardpoint** also has a 3D position + orientation, which is what you place in
the **Model Property Editor** on the actual mesh. The script holds the *stats*; the MPE
holds the *positions* — they're linked by hardpoint name.

## Mapping combat concepts you'll use

| BC concept | Use it for | Key stats |
|---|---|---|
| **Beam (phaser)** | Continuous energy weapons; turbolaser sustained fire | damage/sec, recharge, arc, range |
| **Pulse** | Discrete energy bolts; MAC slug; plasma bolts | per-shot damage, fire interval, arc |
| **Torpedo** | Guided/dumb projectiles; missiles, Archer pods, nukes | damage, ammo, reload, tracking |
| **Shields (×6)** | Energy shielding; deflectors, SW shields | max per facing, recharge rate |
| **Hull** | Physical structure; UNSC titanium armor | total HP |
| **Subsystems** | Targetable parts | per-subsystem HP, disable effects |

## Worked design notes for our first ship (UNSC frigate)
Lore-accurate UNSC = **no shields, tough hull, one devastating MAC, many missiles.** In
hardpoint terms:
- **Shields:** all 6 facings ≈ 0 (or a token value). UNSC ships tank with armor, not shields.
- **Hull:** high — survivability comes from here.
- **MAC gun:** a single **pulse** weapon, very high per-shot damage, **long recharge**
  (one big punch, not a stream), narrow forward arc, long range.
- **Archer missile pods:** **torpedo**-type, modest per-missile damage but **large
  salvos / generous ammo**, decent tracking, wide-ish arc.
- **(Optional) Shiva nuke:** a special, very-high-damage, very-limited-ammo torpedo.
- **Point-defense (50mm):** optional short-range rapid **pulse** turrets vs. incoming.

Concrete numbers live in `05-cross-universe-guide.md` and in
`../ships/unsc-frigate/scripts/Hardpoints/UNSCFrigate.py`.

## Ground-truth workflow (do this once on your PC)
Because the `App.*` API can't be validated off-PC:

1. Pick a stock ship close to your target class (e.g. `Hardpoints/Galaxy.py`,
   `Hardpoints/Sovereign.py`, or a frigate-sized one).
2. **Copy it** into your ship's folder as `STOCK_REFERENCE.py` (do not edit it).
3. Diff our template / the generated UNSC file **against** that stock file: align the exact
   function names, property constructors, and registration calls.
4. Keep the **structure** from the stock file, swap in **our stats** from `05`.
5. The Model Property Editor will round-trip the file — open it in MPE, confirm it parses,
   place hardpoints, save.

This way you get a guaranteed-valid file with our balance baked in, instead of trusting
remembered API names.

→ Next: `05-cross-universe-guide.md`
