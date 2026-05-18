def reverse(num):
    lst = [i for i in str(num)]
    lst.reverse()
    return int("".join(list(map(str, lst))))

def is_odd(num):
    for char in str(num):
        if int(char) % 2 == 0:
            return False
    return True

total = 0
for num in range(1, 10**9, 2):
    if str(num)[0] == str(num)[-1]: continue
    if num % (10**6) == 1:
        print(num)
    if is_odd(num + reverse(num)):
        total += 2
print(total)