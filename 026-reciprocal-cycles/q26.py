from decimal import *

getcontext().prec = 2000

lengths = {}
for d in range(1, 1000):

    num = Decimal(1)/Decimal(d)
    s = str(num)
    if len(s) < 10:
        lengths[d] = 0
        continue
    dpart = s[s.index(".")+1:]

    for startidx in range(len(dpart)):
        found = False
        for endidx in range(startidx+1, len(dpart)//2):
            curr = dpart[startidx:endidx]
            if curr == dpart[endidx:endidx+len(curr)] and curr != "0":
                found = True
                break
        if found:
            lengths[d] = len(curr)
            break  

    # print(d)
print(lengths)

largestk, largestv = 0, 0
for k, v in lengths.items():
    if v > largestv:
        largestv = v
        largestk = k
print(largestk, largestv)

    
            