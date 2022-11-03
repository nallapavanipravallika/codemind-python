def self_dividing(n):
    for i in str(n):
        if i=='0' or n%int(i)>0:
            return False
    return True
left=int(input())
right=int(input())
for n in range(left,right+1):
    if self_dividing(n):
        print(n,end=" ")