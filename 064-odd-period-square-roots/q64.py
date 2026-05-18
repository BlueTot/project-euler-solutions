from fractions import Fraction
from math import sqrt
from decimal import *
import sys

getcontext().prec = 500
sys.setrecursionlimit(2500)

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

num_odd_periods = 0
for N in range(1, 10000+1):
    if sqrt(N) % 1 == 0:
        continue
    sequence = get_coefficients(Fraction(Decimal(N).sqrt()), 250)
    for idx in range(1, len(sequence)):
        if sequence[idx] == 2 * sequence[0]:
            length = idx
            break
    if length % 2 == 1:
        num_odd_periods += 1
    print(N)

print(num_odd_periods)

