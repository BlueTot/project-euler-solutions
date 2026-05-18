#!/bin/python3

def sum_of_squares(n: int) -> int:
    return n * (n+1) * (2*n+1) // 6

def square_of_sum(n: int) -> int:
    sum = n * (n+1) // 2
    return sum * sum

def euler6(N: int) -> int:
    return square_of_sum(N) - sum_of_squares(N)

n = int(input())
for _ in range(n):
    print(euler6(int(input())))
