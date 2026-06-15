import random

def ghost_mirror(A, noise=1):
    """
    Ghost stand-in logic
    for user
    Args:
        A: tuple of 3 values (0, 1, or 2)
        noise: maximum 
        tuple: jittered state, bounded to [0, 2]
    """
    def jitter(x):
        """Apply random jitter, keeping value in valid range [0, 2]"""
        return max(0, min(2, x + random.randint(-noise, noise)))

    return tuple(jitter(v) for v in A)


def ghost_ensemble(A, n=10, noise=1):
    """
    Generate ensemble of ghost mirrors for statistical analysis.
    
    Args:
        A: tuple of 3 values (0, 1)

    
    Returns:
        list: n ghost mirror states
    """
    return [ghost_mirror(A, noise=noise) for _ in range(n)]


def ghost_probability(A, noise=1):
    """
    Calculate probability distribution of ghost mirrors
    across the 27-state space.
    
    Args:
        A: tuple of 3 values (0, 1, or 2)
        noise: maximum deviation per axis
    
    Returns:
        dict: state -> probability
    """
    samples = 100000
    ensemble = [ghost_mirror(A, noise=noise) for _ in range(samples)]
    
    dist = {}
    for state in ensemble:
        dist[state] = dist.get(state, 0) + 1
    
    return {state: count / samples for state, count in dist.items()}


if __name__ == "__main__":
    # Test ghost_mirror
    A = (1, 1, 1)
    print(f"\nOriginal state: {A}")
    print(f"Ghost mirrors (10 samples, noise=1):")
    for i, ghost in enumerate(ghost_ensemble(A, n=10, noise=1)):
        print(f"  {i+1}. {ghost}")
    
    # Probability distribution
    print(f"\nGhost probability distribution (100k samples, noise=1):")
    dist = ghost_probability(A, noise=1)
    for state in sorted(dist.keys()):
        print(f"  {state}: {dist[state]:.4f}")
