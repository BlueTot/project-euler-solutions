from math import sqrt

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = set()
    list_of_primes.add(2)

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.add(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

N = 10**8
ps = primes(N)
is_prime = lambda n :  n in ps

def dpf(num):
    if num % 2 == 0:
        num //= 2
        if is_prime(num): return [2, num]
        else: return
    for factor in range(3, int(sqrt(num))+1, 2): # O(sqrt N) time complexity
        if num % factor == 0:
            num //= factor
            if is_prime(num): return [factor, num]
            else: return

total = 0
for num in range(1, N):
    if num % 10**5 == 0:
        print(num)
    if not is_prime(num): # composite
        if (root := sqrt(num)) % 1 == 0 and is_prime(root):
            total += 1
        elif (factors := dpf(num)) is not None:
            total += 1
print(total)

