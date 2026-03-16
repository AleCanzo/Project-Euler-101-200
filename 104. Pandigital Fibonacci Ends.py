import numpy as np
import sys
sys.set_int_max_str_digits(0)

def Fibonacci(n, F):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return F[n-1] + F[n-2]
    
def solution(F):
    Flag = False
    n = 1
    while Flag == False:
        print(n)
        if F[n] == 0:
            F[n] = Fibonacci(n, F)
        fib_num = F[n]
        first_nine = str(fib_num)[0:9]
        last_nine = str(fib_num)[:-10:-1]
        #print(set(last_nine), set(map(str,range(1,10))), n, fib_num)
        if set(first_nine) == set(map(str,range(1,10))) and set(last_nine) == set(map(str,range(1,10))):
            print(first_nine, last_nine, n, fib_num)
            Flag = True
        n += 1
        
if __name__ == "__main__":
    F = [0] * 100_000
    solution(F)
    
    
# Algoritmo lento