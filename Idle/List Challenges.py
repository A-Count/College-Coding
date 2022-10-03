IntList = [100, 53, 1, 18, 44]
StrList = ["Hello", "World", "00", "Print", "Danger"]

StrList.reverse()
print (StrList)

StrList.extend(IntList)
print (StrList)

for x in IntList:
    x = x**2
    print (x)
