n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
    k=s//n
for i in l:
    if i==k:
        print("True")
        break
else:
        print("False")