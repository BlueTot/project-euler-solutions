def is_pandigital(num):
    for i in range(1, 10):
        if str(i) not in num:
            return False
    return True

pans = set()
for num in range(1, 10000000):
    s = ""
    n = 1
    while len(s) < 9:
        s += str(num*n)
        n += 1
    if len(s) == 9 and n > 2 and is_pandigital(str(s)):
        pans.add(int(s))
print(max(pans))