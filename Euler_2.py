
def Fibonacci():
    Fib_list = []
    one = 1
    two = 2
    Fib_list.append(two)
    while two <= 4000000:
        sum_one = one + two
        sum_two = sum_one + two
        if sum_one % 2 == 0:
            Fib_list.append(sum_one)
        if sum_two % 2 == 0:
            Fib_list.append(sum_two) 
        one = sum_one
        two = sum_two
    print(Fib_list)
    print(sum(Fib_list))
    return Fib_list

Fibonacci()
