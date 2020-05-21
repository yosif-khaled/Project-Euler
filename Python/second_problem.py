#prints the febonacci list
#only if first 3 numbers are defined
#can't single out even numbers in printed list
#x = []
#for i in range(100):

    #if y <= 4e6:
        #y = x[i + 1] + x[i + 2]
        #x.append(y)
    #else:
        #break

#the fibonacci function
#on my own with no help just progress and coming back took me 3 days to solve
def _fib(a, b):

    fibonacci_list = []
    fibonacci_list.append(a)
    fibonacci_list.append(b)

    while True:
        c = a + b
        a = b
        b = c
        fibonacci_list.append(c)
        n = int(len(fibonacci_list))
        if c%2 == 0:
            print(c)

        elif c >= 4e6:
            print(n)
            break

feb = _fib(1, 2)


