#!/bin/python3

from math import comb


# we must make N vertical movements and M horizontal movements to get to the 
# bottom right

# there are (N+M)! ways to arrange everything
# divide by N! * M! to account for rearrangements within the same movement type
# since that doesn't make a difference

# so formula is (N+M)!/(N! M!) = N+M choose N

MOD = 10**9 + 7

def euler15(N: int, M: int) -> int:
    return comb(N+M, N) % MOD


n = int(input())
for _ in range(n):
    N, M = list(map(int, input().split()))
    print(euler15(N, M))

