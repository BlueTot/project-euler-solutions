#!/bin/python3


from math import sqrt
from functools import cache


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


def num_of_factors(a: dict[int, int], b: dict[int, int]) -> int:
    """
        calculate number of factors of ith triangular number
        where a = dpf(i) and b = dpf(i+1)
        since n = i*(i+1)/2, we merge a, b and subtract 1 from the occurrence of 2
        and apply the formula
        d(n) = (e1+1)(e2+1)...(en+1)

    """
    res = 1

    for k in a.keys():
        if k in b:
            e = a[k]+b[k]-1 if k == 2 else a[k]+b[k]
        else:
            e = a[k]-1 if k == 2 else a[k]
        res *= e+1

    for k in b.keys():
        e = b[k]-1 if k == 2 else b[k]
        res *= e + 1

    return res


def euler12(N: int) -> int:

    # nth triangular number is i*(i+1)/2
    # calculate dpf of i, i+1 for efficiency instead of calculating dpf(n)
    # which grows quadratically by each iteration

    # we calculate d(i*(i+1)/2) by merging dpf of i, i+1
    # iterating until we reach more than N factors

    i = 1
    a, b = dpf(1), dpf(2)

    while True:

        num_factors = num_of_factors(a, b)

        if num_factors > N:
            return i * (i+1) // 2

        i += 1
        a = b
        b = dpf(i+1)


n = int(input())
for _ in range(n):
    print(euler12(int(input())))
