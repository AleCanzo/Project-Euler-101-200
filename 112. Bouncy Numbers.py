def is_bouncy(n):
    n_str = str(n)
    bouncy = False
    not_bouncy = True
    for i in range(len(n_str)):
        
        
    return 

if __name__ == "__main__":
    n = 1
    num_bouncy = 0
    Flag = False
    while Flag == False:
        if is_bouncy(n):
            num_bouncy += 1
        if (num_bouncy*100)/n == 99:
            Flag == True
        n += 1