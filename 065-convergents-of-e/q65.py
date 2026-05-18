import sys

sys.setrecursionlimit(1500)

n = 10000
lst = [2, 1, 2, 1, 1, 4, 1, 1, 6]
for i in range(n):
    lst += [1, 1, 2 * i + 8]

class Number:
    def __init__(self, n, d) -> None:
        self.n = n
        self.d = d
    
    def __repr__(self):
        return f"{self.n}/{self.d} = {self.n/self.d}"

def flip(num):
    num.n, num.d = num.d, num.n
    return num

def addint(num, i):
    num.n += num.d * i
    return num

def __evaluate(depth, maxdepth):
    if depth == maxdepth:
        return Number(lst[depth], 1)
    else:
        return addint(flip(__evaluate(depth + 1, maxdepth)), lst[depth])
    
def evaluate(depth):
    if depth == 0:
        return Number(lst[0], 1)
    output = addint(flip(__evaluate(1, depth)), lst[0])
    return output


# total = 0
# for expansion in range(20):
#     num = evaluate(expansion)
#     if len(str(num.n)) > len(str(num.d)):
#         total += 1
#     print(expansion)
#     print(num)
# print(total)

n=100
num = evaluate(n-1)
numerator = str(num.n)
digits = sum([int(i) for i in numerator])
# print(num)
print(digits)

