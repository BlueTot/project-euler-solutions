from math import log10

def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

a = []

nth_powers = []
for n in range(2, 100):
    for power in range(2, 10):
        nth_powers.append(n**power)

for n in sorted(nth_powers):
    if len(str(n)) >= 2:
        s = sum_of_digits(n)
        try:
            power = round(log10(n)/log10(s))
            if s ** power == n and n not in a:
                print(n)
                a.append(n)
        except ZeroDivisionError:
            pass

print(a)
print(len(a))
print(a[29])