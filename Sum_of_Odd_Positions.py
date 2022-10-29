n=int(input())
m=list(map(int,input().split()))
s=0
for i in range(len(m)):
    if i%2!=0:
        s+=m[i]
print(s)