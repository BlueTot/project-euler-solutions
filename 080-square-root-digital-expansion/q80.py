import decimal
import math

decimal.getcontext().prec = 102

def sum_up_to(n):

    Sum = 0
    for n in range(1, n+1):
        if int(math.sqrt(n))**2 != n:
            dec = decimal.Decimal(n).sqrt()
            s = str(dec)
            s = s[0]+s[2:-2]
            print(s)
            total = sum([int(n) for n in s if n != "."])
            Sum += total
    return Sum

print(sum_up_to(100))
# decimal.getcontext().prec = 100
# print(sum_up_to(2))