from scipy.interpolate import lagrange
import numpy as np

def OP(n):
    x,y = [],[]
    for i in range(1,n):
        print(i)
        y.append(sum([pow((-1*i),p) for p in range(0,11)]))
        x.append(i)
    print(x, y)
    return lagrange(x, y)

p = OP(4)

p.c[np.abs(p.c) < 1e-10] = 0
print(p)