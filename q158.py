a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
count=0
for i in range(a,b+1):
    if(i%c==0):
        count+=1

print(count)