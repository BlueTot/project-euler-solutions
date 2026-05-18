def m(k):
    if k == 1:
        return 0
    min_mults = float("inf")
    for i in range(1, k // 2 + 1):
        if i == k-i:
            min_mults = min(min_mults, m(i) + 1)
        else:
            min_mults = min(min_mults, m(i) + m(k-i) + 1)
    return min_mults


for i in range(1, 16):
    print(i, m(i))
