const = ""
curr = 1
while len(const) < 10**6:
    const += str(curr)
    curr += 1
# print(const)
print(int(const[0])*int(const[10-1])*int(const[10**2-1])*int(const[10**3-1])*int(const[10**4-1])*int(const[10**5-1])**int(const[10**6-1]))
