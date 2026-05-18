X = [1, 7]
Y = [1, 5]
D=2

found = False
while not found:
    x = X[-2]*X[0]**2+D*X[-2]*Y[0]**2+2*D*Y[-2]*Y[0]*X[0]
    y = Y[-2]*X[0]**2+D*Y[-2]*Y[0]**2+2*X[-2]*Y[0]*X[0]
    X.append(x)
    Y.append(y)
    b, t = (1+y)/2, (1+x)/2
    if t > 10**12:
        print(b, t)
        found = True