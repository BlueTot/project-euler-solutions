from math import inf, sqrt
from collections import Counter

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

def totient(n):
    product = n
    for num in dpf(n):
        product *= 1 - 1/num
    return round(product)

def highest(n):
    origlst = [int(i) for i in str(n)]
    newlst = []
    while origlst:
        newlst.append(n := max(origlst))
        origlst.remove(n)
    return int("".join(list(map(str, newlst))))


# print(dpf(50))
ratio = inf
valofn = 0
for curr in range(2, 10**7):
    phi = totient(curr)
    if len(str(curr)) == len(str(phi)):
        if highest(curr) == highest(phi):
            if curr/phi < ratio:
                ratio = curr/phi
                valofn = curr
                # print(curr, ratio)
    if curr % 1000 == 0:
        print(curr)
print(valofn)


# print(totient(3))
# ratio = inf
# valofn = 0
# for curr in list_of_primes:
#     phi = curr - 1
#     if len(str(curr)) == len(str(phi)):
#         if highest(curr) == highest(phi):
#     # if dict(Counter([i for i in str(curr)])) == dict(Counter([i for i in str(phi)])):
#             if curr/phi < ratio:
#                 ratio = curr/phi
#                 valofn = curr
#                 print(curr, ratio)
#     if curr % 1000 == 0:
#         print(curr)
# print(valofn)