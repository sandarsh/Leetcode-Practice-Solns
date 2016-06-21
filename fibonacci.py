def Fib(n):
    fib = [0 for i in range(n)]
    for i in range(0,n):
        if i <= 1:
            fib[i] = 1
        else:
            num = fib[i-1] + fib[i-2]
            fib[i] = num
    print fib
    return fib[n-1]


n = 20
fibo = Fib(n)
print fibo
