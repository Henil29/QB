'''
hra :>> class 1 cities=0.3*bp
hra :>> class 2 cities=0.2*bp
hra :>> class 3 cities=0.1*bp
dra=0.5*bp
pf=0.11*bp
ta=900

gp=bp+hra+dra+oa+ta-pt-pf
ap=gp*12
'''

grade=input("Enter grade level(A,B,C,D,E or F): ")

pt=200
hra=0
ta=900
gp=0
ap=0
tex=0
if(grade=="a" or grade=="A"):
    bp=60000 #change for every city grade
    oa=8000
    
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
    
if(grade=="b" or grade=="B"):
    bp=50000 #change for every city grade
    oa=7000
    
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

if(grade=="c" or grade=="C"):
    bp=40000 #change for every city grade
    oa=6000
    
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

if(grade=="d" or grade=="D"):
    bp=30000 #change for every city grade
    oa=5000
    
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
    
if(grade=="e" or grade=="E"):
    bp=20000 #change for every city grade
    oa=4000
    
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
    
if(grade=="f" or grade=="F"):
    bp=10000 #change for every city grade
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