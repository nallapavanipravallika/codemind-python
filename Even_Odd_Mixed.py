n=int(input())
a=n%10
b=n%100
c=b//10
d=n//100
if a%2==0 and c%2==0 and d%2==0:
    print("Even")
elif a%2!=0 and c%2!=0 and d%2!=0:
    print("Odd")
else:
    print("Mixed")