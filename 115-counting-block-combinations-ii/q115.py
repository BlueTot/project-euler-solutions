from functools import lru_cache

@lru_cache
def F(m, n):
    if n == 0:
        return 1
    ways = 0
    ways += F(m, n - 1)
    for l in range(m, n+1):
        ways += F(m, n - l - 1 if l != n else 0)
    return ways

m = 50
n = 1
while (v := F(m, n)) <= 10**6:
    print(n, v)
    n += 1
print(n)
    