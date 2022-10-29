n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
    k=s/n
print("{:.2f}".format(k))