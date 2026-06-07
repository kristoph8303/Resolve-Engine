# Cyclic Decision Engine (CDE)

## Mission

To provide a deterministic multi-axis competitive decision system that preserves strategic diversity, avoids dominant strategies, and maintains meaningful uncertainty through cyclic resolution mechanics.

---

## Core Concept

The engine evaluates two participants using three interacting decision axes:

- ZR (Zone Read)
- AM (Action Model)
- IC (Intensity Control)

Each axis follows a cyclic dominance structure, ensuring no permanent optimal strategy exists.

---

## System Properties

- Deterministic resolution
- Full-state symmetry (validated via exhaustive enumeration)
- No dominant strategy under cyclic equilibrium
- Stable entropy distribution across state space

---

## Core Rule Structure

Each match is resolved as:

Where each axis returns:
- +1 (win)
-  0 (tie)
- -1 (loss)

---

## Validation Methods

- Full-state sweep (729-state evaluation)
- Monte Carlo sampling
- Participant swap symmetry test
- Vectorized numpy verification

---

## Core Guarantee

The system maintains:

> Symmetry under participant swap  
> Zero structural bias under full enumeration  
> Stable cyclic interaction across all axes  

---

## Usage

```bash
python engine.py
```