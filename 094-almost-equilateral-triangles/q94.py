
def pyths(N) : 
    c, m = 0, 2
    while c < N : 
        for n in range(1, m) : 
            a = m**2  - n**2
            b = 2*m*n
            c = m**2 + n**2
            if c > N : 
                break
            yield a, b, c
        m  += 1

if __name__ == '__main__' : 

    p = 0
    N = 10**9 // 3 + 2
    for a, b, c in pyths(N):
        a, b, c = sorted([a, b, c])
        if abs(c-a) == 1 and c+c+a <= 10**9:
            #print(a, b, c)
            p += c+c+a
        elif abs(c-b) == 1 and c+c+b <= 10**9:
            #print(a, b, c)
            p += c+c+b
    print(p)

#4303370341998
#518408346