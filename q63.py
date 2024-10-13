#a^x=n where =?
a=int(input("Enter value of a:"))
n=int(input("Enter value of n:"))

x=0
temp=1

if(a>=1 and n==1):
    print("x=0")
elif n<a or  a==1:
    print("No solution exists")
else:
    while temp<n:
        temp=temp*a
        x=x+1
    if(temp==n):
        print(f"x={x}")
    else:
        print("No solution exists")