#!/bin/python3

def euler16(N: int) -> int:
    return sum([int(char) for char in str(1 << N)])

t = int(input())
for _ in range(t):
    print(euler16(int(input())))

