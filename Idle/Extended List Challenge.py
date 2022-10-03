UserList = []
for x in range(10):
    Num = input("Please enter a number")
    UserList.append(Num)

Target = int(input("Please enter a target number"))
Smallest = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000
Biggest = 0
Total = 0
Product = 1

Menu = int(input("""What would you like to do?
Enter 1 to find the target value,
Enter 2 to find the smallest number,
Enter 3 to find the largest number,
Enter 4 to find the sum of the list,
Enter 5 to find the product of the numbers
Enter 6 to exit. """))

if Menu == (1):
    for x in UserList:
        if x == Target:
            print (str(x) + " is the target")
        else:
            print(str(x) + " is not the target")

if Menu == (2):
    for x in UserList:
        if x < Smallest:
            Smallest = x
    print(Smallest)

if Menu == (3):
    for x in UserList:
        if x > Biggest:
            Biggest = x
    print(Biggest)

if Menu == (4):
    for x in UserList:
        Total = Total + x
    print(Total)
            
if Menu == (5):
    for x in UserList:
        Product = Product * int(x)
    print(Product)

if Menu == (6):
    print("Goodbye!")
