base = 1
for _ in range(7830457):
    base *= 2
    if len(str(base)) >= 20:
        base = int(str(base)[-10:])
print(base)
base = int(str(base)[-10:])
print(num:=28433*base+1)
print(int(str(num)[-10:]))