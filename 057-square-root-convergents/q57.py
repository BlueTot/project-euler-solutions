import sys

sys.setrecursionlimit(1500)

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

def __evaluate(depth):
    if depth == 1:
        return Number(2, 1)
    else:
        return addint(flip(__evaluate(depth - 1)), 2)
    
def evaluate(depth):
    output = addint(flip(__evaluate(depth)), 1)
    return output

total = 0
for expansion in range(1, 1000+1):
    num = evaluate(expansion)
    if len(str(num.n)) > len(str(num.d)):
        total += 1
    print(expansion)
    print(num)
print(total)

