def fct(n):
    return 1 if n==1 else n*fct(n-1)



def fibonacci(limit):
    fib_nums = []

    curent_num = 0
    next_num =1

    while next_num < limit:
        curent_num, next_num = next_num, next_num + curent_num
        fib_nums.append(curent_num)

    return fib_nums

def fibonacci_co(limit):
    fib_nums = []

    curent_num = 0
    next_num =1

    while next_num < limit:
        curent_num, next_num = next_num, next_num + curent_num
        yield curent_num



fibs = fibonacci_co(100)
for fib in fibs:
    print(fib, end=',')
