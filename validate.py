from itertools import product
import random
from engine import resolve

# ---------------------------
# FULL STATE SWEEP
# ---------------------------

def full_state_sweep():
    """Exhaustive 729-state evaluation"""
    states = list(product([0, 1, 2], repeat=3))
    results = {"A": 0, "B": 0, "T": 0}

    for A in states:
        for B in states:
            r = resolve(A, B)
            if r == 1:
                results["A"] += 1
            elif r == -1:
                results["B"] += 1
            else:
                results["T"] += 1

    total = sum(results.values())

    print("\n" + "="*40)
    print("FULL STATE SWEEP (729 STATES)")
    print("="*40)
    print(f"Player A Wins: {results['A']} ({results['A']/total:.2%})")
    print(f"Player B Wins: {results['B']} ({results['B']/total:.2%})")
    print(f"Ties:         {results['T']} ({results['T']/total:.2%})")
    print("="*40)

    return results


# ---------------------------
# MONTE CARLO TEST
# ---------------------------

def random_state():
    """Generate random state tuple"""
    return (
        random.randint(0, 2),
        random.randint(0, 2),
        random.randint(0, 2)
    )


def monte_carlo(n=10000):
    """Monte Carlo sampling validation"""
    results = {"A": 0, "B": 0, "T": 0}

    for _ in range(n):
        A = random_state()
        B = random_state()
        r = resolve(A, B)

        if r == 1:
            results["A"] += 1
        elif r == -1:
            results["B"] += 1
        else:
            results["T"] += 1

    total = sum(results.values())

    print("\n" + "="*40)
    print(f"MONTE CARLO ({n} SAMPLES)")
    print("="*40)
    print(f"Player A Wins: {results['A']} ({results['A']/total:.2%})")
    print(f"Player B Wins: {results['B']} ({results['B']/total:.2%})")
    print(f"Ties:         {results['T']} ({results['T']/total:.2%})")
    print("="*40)

    return results


# ---------------------------
# SWAP TEST (Symmetry Validation)
# ---------------------------

def swap_test():
    """Participant swap symmetry test"""
    states = list(product([0, 1, 2], repeat=3))
    failures = 0

    for A in states:
        for B in states:
            if resolve(A, B) != -resolve(B, A):
                failures += 1

    print("\n" + "="*40)
    print("SWAP TEST (Symmetry Validation)")
    print("="*40)
    print(f"Failures: {failures}")
    if failures == 0:
        print("✓ PERFECT SYMMETRY: resolve(A,B) == -resolve(B,A)")
    else:
        print("✗ SYMMETRY VIOLATED")
    print("="*40)

    return failures == 0


# ---------------------------
# BIAS TEST
# ---------------------------

def bias_test():
    """Check for structural bias in full state space"""
    states = list(product([0, 1, 2], repeat=3))
    results = {"A": 0, "B": 0, "T": 0}

    for A in states:
        for B in states:
            r = resolve(A, B)
            if r == 1:
                results["A"] += 1
            elif r == -1:
                results["B"] += 1
            else:
                results["T"] += 1

    total = sum(results.values())
    a_pct = results["A"] / total
    b_pct = results["B"] / total

    print("\n" + "="*40)
    print("BIAS TEST (Structural Fairness)")
    print("="*40)
    print(f"Player A Win Rate: {a_pct:.2%}")
    print(f"Player B Win Rate: {b_pct:.2%}")
    print(f"Difference: {abs(a_pct - b_pct):.4%}")

    if a_pct == b_pct:
        print("✓ NO STRUCTURAL BIAS")
    else:
        print("⚠ Minor asymmetry (expected with odd state space)")
    print("="*40)

    return abs(a_pct - b_pct) < 0.01


# ---------------------------
# RUN ALL VALIDATION
# ---------------------------

if __name__ == "__main__":
    print("\n" + "█"*40)
    print("█ CDE VALIDATION SUITE")
    print("█"*40)

    full_state_sweep()
    monte_carlo(10000)
    swap_test()
    bias_test()

    print("\n" + "█"*40)
    print("█ VALIDATION COMPLETE")
    print("█"*40 + "\n")
