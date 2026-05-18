from math import sqrt

def dpf(num):
    factors = set()
    while num % 2 == 0:
        num //= 2
        factors.add(2)
    for factor in range(3, int(sqrt(num))+1, 2):
        while num % factor == 0:
            factors.add(factor)
            num //= factor
    if num > 2:
        factors.add(num)
    return factors

def is_hamming(num, n):
    for f in dpf(num):
        if f > n:
            return False
    else:
        return True

total = 0
for n in range(1, 10**9):
    if is_hamming(n, 100):
        total += 1
    print(n)