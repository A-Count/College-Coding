print("Finding the largest number in a list")
Big = 0
List = [80, 4, 1000, 900, 87500, 0]
print (List)
for x in List:
    if Big < x:
        Big = x

print (Big)

print("Finding the sum of numbers in a list")
Total = 0
for x in List:
    Total = Total + x

print (Total)
