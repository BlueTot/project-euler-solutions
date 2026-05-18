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

def totient(n):
    if n == 1:
        return 1
    product = n
    for num in dpf(n):
        product *= 1 - 1/num
    return round(product)

total = 0
for d in range(2, 10**6+1):
    total += totient(d)
    if d % 1000 == 0:
        print(d)

print(total)
