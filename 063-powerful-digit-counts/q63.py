ns = 0
for power in range(1, 1001):
    base = 1
    while True:
        num = base ** power
        if len(str(num)) == power:
            print(base, power, num)
            ns += 1
        if len(str(num)) > power:
            break
        base += 1
print(ns)