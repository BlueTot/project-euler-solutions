def pent(n):
    return n * (3*n-1)//2

def generalised_pents(n):
    for k in range(1, n+1):
        yield (k1 := int(pent(k))), int((-1)**(k+1))
        if n - k1 < 0: break
        yield (k2 := int(pent(-k))), int((-1)**(-k+1))
        if n - k2 < 0: break

def euler78():
    n=1
    lst = [1]+[0]*(n+1)
    while True:
        i = n
        for p, k in generalised_pents(n):
            lst[i] += k * (lst[i - p] if i - p >= 0 else 0)
        if lst[n-1] % 10**6 == 0 and lst[n-1] != 0:
            print(n-1)
            break
        if n % 1000 == 0:
            print(n-1)
        n += 1
        lst.append(0)

if __name__ in "__main__":
    from time import perf_counter
    stime = perf_counter()
    euler78()
    print("time elapsed: ", perf_counter() - stime)

'''best time: 8.638074299989967 seconds'''
