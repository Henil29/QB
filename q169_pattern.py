'''
*  *  *  *
   *  *  *
      *  *
         *
'''

a=int(input("Enter a:"))

for i in range(1,a+1):
    print(" "*(i-1)+"#"*(a-i+1))