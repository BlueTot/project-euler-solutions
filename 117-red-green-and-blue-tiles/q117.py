from functools import lru_cache

@lru_cache
def num_ways(n):
    if n == 0:
        return 1
    ways = 0
    ways += num_ways(n - 1)
    for l in (2, 3, 4):
        if n - l >= 0:
            ways += num_ways(n - l)
    return ways

print(num_ways(50))
