n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in l:
    if i==m:
        print("True")
        break
else:
       print("False")