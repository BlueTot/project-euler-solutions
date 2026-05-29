#!/bin/python3

from math import factorial


def euler20(N: int) -> int:
    return sum([int(char) for char in str(factorial(N))])

t = int(input())
for _ in range(t):
    print(euler20(int(input())))
