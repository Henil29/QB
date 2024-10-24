
grade=input("Enter grade level(A,B,C,D,E or F): ")

pt=200
hra=0
ta=900
gp=0
ap=0
tex=0
if(grade=="a" or grade=="A"):
    bp=60000
    oa=8000
       
elif(grade=="b" or grade=="B"):
    bp=50000
    oa=7000

elif(grade=="c" or grade=="C"):
    bp=40000
    oa=6000
    
elif(grade=="d" or grade=="D"):
    bp=30000
    oa=5000  
    
elif(grade=="e" or grade=="E"):
    bp=20000
    oa=4000   
    
elif(grade=="f" or grade=="F"):
    bp=10000
    oa=3000
    
tier=int(input("Enter tier of your city (1,2,3): "))
    
if(tier==1):
    hra=0.3*bp
elif(tier==2):
    hra=0.2*bp
elif(tier==3):
    hra=0.1*bp
    
dra=0.5*bp
pf=0.11*bp

gp=bp+hra+dra+oa+ta-pt-pf
print(f"Gross Pay of an Employee is: {gp}")

ap=gp*12
print(f"Annual Pay of an Employee is: {ap}")


if(ap<=250000):
        tex=0
    
elif(ap>=250001 and ap<=500000):
    tex=(ap-250000)*0.05

elif(ap>=500001 and ap<=750000):
    tex=(ap-500000)*0.10+12500

elif(ap>=750001 and ap<=1000000):
    tex=(ap-750001)*0.15+37500
    
elif(ap>=1000001 and ap<=1250000):
    tex=(ap-1000000)*0.20+750000

elif(ap>=1250001 and ap<=1500000):
    tex=(ap-1250000)*0.25+125000

elif(ap>=1500001):
    tex=(ap-1500000)*0.30+187500
    
print(f"Income tax to be paid by an employee is: {tex}")