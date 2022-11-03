n=int(input())
nsq=n**2
num_of_digits=len(str(n))
last_digits = nsq%pow(10,num_of_digits) 
if last_digits==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
