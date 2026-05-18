#!/bin/python3

# precompute list of prime numbers

NUM_PRIMES = 150000
is_prime = [True]*NUM_PRIMES
is_prime[0] = False
is_prime[1] = False

primes = [2]

for num in range(3, NUM_PRIMES+1, 2):
    if is_prime[num]:
        primes.append(num)
        for i in range(num**2, NUM_PRIMES, num):
            is_prime[i] = False


def euler7(N: int) -> int:
    return primes[N-1]

n = int(input())
for _ in range(n):
    print(euler7(int(input())))
