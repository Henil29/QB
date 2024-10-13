n=int(input("Enter value of n:"))

num1=0
num2=1

for _ in range(n):
    print(num1)
    temp=num1+num2
    num1=num2
    num2=temp