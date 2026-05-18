from functools import lru_cache

N = 100

@lru_cache
def num_increasing(N, prev=0):
    if N == 0:
        return 1
    ways = 0
    for n in range(prev+1 if prev == 0 else prev, 10):
        ways += num_increasing(N-1, prev=n)
    return ways

@lru_cache
def num_decreasing(N, prev=10):
    if N == 0:
        return 1
    ways = 0
    for n in range(prev, -1 if N > 1 else 0, -1):
        ways += num_decreasing(N-1, prev=n)
    return ways

total = 0
for i in range(1, N+1):
    total += num_increasing(i)
    total += num_decreasing(i) - 10
print(total)
