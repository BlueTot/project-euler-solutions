sum_of_rmax = 0
for a in range(3, 1000+1):
    curr_max = 0
    for n in range(1, 10000, 2):
        r = (2*a*n) % (a**2)
        curr_max = max(r, curr_max)
    print(a, curr_max)
    sum_of_rmax += curr_max
print(sum_of_rmax)
