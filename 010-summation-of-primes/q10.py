#!/bin/python3

from bisect import bisect_left

n = 2000000
is_prime = [True]*n
is_prime[0] = False
is_prime[1] = False
primes = [2]

for num in range(3, n+1, 2):
    if is_prime[num]:
        primes.append(num)
        for i in range(num**2, n, num):
            is_prime[i] = False

# construct prefix sum of prime numbers

total = 0
prefix = []
for p in primes:
    total += p
    prefix.append(total)


def euler10(N: int) -> int:

    # get the largest index for which array[value] <= N
    # then return its prefix sum
    
    index = bisect_left(primes, N+1)
    return prefix[index-1]


n = int(input())
for _ in range(n):
    print(euler10(int(input())))

