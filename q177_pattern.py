'''
      1
    1  2
  1  2  3
 1  2  3  4
'''

a=5

for i in range (1,a+1):
    print("  "*(a-i),end="")
    for j in range(1,i+1):
        print(j,end="   ")#more space make more efficient
    print()