#!/bin/python3

def euler2(N):

    a, b = 1, 2
    total = 2

    while True:
        a, b = b, a + b
        if b > N:
            break
        total += b if b % 2 == 0 else 0

    return total

n = int(input())
for _ in range(n):
    print(euler2(int(input())))

