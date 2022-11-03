def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x
x,y=map(int,input().split())
print(GCD(x,y))