from math import factorial

curr = 3
total = 0

while len(str(curr)) < 7:
    factsum = sum([factorial(int(digit)) for digit in str(curr)])
    if factsum == curr:
        total += factsum
        print(factsum)
    curr += 1
print(total)