pip install tabulate
from tabulate import tabulate

mydata = [
    ["Is it mutable?", "Yes", "Yes", "No"]
    ["Can we change the size after creation", "Yes", "Yes", "No"]
    ["Can items in the list be changed?", "Yes", "Yes", "No"]
    ["How many different types of data can be stored?", "4", "1", "4"]
]

head = ["", "List", "Array", "Tuple"]

print(tabulate(mydata, headers=head, tablefmt="grid"))
