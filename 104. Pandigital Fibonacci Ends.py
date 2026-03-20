import sys
sys.set_int_max_str_digits(0)
    
def solution(F):
    Flag = False
    n = 3
    while Flag == False:
        #print(n)
        F[n] = F[n-1] + F[n-2]
        fib_num = F[n]
        first_nine = str(fib_num)[0:9]
        last_nine = str(fib_num)[:-10:-1]
        if set(first_nine) == set(map(str,range(1,10))) and set(last_nine) == set(map(str,range(1,10))):
            print(first_nine, last_nine, n, fib_num)
            Flag = True
        n += 1
        
if __name__ == "__main__":
    F = [0] * 150_000
    F[1] = 1
    F[2] = 1
    solution(F)
