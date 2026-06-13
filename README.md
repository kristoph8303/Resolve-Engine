# Showdown Engine

A deterministic duel resolution system built on a symmetric 3-layer decision model.

## Core Model

Each player submits a 5-part state vector:

- **Zone** (0–2)
- **Action** (0–2)
- **Intensity** (0–2)


Outcome is resolved using deterministic symmetric operators:

- **ZR** (Zone Relation)
- **AM** (Action Matrix)
- **IC** (Intensity Comparison)


## Properties

- ✅ Full-state enumeration verified (729-state sweep)
- ✅ Symmetry invariance confirmed (0% bias in deterministic sweep)
- ✅ No dominant strategy exists under cyclic core design

## Ghost Mirror (Optional Layer)

A non-strategic stand-in system that generates synthetic opponent states by applying bounded stochastic variation to a reference player state.

### Purpose:
- Simulation
- Testing
- AI-less opponent modeling
- Replay scaffolding

**The Ghost Mirror does NOT affect core resolution logic.**

## Philosophy

> A deterministic system where complexity emerges from structure, not randomness.

---

## Project Structure

```
showdown-engine/
├── engine/
│   ├── core.py              # ZR / AM / IC + resolve()
│   ├── tests.py             # sweep, symmetry, bias checks
│
├── ghost/
│   ├── mirror.py            # Ghost stand-in logic
│
├── sim/
│   ├── random_sim.py        # Random state simulations
│   ├── numpy_sim.py         # Vectorized numpy simulations
│
├── ui/
│   ├── index.html           # Showdown UI
│   ├── styles.css           # Styling (optional split)
│   ├── app.js               # Application logic (optional split)
│
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

---

## Quick Start

### 1. Run Core Engine Tests

```bash
python -m engine.tests
```

### 2. Run Simulations

```bash
# Random simulation
python -m sim.random_sim

# NumPy vectorized simulation
python -m sim.numpy_sim
```

### 3. Launch UI

Open `ui/index.html` in a web browser.

---

## Validation

- Full 729-state sweep confirms zero structural bias
- Participant swap symmetry: `resolve(A, B) = -resolve(B, A)`
- No dominant strategy in any state subset

---

## License

Showdown Engine - Deterministic Duel Resolution System
