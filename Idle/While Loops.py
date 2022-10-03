n = 0

while n <=5:
    print(n)
    n = n + 1

Num = int(input("Enter a number"))

while Num != 0:
    if Num == 40:
        print("You entered 40")
        break
    if Num == 20:
        print("You entered 20")
        break
    else:
        Num = int(input("Enter a number"))
