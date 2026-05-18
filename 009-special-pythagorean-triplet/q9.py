for a in range(3, 999):
    for b in range(3, 999):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a+b+c == 1000:
            print(a*b*c)

