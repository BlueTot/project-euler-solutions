from fractions import Fraction
from math import gcd

num = int(3/7 * (10**6-1))
den = 10**6 - 1
frac = Fraction(num, den)
print(frac)
print(frac - Fraction(1, 999999))