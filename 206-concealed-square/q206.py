from math import sqrt

num = int(sqrt(19293949596979899))+1

def is_valid(num):
    for i in range(1, 10):
        if str(num)[2*(i-1)] != str(i):
            return False
    return True
    
while True:
    print(num)
    if is_valid(num**2):
        print(num * 10)
        break
    num -= 2