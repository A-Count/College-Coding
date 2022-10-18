Nums = []
for x in range(3):
    In = input("Please enter a number")
    Nums.append(In)

def mean():
    total = 0
    for x in Nums:
        total = total + int(x)
    Mean = total/3
    print(Mean)

MedList = []
def median():
    Median = 0
    for x in Nums:
        if x in MedList:
            Median = x
        else:
            MedList.append(x)
    if Median != 0:
         print(Median)
    else:
        print("There is no median")
        
        


mean()
median()
