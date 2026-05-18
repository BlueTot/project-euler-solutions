num = 20
while True:
    for divisor in range(1, 21):
        if num % divisor != 0:
            break
    else:
        print(num)
        break
    if num % 1000 == 0:
        print(num)
    num += 20