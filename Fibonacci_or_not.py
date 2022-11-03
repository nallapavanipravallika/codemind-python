def fib(n):
    a=0
    b=1
    while True:
        sum=a+b
        if sum==n:
            print("True")
            break
        a=b
        b=sum
        if sum>n:
            print("False")
            break
n=int(input())
fib(n)