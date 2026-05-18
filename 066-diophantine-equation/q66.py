from math import sqrt

import sys
from fractions import Fraction
from decimal import *

sys.setrecursionlimit(1500)
getcontext().prec = 2000

def _get_coefficients(frac, depth):
    integer_part = int(frac)
    if depth == 1:
        return [integer_part]
    frac_part = frac - Fraction(integer_part, 1)
    reciprocal = 1/ frac_part
    return [integer_part] + _get_coefficients(reciprocal, depth - 1)

def get_coefficients(frac, depth):
    integer_part = int(frac)
    frac_part = frac - Fraction(integer_part, 1)
    reciprocal = 1/ frac_part
    return [integer_part] + _get_coefficients(reciprocal, depth)

class Number:
    def __init__(self, n, d) -> None:
        self.n = n
        self.d = d
    
    def __repr__(self):
        return f"{self.n}/{self.d} = {self.n/self.d}"

def flip(num):
    num.n, num.d = num.d, num.n
    return num

def addint(num, i):
    num.n += num.d * i
    return num

def __evaluate(depth, maxdepth, lst):
    if depth == maxdepth:
        return Number(lst[depth], 1)
    else:
        return addint(flip(__evaluate(depth + 1, maxdepth, lst)), lst[depth])
    
def evaluate(depth, lst):
    if depth == 0:
        return Number(lst[0], 1)
    output = addint(flip(__evaluate(1, depth, lst)), lst[0])
    return output

largestD, largestX = 0, 0
for D in range(1, 1000+1):
    if sqrt(D) % 1 == 0:
        continue
    depth = 1
    while True:
        frac = evaluate(depth, get_coefficients(Fraction(Decimal(D).sqrt()), depth+1))
        x, y = frac.n, frac.d
        # print(frac)
        if x**2 - D * y**2 == 1:
            if x > largestX:
                largestD = D
                largestX = x
            break
        depth += 1
    print(D)
print(largestD, largestX)
