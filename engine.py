# Cyclic Decision Engine (CDE) - CORE MECHANIC

from itertools import product
import random

# ---------------------------
# CYCLIC AXES
# ---------------------------

def ZR(a, b):
    if a == b:
        return 0
    if (a == 0 and b == 2) or (a == 1 and b == 0) or (a == 2 and b == 1):
        return 1
    return -1


def AM(a, b):
    if a == b:
        return 0
    if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
        return 1
    return -1


def IC(a, b):
    if a == b:
        return 0
    if abs(a - b) == 2:
        return 1 if a > b else -1
    return 0


# ---------------------------
# CORE RESOLVER
# ---------------------------

def resolve(A, B):
    score = (
        ZR(A[0], B[0]) +
        AM(A[1], B[1]) +
        IC(A[2], B[2])
    )

    if score > 0:
        return 1
    elif score < 0:
        return -1
    else:
        return 0


# ---------------------------
# FULL STATE SWEEP
# ---------------------------

def full_state_sweep():
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

    print("\nFULL STATE SWEEP (729 STATES)")
    print("--------------------------------")
    print("A:", results["A"] / total)
    print("B:", results["B"] / total)
    print("T:", results["T"] / total)


# ---------------------------
# MONTE CARLO TEST
# ---------------------------

def random_state():
    return (
        random.randint(0, 2),
        random.randint(0, 2),
        random.randint(0, 2)
    )


def monte_carlo(n=10000):
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

    print("\nMONTE CARLO")
    print("----------------")
    print(results)


# ---------------------------
# SWAP TEST
# ---------------------------

def swap_test():
    states = list(product([0, 1, 2], repeat=3))
    failures = 0

    for A in states:
        for B in states:
            if resolve(A, B) != -resolve(B, A):
                failures += 1

    print("\nSWAP TEST")
    print("Failures:", failures)


# ---------------------------
# RUN ALL
# ---------------------------

if __name__ == "__main__":
    full_state_sweep()
    monte_carlo()
    swap_test()
