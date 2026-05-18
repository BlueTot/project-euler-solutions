maxdigitsum=0
for a in range(1, 100):
    for b in range(1, 100):
        num = a**b
        digitsum = sum([int(i) for i in str(num)])
        maxdigitsum = max(maxdigitsum, digitsum)
print(maxdigitsum)