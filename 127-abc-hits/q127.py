from math import gcd, sqrt
from time import perf_counter
from prime_factorisation import factorisation

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

def rad_less_than_c(a, b, c):
    product = 1
    for n in (a, b, c):
        for i in dpf(n):
            product *= i
            if product >= c: return False
    return True

s = perf_counter()
N = 5000
total = 0
n = 0
count, pass_gcd, fail_gcd = 0, 0, 0
for c in range(1, N): # loop through c values from 1 to N-1 inclusive
    # if c % 100 == 0: print(c)
    for b in range(c//2+1, c): # loop through b values from c/2 to c such that b > a
        a = c - b # calculate a
        if gcd(a, b) == 1 and gcd(a, c) == 1 and gcd(b, c) == 1: # check coprime
            pass_gcd += 1
            if rad_less_than_c(a, b, c): # do the check
                total += c
                print(a, b, c, factorisation(c))
                n += 1
        else:
            fail_gcd += 1
        count += 1
print(total)
print(count, pass_gcd, fail_gcd, n)
print(perf_counter() - s)

# def coprime_to_n(n):
#     for i in range(n//2+1, n):
#         if n % i != 0:
#             yield i

# s = perf_counter()
# N = 1000
# total = 0
# count = 0
# hits = 0
# for c in range(1, N):
#     for b in coprime_to_n(c):
#         a = c - b
#         count += 1
#         if gcd(a, c) == 1 and a < b and gcd(a, b) == 1:
#             hits += 1
#             if rad(a, b, c) < c:
#                 total += c
# print(total)
# print(count, hits)
# print(perf_counter() - s)

'''
method 1: 0.7958678000140935
method 2: 0.8357580999727361



'''