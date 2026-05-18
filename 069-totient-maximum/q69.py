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
    if len(factors) == 0:
        factors.add(num)
    return factors

def totient(n):
    product = n
    for num in dpf(n):
        product *= 1 - 1/num
    return round(product)

# maxresult, maxn = 0, 0
# for n in range(2, 10**6+1):
#     phi = totient(n)
#     result = n / phi
#     if result > maxresult:
#         maxresult = result
#         maxn = n
#         # print(n)
#     if n % 1000 == 0:
#         print(n)
# print(maxresult, maxn)

for i in range(2, 100):
    print(i, i, totient(i), i/totient(i))
    print(dpf(i))