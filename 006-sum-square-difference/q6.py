s1 = sum([i**2 for i in range(1, 101)])
s2 = sum([i for i in range(1, 101)]) ** 2
print(abs(s2 - s1))