from functools import lru_cache

@lru_cache
def num_ways(m, n):
    if n == 0:
        return 1
    ways = 0
    ways += num_ways(m, n - 1)
    if n >= m:
        ways += num_ways(m, n - m)
    return ways

total = 0
n = 50
for m in (2, 3, 4):
    total += (v := num_ways(m, n) - 1)
    print(v)
print(total)
