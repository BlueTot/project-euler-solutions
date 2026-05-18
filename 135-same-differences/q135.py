def divisors(num):
    for factor in range(1, int(num ** 0.5)+1):
        if num % factor == 0:
            yield factor, num//factor

total = 0
for n in range(1, 10**6):
    nsols = set()
    for f1, f2 in divisors(n):
        for y in (f1, f2):
            if (d := (-f1-f2)/4) % 1 == 0:
                if (y - d) > 0 and (y + d) > 0:
                    nsols.add(tuple(sorted((y - d, y, y+d))))
    if len(nsols) == 10:
        total += 1
        print(n, len(nsols))
print(total)