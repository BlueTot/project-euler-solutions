import sys

sys.setrecursionlimit(1900)

a = 1777
b = 1855

digits = 8

def exp(a, k):
    base = 1
    count = 0
    while count < k:
        base = (base * a) % (10**digits)
        if base == 1777 and (count + 1250000) < k:
            count += ((k - count)//1250000)*1250000
        count += 1
    return base

def tetration(a, k):
    if k == 1:
        return a
    output = exp(a, tetration(a, k - 1)) % (10**digits)
    print(k)
    return output

print(tetration(a, b))