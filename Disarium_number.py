n=int(input())
temp=n
s=str(n)
sum=0
for i in range(len(s),0,-1):
    r=int(n)%10
    sum+=(r**i)
    n=n//10
if sum==temp:
    print("True")
else:
    print("False")