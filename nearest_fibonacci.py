def fib(n):
    a=0
    b=1
    sum=a+b
    while(sum<=n):
        a=b
        b=sum
        sum=a+b
    if(abs(sum-n)==abs(b-n)):
        print(b,sum)
    else:
        if (abs(sum-n)>=abs(b-n)):
            ans=b
        else:
            ans=sum
    print(ans)
n=int(input())
fib(n)