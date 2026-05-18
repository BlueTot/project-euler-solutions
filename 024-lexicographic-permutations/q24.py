from itertools import permutations

lst = []
for p in permutations([str(i) for i in range(10)]):
    lst.append("".join(list(p)))
print(lst[10**6-1])