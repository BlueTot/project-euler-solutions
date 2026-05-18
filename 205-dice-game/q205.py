from fractions import Fraction
from time import perf_counter

def prob(dist, n): # Get P(X=n) given distribution of X
    return dist.get(n, 0)

def add(dist1, dist2): # Discrete convolution of X and Y
    dist_sum = {}
    for n in range(min(dist1)+min(dist2), max(dist1)+max(dist2)+1):
        total = 0
        for k in range(n+1):
            total += prob(dist1, k) * prob(dist2, n-k)
        dist_sum[n] = total
    return dist_sum

def p_greater_than(dist, n): # Get P(X>n) given distribution of X
    total = 0
    for x, p in dist.items():
        if x > n:
            total += p
    return total

def prob_dist(N): # Get probability distribution for Peter (9 throws) and Colin (6 throws)
    D = 36 // N

    dist1 = {i : Fraction(1)/Fraction(N) for i in range(1, N+1)}
    distsum = dist1.copy()
    for _ in range(2, D+1):
        distsum = add(dist1, distsum)

    return distsum

def euler205():

    X = prob_dist(4) # Peter
    Y = prob_dist(6) # Colin

    print(X)
    print(Y)

    # Find P(X>Y) using double for loop
    total = 0
    for x in X:
        for y in Y:
            if x > y:
                total += X[x] * Y[y]
    
    return round(total, 7)

if __name__ in "__main__":
    t = perf_counter()
    print(euler205())
    print(f"time taken: {perf_counter() - t}s")