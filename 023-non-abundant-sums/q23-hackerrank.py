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


abundants = []
for i in range(1, 200000):
    if sum_of_proper_divisors(i) > i:
        abundants.append(i)


def euler23(n: int) -> str:
    left = 0
    right = len(abundants) - 1

    while (left <= right):
        curr = abundants[left] + abundants[right]
        if curr < n:
            left += 1
        elif curr > n:
            right -= 1
        else:
            return "YES"
    
    return "NO"


t = int(input())
for _ in range(t):
    print(euler23(int(input())))



