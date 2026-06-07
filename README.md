# 📘 Cyclic Decision Engine (CDE)

## Overview

The Cyclic Decision Engine is a deterministic multi-axis competitive decision system that preserves strategic diversity, avoids dominant strategies, and maintains meaningful uncertainty through cyclic resolution mechanics.

---

## Core Concept

The engine evaluates two participants using three interacting decision axes:

- **ZR (Zone Read)** - Cyclic dominance: 0→2→1→0
- **AM (Action Model)** - Cyclic dominance: 0→1→2→0
- **IC (Intensity Control)** - Absolute difference dominance: |a-b|=2

Each axis follows a cyclic dominance structure, ensuring no permanent optimal strategy exists.

---

## System Properties

- ✅ Deterministic resolution
- ✅ Full-state symmetry (validated via exhaustive enumeration)
- ✅ No dominant strategy under cyclic equilibrium
- ✅ Stable entropy distribution across state space

---

## Resolution Mechanics

### Total Score Calculation

```
TOTAL SCORE = ZR(A, B) + AM(A, B) + IC(A, B)
```

Each axis returns:
- **+1** (win)
- **0** (tie)
- **-1** (loss)

### Result Interpretation

- **Score > 0** → Player A wins
- **Score < 0** → Player B wins
- **Score = 0** → Tie

---

## Validation Methods

- ✅ Full-state sweep (729-state evaluation)
- ✅ Monte Carlo sampling
- ✅ Participant swap symmetry test
- ✅ Vectorized numpy verification

---

## Core Guarantee

The system maintains:

> **Symmetry under participant swap**  
> **Zero structural bias under full enumeration**  
> **Stable cyclic interaction across all axes**

---

## Status

| Component | Status |
|-----------|--------|
| Core | Frozen ✓ |
| Validation | Complete ✓ |
| Layer System | Optional (future expansion) |

---

## Usage

### Run Core Engine with Validation

```bash
python engine.py
```

### Run Validation Suite

```bash
python validate.py
```

---

## Project Structure

```
Resolve-Engine/
├── README.md          # This file
├── engine.py          # Core mechanic (deterministic resolver)
├── validate.py        # Validation suite (sweep, Monte Carlo, swap test)
└── CDE_MISSION.md     # Detailed mission & concept documentation
```

---

## Quick Start

1. **Review the mechanics**: See `CDE_MISSION.md`
2. **Run the engine**: `python engine.py`
3. **Validate symmetry**: `python validate.py`

---

## License

This is the Cyclic Decision Engine core specification.
