from collections import Counter

def digits_in(num):
    return set(dict(Counter(str(num))).keys())

curr = 1
while True:
    ds = set.union(*[digits_in(curr*i) for i in range(1, 7)])
    if ds == digits_in(curr):
        print(curr)
        break
    if curr % 100 == 0:
        print(curr)
    curr += 1