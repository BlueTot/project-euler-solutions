#!/bin/python3

from math import sqrt

def dpf(num):
    factors = set()
    while num % 2 == 0:
        num //= 2
        factors.add(2)
    for factor in range(3, int(sqrt(num))+1, 2):
        while num % factor == 0:
            factors.add(factor)
            num //= factor
    if num > 2:
        factors.add(num)
    return factors

def euler3(N):
    return max(dpf(N))

n = int(input())
for _ in range(n):
    print(euler3(int(input())))

