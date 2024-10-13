#!/usr/bin/env python
# coding: utf-8

# In[6]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

print(f"Value of a is {a}")
print(f"Value of b is {b}")
print("sum is:",a+b)
print("sub is:",a-b)
print("mult is:",a*b)
print("div is:",int(a/b))
print("squre ios a is",a**2)


# In[8]:


a=int(input("Enter base value:"))
b=int(input("Enter height value:"))

print(f"Value of base is {a}")
print(f"Value of heigth is {b}")
print(f"area of triangle is {0.5*a*b}")


# In[8]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

print(f"Value of a is {a}")
print(f"Value of b is {b}")
print("sum is:",a+b)
print("sub is:",a-b)
print("mult is:",a*b)
print("div is:",int(a/b))
print("mod is:",a%b)
print("squre is a is",a**2)


# In[9]:


a=int(input("Enter base value:"))
b=int(input("Enter height value:"))

print(f"height of triangle is {a} and base is {b} area of triangle is {0.5*a*b}")

print(f"Radius of circle is {a} and area is {(22/7)*a*a}")
print(f"Size of square is {a} and area is {a**2}")
print(f"Height and base of rectangle is {a},{b} and area is {a*b}")


# In[17]:


# import math
# x=math.pie()
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

print(f"Value of a is {a}")
print(f"Value of b is {b}")
print()
print("Cal")
print("sum is:",a+b)
print("sub is:",a-b)
print("mult is:",a*b)
print("div is:",int(a/b))
print("mod is:",a%b)
print("squre is a is",a**2)

print()
print("Area of shapes")
print()

a=int(input("Enter height of triangle:"))
b=int(input("Enter base of triangle:"))
print(f"height of triangle is {a} and base is {b} area of triangle is {0.5*a*b}")
print()
a=int(input("Enter radius of circle:"))
print(f"Radius of circle is {a} and area is {(22/7)*a*a}")
print()
a=int(input("Enter height of square:"))
print(f"Size of square is {a} and area is {a**2}")
print()
a=int(input("Enter height of rectangle:"))
b=int(input("Enter base of rectangle:"))
print(f"Height and base of rectangle is {a},{b} and area is {a*b}")
print()
h=int(input("Enter height:"))
b1=int(input("Enter base 1:"))
b2=int(input("Enter base 2:"))


# In[29]:


import math
p=math.pi
print("Area of cylinder")
r=int(input("Enter radius os cylinder"))
h=int(input("Enter height of cylinder"))
print(f"Area of cylinder is {2*p*r*(r+h)}")

print()
print("Area of Trapezoid")
h=int(input("Enter height:"))
b1=int(input("Enter base 1:"))
b2=int(input("Enter base 2:"))
print(f"Area of trapezoid is {0.5*h*(b1+b2)}")

print()
print("C to f")
c=int(input("Enter cel:"))
print(f"Fer of given cel is {((9/5)*c)+32}℉")

print()
print("F to C")
f=int(input("Enter fer:"))
print(f"Cel of given fer is {(f-32)*(5/9)}℃")

print()
print("Squreroot")
a=int(input("Enter number:"))
print(f"Squreroot of {a} is {math.sqrt(a)}")


# In[37]:


year=0
month=0

day=int(input("Enter days:"))

while(day>30):
    if(day>=365):
        year+=1
        day=day-365

    if(day>30):
        month+=1
        day=day-30

print(f"total year is {year},total month is {month} and day is {day}")


# In[38]:


day=int(input("Enter days:"))

print(f"year is {day//365} , month is {day%365//30} , day is {day%365%30}")


# In[1]:


print("Hi")


# In[7]:

hour=int(input("Enter hours:"))

print(f"Total minutes is {hour*60} and second is  {hour*60*60}")


# In[8]:


sec=int(input("Enter seconds:"))

# print(f"Days is {sec//(3600*24)} ,Hours is {sec%(3600*24)//3600} , minutes is {sec%(3600*24)%3600//60} , seconds is {sec%(3600*24)%3600%60}")

print(f"Years is {sec // 31536000} Months is {(sec % 31536000) // 2592000} ,Days is {(sec % 2592000) // 86400},Hours is {(sec % 86400) // 3600},Minutes is {(sec % 3600) // 60},Seconds is {sec % 60}")


# In[13]:


import math

deg=int(input("Enter degree:"))

red=(math.pi/180)*deg
print(f"Red is {red}")
print(f"Area of circul {math.pi*(red**2)}")


# In[ ]:


year=0
month=0

day=int(input("Enter days:"))

while(day>30):
    if(day>=365):
        year+=1
        day=day-365

    if(day>30):
        month+=1
        day=day-30

print(f"total year is {year},total month is {month} and day is {day}")


# In[16]:


a=int(input("Enter a:"))
if(a%2==0):
    print(f"{a} is Even")
elif(a%3==0):
    print(f"{a} is divisible by 3")
else:
    print(f"{a} is odd")


# In[19]:


a=int(input("Enter a:"))
if(a>0):
    print(f"{a} is positive")
elif(a<0):
    print(f"{a} is negative")
else:
    print(f"{a} is Zero")


# In[3]:


print('''1 for sum
2 for sub
3 for mult
4 for div
5 for squre''')

c=int(input("Enter your choice"))
if(c==1):
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    print(f"Value of a is {a}")
    print(f"Value of b is {b}")
    print("sum is:",a+b)
elif(c==2):
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    print(f"Value of a is {a}")
    print(f"Value of b is {b}")
    print("sub is:",a-b)
elif(c==3):
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    print(f"Value of a is {a}")
    print(f"Value of b is {b}")
    print(f"mult is:{a*b}")

elif(c==4):
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    print(f"Value of a is {a}")
    print(f"Value of b is {b}")
    
    if(b!=0):
        print("div is:",int(a/b))
    else:
        print("Can not divisible by zero")

elif(c==5):
    a=int(input("Enter value of a:"))
    print(f"Value of a is {a}")
    print("squre is a is",a**2)
else:
    print("Incorrect input")



# In[23]:


a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if(a>b and a>c):
    print(f"{a} is large")
elif(b>c):
    print(f"{b} is large")
elif(c>b):
    print(f"{c} is large")


# In[2]:


a=int(input("Enter value of a:"))

# if(a%3==0 and a%5==0):
#     print(f"{a} is divisible by 3 and 5")
if(a%3==0):
    if(a%5==0):
        print(f"{a} is divisible by 3 and 5")
else:
    print(f"{a} is not divisible by 3 and 5")
    


# In[14]:


a=(input("Enter value of a:"))

# if((a=="A" or a=="a") or (a=="E" or a=="e") or (a=="I" or a=="i") or (a=="O" or a=="o") or (a=="U" or a=="u")):
#     print(f"{a} is vowels")
# else:
#     print(f"{a} is not vowels")
a=a.lower()
if a in 'aeiou':
    print(f"{a} is vowels")
else:
    print(f"{a} is not vowels")


# In[19]:


# Extra
a="Hii"
print(len(a))
print(a[0])


# In[26]:


a=input("Enter value of a only 3 digit please:")

if (len(a)==3):
    a=int(a)
#     print(f"First digit is {a[0]}")
#     print(f"Third digit is {a[2]}")
    print(f"first digit is {a//100}")
    print(f"Second digit is {a%10}")
    
    
          
else:
    print("Enter only 3 digits")


# In[44]:


a=input("Enter value of only digit please:")
b=len(a)
a=int(a)

print(f"first digit is {a//(10**(b-1))}")
print(f"Middle digit is {(a%(10**(b-1)))//10}")
print(f"last digit is {a%10}")

# p=str(a%10)
# q=str((a%(10**(b-1)))//10)
# r=str(a//(10**(b-1)))


# print(f"Swap is {p+q+r}")


print(f"swap is {((a%10)*(10**(b-1)) )+(((a%(10**(b-1)))//10)*10)+(a//(10**(b-1)))}")

