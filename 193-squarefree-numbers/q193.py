# from math import sqrt

# def square_free(num):
#     factors = set()
#     while num % 2 == 0:
#         num //= 2
#         if 2 not in factors:
#             factors.add(2)
#         else:
#             return False
#     for factor in range(3, int(sqrt(num))+1, 2):
#         while num % factor == 0:
#             if factor not in factors:
#                 factors.add(factor)
#             else:
#                 return False
#             num //= factor
#     if num > 2:
#         factors.add(num)
#     return True

# total = 0
# for n in range(1, 2**50):
#     if n % 4 == 0: continue
#     if square_free(n):
#         total += 1
#     if n % 10**4 == 1: print(n)
# print(total)

def primes(n):
    primes = [True]*n
    primes[0] = False
    primes[1] = False
    list_of_primes = [2]

    for num in range(3, n+1, 2):
        if primes[num]:
            list_of_primes.append(num)
            for i in range(num**2, n, num):
                primes[i] = False
    return list_of_primes

ps = primes(10**6)

idx = 0
n = ps[0]
while n < 10**6:
    print(idx)
    if idx != 0: n *= ps[idx]
    for k in range(1, ps[idx+1]):
        print(n*k)
    idx += 1