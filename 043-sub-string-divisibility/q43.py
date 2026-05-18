from itertools import permutations

def has_property(num):
    # num = str(num).zfill(10)
    if int(num[2-1]+num[3-1]+num[4-1]) % 2 == 0:
        if int(num[3-1]+num[4-1]+num[5-1]) % 3 == 0:
            if int(num[4-1]+num[5-1]+num[6-1]) % 5 == 0:
                if int(num[5-1]+num[6-1]+num[7-1]) % 7 == 0:
                    if int(num[6-1]+num[7-1]+num[8-1]) % 11 == 0:
                        if int(num[7-1]+num[8-1]+num[9-1]) % 13 == 0:
                            if int(num[8-1]+num[9-1]+num[10-1]) % 17 == 0:
                                return True
    return False

total=0
for p in permutations([str(i) for i in range(10)]):
    num = "".join(p)
    if has_property(num):
        print(num)
        total += int(num)
print(total)