def is_pandigital(num):
    num = str(num)
    for i in range(1, len(num)+1):
        if str(i) not in num:
            return False
    return True

# def is_pandigital(number, digit):
#     return {f'{i}' for i in range(1, digit+1)} == set(str(number))

products = set()
for a in range(1, 3000):
    for b in range(1, 3000):
        p = a*b
        together = str(a)+str(b)+str(p)
        if len(together) == 9 and is_pandigital(together, len(together)):
            products.add(p)
    print(a)
print(sum(products))