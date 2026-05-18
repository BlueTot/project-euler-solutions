#!/bin/python3

from math import ceil

def sum_to_N(n):
    return n*(n+1)//2

def euler1(N):
    multiples_of_3 = 3 * sum_to_N(ceil(N/3 - 1))
    multiples_of_5 = 5 * sum_to_N(ceil(N/5 - 1))
    multiples_of_15 = 15 * sum_to_N(ceil(N/15 - 1))
    return multiples_of_3 + multiples_of_5 - multiples_of_15

n = int(input())
for _ in range(n):
    print(euler1(int(input())))

