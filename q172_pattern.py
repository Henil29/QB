'''
1  2  3  4  5
1  2  3  4
1  2  3 
1  2  
1
'''

a=10

for i in range(1,a+1):
    for j in range(1,a-i+2):
        print(j,end=" ")
    print()