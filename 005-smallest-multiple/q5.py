#!/bin/python3

from math import lcm


def euler5(N: int) -> int:

    nums = list(range(1, N+1))
    return lcm(*nums)


n = int(input())
for _ in range(n):
    print(euler5(int(input())))
