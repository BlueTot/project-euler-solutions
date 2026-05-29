#!/bin/python3


def euler18(tri: list[list[int]]) -> int:
    max_row = len(tri)-2
    for row in range(max_row, -1, -1):
        for col in range(row+1):
            tri[row][col] += max(tri[row+1][col], tri[row+1][col+1])    
    return tri[0][0]


t = int(input())
for _ in range(t):
    n = int(input())
    tri = []
    for _ in range(n):
        tri.append(list(map(int, input().split())))
    print(euler18(tri))

