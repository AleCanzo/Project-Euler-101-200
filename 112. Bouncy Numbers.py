def is_bouncy(n):
    n_str = str(n)
    type_n = None
    for i in range(len(n_str)):
        if i == 0:
            continue
        if int(n_str[i]) > int(n_str[i-1]):
            if type_n == "decresc":
                return True
            elif type_n == None:
                type_n = "cresc"
        elif int(n_str[i]) < int(n_str[i-1]):
            if type_n == "cresc":
                return True
            elif type_n == None:
                type_n = "decresc"
        elif int(n_str[i]) == int(n_str[i-1]):
            continue
    return False


if __name__ == "__main__":
    n = 101
    num = 0
    num_bouncy = 0
    while num != 99:
        if is_bouncy(n):
            num_bouncy += 1
        num = int((num_bouncy*100)/n)
        n += 1
    print(n, "ha percentuale pari a", num)