def is_bouncy(num):
    s = str(num)
    inc, dec = False, False
    for idx in range(len(s)-1):
        if int(s[idx+1]) > int(s[idx]):
            inc = True
        elif int(s[idx+1]) < int(s[idx]):
            dec = True
        if inc and dec:
            return True
    return False

num_bouncy = 0
n = 100
while True:
    n += 1
    print(n, num_bouncy/n)
    if is_bouncy(n):
        num_bouncy += 1
    if num_bouncy / n == 0.99:
        print(n)
        break
    