n=int(input())
nsq=n*n
s=0
while nsq>0:
    a=nsq%10
    s+=a
    nsq=nsq//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")