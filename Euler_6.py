def square(n):
    sums = []
    for i in range(n):
        sum_s = i**2
        sums.append(sum_s)  
    fs=sum(sums)
    print(fs)
    return fs     

def s_squares(n):
    s_sums = []
    for i in range(n):
        sum_s = i
        s_sums.append(sum_s)
    fsq = sum(s_sums)**2
    print(fsq)
    return fsq

def sott():
    sot = s_squares(101) - square(101)
    print(sot)
    return sot

sott()