n=100
lst = [0]*(n+1)
lst[0]=1
for i in range(1, n):
    for j in range(n+1):
        if j - i >= 0:
            lst[j] += lst[j - i]
print(lst)
print(lst[n])