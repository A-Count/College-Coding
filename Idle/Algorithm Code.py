nums = []
for i in range(5):
    user = input("Please enter a number")
    nums.append(user)
print(nums)

biggest = 0
smallest = 100000000000000000000000000000000000000
for x in nums:
    if int(x) > biggest:
        biggest = int(x)
    elif int(x) < smallest:
        smallest = int(x)
print (biggest - smallest)
