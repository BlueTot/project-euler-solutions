from random import randint

N = 10**6
balls = list("".join([colour*10 for colour in ("R","O","Y","G","B","I","V")]))
total = 0
for _ in range(N):
    if _ % 10 **4 == 0:
        print(_)
    curr_balls = balls[:]
    colours = set()
    for _ in range(20):
        num = randint(0, len(curr_balls) - 1)
        colours.add(curr_balls.pop(num))
    total += len(colours)
print(total/N)
        