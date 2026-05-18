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

def rad(n):
    product = 1
    for f in dpf(n):
        product *= f
    return product

lst = sorted([(rad(n), n) for n in range(1, 10**5+1)])
print(lst[10000-1][1])