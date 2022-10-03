def minconvert(a):
    OutMin = a*60
    print (OutMin)
    
InMin = int(input("How many minutes?"))
minconvert(InMin)

def addition(a,b):
    OutAdd = a+b
    print (OutAdd)

InAdd1 = int(input("Enter first number."))
InAdd2 = int(input("Enter second number."))

addition(InAdd1,InAdd2)

def ageconvert(a):
    days = a*365
    print(days)
    
Age = int(input("How old are you?"))
ageconvert(Age)

def degreeconvert(a):
    Outdeg = a-32
    Outdeg = Outdeg/1.8
    print(Outdeg)

InDeg = int(input("Enter degree in farenheit"))
degreeconvert(InDeg)
