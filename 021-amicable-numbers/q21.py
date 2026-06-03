#!/bin/python3

from functools import cache
from math import sqrt


@cache
def dpf(num: int) -> dict[int, int]:
    """
        find distinct prime factors of number
        returning dictionary of (factor, ocurrence)
    """
    factors = {}
    while num % 2 == 0:
        num //= 2
        factors[2] = factors.get(2, 0) + 1
    for f in range(3, int(sqrt(num))+1, 2):
        while num % f == 0:
            factors[f] = factors.get(f, 0) + 1
            num //= f
    if num > 2:
        factors[num] = factors.get(num, 0) + 1
    return factors


@cache
def sum_of_proper_divisors(n: int) -> int:
    """
        calculates the sum of proper divisors of a number n
    """
    if n == 0:
        return 0
    
    res = 1

    for p, e in dpf(n).items():
        res *= (p ** (e+1) - 1) // (p - 1)

    return res - n


# precomputation


MAX_N = 100000
res = [0]*(MAX_N+1)

curr = 0
visited = set()

for a in range(1, MAX_N):
    b = sum_of_proper_divisors(a)
    if sum_of_proper_divisors(b) == a and a != b:
        if a not in visited:
            curr += a
            visited.add(a)
        if b < a and b not in visited:
            curr += b
            visited.add(b)

    res[a] = curr


def euler21(N: int) -> int:
    return res[N]


t = int(input())
for _ in range(t):
    print(euler21(int(input())))
