unique_nums = set()

for a in range(2, 101):
    for b in range(2, 101):
        unique_nums.add(a ** b)
print(len(unique_nums))