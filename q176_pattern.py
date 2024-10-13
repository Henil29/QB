'''
1
0  1
1  0  1
0  1  0  1
'''

a=5

for i in range(1,a+1):
    for j in range(1,i+1):
        if((i%2==0 and j%2!=0) or (j%2==0 and i%2!=0)):
            print("0 ",end="")
        else:
            print("1 ",end="")
    print()