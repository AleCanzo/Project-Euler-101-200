from scipy.interpolate import lagrange
import numpy as np

def OP(n):
    x,y = [],[]
    for i in range(1,n):
        y.append(sum([pow((-1*i),p) for p in range(0,11)]))
        x.append(i)
    return lagrange(x, y)

if __name__=="__main__":
    s = 0
    for i in range(2, 12):    
        p = OP(i)
        p.c[np.abs(p.c) < 1e-1] = 0
        s += int(round(p(i)))
    print(s)