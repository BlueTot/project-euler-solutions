#!/bin/python3

from bisect import bisect_left

def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]

# precompute all palindromic products and sort them

palindromic_products = []
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i * j
        if is_palindrome(p):
            palindromic_products.append(p)

palindromic_products.sort()

def euler4(N: int) -> int:

    # returns the index in the list where N is inserted
    # first index where array[index] >= N
    # we want < N so we subtract 1

    index = bisect_left(palindromic_products, N)
    return palindromic_products[index-1]

n = int(input())
for _ in range(n):
    print(euler4(int(input())))
