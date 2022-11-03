def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,b,end=" ")
    for i in range(3,n+1):
        sum=a+b
        print(sum,end=' ')
        a=b
        b=sum
n=int(input())
fib(n)