num_ways = [0]*201
num_ways[0] = 1
for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
    for v in range(201):
        if v - coin >= 0:
            num_ways[v] += num_ways[v - coin]
print(num_ways)
print(num_ways[200])
