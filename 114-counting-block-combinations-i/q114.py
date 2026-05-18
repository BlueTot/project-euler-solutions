from functools import lru_cache

@lru_cache
def num_ways(length):
    if length == 0:
        return 1
    ways = 0
    ways += num_ways(length - 1)
    for l in range(3, length+1):
        ways += num_ways(length - l - 1 if l != length else 0)
    return ways

print(num_ways(50))
    