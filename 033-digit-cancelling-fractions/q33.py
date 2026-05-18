fractions = set()
for n in range(10, 99):
    for d in range(n+1, 99):
        if not (n % 10 == 0 and d % 10 == 0):
            if str(n)[0] == str(d)[0]:
                pos_to_rmv = (0, 0)
            elif str(n)[0] == str(d)[1]:
                pos_to_rmv = (0, 1)
            elif str(n)[1] == str(d)[0]:
                pos_to_rmv = (1, 0)
            elif str(n)[1] == str(d)[1]:
                pos_to_rmv = (1, 1)
            else:
                pos_to_rmv = None
            if pos_to_rmv is not None:
                nn = str(n)[1-pos_to_rmv[0]]
                nd = str(d)[1-pos_to_rmv[1]]
                try:
                    if int(nn)/int(nd) == n/d:
                        fractions.add((n, d))
                except ZeroDivisionError:
                    pass
print(fractions)
num, den = 1, 1
for frac in fractions:
    num *= frac[0]
    den *= frac[1]
print(num, den)
            