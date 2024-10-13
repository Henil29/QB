'''
      *
    #  #
  *  *  *
 #  #  #  #
'''

a=5

for i in range(1,a+1):
    print("  "*(a-i),end="")
    for j in range(1,i+1):
        if(i%2!=0):
            print("*",end="   ")
        else:
            print("#",end="   ")
    print()