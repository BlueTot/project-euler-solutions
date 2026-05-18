def proper_divisors(num):
    factors = []
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0 and factor != num:
            factors.append(factor)
            if factor != num / factor and num//factor != num:
                factors.append(num//factor)
    return factors

amicables = set()
for a in range(1, 10000):
    b = sum(proper_divisors(a))
    if sum(proper_divisors(b)) == a and a != b:
        amicables.add(a)
        amicables.add(b)
        print(a, b)
print(sum(amicables))
