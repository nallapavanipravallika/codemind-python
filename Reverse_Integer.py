n=int(input())
p=abs(n)
r=0
while p>0:
    m=p%10
    r=r*10+m
    p=p//10
if n<0:
    print(-r)
else:
    print(r)
    